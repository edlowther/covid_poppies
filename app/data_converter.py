import datetime
import pandas as pd
import numpy as np

class DataConverter:
    def __init__(self, download_new_data, top_countries, bottom_countries, orchestration_mapper, score_manager):
        self.top_countries = top_countries
        self.bottom_countries = bottom_countries
        self.dynamics = list(orchestration_mapper.keys())
        self.score_manager = score_manager
        self.df = self.initialise_df(download_new_data)

    def initialise_df(self, download_new_data):
        if download_new_data:
            print('Downloading new data...')
            df = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/nationalcasedeath/csv')
            df.to_csv('./data/latest_ecdc_data.csv', index = False)
            print('Download finished')
        else:
            print('Loading data locally')
            df = pd.read_csv('./data/latest_ecdc_data.csv')
        df['date'] = pd.to_datetime([datetime.datetime.strptime(d + '-1', '%G-%V-%u') for d in df['year_week']])
        # Split, apply, combine
        df_cases = df.loc[df['indicator'] == 'cases', ['country', 'country_code', 'date', 'weekly_count', 'cumulative_count']].rename(columns = {
            'weekly_count': 'weekly_cases',
            'cumulative_count': 'cumulative_cases'
        })
        df_deaths = df.loc[df['indicator'] == 'deaths', ['country', 'country_code', 'date', 'weekly_count', 'cumulative_count']].rename(columns = {
            'weekly_count': 'weekly_deaths',
            'cumulative_count': 'cumulative_deaths'
        })
        df = pd.merge(df_cases, df_deaths, on=['country', 'country_code', 'date'])
        df = df.loc[df['country'].isin(self.top_countries + self.bottom_countries)]
        def get_vaccination_status(name):
            if name in self.top_countries:
                return 'Top'
            elif name in self.bottom_countries:
                return 'Bottom'
            return 'Error'
        df['name'] = df['country'].apply(get_vaccination_status)
        # df.rename(columns = {'country': 'name'}, inplace = True)
        df = df[
            ['date', 'name', 'weekly_cases', 'weekly_deaths', 'cumulative_deaths']
        ]
        # Convert to monthly data:
        df['year'] = df['date'].dt.strftime('%Y')
        df['week_number'] = df['date'].dt.strftime('%W')
        df['fortnight_number'] = np.floor((pd.to_numeric(df['week_number']) + 1) / 2)

        monthly_df = df.groupby(['name', 'year', 'fortnight_number'])[
            ['weekly_cases', 'weekly_deaths']
        ].mean().reset_index().rename(columns = {'weekly_cases': 'avg_weekly_cases',
                                                'weekly_deaths': 'avg_weekly_deaths'})
        monthly_df.to_csv('~/Downloads/monthly_df.csv', index = False)
        return monthly_df

    def to_score(self):
        for vaccination_status in ['Top', 'Bottom']:
            self.convert_data_by_vaccination_status_to_score(vaccination_status)

    def convert_data_by_vaccination_status_to_score(self, vaccination_status):
        filtered_df = self.df.loc[self.df['name'] == vaccination_status]
        monthly_deaths_data = filtered_df['avg_weekly_deaths'].apply(lambda x: 0 if np.isnan(x) else int(x))
        max_deaths = monthly_deaths_data.max()
        for monthly_deaths in monthly_deaths_data:
            # Useful for clipping notes in pp bars:
            clip = None
            if monthly_deaths == 0:
                dynamic = 'bar_of_rest'
            else:
                num_thresholds = len(self.dynamics) - 1
                dynanics_idx = round(monthly_deaths / max_deaths * num_thresholds)
                dynamic = self.dynamics[dynanics_idx]
                if dynamic == 'pp':
                    bucket_width = max_deaths / num_thresholds
                    # Why * 6 / 2? just to calibrate to accuracy of 0.5 notes within range of 3 (i.e. length of dotted minim)
                    clip = np.ceil(monthly_deaths / bucket_width * 6) / 2
            self.score_manager.add_bar(vaccination_status, dynamic, clip)

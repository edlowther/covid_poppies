from collections import namedtuple

from app.app import App

# Config here:
download_new_data = False

# countries_to_output = ['United Kingdom', 'Brazil', 'Russia', 'United States Of America', 'India', 'Peru', 'France', 'Italy', 'Netherlands']
countries_to_output = ['United Kingdom', 'France', 'Peru', 'South Africa']

# countries by vaccination status:
top_countries = ['United Arab Emirates', 'Portugal', 'Spain', 'Singapore', 'Uruguay', 'Denmark', 'Chile', 'China',
                 'Canada', 'Ireland', 'Finland', 'France', 'Italy', 'United Kingdom', 'Brazil']
bottom_countries = ['Tanzania', 'Nigeria', 'Ethiopia', 'Kenya', 'Egypt', 'Bangladesh', 'South Africa', 'Pakistan',
                    'Vietnam', 'Indonesia', 'Russia', 'Iran', 'Thailand', 'India', 'Mexico']

Instrument = namedtuple('Instrument', ['name', 'abbr', 'phrase_idx', 'vaccination_status'])
instruments = [
    Instrument('Violin 1',    'Vln1',   0, 'Top'),
    Instrument('Violin 2',    'Vln2',   1, 'Top'),
    Instrument('Viola',       'Vla',    2, 'Top'),
    Instrument('Cello',       'Cello',  3, 'Top'),
    Instrument('Trumpet',     'Trmpt',  1, 'Bottom'),
    Instrument('French horn', 'Hrn',    1, 'Bottom'),
    Instrument('Bassoon',     'Bsn',    3, 'Bottom'),
    Instrument('Flute',       'Flt',    0, 'Bottom'),
    Instrument('Clarinet',    'Clnt',   2, 'Bottom'),
    Instrument('Oboe',        'Oboe',   1, 'Bottom'),

]
orchestration_mapper = {
    'pp': ['Cello', 'Clnt'],
    'p' : ['Vln2', 'Cello', 'Clnt', 'Oboe'],
    'mp': ['Vln1', 'Vln2', 'Vla', 'Cello', 'Oboe', 'Bsn'],
    'mf': ['Vln1', 'Vln2', 'Vla', 'Cello', 'Hrn', 'Flt', 'Bsn'],
    'f' : ['Vln1', 'Vln2', 'Vla', 'Cello', 'Clnt', 'Hrn', 'Oboe', 'Trmpt'],
    'ff': ['Vln1', 'Vln2', 'Vla', 'Cello', 'Clnt', 'Flt', 'Oboe', 'Trmpt', 'Bsn']
}
output_filepath = './output/coronavirus_data_by_vaccination_status_v2.xml'

app = App(download_new_data, top_countries, bottom_countries, instruments, orchestration_mapper, output_filepath)

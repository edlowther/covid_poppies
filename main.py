from collections import namedtuple

from app.app import App

# Config here:
download_new_data = True

# countries_to_output = ['United Kingdom', 'Brazil', 'Russia', 'United States Of America', 'India', 'Peru', 'France', 'Italy', 'Netherlands']
countries_to_output = ['United Kingdom', 'France', 'Peru', 'South Africa']
Instrument = namedtuple('Instrument', ['name', 'abbr', 'phrase_idx'])
instruments = [
    Instrument('Violin 1',    'Vln1',   0),
    Instrument('Violin 2',    'Vln2',   1),
    Instrument('Viola',       'Vla',    2),
    Instrument('Cello',       'Cello',  3),
    Instrument('Trumpet',     'Trmpt',  1),
    Instrument('French horn', 'Hrn',    1),
    Instrument('Bassoon',     'Bsn',    3),
    Instrument('Flute',       'Flt',    0),
    Instrument('Clarinet',    'Clnt',   2),
    Instrument('Oboe',        'Oboe',   1),

]
orchestration_mapper = {
    'pp': ['Vln2', 'Cello'],
    'p' : ['Vln1', 'Vln2', 'Cello', 'Clnt'],
    'mp': ['Vln1', 'Vln2', 'Vla', 'Cello', 'Oboe'],
    'mf': ['Vln1', 'Vln2', 'Vla', 'Cello', 'Hrn', 'Flt', 'Bsn'],
    'f' : ['Vln1', 'Vln2', 'Vla', 'Cello', 'Clnt', 'Hrn', 'Oboe', 'Trmpt'],
    'ff': ['Vln1', 'Vln2', 'Vla', 'Cello', 'Clnt', 'Flt', 'Oboe', 'Trmpt', 'Bsn']
}
output_filepath = './output/coronavirus_data_{}_v1.xml'

app = App(download_new_data, countries_to_output, instruments, orchestration_mapper, output_filepath)

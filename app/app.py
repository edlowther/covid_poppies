from app.data_converter import DataConverter
from app.score_manager import ScoreManager

class App():
    def __init__(self, download_new_data, countries_to_output, instruments, orchestration_mapper, output_filepath):
        self.countries_to_output = countries_to_output
        self.instruments = instruments
        self.orchestration_mapper = orchestration_mapper
        self.score_manager = ScoreManager(countries_to_output, instruments, orchestration_mapper, output_filepath)
        self.data_converter = DataConverter(download_new_data, countries_to_output, orchestration_mapper, self.score_manager)
        self.data_converter.to_score()
        self.score_manager.write()

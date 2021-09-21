from app.data_converter import DataConverter
from app.score_manager import ScoreManager

class App():
    def __init__(self, download_new_data, top_countries, bottom_countries, instruments, orchestration_mapper, output_filepath):
        self.score_manager = ScoreManager(instruments, orchestration_mapper, output_filepath)
        self.data_converter = DataConverter(download_new_data, top_countries, bottom_countries, orchestration_mapper, self.score_manager)
        self.data_converter.to_score()
        self.score_manager.write()

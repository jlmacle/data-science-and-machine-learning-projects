import os
from jl_ml_utils._data_path import DataPath as data_path_class

class _DataPath:
    def __init__(self) -> None:
        self.data_path = data_path_class()

        self.data_path.set_path_to_csv_folder(os.path.join(os.getcwd(),"MachineLearningRepository_Adult-dataset","data"))
        self.data_path.set_file_name_for_csv_with_original_data("adult.csv")
        self.data_path.set_file_name_for_csv_with_cleaned_data("adult_na_removed.csv")
        self.data_path.set_path_to_cleaned_csv_file(os.path.join(self.data_path.get_path_to_csv_folder(), self.data_path.get_file_name_for_csv_with_cleaned_data()))
            
        self.data_path.set_path_to_folder_with_data_for_reporting(os.path.join(os.getcwd(),"MachineLearningRepository_Adult-dataset","data_for_report"))       
        self.data_path.set_file_name_for_csv_file_with_data_for_reporting("data_for_report.csv")
        self.data_path.set_file_name_for_txt_file_with_data_for_reporting("data_for_report.txt")


    def get_data_path_object(self):
        return self.data_path




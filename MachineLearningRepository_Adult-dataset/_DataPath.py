import os

class _DataPath:
    def __init__(self) :
        self.path_to_csv_folder = os.path.join(os.getcwd(),"MachineLearningRepository_Adult-dataset","data")
        self.csv_name_original = "adult.csv"
        self.csv_name_cleaned = "adult_na_removed.csv"

    def get_path_to_csv_folder(self):
        return self.path_to_csv_folder
    
    # Getting the data provided by the web site
    def get_file_name_for_csv_with_original_data(self):
        return self.csv_name_original
                            
    # Getting the data when non available data has been removed
    def get_path_to_cleaned_csv_file(self):
        return os.path.join(self.path_to_csv_folder, self.csv_name_cleaned)

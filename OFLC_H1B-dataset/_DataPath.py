import os

class _DataPath:
    def __init__(self) :
        self.path_to_data_folder = os.path.join(os.getcwd(),'OFLC_H1B-dataset','data')        
        self.file_name_for_original_data = "Data-Restricted-to-computer-related-fields.csv"       

    def get_path_to_data_folder(self):
        return self.path_to_data_folder
        
    def get_file_name_for_original_data(self):
        return self.file_name_for_original_data
    
                            
   
import os

class _DataPath:
    def __init__(self) :
        self.path_to_csv_folder = os.path.join(os.getcwd(),'data')
        self.csv_name_original = "adult.csv"
        self.csv_name_cleaned = "adult_na_removed.csv"

    def get_path_to_csv_folder(self):
        return self.path_to_csv_folder
    
    # Getting the data provided by the web site
    def get_path_to_original_csv_file(self):
        return os.path.join(self.path_to_csv_folder, self.csv_name_original)
                            
    # Getting the data when non available data has been removed
    def get_path_to_cleaned_csv_file(self):
        return os.path.join(self.path_to_csv_folder, self.csv_name_cleaned)
    
    # To help test the class
    def test(self):
        # extra empty line for readability
        print(os.linesep)
        if not os.path.exists(self.get_path_to_original_csv_file()) :
            raise FileNotFoundError(self.get_path_to_original_csv_file()+" does not exist")
        else :
            print ("Original csv file exists : ",os.linesep,self.get_path_to_original_csv_file())
        
        print(os.linesep)
        if not os.path.exists(self.get_path_to_cleaned_csv_file()) :
            raise FileNotFoundError(self.get_path_to_cleaned_csv_file()+" does not exist")
        else :
            print("Cleaned csv file exists: ",os.linesep,self.get_path_to_cleaned_csv_file())

# dp = _DataPath()
# dp.test()
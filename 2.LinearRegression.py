from jl_ml_utils.linear_regression import LinearRegression as lr_class
from jl_ml_utils.data_cleaning_and_processing import DataCleaningAndProcessing as dcp_class
from _DataPath import _DataPath as data_path_class

# Goal : to predict the income based of the provision of features
data_path = data_path_class()
dcp = dcp_class()
lr = lr_class()



# Importing the cleaned data for processing
data_array = dcp.import_csv_to_numpy_array(data_path.get_path_to_cleaned_csv_file())


from jl_ml_utils.data_cleaning_and_processing import DataCleaningAndProcessing as dcp_class
from jl_ml_utils.data_visualization import DataVisualization as dv_class
from _DataPath import _DataPath as data_path_class
import os

# Cleaning the data before processing
dp = data_path_class()
dv = dv_class()
dc = dcp_class()

# Removing rows with unvavailable data
dc.remove_rows_with_data_unavailable_from_csv_file(dp.get_path_to_csv_folder(), dp.get_path_to_original_csv_file())


    




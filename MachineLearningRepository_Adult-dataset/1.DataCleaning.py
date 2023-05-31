from jl_ml_utils.data_cleaning_and_processing import DataCleaningAndProcessing as dcp_class
from jl_ml_utils.data_visualization import DataVisualization as dv_class
from _DataPath import _DataPath as data_path_class
import os

# Cleaning the data before processing
data_path = data_path_class()
dcp = dcp_class()
dv = dv_class()


# Removing rows with unvavailable data
dcp.remove_rows_with_data_unavailable_from_csv_file(data_path.get_path_to_csv_folder(), data_path.get_file_name_for_csv_with_original_data())


    





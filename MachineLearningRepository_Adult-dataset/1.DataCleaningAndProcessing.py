from jl_ml_utils.data_cleaning_and_processing import DataCleaningAndProcessing as dcp_class
from jl_ml_utils.data_visualization import DataVisualization as dv_class
from _DataPath import _DataPath as _data_path_class


# Cleaning the data before processing
dcp = dcp_class()
dv = dv_class()
_data_path = _data_path_class()
data_path = _data_path.get_data_path_object()

# Removing rows with unvavailable data
dcp.remove_rows_with_data_unavailable_from_csv_file(data_path.get_path_to_csv_folder(), data_path.get_file_name_for_csv_with_original_data())


    





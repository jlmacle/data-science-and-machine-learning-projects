from ds_ml_utils.exploratory_analysis import ExploratoryAnalysis as ea_class
from ds_ml_utils.data_cleaning_and_processing import DataCleaningAndProcessing as dcp_class
from _DataPath import _DataPath as _data_path_class

ea = ea_class()
dcp = dcp_class()
_data_path = _data_path_class()
data_path = _data_path.get_data_path_object()

path_to_cleaned_data = data_path.get_path_to_cleaned_csv_file()
df = dcp.import_csv_to_df(path_to_cleaned_data, low_memory_setting=False)

ea.df_info(df)



from jl_ml_utils.data_cleaning_and_processing import DataCleaningAndProcessing as dcp_class
from jl_ml_utils.data_visualization import DataVisualization as dv_class
from _DataPath import _DataPath as _data_path_class
import os

# Planning a data exploration based on unsupervised learning and visualization
dcp = dcp_class()
dv = dv_class()
_data_path = _data_path_class()
data_path = _data_path.get_data_path_object()

# Setting the folder path and csv/txt files names
dv.set_report_folder_path(data_path.get_path_to_folder_with_data_for_reporting())
dv.set_csv_report_file_name(data_path.get_file_name_for_csv_file_with_data_for_reporting())
dv.set_txt_report_file_name(data_path.get_file_name_for_txt_file_with_data_for_reporting())
dv.set_path_to_cleaned_data(data_path.get_path_to_cleaned_csv_file())

# Deleting the files if existing
print("** Deleting existing files if any **")
path_to_csv_file = data_path.get_path_to_csv_file_with_data_for_reporting()
if os.path.exists(path_to_csv_file):
    os.remove(path_to_csv_file)
    print("Existing csv file deleted")

path_to_txt_file = data_path.get_path_to_txt_file_with_data_for_reporting()
if os.path.exists(path_to_txt_file):
    os.remove(path_to_txt_file)
    print("Existing txt file deleted")

# Report data creation
path_to_cleaned_data = data_path.get_path_to_cleaned_csv_file()
df = dcp.import_csv_to_df(path_to_cleaned_data,low_memory_setting=False)
    # Unique count of values for "SOC_TITLE" column, listing the job titles
job_types_data = dv.count_unique_values(df, "JOB_TITLE", is_order_ascending=False)
    # To txt
dv.print_to_txt_file("View over the most represented job types in the dataset")
dv.print_to_txt_file(job_types_data)
    # To csv
dv.print_to_csv_file(",Unique Values,Count")
# 1 row to ignore
dv.print_to_csv_file(dv.table_data_to_csv(job_types_data, 1))

# Issues encountered:
# DtypeWarning: Columns (76,89) have mixed types. Specify dtype option on import or set low_memory=False.
# return pd.read_csv(path_to_csv_file)
# -> Fixed by adding the low_memory option in the import_csv_to_df() method

from jl_ml_utils.data_cleaning_and_processing import DataCleaningAndProcessing as dcp_class
from jl_ml_utils.data_visualization import DataVisualization as dv_class
from _DataPath import _DataPath as data_path_class
import os, time

# Planning a data exploration based on unsupervised learning and visualization
data_path = data_path_class()
dcp = dcp_class()
dv = dv_class()

# Using a csv file for easier data imports
path_to_folder = os.path.join(os.getcwd(),"data_report")
csv_file_name = "data_report.csv"
txt_file_name = "data_report.txt"
path_to_cleaned_data = data_path.get_path_to_cleaned_csv_file()

# Setting the folder path and csv/txt files names
dv.set_report_folder_path(path_to_folder)
dv.set_csv_report_file_name(csv_file_name)
dv.set_txt_report_file_name(txt_file_name)
dv.set_path_to_cleaned_data(path_to_cleaned_data)

# Deleting the files if existing
path_to_csv_file = os.path.join(path_to_folder,csv_file_name)
if os.path.exists(path_to_csv_file):
    os.remove(path_to_csv_file)
    print("Existing csv file deleted")

path_to_txt_file = os.path.join(path_to_folder, txt_file_name)
if os.path.exists(path_to_txt_file):
    os.remove(path_to_txt_file)
    print("Existing txt file deleted")

# Importing the cleaned data for visualizing
# data_array = dcp.import_csv_to_numpy_array(data_path.get_path_to_cleaned_csv_file())
df = dcp.import_csv_to_df(path_to_cleaned_data)

dv.simple_stats(df)
dv.print_to_txt_file(dv.count_unique_values(df, "Native country", False))

# dv.histogram(df, "Native country")



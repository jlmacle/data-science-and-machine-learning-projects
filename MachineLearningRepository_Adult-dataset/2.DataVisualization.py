from jl_ml_utils.data_cleaning_and_processing import DataCleaningAndProcessing as dcp_class
from jl_ml_utils.data_visualization import DataVisualization as dv_class
from _DataPath import _DataPath as data_path_class
import pandas as pd
import os

# Planning a data exploration based on unsupervised learning and visualization
data_path = data_path_class()
dcp = dcp_class()
dv = dv_class()

# Using a csv file for easier data imports
path_to_folder = os.path.join(os.getcwd(),"MachineLearningRepository_Adult-dataset","data_report")
csv_report_file_name = "data_report.csv"
txt_report_file_name = "data_report.txt"
path_to_cleaned_data = data_path.get_path_to_cleaned_csv_file()

# Setting the folder path and csv/txt files names
dv.set_report_folder_path(path_to_folder)
dv.set_csv_report_file_name(csv_report_file_name)
dv.set_txt_report_file_name(txt_report_file_name)
dv.set_path_to_cleaned_data(path_to_cleaned_data)

# Deleting the files if existing
print("** Deleting existing files **")
path_to_csv_file = os.path.join(path_to_folder,csv_report_file_name)
if os.path.exists(path_to_csv_file):
    os.remove(path_to_csv_file)
    print("Existing csv file deleted")

path_to_txt_file = os.path.join(path_to_folder, txt_report_file_name)
if os.path.exists(path_to_txt_file):
    os.remove(path_to_txt_file)
    print("Existing txt file deleted")

# Importing the cleaned data for visualizing
# data_array = dcp.import_csv_to_numpy_array(data_path.get_path_to_cleaned_csv_file())
df = dcp.import_csv_to_df(path_to_cleaned_data, hasLowMemoryOption=False)

# Common to all reports
dv.simple_stats(df)

# Specific to this report

# A view on the most represented native countries
native_country_data = dv.count_unique_values(df, "Native country", False)
   # To txt
dv.print_to_txt_file(os.linesep)
dv.print_to_txt_file("View over the most represented native countries")
dv.print_to_txt_file(native_country_data)
   # To csv
dv.print_to_csv_file("View over the most represented native countries")
dv.print_to_csv_file(",Unique Values,Count")
dv.print_to_csv_file(dv.table_data_with_label_row_ignored_to_csv(native_country_data))

# TODO: a quick experiment to clean up
# A view on the most represented occupations under high school grad
df_less_than_high_school_grad = df[df["Education-Num"] <= 9]
occupation_data_for_less_than_high_school_grad = dv.count_unique_values(df_less_than_high_school_grad, "Workclass", False)
print(os.linesep)
print("View over the most represented occupations under high school grad")
print(occupation_data_for_less_than_high_school_grad)

   # To txt
dv.print_to_txt_file(os.linesep)
dv.print_to_txt_file("View over the most represented occupations under high school grad")
dv.print_to_txt_file(occupation_data_for_less_than_high_school_grad)
   # To csv
dv.print_to_csv_file("View over the most represented occupations under high school grad")
dv.print_to_csv_file(",Unique Values,Count")
dv.print_to_csv_file(dv.table_data_with_label_row_ignored_to_csv(occupation_data_for_less_than_high_school_grad))


print(os.linesep)
df_master_s_degree = df[df["Education-Num"] == 14]
occupation_data_for_master_s_degree = dv.count_unique_values(df_master_s_degree, "Workclass", False)
print(occupation_data_for_master_s_degree)
# To txt
dv.print_to_txt_file(os.linesep)
dv.print_to_txt_file("View over the most represented occupations with a master's degree")
dv.print_to_txt_file(occupation_data_for_master_s_degree)
   # To csv
dv.print_to_csv_file("View over the most represented occupations with a master's degree")
dv.print_to_csv_file(",Unique Values,Count")
dv.print_to_csv_file(dv.table_data_with_label_row_ignored_to_csv(occupation_data_for_master_s_degree))




# Issues encountered:
# DtypeWarning: Columns (76,89) have mixed types. Specify dtype option on import or set low_memory=False.
# return pd.read_csv(path_to_csv_file)
# -> Fixed by adding the low_memory option in the import_csv_to_df() method






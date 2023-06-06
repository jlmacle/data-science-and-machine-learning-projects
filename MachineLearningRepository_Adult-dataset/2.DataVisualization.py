from jl_ml_utils.data_cleaning_and_processing import DataCleaningAndProcessing as dcp_class
from jl_ml_utils.data_visualization import DataVisualization as dv_class
from _DataPath import _DataPath as _data_path_class
import pandas as pd
import os

_data_path = _data_path_class()
data_path = _data_path.get_data_path_object()
dcp = dcp_class()
dv = dv_class()

# Setting the folder path and csv/txt files names
dv.set_report_folder_path(data_path.get_path_to_folder_with_data_for_reporting())
dv.set_csv_report_file_name(data_path.get_file_name_for_csv_file_with_data_for_reporting())
dv.set_txt_report_file_name(data_path.get_file_name_for_txt_file_with_data_for_reporting())
dv.set_path_to_cleaned_data(data_path.get_path_to_cleaned_csv_file())

# Deleting the files if existing
print("** Deleting existing files with report data **")
path_to_csv_file = data_path.get_path_to_csv_file_with_data_for_reporting()
if os.path.exists(path_to_csv_file):
    os.remove(path_to_csv_file)
    print("Existing csv file deleted")

path_to_txt_file = data_path.get_path_to_txt_file_with_data_for_reporting()
if os.path.exists(path_to_txt_file):
    os.remove(path_to_txt_file)
    print("Existing txt file deleted")

# Importing the cleaned data for visualizing
path_to_cleaned_data = data_path.get_path_to_cleaned_csv_file()
df = dcp.import_csv_to_df(path_to_cleaned_data, has_low_memory_option=False)

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
dv.print_to_csv_file(dv.get_unique_count_values_csv_row())
dv.print_to_csv_file(dv.table_data_with_label_row_ignored_to_csv(native_country_data))

# A view on the most represented occupations under high school grad
df_less_than_high_school_grad = df[df["Education-Num"] <= 9]
occupation_data_for_less_than_high_school_grad = dv.count_unique_values(df_less_than_high_school_grad, "Workclass", False)
   # To txt
dv.print_to_txt_file(os.linesep)
dv.print_to_txt_file("View over the most represented occupations under high school grad")
dv.print_to_txt_file(occupation_data_for_less_than_high_school_grad)
   # To csv
dv.print_to_csv_file("View over the most represented occupations under high school grad")
dv.print_to_csv_file(dv.get_unique_count_values_csv_row())
dv.print_to_csv_file(dv.table_data_with_label_row_ignored_to_csv(occupation_data_for_less_than_high_school_grad))

# A view over the most represented occupations with a master's degree
df_master_s_degree = df[df["Education-Num"] == 14]
occupation_data_for_master_s_degree = dv.count_unique_values(df_master_s_degree, "Workclass", False)
   # To txt
dv.print_to_txt_file(os.linesep)
dv.print_to_txt_file("View over the most represented occupations with a master's degree")
dv.print_to_txt_file(occupation_data_for_master_s_degree)
   # To csv
dv.print_to_csv_file("View over the most represented occupations with a master's degree")
dv.print_to_csv_file(",Unique Values,Count")
dv.print_to_csv_file(dv.table_data_with_label_row_ignored_to_csv(occupation_data_for_master_s_degree))

# A view over the most represented paycheck category for individuals with a master's degree
income_data_for_master_s_degree = dv.count_unique_values(df_master_s_degree, ">50K, <=50K", False)
   # To txt
dv.print_to_txt_file(os.linesep)
dv.print_to_txt_file("View over the most represented paycheck category for individuals with a master's degree")
dv.print_to_txt_file(income_data_for_master_s_degree)
   # To csv
dv.print_to_csv_file("View over the most represented paycheck category for individuals with a master's degree")
dv.print_to_csv_file(",Unique Values,Count")
dv.print_to_csv_file(dv.table_data_with_label_row_ignored_to_csv(income_data_for_master_s_degree))

# Verifying that all values for the column "Education" are unique for a given value of "Education-Num"
potential_values_for_education_num = df["Education-Num"].unique()
# For every values, verification that the corresponding values for "Education" are unique
for value in potential_values_for_education_num:
   education_num_group_data_for_specific_value = df[df["Education-Num"] == value]
   df_related_to_education_for_the_specific_value_of_eduction_num = education_num_group_data_for_specific_value["Education"]
   # Verifying the number of values available
   print(df_related_to_education_for_the_specific_value_of_eduction_num.unique())

# Issues encountered:
# DtypeWarning: Columns (76,89) have mixed types. Specify dtype option on import or set low_memory=False.
# return pd.read_csv(path_to_csv_file)
# -> Fixed by adding the low_memory option in the import_csv_to_df() method






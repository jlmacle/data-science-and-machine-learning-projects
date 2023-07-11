from ds_ml_utils.data_cleaning_and_processing import DataCleaningAndProcessing as dcp_class
from ds_ml_utils.data_visualization import DataVisualization as dv_class
from _DataPath import _DataPath as _data_path_class
import pandas as pd
import matplotlib.pyplot as plt
import os

_data_path = _data_path_class()
data_path = _data_path.get_data_path_object()
dcp = dcp_class()
dv = dv_class()

# Setting the folder path and csv/txt files names
dv.set_report_folder_path(data_path.get_path_to_folder_with_data_for_reporting())
dv.set_file_name_for_file_with_reporting_data_in_csv_format(data_path.get_file_name_for_csv_file_with_data_for_reporting())
dv.set_file_name_for_file_with_reporting_data_in_txt_format(data_path.get_file_name_for_txt_file_with_data_for_reporting())
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
df = dcp.import_csv_to_df(path_to_cleaned_data, low_memory_setting=False)

# Common to all reports
dv.simple_stats(df)

# Specific to this report

# A view on the most represented native countries
native_country_data = dv.count_unique_values(df, "native-country", False)
   # To txt
dv.print_to_txt_file("")
dv.print_to_txt_file("A view over the most represented native countries")
dv.print_to_txt_file(native_country_data)
   # To csv
dv.print_to_csv_file("A view over the most represented native countries")
dv.print_to_csv_file(dv.get_unique_count_values_csv_row())
# 1 row to ignore
dv.print_to_csv_file(dv.table_data_to_csv(native_country_data, 1))

# A view on the most represented occupations under high school grad
df_less_than_high_school_grad = df[df["education-num"] <= 9]
occupation_data_for_less_than_high_school_grad = dv.count_unique_values(df_less_than_high_school_grad, "workclass", False)
   # To txt
dv.print_to_txt_file("")
dv.print_to_txt_file("A view over the most represented workclasses under high school grad")
dv.print_to_txt_file(occupation_data_for_less_than_high_school_grad)
   # To csv
dv.print_to_csv_file("A view over the most represented workclasses under high school grad")
dv.print_to_csv_file(dv.get_unique_count_values_csv_row())
# 1 row to ignore
dv.print_to_csv_file(dv.table_data_to_csv(occupation_data_for_less_than_high_school_grad, 1))

# A view over the most represented occupations with a master's degree
df_master_s_degree = df[df["education-num"] == 14]
occupation_data_for_master_s_degree = dv.count_unique_values(df_master_s_degree, "workclass", False)
   # To txt
dv.print_to_txt_file("")
dv.print_to_txt_file("A view over the most represented workclasses with a master's degree")
dv.print_to_txt_file(occupation_data_for_master_s_degree)
   # To csv
dv.print_to_csv_file("A view over the most represented workclasses with a master's degree")
dv.print_to_csv_file(",Unique Values,Count")
# 1 row to ignore
dv.print_to_csv_file(dv.table_data_to_csv(occupation_data_for_master_s_degree, 1))

# A view over the most represented paycheck category for individuals with a master's degree
income_data_for_master_s_degree = dv.count_unique_values(df_master_s_degree, ">50K__<=50K", False)
   # To txt
dv.print_to_txt_file("")
dv.print_to_txt_file("A view over the most represented paycheck category for individuals with a master's degree")
dv.print_to_txt_file(income_data_for_master_s_degree)
   # To csv
dv.print_to_csv_file("A view over the most represented paycheck category for individuals with a master's degree")
dv.print_to_csv_file(",Unique Values,Count")
# 1 row to ignore
dv.print_to_csv_file(dv.table_data_to_csv(income_data_for_master_s_degree, 1))

#  With 'education-num' and 'Education' as first colums,
#  using the values of column '>50K, <=50K' to create new columns
pivot_table = pd.pivot_table(df, index=['education-num','education'], columns='>50K__<=50K', aggfunc='size', fill_value=0)
pivot_table.columns = ['<=50K', '>50K']
   # To txt
dv.print_to_txt_file("")
dv.print_to_txt_file("A view on 'education-num','education', '>50K' and '<=50K'")
dv.print_to_txt_file(pivot_table)
   # To csv
dv.print_to_csv_file("")
dv.print_to_csv_file("A view on 'education-num'_'education'_and_'>50K' and '<=50K'")
# 2 rows to ignore
dv.print_to_csv_file(dv.table_data_to_csv(pivot_table, 2))


pd.set_option('display.max_rows', None)
# With 'Workclass' and 'Occupation' as first columns,
# using the values of column '>50K, <=50K' to create new columns
pivot_table = pd.pivot_table(df, index=['occupation'], columns='>50K__<=50K', aggfunc='size', fill_value=0)
pivot_table.columns = ['<=50K', '>50K']
pivot_table = pivot_table.sort_values(by=['>50K'], ascending=False)
   # To txt
dv.print_to_txt_file("")
dv.print_to_txt_file("A view on 'Occupation', '>50K' and '<=50K'")
dv.print_to_txt_file(pivot_table)
   # To csv
dv.print_to_csv_file("")
dv.print_to_csv_file("A view on 'Occupation'_and_'>50K' and '<=50K'")
# 2 rows to ignore
dv.print_to_csv_file(dv.table_data_to_csv(pivot_table, 2))

# Bar chart creation
path_to_image = os.path.join(data_path.get_path_to_folder_with_data_for_reporting(),'IncomeDistributionByOccupation.png')
if not os.path.exists(path_to_image):
   fig, ax = plt.subplots(figsize=(10, 6))
   pivot_table.sort_values(by=['>50K'], ascending=False).plot(kind='bar', ax=ax)
      # Setting the plot labels and title
   ax.set_xlabel('Occupation')
   ax.set_ylabel('Count')
   ax.set_title('Income Distribution by Occupation')
      # Rotate the x-axis labels for better readability
   plt.xticks(rotation=45)
      # Display the plot
   plt.show()
   fig.savefig(path_to_image)

 
# Issues encountered:
# DtypeWarning: Columns (76,89) have mixed types. Specify dtype option on import or set low_memory=False.
# return pd.read_csv(path_to_csv_file)
# -> Fixed by adding the low_memory option in the import_csv_to_df() method






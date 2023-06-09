'''
NOTE: I did the exploratory analysis while working on 1.DataCleaningAndProcessing.py.
Adding 0.ExploratoryAnalysis.py to have a more rigorous process.
Currently re-writing code in both files.
'''
from ds_ml_utils.exploratory_analysis import ExploratoryAnalysis as ea_class
from ds_ml_utils.data_cleaning_and_processing import DataCleaningAndProcessing as dcp_class
from ds_ml_utils.data_visualization import DataVisualization as dv_class
from _DataPath import _DataPath as _data_path_class
import pandas as pd
import os


# Cleaning the data before processing
ea = ea_class()
dcp = dcp_class()
dv = dv_class()
_data_path = _data_path_class()
data_path = _data_path.get_data_path_object()

df = pd.read_csv(os.path.join(data_path.get_path_to_data_folder(), data_path.get_file_name_for_csv_with_original_data()),low_memory=False)

# EA1 : only 1 null value in the "Age" column
# Dropping the line
print("--> Dropping the line with the NaN value in the 'Age' column")
df = df.dropna()

print("--> Dropping the potentially duplicate lines")
df = df.drop_duplicates()

# Headers processing
#EA2, EA3, EA4
df = dcp.trim_concatenate_lower_case_header_content(df, separator_to_replace_space="-")
#EA5
print("--> Renaming '>50k,-<=50k' into '>50K__<=50K'")
df = df.rename(columns={">50k,-<=50k":">50K__<=50K"})
# Printing every column names, in alphabetical order, with a line break after each column name
column_names_list_for_visual_inspection = ea.list_vertically_with_separator_to_string(df.columns.to_list(), "*")
print("".join(column_names_list_for_visual_inspection))

# Cells processing
#EA6
df = dcp.cells_processing_basic(df, separator_to_replace_space="_")

#EA7: removing the row with the 99999 value in capital-gain
print("--> Removing the row with the 99999 value in capital-gain")
df = df[df["capital-gain"] != 99999]

#EA8
# Replacing "South" with "South Korea" in the "native-country" column 
print("--> Replacing 'South' with 'South Korea' in the 'native-country' column")  
df["native-country"] = df["native-country"].str.replace( "South", "South Korea")

#EA9 : Removing the rows containing "Hong" in the "native-country" column
print("--> Removing the rows containing 'Hong' in the 'native-country' column")
df = df[df["native-country"] != "Hong"]

# Pre-cleaning before using a pivot table
#EA10
results = dcp.pre_pivot_table_cleaning_need_detection(df, "education-num", "education",print_data_for_unique_values=False)
# df is untouched by this step
print("--> Education data in need of cleaning")
print(results)
# Using the previous results to locate the rows with the data anomalies
if(results != {}):
    print()
    lines = dcp.line_finding_given_labels_and_column(df,"education", ["Bachelors2", "Masters2","Some-college2"])
    print(lines)
    print()
    print("""** Todo: line cleaning in Data-automatically_cleaned-Potential_need_to_add_a_manual_cleaning.csv if neccessary, 
    then file saving as Cleaned_data.csv **""")
    print()

df.to_csv(os.path.join(data_path.get_path_to_data_folder(),"Data-automatically_cleaned-Potential_need_to_add_a_manual_cleaning.csv"), index=False)

# TODO : re-run the exploratory analysis



    





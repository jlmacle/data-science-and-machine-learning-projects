'''
NOTE: I did the exploratory analysis while working on 1.DataCleaningAndProcessing.py.
Adding 0.ExploratoryAnalysis.py to have a more rigorous process.
Currently re-writing code in both files.

Also, I sometimes choose to use Pandas and not the methods from ds_ml_utils
in order to practice using Pandas.
'''


'''
To fix:
1. A null value in the "Age" column
Headers:
   2 A trimming issue *    Workclass*
   3 Inconsistency in the use of word separators: *Hours-per-week* vs  *Marital status*
   4 Spaces in the column names preventing the use of df.column_name
   5 A column name with a comma in it: *>50K, <=50K*, an issue when generating data toward a csv file
6. Data trimming to do in the unique values
7. A 99999 capital gain that seems unrealistic
8. "Hong" alone appears 20 times in the "Country" column. "Hong Kong" does not appear.
   Planning to search data about the main immigrant nationalities 
   before replacing by Hong Kong (or South Korea. See 10.)
9. "South" alone appears 80 times in the "Country" column. "South Korea" does not appear.
10. Some education labels had been duplicated on purpose to test a cleaning method
   They appear in the data to clean.

'''
from ds_ml_utils.exploratory_analysis import ExploratoryAnalysis as ea_class
from ds_ml_utils.data_cleaning_and_processing import DataCleaningAndProcessing as dcp_class
from _DataPath import _DataPath as _data_path_class
ea = ea_class()
dcp = dcp_class()
_data_path = _data_path_class()
data_path = _data_path.get_data_path_object()

import os
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = dcp.import_csv_to_df(data_path.get_path_to_original_csv_file(),low_memory_setting=False)

# Dataframe shape
print()
print("Dataframe shape: ", df.shape)
print()

# Dataframe info
print("Location of null values: ")
mask = df.isnull().sum() != 0
serie = df.isnull().sum()
null_values_only = serie[mask]
print(null_values_only)
print()

# Data types
print("Data types: ", df.dtypes.unique())   #df.dtypes is of type Series
print()  #https://pandas.pydata.org/docs/reference/api/pandas.Series.html
                                  
# Printing every column names, in alphabetical order, with a line break after each column name
column_names_list_for_visual_inspection = ea.list_vertically_with_separator_to_string(df.columns.to_list(), "*")
print("".join(column_names_list_for_visual_inspection))

# Printing the unique values for each column to a file
# to check for potential mispellings, or other issues
ea.print_unique_values_to_file(df, os.path.join(data_path.get_path_to_folder_with_data_for_exploratory_analysis(),"unique_values.txt"))
  # Searching more info about "Kong" and "South" in the df
print("Searching more info about 'Hong' and 'South' in the df")
  # Searching how many times "Hong" is alone in the cell
  # and how many times other words are in the cell
  # (same for "South")
mask_Hong_in_cell = df["Native country"].str.contains("Hong")
mask_South_in_cell = df["Native country"].str.contains("South")
# Series with the unique values and the count of each value 
print('df["Native country"][mask_Hong_in_cell].value_counts()')
df_Hong = df["Native country"][mask_Hong_in_cell].value_counts()
print(df_Hong)
print()
print('df["Native country"][mask_South_in_cell].value_counts()')
df_South = df["Native country"][mask_South_in_cell].value_counts()
print(df_South)



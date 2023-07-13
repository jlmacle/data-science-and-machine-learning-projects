'''
NOTE: I did the exploratory analysis while working on 1.DataCleaningAndProcessing.py.
Adding 0.ExploratoryAnalysis.py to have a more rigorous process.
Currently re-writing code in both files.

Also, I sometimes choose to use Pandas and not the methods from ds_ml_utils to practice using Pandas.
'''

'''
Notes:
- 86 000+ null values in every column
- All columns are of type object


'''

from ds_ml_utils.data_cleaning_and_processing import DataCleaningAndProcessing as dcp_class
from ds_ml_utils.exploratory_analysis import ExploratoryAnalysis as ea_class
from _DataPath import _DataPath as _data_path_class
_data_path = _data_path_class()
data_path = _data_path.get_data_path_object()
dcp = dcp_class()
ea = ea_class()

df = dcp.import_csv_to_df(data_path.get_path_to_original_csv_file(),low_memory_setting=False)

# Dataframe shape
print()
print("Dataframe shape: ", df.shape)
print()

# Location of null values
print("Location of null values: ")
null_value_series = df.isnull().sum()
print(type(null_value_series))
print(df.isnull().sum())
print()

# Data types
print("Data types: ", df.dtypes.unique())
print()

# Printing every column name in alphabetical order, with delimiters, with a line break after each column name 
column_names_list_for_visual_inspection = ea.list_vertically_with_separator_to_string(df.columns.to_list(), "*")
print("".join(column_names_list_for_visual_inspection))
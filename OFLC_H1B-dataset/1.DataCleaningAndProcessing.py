from ds_ml_utils.data_cleaning_and_processing import DataCleaningAndProcessing as dcp_class
from ds_ml_utils.data_visualization import DataVisualization as dv_class
from _DataPath import _DataPath as _data_path_class
import os

# Cleaning the data before processing
dcp = dcp_class()
dv = dv_class()
_data_path = _data_path_class()
data_path = _data_path.get_data_path_object()

"""
    The dataset has been filtered manually to keep only job titles related to computers.
    Doing so left some of the rows with only commas.
"""

# 1. Data imports
path_to_csv_folder = data_path.get_path_to_data_folder()
filtered_data_file_name = data_path.get_file_name_for_csv_with_original_data()

# 2. Data encoding fixing 
    # Issue encountered when running the remove_rows_with_commas_only() method:
    # File "C:\Python311\Lib\encodings\cp1252.py", line 23, in decode
    # return codecs.charmap_decode(input,self.errors,decoding_table)[0]
    # UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 5408: character maps to <undefined> 
    # --> Fixed by converting the file to utf-8 in reading and writing in the method remove_rows_with_commas_only()

# 3. Row removals
cleaned_file_name = dcp.remove_rows_with_commas_only(path_to_csv_folder, filtered_data_file_name, 9)
#  Keeping with empty data, as this is not an issue for the analysis
#  Actually removing the rows with empty data would prevent the analysis of the data

# 4. Column cell content concatenation
path_to_cleaned_data = os.path.join(data_path.get_path_to_data_folder(), cleaned_file_name)
df = dcp.import_csv_to_df(path_to_cleaned_data,low_memory_setting=False)
df = dcp.concatenate_words_in_column_cells(df,"JOB_TITLE", "_")

# 5. Trimming the column names and the column cells
# TODO : to finish
df = dcp.trim_cells_content(df)

path_to_new_cleaned_data = path_to_cleaned_data.split(".")[0] + "-Job_titles_concatenated.csv"
df.to_csv(path_to_new_cleaned_data, index=True)
# New value for self.data_path.set_file_name_for_csv_with_cleaned_data
# set in _DataPath.py







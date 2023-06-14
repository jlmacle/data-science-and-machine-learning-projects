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

# # Data imports
path_to_csv_folder = data_path.get_path_to_data_folder()
original_and_filtered_data_file_name = data_path.get_file_name_for_csv_with_original_data()

# # Data encoding fixing 
    # Issue encountered when running the remove_rows_with_commas_only() method:
    # File "C:\Python311\Lib\encodings\cp1252.py", line 23, in decode
    # return codecs.charmap_decode(input,self.errors,decoding_table)[0]
    # UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 5408: character maps to <undefined> 
    # --> Fixed by converting the file to utf-8 in reading and writing in the method remove_rows_with_commas_only()

# # Row removals
df = dcp.remove_rows_with_commas_only(path_to_csv_folder, original_and_filtered_data_file_name, 9, low_memory_setting=False)
#  Keeping with empty data, as this is not an issue for the analysis
#  Actually removing the rows with empty data would prevent the analysis of the data

# # Headers processing
print()
df = dcp.header_processing(df, separator_to_replace_space="-")

# # Cells processing
df = dcp.cells_processing(df, separator_to_replace_space="_")
df.to_csv(os.path.join(data_path.get_path_to_data_folder(),"cleaned_data.csv"), index=False)





from ds_ml_utils.data_cleaning_and_processing import DataCleaningAndProcessing as dcp_class
from ds_ml_utils.data_visualization import DataVisualization as dv_class
from _DataPath import _DataPath as _data_path_class
import os

dcp = dcp_class()
dv = dv_class()
_data_path = _data_path_class()
data_path = _data_path.get_data_path_object()
projects_folder = "data-science-and-machine-learning-projects"

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
df = dcp.drop_duplicates_and_remove_rows_with_only_empty_data_from_df(path_to_csv_folder, original_and_filtered_data_file_name, low_memory_setting=False)
df = dcp.removes_rows_with_empty_data_from_column(df, "WAGE_RATE_OF_PAY_TO")
#  Keeping some of the rows with empty data, as this is not an issue for the analysis
#  Actually, removing the rows with empty data would prevent the analysis of the data

# # Headers processing
print()
df = dcp.header_processing(df, separator_to_replace_space="-")

# # Cells processing
df = dcp.cells_processing_basic(df, separator_to_replace_space="_")
df = dcp.cells_processing_to_uppercase_in_column(df, "JOB_TITLE")
    # Converting amount in $ to float
df = dcp.from_dollar_strings_to_floats(df, "WAGE_RATE_OF_PAY_TO")

# Pattern removal
print("--> Removing patterns of data in the JOB_TITLE column")
   # Removing patterns similar to _(017040.000997) 
pattern = r"_\(\d+\.\d+\)"
df = dcp.remove_pattern_from_column(df, "JOB_TITLE", pattern)
   # Removing patterns similar to _(017040000997)
pattern = r"_\(\d+\)"
df = dcp.remove_pattern_from_column(df, "JOB_TITLE", pattern)
    # Removing patterns similar to _(017040.000997.000997)
pattern = r"_\(\d+\.\d+\.\d+\)"
df = dcp.remove_pattern_from_column(df, "JOB_TITLE", pattern)

# # Storing words related to the job titles in a trie
trie = dcp.get_trie_with_words_from_column(df, "JOB_TITLE",'_')
data = trie.print_alphabetical_to_string()
file_name = "words_in_trie.txt"
file_name_with_data_about_trie = "data about trie.txt"
nbr_of_words_in_trie = trie.get_nbr_of_words()
path_to_words_in_trie = os.path.join(data_path.get_path_to_folder_with_data_for_reporting(),file_name)
dv.print_to_specified_txt_file(data,path_to_words_in_trie, 'w')
short_path = path_to_words_in_trie.split(projects_folder)[1]
print(f"--> Storing words related to the job titles, and splitted with '_', in {short_path}")
# print("-----> Number of words in the trie: ", nbr_of_words_in_trie)
# To understand: the inconsistency between the number of words in the trie and the number of words in the file
# dv.print_to_specified_txt_file("Initial nbr of words in trie : "+str(nbr_of_words_in_trie),os.path.join(data_path.get_path_to_folder_with_data_for_reporting(),file_name_with_data_about_trie), 'w')
path_to_file_with_data_about_trie = os.path.join(data_path.get_path_to_folder_with_data_for_reporting(),file_name_with_data_about_trie)

path_to_cleaned_data = os.path.join(data_path.get_path_to_data_folder(),data_path.get_file_name_for_csv_with_cleaned_data())
print("Saving the cleaned data to: ", path_to_cleaned_data)
df.to_csv(path_to_cleaned_data, index=False)






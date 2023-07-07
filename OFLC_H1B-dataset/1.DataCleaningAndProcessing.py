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

line_numbers_before_cleaning = 0
line_numbers_after_cleaning = 0
data_removed = []


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
line_numbers_before_cleaning = df.shape[0]


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
    # Removing patterns similar to _(017040.000997.000997)
pattern = r"_\(\d+\.\d+\.\d+\)"
df = dcp.remove_pattern_in_column(df, "JOB_TITLE", pattern)

   # Removing patterns similar to _(017040.000997) 
pattern = r"_\(\d+\.\d+\)"
df = dcp.remove_pattern_in_column(df, "JOB_TITLE", pattern)

   # Removing patterns similar to _(017040000997)
pattern = r"_\(\d+\)"
df = dcp.remove_pattern_in_column(df, "JOB_TITLE", pattern)

    # Removing patterns similar to (_20637.580)
pattern = r"\(\_\d+\.\d+\)"
df = dcp.remove_pattern_in_column(df, "JOB_TITLE", pattern)

    # Removing patterns similar to _20637.235.7
pattern = r"\_\d+\.\d+\.\d+"
df = dcp.remove_pattern_in_column(df, "JOB_TITLE", pattern)

    # Removing patterns similar to _017040.001775
pattern = r"\_\d+\.\d+"
df = dcp.remove_pattern_in_column(df, "JOB_TITLE", pattern)

    # Removing patterns similar to _[00040133]
pattern = r"\_\[\d+\]"
df = dcp.remove_pattern_in_column(df, "JOB_TITLE", pattern)
 
    # Changing TIER_2 to TIER2 in preparation for the next pattern removal
    # ChatGPT 23/07
    # In the code above, 
    # we use the regular expression pattern r'TIER_(\d)' to match "TIER_" 
    # followed by a digit. 
    # The parentheses (\d) create a capturing group 
    # to capture the digit for use in the replacement.
    # The replacement pattern r'TIER\1' uses \1 
    # to refer to the captured digit from the pattern. 
    # This allows us to replace "TIER_" and the following digit 
    # with "TIER" followed by the same digit.
pattern = r'TIER_(\d)'
replacement = r'TIER\1'
df = dcp.replace_pattern_in_column(df, "JOB_TITLE", pattern, replacement)

    # Removing patterns similar to _4
pattern = r"\_\d+$"
dcp.remove_pattern_in_column(df, "JOB_TITLE", pattern)

    # Replacing ENGINEER_(digit) with ENGINEER_
    # Found in data :
    # ENGINEER_4_PRODUCT_DEVELOPMENT_ENGINEERING
    # ENGINEER_4_NETWORK_ENGINEERING
pattern = r"ENGINEER_\d_"
replacement = "ENGINEER_"
df = dcp.replace_pattern_in_column(df, "JOB_TITLE", pattern, replacement)

    # Replacing MANAGER_(digit) with MANAGER_
    # Found in data :
    # MANAGER_1_SOFTWARE_DEVELOPMENT_&_ENGINEERING
    # MANAGER_1_ENTERPRISE_DATA_ENGINEERING
pattern = r"MANAGER_\d_"
replacement = "MANAGER_"
df = dcp.replace_pattern_in_column(df, "JOB_TITLE", pattern, replacement)

    # Replacing ARCHITECT_(digit) with ARCHITECT_
    # Found in data :
    # ARCHITECT_5_SOFTWARE_ARCHITECTURE 
    # ARCHITECT_4_SOFTWARE_DEVELOPMENT_&_ENGINEERING 
pattern = r"ARCHITECT_\d_"
replacement = "ARCHITECT_"
df = dcp.replace_pattern_in_column(df, "JOB_TITLE", pattern, replacement)

    # Replacing PROFESSIONAL_(digit) with PROFESSIONAL_
    # Found in data :
    # PROFESSIONAL_5_INFORMATION_TECHNOLOGY
    # PROFESSIONAL_4_INFORMATION_TECHNOLOGY
pattern = r"PROFESSIONAL_\d_"
replacement = "PROFESSIONAL_"
df = dcp.replace_pattern_in_column(df, "JOB_TITLE", pattern, replacement)

    # Replacing DEVELOPER_(digit) with DEVELOPER_
    # Found in data :
    # DEVELOPER_4_SYSTEMS_SOFTWARE
    # DEVELOPER_4_APPLICATION_DEVELOPMENT
pattern = r"DEVELOPER_\d_"
replacement = "DEVELOPER_"
df = dcp.replace_pattern_in_column(df, "JOB_TITLE", pattern, replacement)

    # Replacing ANALYST_(digit) with ANALYST_
    # Found in data :
    # ANALYST_5_IT_SECURITY
    # ANALYST_5_PROGRAMMING
pattern = r"ANALYST_\d_"
replacement = "ANALYST_"
df = dcp.replace_pattern_in_column(df, "JOB_TITLE", pattern, replacement)


    # Replacing DIRECTOR_(digit) with DIRECTOR_
    # Found in data :
    # DIRECTOR_1_PROGRAM_MANAGEMENT
    # DIRECTOR_1_SOFTWARE_DEVELOPMENT_&_ENGINEERING
pattern = r"DIRECTOR_\d_"
replacement = "DIRECTOR_"
df = dcp.replace_pattern_in_column(df, "JOB_TITLE", pattern, replacement)


    # Changing DAT_3.X to DAT3.X
pattern = r"DAT\_3\.X"
replacement = "DAT3.X"
df = dcp.replace_pattern_in_column(df, "JOB_TITLE", pattern, replacement)


# reviewed until this point
    # Removing patterns similar to APPLICATION_DEVELOPMENT_AND_SWIFT_INTEGRATION_LEAD_00045446
    # Minding to keep these patterns untouched:
    # MANAGER_2_SOFTWARE_DEVELOPMENT_AND_ENGINEERING
    # ENGINEER_4_PRODUCT_DEVELOPMENT_AND_ENGINEERING
    # SENIOR_5G_RAN_SYSTEMS_ENGINEER
    # SOFTWARE_DEVELOPMENT_&_ENGINEERING
    # SENIOR_ANALYST_PAYROLL_APPLICATIONS_(LEVEL_3)
pattern = r"\_\d+"
dcp.locate_pattern_in_column(df, "JOB_TITLE", pattern)



# Unfinished work in progress
# # Pattern location : non-word characters


# To process later:
# SOFTWARE_ENGINEER_[5103_SOFTWARE_DEVELOPMENT_ENGINEER_3]
# _OFFICE_365
# SR. SR SENIOR
# SOFT.   _-_   _-    _/_   ACHITECT

# To add at the end: a trimming of '_'

# # Storing words related to the job titles in a trie
trie = dcp.get_trie_with_words_from_column(df, "JOB_TITLE",'_')
data = trie.print_alphabetical_to_string()
file_name = "words_in_trie.txt"
file_name_with_data_about_trie = "data about trie.txt"
nbr_of_words_in_trie = trie.get_nbr_of_words()
path_to_words_in_trie = os.path.join(data_path.get_path_to_folder_with_data_for_reporting(),file_name)
dv.print_to_specified_txt_file(data,path_to_words_in_trie, 'w')
short_path = path_to_words_in_trie.split(projects_folder)[1]
print(f"--> Storing words related to the job titles ( pattern removed ), and splitted with '_', in {short_path}")
# print("-----> Number of words in the trie: ", nbr_of_words_in_trie)
# To understand: the inconsistency between the number of words in the trie and the number of words in the file
# dv.print_to_specified_txt_file("Initial nbr of words in trie : "+str(nbr_of_words_in_trie),os.path.join(data_path.get_path_to_folder_with_data_for_reporting(),file_name_with_data_about_trie), 'w')
path_to_file_with_data_about_trie = os.path.join(data_path.get_path_to_folder_with_data_for_reporting(),file_name_with_data_about_trie)

path_to_cleaned_data = os.path.join(data_path.get_path_to_data_folder(),data_path.get_file_name_for_csv_with_cleaned_data())
print("--> Saving the cleaned data to: ", path_to_cleaned_data)
df.to_csv(path_to_cleaned_data, index=False)

line_numbers_after_cleaning = df.shape[0]
print(f'''--> About the cleaning:
      \t Number of rows before cleaning:  {line_numbers_before_cleaning}
      \t Number of rows after cleaning:   {line_numbers_after_cleaning}
      \t Data removed: {data_removed}''')






from ds_ml_utils.data_cleaning_and_processing import DataCleaningAndProcessing as dcp_class
from ds_ml_utils.data_visualization import DataVisualization as dv_class
from _DataPath import _DataPath as _data_path_class
import os


# Cleaning the data before processing
dcp = dcp_class()
dv = dv_class()
_data_path = _data_path_class()
data_path = _data_path.get_data_path_object()

# # Removing rows with duplicates and unvavailable data 
df  = dcp.drop_duplicates_and_remove_rows_with_data_unavailable_from_csv_file(data_path.get_path_to_data_folder(), data_path.get_file_name_for_csv_with_original_data(),low_memory_setting=False)

# # Headers processing
print()
df = dcp.header_processing(df, separator_to_replace_space="-")
df = df.rename(columns={">50K,-<=50K":">50K__<=50K"})

# # Cells processing
df = dcp.cells_processing(df, separator_to_replace_space="_")
df.to_csv(os.path.join(data_path.get_path_to_data_folder(),"adult-Automatically_cleaned-Potential_need_to_add_a_manual_cleaning.csv"), index=False)

# # Pre-cleaning before using a pivot table
# File used : adult_na_and_duplicates_removed.csv
results = dcp.pre_pivot_table_cleaning_need_detection(df, "Education-Num", "Education",print_data_for_unique_values=False)
# df is untouched by this step
print("--> Education data in need of cleaning")
print(results)
# Using the previous results to locate the rows with the data anomalies
if(results != {}):
    print()
    lines = dcp.line_finding_given_labels_and_column(df,"Education", ["Bachelors2", "Masters2","Some-college2"])
    print()
    print("""** Todo: copy and pasting of adult-Automatically_cleaned-Potential_need_to_add_a_manual_cleaning.csv, 
    line cleaning if neccessary, 
    saving the copied and pasted file as adult-cleaned_data.csv **""")
    print()



    





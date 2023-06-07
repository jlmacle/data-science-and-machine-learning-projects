from jl_ml_utils.data_cleaning_and_processing import DataCleaningAndProcessing as dcp_class
from jl_ml_utils.data_visualization import DataVisualization as dv_class
from _DataPath import _DataPath as _data_path_class


# Cleaning the data before processing
dcp = dcp_class()
dv = dv_class()
_data_path = _data_path_class()
data_path = _data_path.get_data_path_object()

# Removing rows with duplicates and unvavailable data 
dcp.drop_duplicates_and_remove_rows_with_data_unavailable_from_csv_file(data_path.get_path_to_csv_folder(), data_path.get_file_name_for_csv_with_original_data(),low_memory_setting=False)

df= dcp.import_csv_to_df( data_path.get_path_to_cleaned_csv_file(),low_memory_setting=False)
# Pre-cleaning before using a pivot table
results = dcp.pre_pivot_table_pre_cleaning(df, "Education-Num", "Education",print_data_for_unique_values=False)
print(results)
# Using the previous results to locate the rows with missing data
lines = dcp.line_finding_given_labels_and_column(df,"Education", [" Bachelors2", " Masters2"," Some-college2"])



# Cleaning the data and re-setting the value for the cleaned data file name

    





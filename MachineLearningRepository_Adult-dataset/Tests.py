from _DataPath import _DataPath as data_path_class 
from jl_ml_utils.data_cleaning_and_processing import DataCleaningAndProcessing as dcp_class
from jl_ml_utils.data_visualization import DataVisualization as dv_class
import os

data_path = data_path_class()
dcp = dcp_class()
dv = dv_class()

# Getting the dataframe
df = dcp.import_csv_to_df(data_path.get_path_to_cleaned_csv_file(),hasLowMemoryOption=False)

print(df.describe())

print(os.linesep)
stats = df.describe().values.tolist()
print(dv.print_describe_nested_list_to_csv_string(stats))

# No extra line needed
data = dv.count_unique_values(df, "Native country", is_order_ascending=False)
print(data)

print(os.linesep)
print(dv.table_data_with_label_row_ignored_to_csv(data))



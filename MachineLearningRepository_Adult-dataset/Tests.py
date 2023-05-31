from _DataPath import _DataPath as data_path_class 
from jl_ml_utils.data_cleaning_and_processing import DataCleaningAndProcessing as dcp_class
from jl_ml_utils.data_visualization import DataVisualization as dv_class
import os

data_path = data_path_class()
dcp = dcp_class()
dv = dv_class()

# Getting the dataframe
df = dcp.import_csv_to_df(data_path.get_path_to_cleaned_csv_file())
'''
print(df.describe())

print(os.linesep)
stats = df.describe().values.tolist()
print(dv.print_describe_nested_list_to_csv_string(stats))

# No extra line needed
data = dv.count_unique_values(df, "Native country", False)
print(data)

print(os.linesep)
print(dv.table_data_with_label_row_ignored_to_csv(data))
'''

# # Filter the DataFrame to include only data for 12th grade and below
# filtered_df = df[df['Education'].isin(['6th', '7th', '8th', '9th', '10th', '11th', '12th'])]
# print(filtered_df.head())
# # Access the 'workclass' column in the filtered DataFrame
# workclass_data = filtered_df['Workclass']
# # Print the workclass data
# print(workclass_data)

df_tmp = df.isin(['6th', '7th', '8th', '9th', '10th', '11th', '12th'])
print(df_tmp)
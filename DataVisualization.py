from jl_ml_utils.data_cleaning_and_processing import DataCleaningAndProcessing as dcp_class
from jl_ml_utils.data_visualization import DataVisualization as dv_class
from _DataPath import _DataPath as data_path_class
import os

# Planning a data exploration based on unsupervised learning and visualization
data_path = data_path_class()
dcp = dcp_class()
dv = dv_class()

# Importing the cleaned data for visualizing
# data_array = dcp.import_csv_to_numpy_array(data_path.get_path_to_cleaned_csv_file())
dataframe = dcp.import_csv_to_dataframe(data_path.get_path_to_cleaned_csv_file())

dv.simple_stats(dataframe)

# dv.histogram(dataframe, "Native country")



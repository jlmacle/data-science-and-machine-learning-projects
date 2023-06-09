from _DataPath import _DataPath as data_path_class 
from jl_ds_ml_utils.data_cleaning_and_processing import DataCleaningAndProcessing as dcp_class
from jl_ds_ml_utils.data_reporting_ReportLab_Archivedg import DataReporting as dr_class
from jl_ds_ml_utils.data_visualization import DataVisualization as dv_class

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import os

data_path = data_path_class()
dcp = dcp_class()
dv = dv_class()
dr = dr_class()

############################################################################################
# Function used to split the data returned by the count_unique_values function
# while making sure to control the tabulation within a line
# Printing line by line in the pdf was showing that the tabulation was lost
def tabulation_rebuild(data_array, tabulation_nbr1, tabulation_nbr2):
    new_array = []
    for line in data_array:
        elements_array = line.split()
        # Creating the string from the elements, while adding the number of tabulations needed
        new_line = elements_array[0]+'\n'+elements_array[1]+'\t'+elements_array[2]
        new_array.append(new_line)
    return new_array

# Setting font data
pdfmetrics.registerFont(TTFont('Arial','Arial.ttf'))

# Setting the report path related data
dr.set_report_folder_path(os.path.join(os.getcwd(),"data_report"))
dr.set_pdf_report_file_name("data_report.pdf")

# Getting the dataframe
df = dcp.import_csv_to_df(data_path.get_path_to_cleaned_csv_file())

# Setting the margin and spacing to use
top_margin = 100
dr.set_margin_from_left_side(100)
dr.set_margin_from_top(top_margin)
dr.set_spacing_between_inputs(20)

# Setting the writer
dr.set_pdf_writer()

# Setting the metadata
dr.set_metadata_title("Machine Learning Repository : Adult dataset")
dr.set_metadata_author("Jean-Louis Macle")


# Section 1 : Title, date and author
dr.set_font("Arial", 20)
dr.set_title()
dr.add_string_data("", top_margin, y_increment=1)
dr.set_font("Arial", 16)
dr.set_date()
dr.set_author()
dr.add_page_number()
dr.finish_page()

# Section 2 : Overview of some of the column data
    # Overview of the count for each native country value
    # 41 lines in the data to add to the page
    # After 30 lines, I should split to a new page
data_array = dv.count_unique_values(df, 'Native country', is_order_ascending=False)
# 05/25 : tabulation is lost when printing the data
# Using a utility function to rebuild the tabulation for each line
# Code failing. Adds black squares while ingnoring the tabulation usual behavior
#data_array = tabulation_rebuild(data_array, 4, 4)
for i,line in enumerate(data_array):
    print(line)
    dr.add_string_data(str(line), top_margin, y_increment=i+1)
   
# dr.add_string_data(str(dv.count_unique_values(df, 'Native country', is_order_ascending=False)), top_margin , y_increment=1)

dr.add_page_number()
dr.finish_page() 

# Saving the report
dr.finish_document()





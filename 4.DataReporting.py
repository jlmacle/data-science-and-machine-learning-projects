from _DataPath import _DataPath as data_path_class 
from jl_ml_utils.data_cleaning_and_processing import DataCleaningAndProcessing as dcp_class
from jl_ml_utils.data_reporting import DataReporting as dr_class
from jl_ml_utils.data_visualization import DataVisualization as dv_class

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import os

data_path = data_path_class()
dcp = dcp_class()
dv = dv_class()
dr = dr_class()

# Setting font data
pdfmetrics.registerFont(TTFont('Arial','Arial.ttf'))

# Setting the report path related data
dr.set_report_folder_path(os.path.join(os.getcwd(),"data_report"))
dr.set_pdf_report_file_name("data_report.pdf")

# Getting the dataframe
df = dcp.import_csv_to_df(data_path.get_path_to_cleaned_csv_file())

# Setting the margin and spacing to use
dr.set_margin_from_left_side(100)
dr.set_margin_from_top(100)
dr.set_spacing_between_inputs(20)

# Setting the writer
dr.set_pdf_writer()

# Setting the metadata
dr.set_metadata_title("Machine Learning Repository : Adult dataset")
dr.set_metadata_author("Jean-Louis Macle")


# Section 1 : Title, date and author
dr.set_font("Arial", 20)
dr.set_title()
dr.add_string_data("", y_increment=1)
dr.set_font("Arial", 16)
dr.set_date()
dr.set_author()
dr.add_page_number()
dr.finish_page()

# Section 2 : Overview of some of the column data
    # Overview of the count for each native country value
# dr.add_string_data(dv.count_unique_values(df, 'Native country', is_order_ascending=False), y_increment=1)
dr.add_page_number()
dr.finish_page() 

# Saving the report
dr.finish_document()



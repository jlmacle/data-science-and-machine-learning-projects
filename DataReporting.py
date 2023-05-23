from jl_ml_utils.data_reporting import DataReporting as dr_class

import os

dr = dr_class()

dr.set_report_folder_path(os.path.join(os.getcwd(),"data_report"))
dr.set_pdf_report_file_name("data_report.pdf")
dr.set_title("Machine Learning Repository : Adult dataset")
dr.set_margin_from_left_side(100)
dr.set_margin_from_top(700)
dr.set_spacing_between_inputs(20)

dr.generate_pdf_report()


''' 
The statement import sys in Python imports the sys module, which provides access to system-specific parameters 
and functions. This module allows interaction between a Python program and the Python interpreter, 
as well as the underlying operating system environment. 

'''
import sys
import traceback

class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = self.get_detailed_error_message(error_message, error_details)

    def get_detailed_error_message(self, error_message, error_details: sys):
        _, _, exc_tb = error_details.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        detailed_message = f"Error occurred in file '{file_name}' at line {line_number}: {error_message}"
        return detailed_message

    def __str__(self):
        return self.error_message

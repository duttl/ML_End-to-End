import sys

def error_message_detail(error, error_detail:sys): # we call this function whenever an error is raised
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename # to get the file name from the exception error
    error_message = "Error occured in python script [{0}] line number [{1} error messsage [{2}]]".format(
        file_name, exc_tb.tb_lineno, str(error))
    return error_message
    

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
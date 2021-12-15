import os, sys
from flask import jsonify
import ast 
import base64
import re

from datetime import datetime


def send_error_msg(): 
    return jsonify({'error_msg':'Internal Server Error'}), 505

def parse_dictionary(data):
    return (ast.literal_eval(data))    


def send_sucess_msg(response,**kwargs):
    try:
        if not type(response) ==  dict:
            response = parse_dictionary(response)
        response['message'] = 'Sucess'
        for k,v in kwargs.items():
            response[k] =  v
        return jsonify(response), 200
    except Exception as e:
        print (e)


def get_error_traceback(sys, e):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    return "%s || %s || %s || %s" %(exc_type, fname, exc_tb.tb_lineno,e)


def get_current_date_time():
    try:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        return dt_string
    except Exception as e:
        print (e)


import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '../')))
from flask_app.helpers import common_module_util, common_ref_string


def test_main():
    try:
        return common_ref_string.Common.unauthrized_user

    except Exception as e:
        print ("Mongo connection Error")


def test_db():
    try:

        return common_ref_string.Common.db_opertaion_sucsess

    except Exception as e:
        print ("Mongo connection Error")

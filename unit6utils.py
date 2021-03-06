__author__ = 'Kalyan'

import inspect
import os

def get_module_dir():
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return mod_dir


def get_temp_dir():
    module_dir = get_module_dir()
    temp_dir = os.path.join(module_dir, "tempfiles")
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)
    return temp_dir


# open files generated as a part of the tests. Allow them to be in a different dir via DATA_DIR
def get_temp_file(file):
    data_dir = os.getenv("DATA_DIR", default=get_temp_dir())
    return os.path.join(data_dir, file)

# returns file path from module directory. These are input files that are part of course material
def get_input_file(file):
    mod_dir = get_module_dir()
    return  os.path.join(mod_dir, file)


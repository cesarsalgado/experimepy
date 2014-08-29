from cesarpy.misc import get_current_date_and_time_str
import inspect
from os.path import join
import os
import shutil

def init_experiment(base='result'):
  exp_date = get_current_date_and_time_str()
  stack = inspect.stack()
  method_name = stack[1][3]
  this_exp_dir_path = join(base, method_name, exp_date)
  os.makedirs(this_exp_dir_path)
  callers_module = inspect.getmodule(stack[1][0])
  filename = callers_module.__name__+'.py'
  dst_file_path = join(this_exp_dir_path, filename)
  shutil.copyfile(filename, dst_file_path)
  return this_exp_dir_path

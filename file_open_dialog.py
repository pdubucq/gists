# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 15:24:34 2018

@author: pasca
"""
from pandas import read_json
from pathlib import Path
from  tkinter import Tk, filedialog

config = read_json('file_open_dialog_config.json',typ='series')
root = Tk()

root.filename =  filedialog.askopenfilename(
        initialdir = Path(config['input_file_dir']),
        title = config['title'],
        filetypes = ((config['input_file_name'],f"*.{config['input_file_extension']}"),
                     ("all files","*.*")))

print (root.filename)

path = Path(root.filename)

root.withdraw()
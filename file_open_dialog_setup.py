from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = r'C:\ProgramData\Miniconda3\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\ProgramData\Miniconda3\tcl\tk8.6'

base = None    

executables = [Executable("file_open_dialog.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':['pathlib', 'tkinter'],
    },    
}

setup(
    name = "File Dialog print path",
    options = options,
    version = "0.1",
    description = 'Opens a file dialog, chosen excel file is saved as pandas pickle',
    executables = executables
)
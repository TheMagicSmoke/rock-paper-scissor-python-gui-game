#After configuration of this file, place it together with your python program, in the command line type :
# python setup.py build
# This will successfully convert your python program to an executable file.

import sys
from cx_Freeze import setup,Executable

#If you convert a GUI python project to a .exe which will not show the output in cmd window, then base variable
#needs to be Win32GUI otherwise with base = Win32 (which is the default value of the base parameter of cx_Freeze) ,
# a cmd window will open even though the project might have graphics components.

#I your python program shows its output in a cmd window only, then the next three lines of code should be omitted.
base = None
if (sys.platform == "win32"):
    base = "Win32GUI"


setup(name = 'rockpaperscissor_v2' , #name of the executable
      version = '2.0',
      description = '',
      #For the first argument below, you need to mention the name of the python program which will be converted
      #to a .exe file. The second argument 'base = base' should be written only if you do not want a cmd window
      #when the .exe file is run. The base argument by default has the value 'Win32'
      executables = [Executable('rockpaperscissor_v2.py',base = base)]
)

"""
python
#>>> from colorama import init
#>>> init()
#>>> from colorama import Fore
#>>> print(Fore.RED + "some red text")


**Python package for excel**

python-excel.org 

openpyxl.org 


** Modules **

modules are .py scripts that you call in another .py script

Packages are a collection of modules


*********
to organize, have folders with __init__.py inside
  a Package with modules (.py files) inside
*********

"""

#import from module
from mymodule import my_func

my_func()

#import form pkg, organize into (sub)directories

from MyMainPkg import main_script
#OR
# to import specific func
#from MyMainPkg.main_script import main_report
from MyMainPkg.SubPkg import mysub_script

main_script.main_report()

mysub_script.sub_report()
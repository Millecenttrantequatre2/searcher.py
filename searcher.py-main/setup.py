import os 
import sys
import platform

print("Installing the python modules required for the searcher:")
if sys.platform.startswith("win"):
    "WINDOWS"
    os.system("pip install --upgrade pip install colorama")
    os.system("pip install --upgrade pip install pip install tqdm")

if sys.platform.startswith("linux"):
    "LINUX"
    os.system("pip install --upgrade pip install colorama")
    os.system("pip install --upgrade pip install pip install tqdm")

import sys
from cx_Freeze import setup, Executable

setup(
    name = "Cripto Extreme Edition",
    version = "2.0",
    description = "Cripto Extreme Edition v2.0 by Cripto S.a",
    executables = [Executable("run.py", base = None)])
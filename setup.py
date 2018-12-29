import cx_Freeze
from cx_Freeze import *

setup(
    name='TransformationsGeometryCalc',
    options = {'build_exe':{'packages':['time']}},
    executables = [
        Executable(
            'TransformationsGeometryCalc.py',
        )
    ]
)

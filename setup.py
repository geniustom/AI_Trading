# -*- coding: utf-8 -*-
'''
from distutils.core import setup
import py2exe

setup(console=["strategy/s1.py"])
'''
'''
from distutils.core import setup
import py2exe, sys
sys.argv.append('py2exe')
setup(
    options = {'py2exe': {'bundle_files': 3}},
    windows = [{'script': "strategy/s1.py"}],
    zipfile = None,
)
'''


from distutils.core import setup
import py2exe
import sys
 
#this allows to run it with a simple double click.
sys.argv.append('py2exe')
 
py2exe_options = {
        "includes": ["numpy","pylab","scipy","os"],          #"matplotlib.pyplot" "strategy.common"
        "includes": ["encodings", "encodings.*"],
        "includes": ["lib.filter", "lib.dblib","lib.indicator","lib.strategy_lib","lib.tracking","lib.analytics"],
        "dll_excludes": ["MSVCP90.dll",],
        "compressed": 1,
        "optimize": 2,
        "ascii": 0,
        "bundle_files": 2,
        }
 
setup(
      name = 'First',
      version = '1.0',
      #console = ['s1.py',],
      console = ['strategy/s9.py',],
      zipfile = None,
      options = {'py2exe': py2exe_options}
      )

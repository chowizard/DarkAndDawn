#-*- coding: utf-8 -*-

"""
Created on 2017. 8. 8.

@author: JoSoowoon
"""

import sys
import os

from DnDApp import DnDApp

# Ensure the parent directory is in sys.path so we can import modules correctly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    app = DnDApp()
    app.run()

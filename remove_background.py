# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 15:34:41 2022
pip install rembg
@author: fcu243
"""

from rembg import remove
from PIL import Image

def imageProcess(input_path):
    #input_path = 'input.jpg'
    output_path = 'output.png'
    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)

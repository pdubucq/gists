# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 12:06:01 2018

@author: pasca
"""


import base64
from flask import Flask, render_template
from graphviz import Graph

import os
os.environ["PATH"] += os.pathsep + 'C:/ProgramData/Miniconda3/Library/bin/graphviz'
#%%



app = Flask(__name__)


@app.route('/')
def svgtest():
  chart_data = Graph()

  chart_data.node('H', 'Hello')
  chart_data.node('W', 'World')
  chart_data.edge('H', 'W')

  chart_output = chart_data.pipe(format='png')
  chart_output = base64.b64encode(chart_output).decode('utf-8')

  return render_template('poc_flask_graphviz.html', chart_output=chart_output)


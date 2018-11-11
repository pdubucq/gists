# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 12:32:29 2018

@author: pasca
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 12:06:01 2018

@author: pasca
"""


import base64
from flask import Flask, render_template
from graphviz import Digraph

import os
os.environ["PATH"] += os.pathsep + 'C:/ProgramData/Miniconda3/Library/bin/graphviz'
#%%

app = Flask(__name__)

def get_graph():
  chart_data = Digraph(graph_attr=[('rankdir','LR')])
  
  # add input nodes to graph
  chart_data.attr('node', shape='ellipse')
  node_def={'BS1':'BS1','BS2':'BS2','BS3':'BS3','Qeg':'Qgen'}
  [chart_data.node(identifier, label) for identifier, label in node_def.items()]
  
  # add output nodes to graph
  node_def={'Qhk1':'Qhk1'}  
  chart_data.attr('node', shape='ellipse')
  [chart_data.node(identifier, label) for identifier, label in node_def.items()]

  # add transformation nodes to graph as rectangles
  chart_data.attr('node', shape='record')
  node_def={'SUM':'SUM','a-b':'a-b','a-b (2)':'a-b','a/b':'a/b'}
  [chart_data.node(identifier, label) for identifier, label in node_def.items()]
  
  # add output nodes to graph
  chart_data.edge('Qeg','a-b',label='a')
  chart_data.edge('Qgen','a-b',label='b')
  chart_data.edge('a-b','a-b (2)')
  chart_data.edge('a-b (2)','Qhk1')
  chart_data.edge('BS1','SUM')
  chart_data.edge('BS2','SUM')
  chart_data.edge('BS3','SUM')
  chart_data.edge('BS1','a/b',label='a')
  chart_data.edge('SUM','a/b',label='b')
  chart_data.edge('a/b','a-b (2)')

  return chart_data

@app.route('/')
def render_webapp():

  chart_output = get_graph().pipe(format='svg').decode('utf-8')
  #chart_output = base64.b64encode(chart_output).decode('utf-8')

  return render_template('poc_flask_graphviz.html', chart_output=chart_output)

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD']=True
    app.config['DEBUG'] = True
    app.config['SERVER_NAME'] = "127.0.0.1:4000"         
    app.run()
import os
from flask import render_template, flash, redirect, url_for, request, jsonify, json
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
from app import app
from app.forms import getGraphs, getFiles
from app.parse import parsetoarray, parsetoarrayfromfile
from app.NemoMapPy import nmp

@app.route('/nmp-text', methods=['GET', 'POST'])
def index():
    form=getGraphs()
    return render_template('index.html', form=form)

@app.route('/senddata', methods=['POST'])
def senddata():
    form=getGraphs()
    if form.validate_on_submit():
        #get the data from the forms
        ig = form.inputGraph.data
        qg = form.queryGraph.data

        #parse the data and strip formatting
        inputGraph=parsetoarray(ig)
        queryGraph=parsetoarray(qg)

        resultdata=nmp(inputGraph, queryGraph)
        #convert to json
        jsonstr=json.dumps(resultdata)
        return jsonstr
    return jsonify(data=form.errors)


ALLOWED_EXTENSIONS = set(['txt'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/nmp-file', methods=['GET', 'POST'])
def fileupload():
    return render_template('fileupload.html')

@app.route('/uploadajax', methods=['GET', 'POST'])
def uploadajax():
    inputFile = request.files['inputFile']
    queryFile = request.files['queryFile']

    if inputFile.filename.lower().endswith('.txt') and queryFile.filename.lower().endswith('.txt'):
        print('text file detected')
        inputFile = inputFile.read()
        inputGraph = parsetoarrayfromfile(str(inputFile))
        queryFile = queryFile.read()
        queryGraph = parsetoarrayfromfile(str(queryFile))
        resultdata=nmp(inputGraph, queryGraph)
        jsonstr=json.dumps(resultdata)
        return jsonstr
    else:
        print('fake')
        #flash stuff
        return render_template('fileupload.html')
    

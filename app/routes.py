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

@app.route('/nmp-file', methods=['GET', 'POST'])
def fileupload():
    form=getFiles()
    return render_template('fileupload.html', form=form)

@app.route('/sendfiles', methods=['POST'])
def sendfiles():
    form=getFiles()
    if form.validate_on_submit():
        inputFile = form.getInput.data
        queryFile = form.getQuery.data
        
        inputFile = inputFile.read()
        inputGraph = parsetoarrayfromfile(str(inputFile))
        queryFile = queryFile.read()
        queryGraph = parsetoarrayfromfile(str(queryFile))

        resultdata=nmp(inputGraph, queryGraph)
        jsonstr=json.dumps(resultdata)
        return jsonstr
    else:
        print("Failed validation")
    return jsonify(data=form.errors)

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



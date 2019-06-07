from flask import render_template, flash, redirect, url_for, request, jsonify, json
from werkzeug.urls import url_parse
from app import app
from app.forms import getGraphs
from app.parse import parsetoarray
from app.NemoMapPy import nmp

@app.route('/index', methods=['GET', 'POST'])
def index():
    form=getGraphs()
    return render_template('index.html', form=form)

@app.route('/test')
def test():
    return render_template("test.html")

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
        #return jsonify(data=resultdata)
        return jsonstr
    return jsonify(data=form.errors)



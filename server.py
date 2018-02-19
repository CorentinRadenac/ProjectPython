#!/usr/bin/python
# -*- coding: utf-8 -*
import os
from flask import Flask, jsonify, request, make_response, render_template
from datetime import timedelta
import sqlite3

"""
Application de tests
"""
app = Flask(__name__)
@app.route('/api/carac/', methods=['POST' , 'GET'])
def carac():
	try:
		conn = sqlite3.connect('ProgPython')
	except Exception:
		print"Erreur connecion MySql"
	else:
		cursor = conn.cursor()
		cursor.execute("""
		CREATE TABLE IF NOT EXISTS donner(
    	host TEXT,
    	os TEXT,
    	uptime TEXT,
    	cpu TEXT,
    	ramused TEXT,
    	ramfree TEXT
		)
		""")
		conn.commit()
	try:
		data=request.json
		print data
		cursor.execute("""
		INSERT INTO donner(host, os, uptime, cpu, ramused, ramfree) VALUES(:host, :os, :uptime, :cpu, :ramused, :ramfree)""", data)
		conn.commit()
	except Exception:
		print"Erreur de la requete insert"
	else:
		print"Insert faite"
		conn.close()
	return "finit"
@app.route('/donnervue', methods=['GET'])
def donnervue():
	try:
		conn = sqlite3.connect('ProgPython')
	except Exception:
		print"Erreur connecion MySql"
	else:
		cursor = conn.cursor()
		data = cursor.execute("""
		SELECT * FROM donner """)
		dataresult = list(data.fetchall())
		return render_template('donnervue.html', data=dataresult)

#select
	#return render_template('donnervue.html', data = data)
	

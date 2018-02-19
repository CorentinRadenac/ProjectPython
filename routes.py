#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import sys, uptime 
import psutil
import socket
import os
from datetime import timedelta

	

r = requests.post('http://localhost:5000/api/carac/', json={'host': socket.gethostname(), 'os': os.name, 'uptime': uptime._uptime_linux(), 'cpu': psutil.cpu_percent(), 'ramused': psutil.virtual_memory().used, 'ramfree': psutil.virtual_memory().free})
print "Status : ", r.status_code
print r.text

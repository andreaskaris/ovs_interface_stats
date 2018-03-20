#!/bin/python

import sys
import subprocess
import json
import time

delay = 10

interface=sys.argv[1]
if len(sys.argv) == 3:
  delay = int(sys.argv[2])


print "Gathering stats on " + interface + " with a delay of " + str(delay)


def jsonize(the_string):
  the_string_json = the_string.replace(" ","")
  the_string_json = the_string_json.replace('"',"")
  the_string_json = the_string_json.replace("=",":")
  the_string_json = the_string_json.replace('{','{"')
  the_string_json = the_string_json.replace('}','"}')
  the_string_json = the_string_json.replace('\,' , '",')
  the_string_json = the_string_json.replace('=' , '="')
  the_string_json = the_string_json.replace(':' , '":"')
  the_string_json = the_string_json.replace(',' , '","')
  return the_string_json

statistics1=subprocess.check_output(['ovs-vsctl','get', 'int', interface, 'statistics'])
statistics1map= json.loads(jsonize(statistics1))

print "sleeping for " + str(delay) +  "  seconds"
time.sleep(delay)

statistics2=subprocess.check_output(['ovs-vsctl','get', 'int', interface, 'statistics'])
statistics2map= json.loads(jsonize(statistics2))

for key, value in statistics1map.iteritems():
  diff = int(statistics2map[key]) - int(statistics1map[key])
  stats = diff / delay
  print key + " =>\n\tAVG: " + str(stats) + " (" + statistics2map[key] + " - " + statistics1map[key] + ") / " + str(delay) + "\n\tABS: " + str(diff)

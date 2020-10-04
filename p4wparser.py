import json
import os
import sys

jsonIn = str(sys.argv[1])

with open(jsonIn) as json_file:
    data = json.load(json_file)
    for task in data['sourceEntityData']:
        print(str(task['name']))

#!/usr/bin/python3

"""Script adds all arguments to a Python list and saves them to a file
"""


import json
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


with open("add_item.json", mode="a+", encoding="utf-8") as f:
    f.seek(0)
    fileContents = f.read()
    argList = []

    if fileContents != "":
        argList = json.loads(fileContents)

    for item in sys.argv[1:]:
        argList.append(item)

    fileContents = json.dumps(argList)

    f.truncate(0)
    f.write(fileContents)

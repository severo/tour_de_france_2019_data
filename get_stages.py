# -*- coding: utf-8 -*-
from urllib.request import urlretrieve
from parse_stage import parse_stage
import tempfile
import os
import json

tempdir = tempfile.gettempdir()
stages = []
for stage_id in range(1,15):
    html_file = os.path.join(tempdir, f"stage-{stage_id}.html") 
    # download if the file does not exist
    try:
        f = open(html_file, "r")
    except IOError:
        urlretrieve(f"https://www.letour.fr/en/rankings/stage-{stage_id}", html_file)
    else:
        f.close()
    # open the file
    with open(html_file, "r") as html:
        stages.append(parse_stage(html))

json_file = "stages.json"
with open(json_file, "w") as f:
    print(json.dumps(stages), file=f)

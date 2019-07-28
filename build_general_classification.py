# -*- coding: utf-8 -*-
from parse_general_classification import parse_stage
import os
import json

stages = []
for stage_id in range(1,22):
    html_file = os.path.join("saved_html", f"stage{stage_id}.html")
    # open the file
    with open(html_file, "r") as html:
        stages.append(parse_stage(html))

json_file = "general_classification.json"
with open(json_file, "w") as f:
    print(json.dumps(stages), file=f)

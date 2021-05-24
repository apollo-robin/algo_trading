# -*- coding: utf-8 -*-
"""
Created on Sun May 23 18:51:41 2021

@author: robin
"""

import toml

output_file = ".streamlit/secrets.toml"

with open("firestore-key.json") as json_file:
    json_text = json_file.read()

config = {"textkey": json_text}
toml_config = toml.dumps(config)

with open(output_file, "w") as target:
    target.write(toml_config)
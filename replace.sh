#!/bin/bash

awk 'BEGIN{getline l < "poya.json"}/REPLACE_ME/{gsub("REPLACE_ME",l)}1' index.html > index_stage.html
echo "Updated index_stage.html file"

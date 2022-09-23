#!/bin/bash
cd ..
cd docs
while read -r line; 
do
    echo "$line";
done < "help.md"
cd ..
cd src
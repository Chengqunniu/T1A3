#!/bin/bash
if [[ -x "$(command -v python3)" ]]
then
    pyv="$(python3 -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
        python3 password.py
    else
        echo "You've got the wrong version of python, sort it out!
        To install Python, check out https://installpython3.com/ ">&2
    fi 
else
    echo "You don't have python, go get it!
    To install Python, check out https://installpython3.com/ " >&2
fi

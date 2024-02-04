#!/bin/bash
#A bash script that displays only the status code of a response header
curl -sIL $1 | head -n1 | cut -d " " -f2

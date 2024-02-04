#!/bin/bash
#Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -sI -i -X OPTIONS $1 -L

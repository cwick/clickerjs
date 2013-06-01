#!/usr/bin/env bash

curl -vvv -H "Viewer-Only-Client: 1" "http://localhost:3689/$1" | ./dacp_decode.py

#!/bin/bash

python server.py &

python client.py "Inputs/text1.txt" "Inputs/text2.txt"

sleep 3


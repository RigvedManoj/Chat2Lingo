#!/bin/bash

python server.py &

SERVER_PID=$!

python client.py "../Inputs/text1.txt" "../Inputs/text2.txt"

sleep 3

kill $SERVER_PID

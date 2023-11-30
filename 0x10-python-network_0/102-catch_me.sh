#!/bin/bash
# causes the server to respond with a message "You got me!"
curl -s -d "@$2" -H "Content-Type: application/json" -X POST "$1"

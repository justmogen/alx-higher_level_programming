#!/bin/bash
# Send a POST request to a URL with email and subject variables, and display the response body
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"

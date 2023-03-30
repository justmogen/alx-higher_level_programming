#!/bin/bash
#takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -w "%{http_code}\n" "$1" | grep -q "200" && curl -s "$1"

#!/bin/bash
# Send a request to a URL and display only the status code of the response
curl -s -w "%{http_code}" "$1"

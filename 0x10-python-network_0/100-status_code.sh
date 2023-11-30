#!/bin/bash
# displays the status code of the response
curl -L -s -X HEAD -w "%{http_code}" "$1"

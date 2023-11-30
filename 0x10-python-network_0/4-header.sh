#!/bin/bash
# sends a GET request to a URL with a header variable
curl -sH "X-User-Id: 98" "${1}"

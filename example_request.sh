#!/bin/bash
# Example curl request for testing the n8n webhook workflow

curl -X POST "https://n8n.srv1042375.hstgr.cloud/webhook-test/nevie/test" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Hello"
  }'


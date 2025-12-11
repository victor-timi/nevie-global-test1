#!/bin/bash
# Example curl request for testing the API directly (for debugging)
# This bypasses n8n and tests the Python API endpoint directly

curl -X POST "http://localhost:8000/nevie/test" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Hello"
  }'


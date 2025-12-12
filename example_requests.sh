#!/bin/bash
# Example curl requests for testing the NEVIE-GLOBAL API

echo "=========================================="
echo "NEVIE-GLOBAL Test 2 - Example Requests"
echo "=========================================="
echo ""

# Test 1: Direct API - Cache Miss
echo "1. Testing Direct API (Cache Miss):"
echo "-----------------------------------"
curl -X POST "http://localhost:8000/nevie/test" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'
echo ""
echo ""

# Test 2: Direct API - Cache Hit (same message)
echo "2. Testing Direct API (Cache Hit - same message):"
echo "--------------------------------------------------"
curl -X POST "http://localhost:8000/nevie/test" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'
echo ""
echo ""

# Test 3: Stats Endpoint
echo "3. Testing Stats Endpoint:"
echo "--------------------------"
curl -X GET "http://localhost:8000/nevie/stats" \
  -H "Content-Type: application/json"
echo ""
echo ""

# Test 4: Error Scenario - Empty message
echo "4. Testing Error Handling (Empty message):"
echo "-------------------------------------------"
curl -X POST "http://localhost:8000/nevie/test" \
  -H "Content-Type: application/json" \
  -d '{"message": ""}'
echo ""
echo ""

# Test 5: Cache Case-Insensitive Test
echo "5. Testing Cache (Case-insensitive - should be cache hit):"
echo "-----------------------------------------------------------"
curl -X POST "http://localhost:8000/nevie/test" \
  -H "Content-Type: application/json" \
  -d '{"message": "HELLO"}'
echo ""
echo ""

# Test 6: n8n Webhook (if n8n is configured)
echo "6. Testing n8n Webhook (optional):"
echo "-----------------------------------"
echo "Uncomment the line below if n8n is running:"
# curl -X POST "https://n8n.srv1042375.hstgr.cloud/webhook/nevie/test" \
#   -H "Content-Type: application/json" \
#   -d '{"message": "Hello"}'
echo ""


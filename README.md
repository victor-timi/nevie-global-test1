# NEVIE-GLOBAL™ Test 1 & 2 - API

This is a FastAPI application that provides an endpoint to process messages through OpenAI summarization. Test 1 includes basic API functionality, and Test 2 extends it with caching, error handling, and statistics.

## Setup Instructions

### 1. Install Dependencies

```bash
# Create a virtual environment (recommended)
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment Variables

1. Copy the example environment file:

   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your OpenAI API key:

   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

   You can get your API key from: https://platform.openai.com/api-keys

### 3. Run the API

```bash
# Option 1: Using uvicorn directly (recommended)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Option 2: Using Python directly
python -m app.main
```

The API will be available at:

- **Local API**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

### 4. Expose API with ngrok (for cloud n8n)

Since n8n is cloud-hosted, you need to expose your local API:

1. **Install ngrok** (if not installed):

   ```bash
   # macOS
   brew install ngrok/ngrok/ngrok

   # Or download from: https://ngrok.com/download
   ```

2. **Start ngrok** (in a new terminal):

   ```bash
   ngrok http 8000
   ```

3. **Copy the HTTPS URL** (e.g., `https://xxxxx.ngrok-free.app`)

4. **Use this URL in n8n HTTP Request node**: `https://YOUR-NGROK-URL.ngrok-free.app/nevie/test`

**Note**: The ngrok URL changes each time you restart ngrok (unless you have a paid plan with a static domain). Keep ngrok running while testing.

## API Endpoint

### POST /nevie/test

**Request:**

```json
{
  "message": "Hello"
}
```

**Response:**

```json
{
  "status": "ok",
  "summary": "A greeting message.",
  "timestamp": "2024-01-15T10:30:00.000000Z"
}
```

## Example Requests

### Direct API Call (Python API):

#### Using curl:

```bash
curl -X POST "http://localhost:8000/nevie/test" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'
```

#### Using Python requests:

```python
import requests

url = "http://localhost:8000/nevie/test"
payload = {"message": "Hello"}
response = requests.post(url, json=payload)
print(response.json())
```

#### Using Postman:

**Test Procedure**:

1. Open Postman and create a new request
2. Set Method to: **POST**
3. Enter URL: `http://localhost:8000/nevie/test`
4. Go to **Headers** tab and add:
   - Key: `Content-Type`
   - Value: `application/json`
5. Go to **Body** tab:
   - Select **raw**
   - Choose **JSON** from dropdown
   - Enter the request body:
     ```json
     {
       "message": "Hello"
     }
     ```
6. Click **Send**
7. Verify the response:
   - Status: `200 OK`
   - Response body should contain:
     ```json
     {
       "status": "ok",
       "summary": "...",
       "timestamp": "..."
     }
     ```

### n8n Webhook (Complete Workflow):

#### Using curl:

```bash
curl -X POST "https://n8n.srv1042375.hstgr.cloud/webhook/nevie/test" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'
```

#### Using Python requests:

```python
import requests

url = "https://n8n.srv1042375.hstgr.cloud/webhook/nevie/test"
payload = {"message": "Hello"}
response = requests.post(url, json=payload)
print(response.json())
```

#### Using Postman:

**Test Procedure**:

1. Open Postman and create a new request
2. Set Method to: **POST**
3. Enter URL: `https://n8n.srv1042375.hstgr.cloud/webhook/nevie/test`
4. Go to **Headers** tab and add:
   - Key: `Content-Type`
   - Value: `application/json`
5. Go to **Body** tab:
   - Select **raw**
   - Choose **JSON** from dropdown
   - Enter the request body:
     ```json
     {
       "message": "Hello"
     }
     ```
6. Click **Send**
7. Verify the response:
   - Status: `200 OK`
   - Response body should contain:
     ```json
     {
       "workflow": "ok",
       "summary": "...",
       "recommendation": "..."
     }
     ```

**Screenshot available**: See `docs/screenshots/postman_test_screenshot.png` for a visual example.

**Expected n8n Response:**

```json
{
  "workflow": "ok",
  "summary": "...",
  "recommendation": "..."
}
```

## Features

### Core Features (Test 1):

- ✅ FastAPI endpoint `/nevie/test`
- ✅ Input validation using Pydantic
- ✅ OpenAI integration for summarization
- ✅ Recommendation function (ready for n8n integration)
- ✅ Health check endpoints

### Extended Features (Test 2):

- ✅ **In-memory cache** - Avoids duplicate AI calls for same messages
- ✅ **Global error handling** - Structured error responses with `error.log`
- ✅ **Separate log files** - `normal.log` for operations, `error.log` for errors
- ✅ **Stats endpoint** - `GET /nevie/stats` for cache statistics
- ✅ **Cache indicator** - Response includes `cached: true/false` field

## File Naming Conventions

This project follows consistent naming conventions:

- **Python files**: Use `snake_case` (e.g., `app/routes.py`, `app/config.py`)
- **JavaScript files**: Use `kebab-case` (e.g., `docs/n8n-code.js`)
- **Markdown files**: Use `kebab-case` (e.g., `README.md` is special case, `docs/ngrok-setup.md`)
- **Shell scripts**: Use `snake_case` (e.g., `example_requests.sh`)
- **JSON files**: Use `kebab-case` or `snake_case` (e.g., `example_request.json`)

## Project Structure

```
nevie-test1/
├── app/                 # Application package
│   ├── __init__.py     # Package initialization
│   ├── main.py         # FastAPI app initialization and entry point
│   ├── core/           # Core functionality
│   │   ├── __init__.py
│   │   ├── config.py   # Configuration settings
│   │   ├── exceptions.py # Global exception handlers
│   │   └── cache.py    # In-memory cache and statistics
│   ├── api/            # API layer
│   │   ├── __init__.py
│   │   └── routes.py   # API endpoints/routes
│   ├── services/       # Business logic
│   │   ├── __init__.py
│   │   └── services.py # OpenAI integration and recommendations
│   └── models/         # Data models
│       ├── __init__.py
│       └── models.py   # Pydantic request/response models
├── requirements.txt           # Python dependencies
├── .env.example               # Environment variables template
├── .gitignore                # Git ignore file
├── README.md                  # This file
├── docs/                      # Documentation folder
│   ├── ngrok-setup.md        # ngrok setup instructions
│   ├── n8n-code.js           # n8n Function/Code node JavaScript
│   ├── n8n-workflow.json     # n8n workflow export (optional)
│   └── screenshots/           # Screenshots
│       ├── n8n_workflow_screenshot.png    # n8n workflow screenshot
│       └── postman_test_screenshot.png    # Postman test screenshot
├── example_requests.sh        # Example curl requests (all endpoints)
├── example_request.json       # Example JSON payload
├── normal.log                 # Normal operation logs (generated at runtime)
└── error.log                  # Error logs (generated at runtime)
```

## Architecture & n8n Workflow

### System Flow Diagram

```
Client / Postman / curl
         │
         ▼
Webhook Trigger (n8n receives JSON)
         │
         ▼
HTTP Request Node → POST to Python API (/nevie/test)
         │
         ▼
Python API processes message → returns summary
         │
         ▼
Function/Code Node (n8n) → generates recommendation from summary
         │
         ▼
Respond Node → returns final JSON (workflow, summary, recommendation) to client
```

### n8n Integration

The API is ready to be called from n8n. The recommendation function is available in the code and can be integrated into the n8n workflow response.

**n8n Workflow Setup:**

### Workflow Diagram:

```
┌─────────────┐
│   Webhook   │ (Trigger)
│   Trigger   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ HTTP Request│ (Calls Python API)
│    Node     │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    IF Node   │ (Checks: $json.status === "error")
│              │
└───┬──────┬───┘
    │      │
    │ TRUE │ FALSE (success)
    │      │
    ▼      ▼
┌──────┐ ┌──────────────┐
│ Set  │ │   Code/      │
│ Node │ │  Function    │
│(Error│ │   Node       │
│Path) │ └──────┬───────┘
└──┬───┘        │
   │            ▼
   │      ┌──────────────┐
   │      │   Set Node   │
   │      │  (Success)   │
   │      └──────┬───────┘
   │             │
   └─────────────┼─────────┐
                 │         │
                 ▼         ▼
         ┌──────────────────┐
         │ Respond to       │
         │ Webhook Node     │
         │ (Both paths      │
         │  connect here)   │
         └──────────────────┘
```

### Step-by-Step Configuration:

1. **Webhook Trigger**: Configure to receive POST requests with JSON payload
   - Input: `{"message": "Hello"}`
2. **HTTP Request Node**: Call the Python API
   - Method: POST
   - URL: `https://YOUR-NGROK-URL.ngrok-free.app/nevie/test` (replace with your actual ngrok URL - see setup above)
   - Body: Pass through the message from webhook
   - **IMPORTANT - Enable "Ignore Response Code"**:
     - Click on the HTTP Request node
     - Look for "Options" tab (usually at the bottom or in a dropdown)
     - Find "Response Code" or "Ignore Response Code" setting
     - Set it to: **"All"** or **"Never throw error"** or enable **"Ignore Response Code"**
     - This allows 500 status codes to pass through to IF node instead of throwing an exception
     - **Why**: Without this, n8n throws an error on 500 status, preventing the IF node from checking the response
   - Response will contain: `status`, `summary`, `timestamp`, `cached` (or `status: "error"` on failure)
   - **Note**: Since n8n is cloud-hosted, we use ngrok to expose the local API
3. **IF Node** (for error handling): Check response status
   - Condition: `{{ $json.status === "error" }}`
   - **True (Error Path)**:
     - Set node to format error response
     - Respond with error format
   - **False (Success Path)**: Continue to Code node
4. **Function/Code Node**: Generate recommendation (only on success path)
   - Language: JavaScript
   - Mode: Run Once for All Items
   - Code: See `docs/n8n-code.js` for the complete code
   - **Note**: Uses `.first()` instead of `.item` and cleans double quotes to avoid JSON issues
   - Quick reference:
     ```javascript
     const summary = $input.first().json.summary;
     const cleanSummary = summary.replace(/"/g, "'");
     const recommendation = `Based on the summary '${cleanSummary}', I recommend reviewing the key points and taking appropriate action.`;
     return { recommendation };
     ```
5. **Set Node - Error Path** (IF True branch):

   - Mode: "Manually"
   - Add fields:
     - `workflow` = `error`
     - `message` = `={{ $json.message }}`
     - `timestamp` = `={{ $json.timestamp }}`

6. **Set Node - Success Path** (after Code node):

   - Mode: "Manually"
   - Add fields:
     - `workflow` = `ok`
     - `summary` = `={{ $('HTTP Request').first().json.summary }}`
     - `recommendation` = `={{ $('Code').first().json.recommendation }}`

7. **Respond to Webhook Node**: Return final JSON response
   - Response Mode: "Using Last Node Output"
   - Both Set nodes (error and success) connect to this node
   - **Success Format**:
     ```json
     {
       "workflow": "ok",
       "summary": "...",
       "recommendation": "..."
     }
     ```
   - **Error Format**:
     ```json
     {
       "workflow": "error",
       "message": "AI processing failed",
       "timestamp": "..."
     }
     ```

## Cache Behavior

The in-memory cache uses the following normalization:

- **Case-insensitive**: "Hello" and "hello" are treated as the same message
- **Whitespace trimmed**: Leading/trailing spaces are removed
- **Cache persists**: Until the API server is restarted
- **Cache key**: Normalized message (lowercase + trimmed)

**Example**:

- `"Hello"` and `"hello"` → Same cache entry
- `"  Hello  "` and `"Hello"` → Same cache entry

## Error Scenarios

The API handles errors gracefully:

1. **OpenAI API Errors**:

   - Network failures, API key issues, rate limits
   - Returns: `{"status": "error", "message": "AI processing failed", "timestamp": "..."}`
   - Logged to `error.log`

2. **Validation Errors**:

   - Empty messages, invalid JSON
   - Returns: HTTP 400/422 with validation details
   - Logged to `normal.log` (expected client errors, not system failures)
   - Note: These are normal operations (bad client input), hence `normal.log`

3. **Unexpected Errors**:
   - Any unhandled exceptions
   - Caught by global exception handler
   - Returns: Structured error response
   - Logged to `error.log` with full stack trace

## API Response Examples

### Success Response (Cache Miss):

```json
{
  "status": "ok",
  "summary": "The message says hello.",
  "timestamp": "2025-12-12T13:00:00Z",
  "cached": false
}
```

### Success Response (Cache Hit):

```json
{
  "status": "ok",
  "summary": "The message says hello.",
  "timestamp": "2025-12-12T13:00:00Z",
  "cached": true
}
```

### Error Response:

```json
{
  "status": "error",
  "message": "AI processing failed",
  "timestamp": "2025-12-12T13:00:00Z"
}
```

### Stats Response:

```json
{
  "total_requests": 10,
  "cache_hits": 5,
  "cache_miss": 5
}
```

## Testing Your Workflow

See `docs/testing-guide.md` for comprehensive testing instructions.

Quick test:

```bash
# Test cache miss
curl -X POST "http://localhost:8000/nevie/test" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'

# Test cache hit (same message)
curl -X POST "http://localhost:8000/nevie/test" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'

# Test stats
curl -X GET "http://localhost:8000/nevie/stats"

# Test n8n workflow
curl -X POST "https://n8n.srv1042375.hstgr.cloud/webhook/nevie/test" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'
```

## Loom Video Checklist

See `docs/loom-video-script.md` for a detailed script and walkthrough guide.

For the mandatory Loom video (3-8 minutes), demonstrate:

- ✅ **API Execution**: Show POST requests to `/nevie/test` endpoint
- ✅ **Cache Behavior**:
  - First request (cache miss) - show `cached: false`
  - Second identical request (cache hit) - show `cached: true`
  - Verify no OpenAI call on cache hit
- ✅ **Log Files**:
  - Show `normal.log` with operation logs
  - Show `error.log` (trigger an error to demonstrate)
- ✅ **n8n Workflow**:
  - Show workflow execution
  - Demonstrate success and error paths
  - Show final response
- ✅ **Stats Endpoint**: Show `/nevie/stats` with cache statistics
- ✅ **Technical Explanation**:
  - Architecture overview
  - Cache implementation
  - Error handling strategy
  - n8n integration

## Deliverables Checklist

### Test 2 Requirements:

- ✅ Full API code (all files in `app/` directory)
- ✅ Cache logic (`app/cache.py`)
- ✅ `normal.log` + `error.log` (generated at runtime)
- ✅ n8n workflow screenshot (`docs/screenshots/n8n_workflow_screenshot.png`)
- ⚠️ n8n workflow export (JSON) - _Recommended: Export from n8n UI_
- ✅ Short README (this file)
- ✅ Postman/curl examples (`example_requests.sh`, `example_request.json`)
- ⚠️ **Mandatory Loom video** - _To be created_

## Troubleshooting

- **OpenAI API Error**: Make sure your `OPENAI_API_KEY` is set correctly in the `.env` file
- **Port already in use**: Change the port in `main.py` or use `--port` flag with uvicorn
- **Module not found**: Make sure you've activated your virtual environment and installed dependencies
- **Cache not working**: Cache is in-memory and resets on server restart
- **n8n connection failed**: Check ngrok is running and URL is correct in n8n HTTP Request node

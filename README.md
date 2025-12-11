# NEVIE-GLOBAL™ Test 1 - API

This is a FastAPI application that provides an endpoint to process messages through OpenAI summarization.

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
# Option 1: Using uvicorn directly
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Option 2: Using Python
python main.py
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
curl -X POST "https://n8n.srv1042375.hstgr.cloud/webhook-test/nevie/test" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'
```

#### Using Python requests:

```python
import requests

url = "https://n8n.srv1042375.hstgr.cloud/webhook-test/nevie/test"
payload = {"message": "Hello"}
response = requests.post(url, json=payload)
print(response.json())
```

#### Using Postman:

**Test Procedure**:

1. Open Postman and create a new request
2. Set Method to: **POST**
3. Enter URL: `https://n8n.srv1042375.hstgr.cloud/webhook-test/nevie/test`
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

- ✅ FastAPI endpoint `/nevie/test`
- ✅ Input validation using Pydantic
- ✅ OpenAI integration for summarization
- ✅ Error handling
- ✅ Logging (console + file: `nevie_api.log`)
- ✅ Recommendation function (ready for n8n integration)
- ✅ Health check endpoints

## Project Structure

```
nevie-test1/
├── app/                 # Application package
│   ├── __init__.py     # Package initialization
│   ├── main.py         # FastAPI app initialization
│   ├── config.py       # Configuration settings
│   ├── models.py       # Pydantic request/response models
│   ├── routes.py       # API endpoints/routes
│   └── services.py     # Business logic (OpenAI, recommendations)
├── main.py                    # Entry point for running the application
├── requirements.txt           # Python dependencies
├── .env.example               # Environment variables template
├── .gitignore                # Git ignore file
├── README.md                  # This file
├── docs/                      # Documentation folder
│   ├── NGROK_SETUP.md        # ngrok setup instructions
│   └── screenshots/           # Screenshots
│       ├── n8n_workflow_screenshot.png    # n8n workflow screenshot
│       └── postman_test_screenshot.png    # Postman test screenshot
├── example_request.sh         # Example curl request (n8n webhook)
├── example_request.json       # Example JSON payload
├── example_request_direct.sh  # Example curl request (direct API - for debugging)
└── nevie_api.log             # Log file (generated at runtime)
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

1. **Webhook Trigger**: Configure to receive POST requests with JSON payload
   - Input: `{"message": "Hello"}`
2. **HTTP Request Node**: Call the Python API
   - Method: POST
   - URL: `https://YOUR-NGROK-URL.ngrok-free.app/nevie/test` (replace with your actual ngrok URL - see setup above)
   - Body: Pass through the message from webhook
   - Response will contain: `status`, `summary`, `timestamp`
   - **Note**: Since n8n is cloud-hosted, we use ngrok to expose the local API
3. **Function/Code Node**: Generate recommendation
   - Use the `get_recommendation()` function logic from `app/services.py`
   - Input: `summary` from HTTP Request node response
   - Output: `recommendation` string
   - Example code:
     ```javascript
     const summary = $input.item.json.summary;
     const recommendation = `Based on the summary '${summary}', I recommend reviewing the key points and taking appropriate action.`;
     return { recommendation };
     ```
4. **Respond Node**: Return final JSON response
   - Format:
     ```json
     {
       "workflow": "ok",
       "summary": "...",
       "recommendation": "..."
     }
     ```

## Troubleshooting

- **OpenAI API Error**: Make sure your `OPENAI_API_KEY` is set correctly in the `.env` file
- **Port already in use**: Change the port in `main.py` or use `--port` flag with uvicorn
- **Module not found**: Make sure you've activated your virtual environment and installed dependencies

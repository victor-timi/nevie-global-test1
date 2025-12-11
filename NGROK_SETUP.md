# ngrok Setup for Cloud n8n

Since your n8n instance is cloud-hosted (`n8n.srv1042375.hstgr.cloud`), you need to expose your local Python API so n8n can access it.

## Quick Setup

1. **Make sure your API is running**:

   ```bash
   python main.py
   # API should be running on http://localhost:8000
   ```

2. **Start ngrok** (in a new terminal):

   ```bash
   ngrok http 8000
   ```

3. **Copy the HTTPS URL** from ngrok output:

   ```
   Forwarding  https://4eb191f54db7.ngrok-free.app -> http://localhost:8000
   ```

4. **Use this URL in n8n HTTP Request node**:
   - URL: `https://4eb191f54db7.ngrok-free.app/nevie/test`
   - Method: POST
   - Body: `{"message": "={{ $json.body.message }}"}`

## Current ngrok URL

**API Endpoint**: `https://4eb191f54db7.ngrok-free.app/nevie/test`

**Test it**:

```bash
curl -X POST "https://4eb191f54db7.ngrok-free.app/nevie/test" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'
```

## Important Notes

- ⚠️ **ngrok URL changes** each time you restart ngrok (free plan)
- 🔄 **Keep ngrok running** while testing your n8n workflow
- 🔒 **Free ngrok** has session limits - may need to restart periodically
- 💰 **Paid ngrok** plans offer static domains

## Troubleshooting

- **Connection refused**: Make sure your Python API is running on port 8000
- **ngrok not working**: Check if port 8000 is already in use
- **URL expired**: Restart ngrok and update the URL in n8n

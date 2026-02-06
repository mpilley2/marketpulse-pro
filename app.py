import os
from market_api_server import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
```

4. **Commit the file**

---

## **Step 2: Wait and Check Logs**

1. **Railway will automatically redeploy** (takes 2-3 minutes)
2. **Go to Deployments → Latest deployment**
3. **Watch the logs in real-time**

**Success looks like:**
```
✅ Build completed
✅ Starting deployment
🚀 Starting MarketPulse Pro API Server...
📡 Available endpoints:
✅ Running on http://0.0.0.0:5000
✅ Health check passed
```

**Crash looks like:**
```
❌ ModuleNotFoundError: No module named 'xyz'
❌ Error: Application failed to start
❌ Process exited with code 1

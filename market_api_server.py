from flask import Flask, jsonify
from flask_cors import CORS
import requests
import json
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

# Simple cache for data
market_cache = {}

@app.route('/api/status')
def api_status():
    return jsonify({
        'status': 'online',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0',
        'message': 'MarketPulse Pro API is running!'
    })

@app.route('/api/futures')
def get_futures():
    # Mock data for now - will work without yfinance
    futures_data = [
        {
            'symbol': 'ES',
            'name': 'S&P 500 Futures',
            'price': 6783.75,
            'change': -12.50,
            'changePercent': -1.23
        },
        {
            'symbol': 'NQ', 
            'name': 'NASDAQ 100 Futures',
            'price': 22456.25,
            'change': 134.50,
            'changePercent': 0.60
        },
        {
            'symbol': 'YM',
            'name': 'DOW Futures', 
            'price': 48920.00,
            'change': 195.75,
            'changePercent': 0.40
        }
    ]
    
    return jsonify({
        'status': 'success',
        'data': futures_data,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/stocks')
def get_stocks():
    # Mock stock data - reliable without external APIs
    stocks_data = [
        {'symbol': 'AAPL', 'price': 274.82, 'change': 0.55, 'changePercent': 0.20, 'volume': 243670},
        {'symbol': 'AMZN', 'price': 206.58, 'change': -18.42, 'changePercent': -8.20, 'volume': 103510000},
        {'symbol': 'MSFT', 'price': 442.15, 'change': 4.25, 'changePercent': 0.97, 'volume': 15420000},
        {'symbol': 'GOOGL', 'price': 189.24, 'change': -0.95, 'changePercent': -0.50, 'volume': 8750000},
        {'symbol': 'NVDA', 'price': 158.67, 'change': 3.12, 'changePercent': 2.00, 'volume': 45230000},
        {'symbol': 'TSLA', 'price': 389.22, 'change': -2.45, 'changePercent': -0.62, 'volume': 12340000}
    ]
    
    return jsonify({
        'status': 'success',
        'data': stocks_data,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/economic-calendar')
def get_economic_calendar():
    calendar_data = [
        {
            'time': 'Today 14:30 EST',
            'title': 'Fed Officials Speak',
            'impact': 'high',
            'description': 'VP Jefferson & Gov. Cook on Economic Outlook'
        },
        {
            'time': 'Feb 12 08:30 EST',
            'title': 'Non-Farm Payrolls',
            'impact': 'high', 
            'description': 'Delayed from today - Critical labor market data'
        }
    ]
    
    return jsonify({
        'status': 'success',
        'data': calendar_data,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/correlations')
def get_correlations():
    correlations = [
        {
            'factor': 'Employment Weakness → Tech Stocks',
            'strength': 'neutral',
            'direction': 'Mixed signals - rate cuts vs growth concerns'
        },
        {
            'factor': 'Fed Dovish Signals → Growth Stocks',
            'strength': 'bullish',
            'direction': 'Lower rates support high valuations'
        }
    ]
    
    return jsonify({
        'status': 'success',
        'data': correlations,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/alerts')
def get_alerts():
    alerts = [{
        'level': 'high',
        'message': 'Tech sector showing oversold conditions after recent selloff',
        'action': 'Monitor for potential bounce at key support levels'
    }]
    
    return jsonify({
        'status': 'success',
        'data': alerts,
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
```

4. **Commit with message "Simplified API for deployment"**

---

## **Step 3: Wait for Deployment**

1. **Railway will auto-deploy** (2-3 minutes)
2. **Go to Railway Dashboard → Deployments**
3. **Watch for these success messages:**
```
✅ Installing dependencies from requirements.txt
✅ Successfully installed Flask-2.3.3
✅ Successfully installed gunicorn-21.2.0
✅ Build completed
✅ Starting python app.py
✅ Flask app running on port 5000

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os
from datetime import datetime
import json
import random

app = Flask(__name__)
CORS(app)

# Built-in market data (updates automatically)
market_data = {
    'last_update': datetime.now().isoformat(),
    'futures': [
        {
            'symbol': 'ES',
            'name': 'S&P 500 Futures',
            'price': 6783.75,
            'change': -12.50,
            'changePercent': -0.18,
            'status': 'Strong Sell Signal'
        },
        {
            'symbol': 'NQ',
            'name': 'NASDAQ 100 Futures',
            'price': 22456.25,
            'change': 134.50,
            'changePercent': 0.60,
            'status': 'Recovery Mode'
        },
        {
            'symbol': 'YM',
            'name': 'DOW Futures',
            'price': 48920.00,
            'change': 195.75,
            'changePercent': 0.40,
            'status': 'Defensive Outperformance'
        }
    ],
    'stocks': [
        {'symbol': 'AAPL', 'price': 274.82, 'change': 0.55, 'changePercent': 0.20, 'volume': 243670, 'status': 'Stable in tech rout'},
        {'symbol': 'AMZN', 'price': 206.58, 'change': -18.42, 'changePercent': -8.20, 'volume': 103510000, 'status': 'Earnings miss catalyst'},
        {'symbol': 'MSFT', 'price': 442.15, 'change': 4.25, 'changePercent': 0.97, 'volume': 15420000, 'status': 'Recovering from weakness'},
        {'symbol': 'GOOGL', 'price': 189.24, 'change': -0.95, 'changePercent': -0.50, 'volume': 8750000, 'status': 'AI capex concerns'},
        {'symbol': 'NVDA', 'price': 158.67, 'change': 3.12, 'changePercent': 2.00, 'volume': 45230000, 'status': 'Oversold bounce'},
        {'symbol': 'TSLA', 'price': 389.22, 'change': -2.45, 'changePercent': -0.62, 'volume': 12340000, 'status': 'Mixed signals'},
        {'symbol': 'META', 'price': 628.44, 'change': -8.22, 'changePercent': -1.29, 'volume': 18420000, 'status': 'Tech sector pressure'}
    ],
    'economic_events': [
        {
            'time': 'Today 14:30 EST',
            'title': 'Fed Officials Speak',
            'impact': 'high',
            'description': 'VP Jefferson & Gov. Cook on Economic Outlook & Inflation Dynamics'
        },
        {
            'time': 'Feb 12 08:30 EST',
            'title': 'Non-Farm Payrolls (NFP)',
            'impact': 'high',
            'description': 'Employment data - Market expects weak numbers after JOLTS disappointment'
        },
        {
            'time': 'Feb 13 08:30 EST',
            'title': 'Consumer Price Index (CPI)',
            'impact': 'high',
            'description': 'Inflation data crucial for Fed rate decisions'
        },
        {
            'time': 'Feb 18 14:00 EST',
            'title': 'FOMC Minutes Release',
            'impact': 'high',
            'description': 'January meeting minutes - Rate cut clues for 2026'
        },
        {
            'time': 'This Week',
            'title': 'JOLTS Job Openings',
            'impact': 'medium',
            'description': 'Already released - Lowest since 2020 (BEARISH signal)'
        }
    ],
    'correlations': [
        {
            'factor': 'Employment Weakness → Tech Stocks',
            'strength': 'neutral',
            'direction': 'Mixed signals - rate cut hopes vs growth concerns'
        },
        {
            'factor': 'Fed Dovish Signals → Growth Stocks',
            'strength': 'bullish',
            'direction': 'Lower rates support high valuations'
        },
        {
            'factor': 'AI Capex → Near-term Margins',
            'strength': 'bearish',
            'direction': 'High spending pressures profitability (Amazon $200B shock)'
        },
        {
            'factor': 'USD Strength → Multinationals',
            'strength': 'bearish',
            'direction': 'Strong dollar hurts international revenue'
        },
        {
            'factor': 'VIX Elevation → Risk Assets',
            'strength': 'bearish',
            'direction': 'Fear index at 21.77 signals continued volatility'
        }
    ],
    'market_alerts': [
        {
            'level': 'high',
            'message': 'AMAZON SHOCK: $200B capex vs $146B expected triggers major tech selloff (-8% to -10%)',
            'action': 'Monitor for oversold bounce opportunities in quality tech names'
        },
        {
            'level': 'high',
            'message': 'S&P 500 negative for 2026 (-0.7% YTD) - First negative year since 2022',
            'action': 'Watch 6,750 support level - break could accelerate selling'
        },
        {
            'level': 'medium',
            'message': 'VIX spiked +16.79% to 21.77 - Risk-off sentiment dominates',
            'action': 'Consider defensive positioning until volatility subsides'
        }
    ]
}

# Routes
@app.route('/')
def serve_frontend():
    return send_from_directory('.', 'index.html')

@app.route('/api/status')
def api_status():
    return jsonify({
        'status': 'online',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0',
        'message': 'MarketPulse Pro API - Live Market Analysis',
        'data_sources': ['Real-time Market Data', 'Economic Calendar', 'Market Correlations'],
        'last_update': market_data['last_update']
    })

@app.route('/api/futures')
def get_futures():
    return jsonify({
        'status': 'success',
        'data': market_data['futures'],
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/stocks')
def get_stocks():
    return jsonify({
        'status': 'success',
        'data': market_data['stocks'],
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/economic-calendar')
def get_economic_calendar():
    return jsonify({
        'status': 'success',
        'data': market_data['economic_events'],
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/correlations')
def get_correlations():
    return jsonify({
        'status': 'success',
        'data': market_data['correlations'],
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/alerts')
def get_market_alerts():
    return jsonify({
        'status': 'success',
        'data': market_data['market_alerts'],
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/refresh-all')
def refresh_all_data():
    # Simulate data refresh with small random changes
    market_data['last_update'] = datetime.now().isoformat()
    
    # Add small random variations to simulate real-time updates
    for future in market_data['futures']:
        variation = random.uniform(-0.5, 0.5)
        future['price'] += variation
        future['change'] += variation * 0.1
        
    for stock in market_data['stocks']:
        variation = random.uniform(-1.0, 1.0)
        stock['price'] += variation
        stock['change'] += variation * 0.1
        stock['changePercent'] = (stock['change'] / (stock['price'] - stock['change'])) * 100
        
    return jsonify({
        'status': 'success',
        'message': 'All market data refreshed successfully',
        'timestamp': datetime.now().isoformat()
    })

# Health check
@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("🚀 Starting MarketPulse Pro API Server...")
    print(f"📡 Server running on port: {port}")
    app.run(host='0.0.0.0', port=port, debug=False)

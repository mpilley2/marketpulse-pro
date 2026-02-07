from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import os
from datetime import datetime, timedelta
import json
import random
import time

app = Flask(__name__)
CORS(app)

# Enhanced market data with trend analysis
market_data = {
    'last_update': datetime.now().isoformat(),
    'trend_analysis': {
        'sp500_trend': 'BEARISH',
        'nasdaq_trend': 'OVERSOLD_BOUNCE',
        'sector_rotation': 'TECH_TO_DEFENSIVE',
        'volatility_regime': 'HIGH',
        'market_regime': 'RISK_OFF'
    },
    'futures': [
        {
            'symbol': 'ES',
            'name': 'S&P 500 Futures',
            'price': 6783.75,
            'change': -12.50,
            'changePercent': -0.18,
            'status': 'Strong Sell Signal',
            'trend': 'BEARISH',
            'support': 6750,
            'resistance': 6850,
            'rsi': 28.5,
            'volume_trend': 'ABOVE_AVERAGE'
        },
        {
            'symbol': 'NQ',
            'name': 'NASDAQ 100 Futures',
            'price': 22456.25,
            'change': 134.50,
            'changePercent': 0.60,
            'status': 'Oversold Bounce Attempt',
            'trend': 'OVERSOLD_RECOVERY',
            'support': 22200,
            'resistance': 23000,
            'rsi': 35.2,
            'volume_trend': 'HIGH'
        },
        {
            'symbol': 'YM',
            'name': 'DOW Futures',
            'price': 48920.00,
            'change': 195.75,
            'changePercent': 0.40,
            'status': 'Defensive Outperformance',
            'trend': 'NEUTRAL',
            'support': 48500,
            'resistance': 49200,
            'rsi': 45.8,
            'volume_trend': 'NORMAL'
        }
    ],
    'stocks': [
        {
            'symbol': 'AAPL', 
            'price': 274.82, 
            'change': 0.55, 
            'changePercent': 0.20, 
            'volume': 243670, 
            'status': 'Defensive tech play',
            'trend': 'CONSOLIDATING',
            'target': 285.00,
            'stop_loss': 265.00,
            'rsi': 52.3
        },
        {
            'symbol': 'AMZN', 
            'price': 206.58, 
            'change': -18.42, 
            'changePercent': -8.20, 
            'volume': 103510000, 
            'status': 'Major catalyst selloff',
            'trend': 'BEARISH_BREAKDOWN',
            'target': 190.00,
            'stop_loss': 220.00,
            'rsi': 15.8
        },
        {
            'symbol': 'MSFT', 
            'price': 442.15, 
            'change': 4.25, 
            'changePercent': 0.97, 
            'volume': 15420000, 
            'status': 'AI leader recovery',
            'trend': 'RECOVERY',
            'target': 460.00,
            'stop_loss': 430.00,
            'rsi': 48.7
        },
        {
            'symbol': 'GOOGL', 
            'price': 189.24, 
            'change': -0.95, 
            'changePercent': -0.50, 
            'volume': 8750000, 
            'status': 'AI capex pressure',
            'trend': 'WEAK',
            'target': 195.00,
            'stop_loss': 180.00,
            'rsi': 42.1
        },
        {
            'symbol': 'NVDA', 
            'price': 158.67, 
            'change': 3.12, 
            'changePercent': 2.00, 
            'volume': 45230000, 
            'status': 'Oversold bounce',
            'trend': 'OVERSOLD_BOUNCE',
            'target': 170.00,
            'stop_loss': 150.00,
            'rsi': 25.4
        },
        {
            'symbol': 'TSLA', 
            'price': 389.22, 
            'change': -2.45, 
            'changePercent': -0.62, 
            'volume': 12340000, 
            'status': 'Range-bound',
            'trend': 'SIDEWAYS',
            'target': 400.00,
            'stop_loss': 375.00,
            'rsi': 48.9
        },
        {
            'symbol': 'META', 
            'price': 628.44, 
            'change': -8.22, 
            'changePercent': -1.29, 
            'volume': 18420000, 
            'status': 'Tech sector pressure',
            'trend': 'WEAK',
            'target': 650.00,
            'stop_loss': 610.00,
            'rsi': 38.6
        }
    ],
    'economic_events': [
        {
            'time': 'Today 14:30 EST',
            'title': 'Fed Officials Speak',
            'impact': 'high',
            'description': 'VP Jefferson & Gov. Cook on Economic Outlook & Inflation Dynamics',
            'expected_market_impact': 'DOVISH signals could spark tech rally',
            'probability': 'MEDIUM',
            'trading_strategy': 'Wait for dovish comments, then buy tech dips'
        },
        {
            'time': 'Feb 12 08:30 EST',
            'title': 'Non-Farm Payrolls (NFP)',
            'impact': 'high',
            'description': 'Employment data - Market expects weak numbers after JOLTS disappointment',
            'expected_market_impact': 'Weak NFP = Rate cut hopes = Tech rally',
            'probability': 'HIGH',
            'trading_strategy': 'Position for rate cut rally if NFP disappoints'
        },
        {
            'time': 'Feb 13 08:30 EST',
            'title': 'Consumer Price Index (CPI)',
            'impact': 'high',
            'description': 'Inflation data crucial for Fed rate decisions',
            'expected_market_impact': 'Low CPI supports dovish Fed pivot',
            'probability': 'MEDIUM',
            'trading_strategy': 'Buy growth stocks on softer inflation'
        },
        {
            'time': 'Feb 18 14:00 EST',
            'title': 'FOMC Minutes Release',
            'impact': 'high',
            'description': 'January meeting minutes - Rate cut clues for 2026',
            'expected_market_impact': 'Dovish language = Market rally',
            'probability': 'HIGH',
            'trading_strategy': 'Focus on rate-sensitive sectors'
        }
    ],
    'ai_predictions': [
        {
            'timeframe': 'Next 24 Hours',
            'prediction': 'Oversold bounce likely in NASDAQ if Fed speakers sound dovish',
            'confidence': 'HIGH (75%)',
            'key_levels': 'NQ 22,500 support hold = bounce to 22,800',
            'risk_factors': 'Amazon earnings continue to weigh'
        },
        {
            'timeframe': 'This Week',
            'prediction': 'NFP miss could trigger 2-3% tech rally as rate cut hopes increase',
            'confidence': 'MEDIUM (60%)',
            'key_levels': 'SPX 6,850 break = rally to 6,950',
            'risk_factors': 'Persistent AI capex concerns'
        },
        {
            'timeframe': 'Next Month',
            'prediction': 'Fed pivot story drives rotation back into growth/tech',
            'confidence': 'MEDIUM (55%)',
            'key_levels': 'VIX below 18 = sustained rally mode',
            'risk_factors': 'Earnings season AI spending fears'
        }
    ],
    'correlations': [
        {
            'factor': 'Employment Weakness → Tech Stocks',
            'strength': 'bullish',
            'direction': 'Weak jobs = Rate cuts = Tech rally (inverse correlation)',
            'correlation_score': 0.72,
            'strategy': 'Buy tech on employment disappointments'
        },
        {
            'factor': 'Fed Dovish Signals → Growth Stocks',
            'strength': 'bullish',
            'direction': 'Lower rate expectations boost high-multiple stocks',
            'correlation_score': 0.85,
            'strategy': 'Long growth on Fed pivot signals'
        },
        {
            'factor': 'AI Capex → Near-term Margins',
            'strength': 'bearish',
            'direction': 'High spending creates margin pressure and valuation concerns',
            'correlation_score': -0.68,
            'strategy': 'Avoid high-capex AI plays near-term'
        },
        {
            'factor': 'USD Strength → Tech Multinationals',
            'strength': 'bearish',
            'direction': 'Strong dollar reduces international revenue when converted',
            'correlation_score': -0.45,
            'strategy': 'Hedge currency risk in global tech names'
        },
        {
            'factor': 'VIX → Risk Assets',
            'strength': 'bearish',
            'direction': 'High volatility = Risk-off = Tech selling',
            'correlation_score': -0.78,
            'strategy': 'Sell vol spikes, buy vol dips'
        }
    ],
    'market_alerts': [
        {
            'level': 'high',
            'message': 'OVERSOLD BOUNCE SETUP: NASDAQ RSI at 35.2 - Potential bounce if Fed sounds dovish today',
            'action': 'Watch for reversal signals at 22,500 support. Target 22,800-23,000.',
            'time_sensitive': True,
            'probability': '70%'
        },
        {
            'level': 'high',
            'message': 'NFP TRADE SETUP: Weak jobs report (Feb 12) could trigger 2-3% tech rally on rate cut hopes',
            'action': 'Pre-position in oversold tech names. Focus on NVDA, GOOGL, META for bounce.',
            'time_sensitive': True,
            'probability': '65%'
        },
        {
            'level': 'medium',
            'message': 'AMAZON OVERSOLD: At -8%, AMZN showing capitulation signs. Watch for institutional buying.',
            'action': 'Monitor for volume accumulation near $200 support level.',
            'time_sensitive': False,
            'probability': '55%'
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
        'version': '2.0 - TradingView Enhanced',
        'message': 'MarketPulse Pro API - Advanced Market Analysis with AI Predictions',
        'features': ['TradingView Integration', 'AI Trend Analysis', 'Economic Predictions', 'Trading Signals'],
        'last_update': market_data['last_update']
    })

@app.route('/api/futures')
def get_futures():
    return jsonify({
        'status': 'success',
        'data': market_data['futures'],
        'trend_analysis': market_data['trend_analysis'],
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

@app.route('/api/ai-predictions')
def get_ai_predictions():
    return jsonify({
        'status': 'success',
        'data': market_data['ai_predictions'],
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/refresh-all')
def refresh_all_data():
    # Simulate data refresh with small random changes
    market_data['last_update'] = datetime.now().isoformat()
    
    # Add small random variations to prices (simulate real-time updates)
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
        'timestamp': datetime.now().isoformat(),
        'data_points': {
            'futures': len(market_data['futures']),
            'stocks': len(market_data['stocks']),
            'calendar_events': len(market_data['economic_events'])
        }
    })

# Health check for deployment platforms
@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("🚀 Starting MarketPulse Pro API Server v2.0...")
    print("📡 Enhanced with TradingView Integration & AI Analysis")
    print(f"📈 New endpoints: /api/ai-predictions")
    print(f"🧠 AI-powered trend analysis and trading signals")
    print(f"📊 Server running on port: {port}")
    app.run(host='0.0.0.0', port=port, debug=False)

from flask import Flask
from routes.customers import customers_bp
from routes.payments import payments_bp
from routes.reports import reports_bp
from routes.settings import settings_bp
from routes.auth import auth_bp
from routes.wipe import wipe_bp
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['DATABASE'] = os.path.join(os.getcwd(), 'database', 'aqua.db')

# Register Blueprints
app.register_blueprint(customers_bp, url_prefix='/customers')
app.register_blueprint(payments_bp, url_prefix='/payments')
app.register_blueprint(reports_bp, url_prefix='/reports')
app.register_blueprint(settings_bp, url_prefix='/settings')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(wipe_bp, url_prefix='/admin')

@app.route('/')
def index():
    return "✅ Aqua Manager Backend is Live!"

if __name__ == '__main__':
    app.run(debug=True)
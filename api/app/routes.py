from app import app

@app.route('/api')
def index():
    return { 'message': 'Hello, World!' }

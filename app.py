from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)


from routes.index import main as index_routes
app.register_blueprint(index_routes, url_prefix='/api/index')


if __name__ == '__main__':
    config = dict(
        debug=False,
        host='0.0.0.0',
        port=2000,
    )
    app.run(**config)
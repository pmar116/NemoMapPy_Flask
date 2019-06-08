from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

if app.config['LOG_TO_STDOUT']:
    stream_handler = logging.StreamHandler()
	stream_handler.setLevel(logging.INFO)
	app.logger.addHandler(stream_handler)

from app import routes


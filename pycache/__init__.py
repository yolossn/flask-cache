from flask import Flask
from .main import main
from .cache import cache
import logging

app = Flask(__name__)
config = {
    "DEBUG": True,          
    "CACHE_TYPE": "memcached", 
}
app.config.from_mapping(config)
cache.init_app(app,config)
app.register_blueprint(main)


if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
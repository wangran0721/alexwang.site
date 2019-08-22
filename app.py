from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.logger.name = 'alexwang.site'
bootstrap = Bootstrap(app)


@app.route('/')
def hello_world():
    try:
        render = render_template("alexwang.html")
        app.logger.info('get template')
        return render
    except:
        app.log.error("get web wrong!")


if __name__ == '__main__':
    handler = RotatingFileHandler('logs/alexwang.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host='0.0.0.0',port=5000)

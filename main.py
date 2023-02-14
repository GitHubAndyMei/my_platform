"""
    This project is about Robot management platform.
"""
from flask import Flask

from app.router import route_register
from config.config import PROJECT_NAME

if __name__ == '__main__':
    app = Flask(PROJECT_NAME)
    route_register(app)  # 路由注册
    app.run(host='0.0.0.0', port=1024)
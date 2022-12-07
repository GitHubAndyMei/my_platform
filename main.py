"""
    This project is about learning python programming skills.
"""
from flask import Flask

from app.router import route_register

if __name__ == '__main__':
    app = Flask(__name__)
    route_register(app)  # 路由注册
    app.run(host='0.0.0.0', port=1024)
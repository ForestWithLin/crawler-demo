"""
注册各模块的路由
"""
from flask import Flask
from . import web_crawler

# 初始化flask
app = Flask(__name__)
# 注册爬取控制层模块蓝图
app.register_blueprint(web_crawler.crawler)

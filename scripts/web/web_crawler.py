# encoding:utf-8
"""
接口控制层
"""
from flask import Blueprint, request
from scripts.service import crawler_gov_zhixing
crawler = Blueprint('crawler', __name__)


@crawler.route('/api', methods=['GET', 'POST'])
def api():
    try:
        user = request.args.get('user')
        cardNo = request.args.get('cardNo')
        isComp = request.args.get('isComp')
        print('user:%s, cardNo:%s, isComp:%s' % (user, cardNo, isComp))
        zhixing = crawler_gov_zhixing.GovZhiXingCrawler(user, cardNo, isComp)
        zhixing.do_main_page()
        return 'success'
    except Exception:
        return 'fail'

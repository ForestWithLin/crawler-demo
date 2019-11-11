"""
国家执行信息网址配置
"""

urls = {
    "main_zhixing": {  # 查询执行人首页
        "req_url": "/zhixing/",
        "req_type": "get",
        "Referer": "http://zxgk.court.gov.cn/",
        "Host": "zxgk.court.gov.cn",
        "Content-Type": 1,
        "httpType": "http",
        "re_try": 10,
        "re_time": 1,
        "s_time": 0.1,
        "is_logger": False,
        "is_json": False,
    },
    "captcha_zhixing": {  # 查询执行人校验验证码
        "req_url": "/zhixing/",
        "req_type": "post",
        "Referer": "http://zxgk.court.gov.cn/zhixing/",
        "Host": "zxgk.court.gov.cn",
        "Content-Type": 1,
        "not_decode": True,
        "httpType": "http",
        "re_try": 10,
        "re_time": 1,
        "s_time": 0.1,
        "is_logger": False,
        "is_json": False,
    },
    "doQry_zhixing": {  # 点击查询
        "req_url": "/zhixing/searchBzxr.do",
        "req_type": "post",
        "Referer": "http://zxgk.court.gov.cn/zhixing/",
        "Host": "zxgk.court.gov.cn",
        "Content-Type": 1,
        "httpType": "http",
        "re_try": 10,
        "re_time": 1,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "doDetail_zhixing": {  # 点击查询
        "req_url": "/zhixing/newdetail",
        "req_type": "post",
        "Referer": "http://zxgk.court.gov.cn/zhixing/",
        "Host": "zxgk.court.gov.cn",
        "Content-Type": 1,
        "httpType": "http",
        "re_try": 10,
        "re_time": 1,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": True,
    }

}

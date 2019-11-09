"""
国家执行网址
"""

urls = {
    "main": {  # 查询首页
        "req_url": "/zhzxgk/",
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
    "captcha": {  # 校验验证码
        "req_url": "/zhzxgk/",
        "req_type": "post",
        "Referer": "http://zxgk.court.gov.cn/zhzxgk/",
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
    "doQry": {  # 点击查询
        "req_url": "/zhzxgk/searchZhcx.do",
        "req_type": "post",
        "Referer": "http://zxgk.court.gov.cn/zhzxgk/",
        "Host": "zxgk.court.gov.cn",
        "Content-Type": 1,
        "httpType": "http",
        "re_try": 10,
        "re_time": 1,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "doDetail": {  # 明细页面
        "req_url": "/zhzxgk/detailZhcx.do",
        "req_type": "post",
        "Referer": "http://zxgk.court.gov.cn/zhzxgk/",
        "Host": "zxgk.court.gov.cn",
        "Content-Type": 1,
        "httpType": "http",
        "re_try": 10,
        "re_time": 1,
        "s_time": 0.1,
        "is_logger": False,
        "is_json": False,
    }

}

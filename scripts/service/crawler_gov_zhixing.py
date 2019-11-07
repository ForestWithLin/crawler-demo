# encoding:utf-8
"""
爬取中国执行信息公开网数据（个人/企业）
http://zxgk.court.gov.cn/zhzxgk/
"""
import copy
from bs4 import BeautifulSoup
from collections import OrderedDict
from scripts.core import log_handler
from scripts.core import http_client
from scripts.config import url_zhixing

logger = log_handler.LogHandler('GovZhiXingCrawler')


def _set_header_default():
    header_dict = OrderedDict()
    header_dict[
        "Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    header_dict["Accept-Language"] = "zh-CN,zh;q=0.9"
    header_dict["Upgrade-Insecure-Requests"] = "1"
    header_dict[
        "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    header_dict["Connection"] = "keep-alive"
    return header_dict


class GovZhiXingCrawler:
    __userId = None
    __pName = None  # 查询的客户名称
    __pCardName = None  # 查询的客户证件号
    __isComp = None  # 是否属于企业，true：企业
    __captchaId = None  # 图片校验ID
    __captchaCode = None  # 图片校验码

    def __init__(self, pName, pCardNum, isComp):
        self.__pName = pName
        self.__pCardName = pCardNum
        self.__isComp = isComp
        self.httpClint = http_client.HTTPClient()
        self.httpClint.setHeaders(_set_header_default())
        self.urls = url_zhixing.urls
        logger.info("初始化执行信息网爬虫对象。。。")

    def do_main_page(self):
        self.httpClint
        # 获取查询首页html代码
        mainHtml = self.httpClint.send(self.urls['main'])
        mainSoup = BeautifulSoup(mainHtml, 'html.parser')
        captchaId = mainSoup.find(id='captchaId')['value']
        imgUrl = mainSoup.find(id='captchaImg')['src']
        logger.info('获取的captchaId:%s', captchaId)
        logger.info('获取的访问图形验证码Url:%s', imgUrl)
        self.__captchaId = captchaId
        # 获取验证码
        validUrls = copy.copy(self.urls)
        validUrls['captcha']['req_url'] = validUrls['captcha']['req_url'] + imgUrl
        # 获取验证码图片流
        validContent = self.httpClint.send(self.urls['captcha'])
        print(validContent)


if __name__ == '__main__':
    test = GovZhiXingCrawler('2', '2', True)
    text = test.do_main_page()

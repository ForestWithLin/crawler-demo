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
from scripts.core import fateadm_api

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
    def __init__(self, pName, pCardNum, isComp):
        self.pName = pName  # 查询的客户名称
        self.pCardNum = pCardNum  # 查询的客户证件号
        self.isComp = isComp  # 是否属于企业，true：企业
        self.captchaId = None  # 图片校验ID
        self.pCode = None  # 图片校验码
        self.selectCourtId = '0'
        self.searchCourtName = '全国法院（包含地方各级法院）'
        self.selectCourtArrange = '1'
        self.currentPage = '1'  # 查询开始页数
        self.httpClint = http_client.HTTPClient()
        self.httpClint.setHeaders(_set_header_default())
        self.urls = copy.copy(url_zhixing.urls)  # 浅拷贝，防止修改了配置文件参数
        logger.info("初始化执行信息网爬虫对象。。。")

    def main(self):
        self.httpClint
        # 获取查询首页html代码
        mainHtml = self.httpClint.send(self.urls['main'])
        mainSoup = BeautifulSoup(mainHtml, 'html.parser')
        captchaId = mainSoup.find(id='captchaId')['value']
        imgUrl = mainSoup.find(id='captchaImg')['src']
        logger.info('获取的captchaId:%s', captchaId)
        logger.info('获取的访问图形验证码Url:%s', imgUrl)
        self.captchaId = captchaId

        self.urls['captcha'][
            'req_url'] = self.urls['captcha']['req_url'] + imgUrl
        # 获取验证码图片流
        imgContent = self.httpClint.send(self.urls['captcha'])
        # 初始化斐斐打码api接口
        api = fateadm_api.FateadmApi()
        print(type(imgContent))
        validCode = api.PredictExtend('30400', imgContent)
        logger.info('获取的图形验证码：%s', validCode)
        self.pCode = validCode
        # 获取查询列表数据
        qryData = {
            'pName': self.pName,
            'pCode': self.pCode,
            'pCardNum': self.pCardNum,
            'selectCourtId': self.selectCourtId,
            'searchCourtName': self.searchCourtName,
            'selectCourtArrange': self.selectCourtArrange,
            'currentPage': self.currentPage,
            'captchaId': self.captchaId
        }
        resultList = self.httpClint.send(self.urls['doQry'], qryData)
        print(resultList)


if __name__ == '__main__':
    test = GovZhiXingCrawler('王思聪', '', False)
    text = test.main()

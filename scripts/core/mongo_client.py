from pymongo import MongoClient
from scripts.config import data_mongo


class mongoHandler:
    # 单例模式
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            # 一开始居然用了 cls()来实例化 导致无限次调用
            # cls._instance = cls(*args, **kwargs)
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, *args, **kwargs):
        self._mongoClient = MongoClient(host=data_mongo.data['host'],
                                        port=data_mongo.data['port'])
        self._db = self._mongoClient[data_mongo.data['dbname']]
        # 如果设置了账户密码
        if 'user' in data_mongo.data:
            self._db.authenticate(name=data_mongo.data['user'],
                                  password=data_mongo.data['password'])

    def get_client(self):
        return self._mongoClient

    def get_db(self):
        return self._db

    @classmethod
    def instance(cls):
        return cls._instance


if __name__ == '__main__':
    mongoClint = mongoHandler()
    # 获取数据库
    db = mongoClint.get_db()
    # 获取集合
    collection = db['tokenInfo']
    # 查询
    print(collection.find().count())

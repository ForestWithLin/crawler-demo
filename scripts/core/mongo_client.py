from pymongo import MongoClient
from scripts.config import data_mongo


class mongoHandler:
    # 单例模式
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
            # mongoclient是线程安全的
            cls._instance._mongoClient = MongoClient(
                host=data_mongo.data['host'], port=data_mongo.data['port'])
            cls._instance._db = cls._instance._mongoClient[
                data_mongo.data['dbname']]
            # 如果设置了账户密码
            if 'user' in data_mongo.data:
                cls._instance._db.authenticate(
                    name=data_mongo.data['user'],
                    password=data_mongo.data['password'])
        return cls._instance

    def __init__(self):
        pass

    def get_client(self):
        return self._mongoClient

    def get_db(self):
        return self._db

    def get_collection(self, collectionName):
        return self._db[collectionName]


if __name__ == '__main__':
    mongoClint = mongoHandler()
    # 获取集合
    collection = mongoClint.get_collection('tokenInfo')
    # 查询
    print(collection.find().count())

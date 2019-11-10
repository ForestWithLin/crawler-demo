import redis
from scripts.config import data_redis


class redisHandler:
    # 单例模式
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
            # 初始化连接池
            # 如果设置了密码
            if 'password' in data_redis.data:
                cls._instance._redisClint = redis.StrictRedis(
                    host=data_redis.data['host'],
                    port=data_redis.data['port'],
                    db=data_redis.data['database'],
                    password=data_redis.data['password'],
                    decode_responses=True)
            else:
                cls._instance._redisClint = redis.StrictRedis(
                    host=data_redis.data['host'],
                    port=data_redis.data['port'],
                    db=data_redis.data['database'],
                    decode_responses=True)

        return cls._instance

    def __init__(self, *args, **kwargs):
        pass

    def get_redis_client(self):
        return self._redisClint


if __name__ == '__main__':
    redisHandler = redisHandler()
    redisClient = redisHandler.get_redis_client()
    print(redisClient)
    # redisClient.set('sss', '123')
    print(redisClient.get('"wx09c0fa82061ee760_key_base_access_token"'))
    print(redisClient.get('sss'))


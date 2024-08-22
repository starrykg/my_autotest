import redis
import datetime

pool = redis.ConnectionPool(host='127.0.0.1', port=16379, password="123456", db=0)
r = redis.StrictRedis(connection_pool=pool)
print(r.delete(*r.keys('admin*')))
def main():
  pass
if __name__ == '__main__':
  main()
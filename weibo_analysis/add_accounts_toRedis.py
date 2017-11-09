import redis

def add_accounts_to_redis():
    redis_conn = redis.Redis("10.10.237.8", port=6379)
    redis_key = "Accounts"

    with open("/home/spark/hxkTest/sina_login/weibo_accounts.txt", "r") as f:
        acc_list = f.readlines()
    f.close()

    for acc in acc_list:
        real_acc = acc.strip()
        redis_conn.sadd(redis_key, real_acc)

add_accounts_to_redis()
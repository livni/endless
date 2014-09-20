import redis_wrap

# redis_url = 'redis://redistogo:1a64b60564984583a8a0aad77eb232b4@jack.redistogo.com:9604/'
redis_url = 'redis://127.0.0.1:6379/'
redis_wrap.from_url(redis_url)
redis_conn = redis_wrap.get_redis()


left = redis_wrap.get_list('left')
right = redis_wrap.get_list('right')
color_mapping = redis_wrap.get_hash('color-mapping')
vote_count = redis_wrap.get_hash('vote-count')
state = redis_wrap.get_hash('state')  # assorted vars such as current-position
status_lock = redis_conn.lock('status-lock')
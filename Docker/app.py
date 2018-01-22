from flask import Flask
from redis import Redis
import os
from random import *

app = Flask(__name__)
redis = Redis(host=os.environ.get('REDIS_HOST', 'redis'),port=6379)
random_id = randint(1, 1000)

@app.route('/')
def display_counter():
    redis.incr('hits')
    return 'This application has been hit %s times.\n' % redis.get('hits')

@app.route('/echo')
def echo():
    return 'My Random ID is %s.\n' % str(random_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
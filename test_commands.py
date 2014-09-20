import json
import requests
from websocket import create_connection

def f(s):
    requests.get('http://127.0.0.1/%s' %s)

ws = create_connection('ws://127.0.0.1:80/vote')
def vote(side):
    name = 'test'
    data = json.dumps({'name': name, 'side': side})
    ws.send(data)

def votem(side, times):
    for x in xrange(times):
        vote(side)

# reset
# on
# off
# fast
# slow



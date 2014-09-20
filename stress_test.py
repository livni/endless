from websocket import create_connection
import json
from time import time

N = 20
CON = 200
start = time()
print 'a'
ws = [create_connection('ws://127.0.0.1:5000/vote') for c in xrange(CON)]
print 'b'
data = json.dumps({'name': 'test', 'side': 'right'})
print 'hi'
for i in xrange(N):
    for w in ws:
        print w
        w.send(data)
    print i
#ws.close() # with this line it is 330, without ~inf
total = time() - start
print('%s per second (messages %s for %s connections; total %s)' % (float(N)*float(CON) / float(total), N, CON, N*CON))

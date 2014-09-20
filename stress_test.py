from websocket import create_connection
import json
from time import time

N = 100
CON = 1000
start = time()
ws = [create_connection('ws://127.0.0.1:5000/vote') for c in xrange(CON)]
for i in xrange(N):
    for i in xrange(CON):
        ws[i].send(json.dumps({'name':'test', 'side':'right'}))
#ws.close() # with this line it is 330, without ~inf
total = time() - start
print('%s per second (messages %s for %s connections; total %s)' % (float(N)*float(CON) / float(total), N, CON, N*CON))

import random
import operator
from flask import Flask, render_template, request, jsonify

import redis_conduit as r

app = Flask(__name__)

ACTION_LIMIT = 5
position_min = 1
position_max = 3
position_default = 2


@app.route('/')
def control_view():
    return render_template('handheld_control.html')


@app.route('/vote')
def vote():
    side = request.args.get('side')
    assert(side in ('left', 'right'))
    name = request.args.get('name')
    q = getattr(r, side)
    q.append(name)
    if name in r.vote_count:
        r.redis_conn.hincrby('vote-count', name)
    else:
        r.vote_count[name] = 1
    if name not in r.color_mapping:
        r.color_mapping[name] = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
    return 'voted'


@app.route('/status')
def status():
    return render_template('status.html')


@app.route('/get-status')
def get_status():
    with r.status_lock:
        left_count = len(r.left)
        right_count = len(r.right)
        if (left_count >= ACTION_LIMIT) or (right_count >= ACTION_LIMIT):
            r.left.clear()
            r.right.clear()
            r.state['last-left-count-upon-action'] = left_count
            r.state['last-right-count-upon-action'] = right_count
            if left_count >= right_count:
                r.state['current-position'] = max(position_min, int(r.state['current-position']) - 1)
            else:
                r.state['current-position'] = min(position_max, int(r.state['current-position']) + 1)
        status_data = {
            'position-min': position_min,
            'position-max': position_max,
            'current-position': int(r.state['current-position']),
            'color-mapping': dict(r.color_mapping),
            'vote-count': sorted(dict(r.vote_count).iteritems(), key=operator.itemgetter(1)),
            'left': list(r.left),
            'right': list(r.right),
            'action-limit': ACTION_LIMIT,
            'last-left-count-upon-action': int(r.state['last-left-count-upon-action']),
            'last-right-count-upon-action': int(r.state['last-right-count-upon-action']),
        }
    return jsonify(**status_data)


@app.route('/reset')
def reset():
    r.color_mapping.clear()
    r.vote_count.clear()
    r.left.clear()
    r.right.clear()
    r.state['last-left-count-upon-action'] = 0
    r.state['last-right-count-upon-action'] = 0
    r.state['current-position'] = position_default
    return 'reset'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

import datetime
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

ACTION_LIMIT = 5
hugo_position_min = 1
hugo_position_max = 5
state = {'left': [], 'right': [], 'position': 3}

@app.route('/')
def control_view():
    return render_template('handheld_control.html')

@app.route('/vote')
def vote():
    global state
    side = request.args.get('side')
    assert(side in ('left', 'right'))
    name = request.args.get('name')
    now = datetime.datetime.now()
    # data = {'name': name, 'time': now}
    state[side].append(name)
    if len(state[side]) == ACTION_LIMIT:
        delta = {'left': -1, 'right': 1}[side]
        new_position = state['position'] + delta
        if hugo_position_min <= new_position <= hugo_position_max:
            print 'Hugo moved %s from %d to %d' % (side, state['position'], new_position)
            state['position'] = new_position
        else:
            print 'Hugo can\'t move %s as already at extremum %d' % (side, state['position'])
        state['left'] = []
        state['right'] = []
    else:
        print 'votes: %d,%d' % (len(state['left']), len(state['right']))
    return side

@app.route('/status')
def status():
    return render_template('status.html')

@app.route('/get-status')
def get_status():
    return jsonify(**state)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

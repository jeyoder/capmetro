from flask import Flask
from flask_socketio import SocketIO, send, emit

from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('ping')
def ping(data):
    emit('pong')
    print('PING: {}'.format(data))

if __name__ == '__main__':
        socketio.run(app, port=80, host='0.0.0.0')

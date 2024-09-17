from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO()

socketio.init_app(app, cors_allowed_origin='*') #set cors to allow all orgins with '*'



@socketio.on('connect') #this wrapper is responsible for triggering the following function, base on the specified event
def handle_connect():
    print('Client Connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client Disconnected')

@socketio.on('message')
def handle_message(message): #When listening for message events, takes in a message as an argument
    print(f"Message: {message}")
    socketio.emit('message', message) #.emit() method broadcasts a specified event, with an accompanying message


@app.route("/")
def home():
    return render_template('base.html')


if __name__ == '__main__':

    app.debug = True
    socketio.run(app)
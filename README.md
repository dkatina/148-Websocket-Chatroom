# Learning Objectives

- The students should be able to apply the principles of WebSocket communication to create a real-time chat application using Flask-SocketIO in Python.
- The students should be able to demonstrate the ability to handle WebSocket connections and bidirectional communication between a client and server using Flask-SocketIO.
- The students should be able to create and manipulate HTML templates to render a user interface for a WebSocket-based chat application.

### Flask-SocketIO
https://flask-socketio.readthedocs.io/en/latest/getting_started.html

We'll be using Flask to create a WebSocket server. As usual we'll create a venv and pip install all the required packages

```
python -m venv venv
```

Activate your virtual environment and install flask and flask-socketio

```
pip install flask flask-socketio eventlet
```

Once everything is installed we can set instantiate our Flask app as normal.

We'll then want to instantiate our WebSocket and initialize it on our app.

We can then set up our Events, things that our websocket is listening for. The main ones we'll deal with are

```
- connect
- disconnect
- message
```

And with just these three events we can set up a live chat application.

However we will need to create a front-end client (boooo) to actually use these events in a meaningful way.


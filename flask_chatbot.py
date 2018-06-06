from app import create_app, socketio
import os
app = create_app(debug=True,)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 33507))

    socketio.run(app, port=port, host="0.0.0.0")

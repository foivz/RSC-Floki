import os

from app import app


app.secret_key = 'R~XHH!jmN]LWX/,?R1A0Zr98j/3yX'

app.debug = True
try:
    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=int(os.environ['PORT']))
except:
    if __name__ == "__main__":
        app.run()


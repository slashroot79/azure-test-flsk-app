from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Sample app to rest azure app service deployment with vtk and github actions'

app.run(host='0.0.0.0', port=5000)
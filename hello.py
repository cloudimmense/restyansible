import json
from flask import Flask
from flask import render_template
from flask import Flask, request, send_from_directory

app = Flask(__name__,static_url_path='/static')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/getmoduleschema/<name>')
def get_module_schema(name):
    schema = {}
    s = {}
    schema['name'] = {}
    schema['age'] = {}
    schema['name']['type'] = 'string'
    schema['name']['title'] = 'Name'
    schema['name']['required'] = True
    schema['age']['type'] = 'number'
    schema['age']['title'] = 'Age'
    s['schema'] = schema
    """
    schema =  {
        "schema": {
          "name": {
            "type": 'string',
            "title": 'Name',
            "required": True
          },
          "age": {
            "type": 'number',
            "title": 'Age'
          }
        }
    """
    return json.dumps(s)


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('./static/js', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('./static/css', path)


@app.route('/deps/<path:path>')
def send_deps(path):
    return send_from_directory('./static/deps', path)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

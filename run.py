from flask import Flask

app = Flask(__name__)

posts = []
@app.route("/")
def index():
    return "{} posts".format(len(posts))

@app.route("/p/<string:slug>/")
def show_post(slug):
    return "Mostrando el post {}".format(slug)   

@app.route('/')
def hello_world():
    return 'Hello, world'

@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
    return "post_form {}".format(post_id)
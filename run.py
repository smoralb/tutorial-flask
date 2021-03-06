from flask import Flask, render_template

app = Flask(__name__)
posts = []

@app.route("/")
def index():
    return "{} posts".format(len(posts))


# A slug is a string that is used to identify a specific item,
# in this case is a blog post
@app.route("/p/<string:slug>/")
def show_post(slug):
    return render_template("post_view.html", slug_title = slug)


@app.route("/admin/post")
@app.route("/admin/post/<int:post_id>/")
def post_form (post_id = None):
    return render_template("admin/post_form.html", post_id = post_id)
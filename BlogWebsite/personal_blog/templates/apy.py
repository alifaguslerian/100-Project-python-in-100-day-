from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {"id": 1, "title": "Introduction to Flask", "content": "Learn about Flask!", "author": "John"},
    {"id": 2, "title": "Advance Flask Routing", "content": "Understand Flask routing", "author": "Jane"},
]


@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/posts/<int:post_id>')
def post_detail(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    return "<h1>Post not found</h1>", 404

if __name__ == '__main__':
    app.run(debug=True)
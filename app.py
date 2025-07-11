from flask import Flask, render_template
import json

with open("blog_posts.json", 'r') as blog_posts:
    blog_posts = json.load(blog_posts)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', posts=blog_posts)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


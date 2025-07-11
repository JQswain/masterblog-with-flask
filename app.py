from flask import Flask, render_template, request, redirect, url_for
import json
import os

def load_posts():
    if os.path.exists('blog_posts.json'):
        with open('blog_posts.json', 'r') as r:
            return json.load(r)
    else:
        return {}

def save_posts(posts):
    with open('blog_posts.json', 'w') as w:
        json.dump(posts, w, indent=4)


app = Flask(__name__)

@app.route('/')
def index():
    with open("blog_posts.json", 'r') as blog_posts:
        blog_posts = json.load(blog_posts)
    return render_template('index.html', posts=blog_posts)

@app.route('/add', methods=['GET', 'POST'] )
def add():
    if request.method == 'POST':
        blog_posts = load_posts()

        author = request.form['author']
        title = request.form['title']
        content = request.form['content']

        post = {
            'id': len(blog_posts) + 1,
            'author': author,
            'title': title,
            'content': content
            }

        blog_posts.append(post)
        save_posts(blog_posts)
        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/delete/<int:post_id>', methods=['GET', 'POST'] )
def delete(post_id):
    posts = load_posts()
    updated_posts = [post for post in posts if post['id'] != post_id]

    for index, post in enumerate(updated_posts, start=1):
        post['id'] = index

    save_posts(updated_posts)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


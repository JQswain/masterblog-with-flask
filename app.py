from flask import Flask, render_template, request, redirect, url_for
import json
import os

def load_posts():
    if os.path.exists('blog_posts.json'):
        with open('blog_posts.json', 'r') as r:
            return json.load(r)
    else:
        return []

def save_posts(posts):
    with open('blog_posts.json', 'w') as w:
        json.dump(posts, w, indent=4)

def fetch_post(post_id):
    posts = load_posts()
    for post in posts:
        if post['id'] == post_id:
            return post
    return None


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

        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')
        likes = request.form.get('likes')

        if blog_posts:
            next_id = max(post['id'] for post in blog_posts) + 1
        else:
            next_id = 1


        post = {
            'id': len(blog_posts) + 1,
            'author': author,
            'title': title,
            'content': content,
            'likes': 0
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

@app.route('/update/<int:post_id>', methods=['GET', 'POST'] )
def update(post_id):
    # Fetch the blog posts from the JSON file
    old_post = fetch_post(post_id)
    if old_post is None:
        # Post not found
        return "Post not found", 404

    if request.method == 'POST':
        # Update the post in the JSON file
        all_posts = load_posts()

        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        new_post = {
            'id': post_id,
            'author': author,
            'title': title,
            'content': content,
            'likes': old_post.get('likes', 0)
         }

        updated_posts = [post for post in all_posts if post['id'] != post_id]
        updated_posts.append(new_post)

        updated_posts.sort(key=lambda p: p['id'])

        save_posts(updated_posts)

        # Redirect back to index
        return redirect(url_for('index'))

    # Else, it's a GET request
    else:
    # So display the update.html page
        return render_template('update.html', post=old_post)


@app.route('/likes/<int:post_id>', methods=['POST'] )
def likes(post_id):
    posts = load_posts()
    for post in posts:
        if post['id'] == post_id:
            post['likes'] = post.get('likes',0) + 1
            save_posts(posts)
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


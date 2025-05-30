import json
import os
from typing import List, Dict

BLOG_POSTS_FILE = 'blog_posts.json'

def load_posts() -> List[Dict]:
    """Load all blog posts from the JSON file."""
    if not os.path.exists(BLOG_POSTS_FILE):
        # If the file doesn't exist, return an empty list
        return []

    try:
        with open(BLOG_POSTS_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: The posts file contains invalid JSON.")
        return []
    except Exception as e:
        print(f"Unexpected error reading posts file: {e}")
        return []


def save_posts(posts: List[Dict]):
    """Save all blog posts to the JSON file."""
    with open(BLOG_POSTS_FILE, 'w') as file:
        json.dump(posts, file, indent=4)


def add_post(author: str, title: str, content: str):
    """Create and save a new blog post."""
    posts = load_posts()

    # Generate new unique ID
    new_id = max((post['id'] for post in posts), default=0) + 1

    new_post = {
        'id': new_id,
        'author': author,
        'title': title,
        'content': content,
        'likes': 0
    }

    posts.append(new_post)
    save_posts(posts)


def delete_post(post_id: int):
    """Delete a blog post by its ID."""
    posts = load_posts()
    posts = [post for post in posts if post['id'] != post_id]
    save_posts(posts)


def fetch_post_by_id(post_id: int):
    """Return a single post by ID, or None if not found."""
    posts = load_posts()
    return next((post for post in posts if post['id'] == post_id), None)


def update_post(post_id: int, author: str, title: str, content: str):
    """Update an existing post with new data."""
    posts = load_posts()
    for post in posts:
        if post['id'] == post_id:
            post['author'] = author
            post['title'] = title
            post['content'] = content
            break
    save_posts(posts)
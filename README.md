# Masterblog 📝

A minimal Flask-powered blog app built as part of a coding bootcamp project. Masterblog lets users create, edit, delete,
and like blog posts in a clean, responsive interface.

## ✨ Features

- Create Posts – Add new blog entries with author, title, and content.

- Edit Posts – Update any existing post with just a click.

- Delete Posts – Remove posts permanently.

- Like System – Each post has a like button to track engagement.

- Responsive Design – The app is styled with CSS to ensure a clean, user-friendly interface.

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/margarita-moeslein/Masterblog.git

# Navigate into the project directory
cd Masterblog

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate

# Run the Flask application
python3 app.py 
```

## 📖 How It Works

- Home (/): Lists all posts with options to edit, delete, or like.

- New Post: Use the "Add Post" button to open a form and submit a new blog entry.

- Edit Post: Click "Update" on any post to pre-fill and modify its content.

- Delete Post: Removes the post immediately upon confirmation.

## ⚙️ Tech Stack

**Flask** – Lightweight Python web framework  
**Jinja2** – HTML templating for dynamic content  
**HTML/CSS** – Simple front-end structure and styling  
**JSON** – Local data storage for blog posts

## 📦 Requirements

- Python 3.x
- Flask 3.0.3
- Jinja2 3.1.4
from flask import Flask, render_template, request, url_for, redirect
from mysql.connector import connect
from pprint import pprint

# Connect to server
# Please change the user and password to yours
db = connect(
    host="127.0.0.1",
    port=3306,
    user="fyp",
    password="1234",
    database="blog_db"
    )

# # Get a cursor
# cursor = db.cursor()

# cursor.execute('SELECT * FROM blogs')
# items = cursor.fetchall()
# for item in items:
#     print(item)

#     id = item[0]
#     title = item[1]
#     subtitle = item[2]
#     category = item[3]
#     content = item[4]
#     tags = item[5]
#     cover_image = item[6]
#     created_at = item[7]

#     blog = {
#         'id': id,
#         'title': title,
#         'subtitle': subtitle,
#         'category': category,
#         'content': content,
#         'cover_img': cover_image,
#         'tags': tags,
#         'created_at': created_at
#     }
#     pprint(blog)

# print(items)

app = Flask(__name__)

# Get a cursor
cursor = db.cursor()

app.secret_key = 'your_secret_key_here'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blogs', methods = ['GET'])
def blogs():
    cursor.execute('SELECT * FROM blogs')
    items = cursor.fetchall()

    blogs = [{
            'id': item[0],
            'title': item[1],
            'subtitle': item[2],
            'category': item[3],
            'content': item[4],
            'tags': item[5],
            'cover_img': item[6],
            'created_at': item[7]
        } for item in items]
    num_of_blogs = len(blogs)
    
    return render_template('blogs.html', blogs = blogs, num_of_blogs = num_of_blogs)

@app.route('/blogs/<id>')
def blog(id):
    cursor.execute(f'SELECT * FROM blogs WHERE id = {id}')
    item = cursor.fetchone()
    blog = {
            'id': item[0],
            'title': item[1],
            'subtitle': item[2],
            'category': item[3],
            'content': item[4],
            'tags': item[5],
            'cover_img': item[6],
            'created_at': item[7]
        
        }
    return render_template('blog.html', blog = blog)

@app.route('/blogs/add', methods = ['GET', 'POST','DELETE'])
def add_blog():
    data = request.form
    if request.method == 'POST':
        data = request.form


        new_blog = (
            data.get('title', ''),
            data.get('subtitle', ''),
            data.get('category', ''),
            data.get('content', ''),
            data.get('tags', ''),
            data.get('cover-image', '')
        )

        sql = 'INSERT INTO blogs (title, subtitle, category, content, tags, cover_img) VALUES (%s, %s, %s, %s, %s, %s)'
        cursor.execute(sql, new_blog)
        db.commit()

        return redirect(url_for('blogs'))

    return render_template('add-blog.html')

@app.route('/blogs/delete/<id>')
def delete_blog(id):
    sql = "DELETE FROM blogs WHERE id = %s"
    cursor.execute(sql, (id,))
    db.commit()
    return redirect(url_for('blogs'))

@app.route('/blogs/edit/<id>', methods = ['GET', 'POST'])
def edit_blog(id):
    if request.method == 'POST':
        # TODO -- 
        return redirect(url_for('blogs'))
    return render_template('edit-blog.html')

@app.route('/users')
def users():
    return [
        {
            'name':'Miku',
            'age':16,
            'role':'Singer'
        },
        {
            'name':'Len',
            'age':15,
            'role':'Singer'
        },
        {
            'name':'Luka',
            'age':20,
            'role':'Singer'
        }
    ]

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
    print('The flask server is running')

"""

CRUD -
CREATE(POST)
READ(GET)
UPDATE(PUT/PATCH)
DELETE(DELETE)
"""
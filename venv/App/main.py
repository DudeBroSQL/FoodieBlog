from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

from werkzeug.utils import redirect



# dummy_data = [
#     {
#         'title':'Post1',
#         'content':'Post1 content ipsum lorem filler text',
#         'author':'Sean'
#     },
#     {
#         'title':'Post2',
#         'content':'Post2 content ipsum lorem filler text'
#     }
# ]




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text, nullable = False) 
    author = db.Column(db.String(20), nullable = False, default = 'N/A') 
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow) 

    def __repr__(self):
        return 'Blog post ' + str(self.id)





@app.route('/')
def home():
    return render_template('index.html')

@app.route('/posts', methods = ['GET'])   
def posts():
    return render_template('posts.html', posts = BlogPost.query.all())

@app.route('/addpost', methods = ['GET','POST'])   
def addpost():
    if request.method == 'POST':
        post_title = request.form['title']
        post_author = request.form['author']
        post_content = request.form['content']
        new_post = BlogPost(title=post_title, content =post_content, author = post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('addpost.html')    


if __name__ == '__main__':
    app.run(debug= True)



import markdown2    
from flask import render_template, request, jsonify, redirect
from .models import Hashtag
from app import app, db
from app.models import Post, Hashtag, post_hashtag


class Form:
    def __init__(self, text, hashtags):
        self.text = text
        self.hashtags = hashtags

def render_markdown(text):
    return markdown2.markdown(text)


@app.route('/')
def main_page():
    return render_template(
        'main_page.html'
    )

@app.route('/create')
def create_page():
    return render_template(
        'create_page.html'
    )
# @app.route('/explore')
# def explore_page():
#     return render_template(
#         'explore_page.html'
#     )

@app.route('/submit', methods=['POST'])
def submit():
    
    text = request.form.get('text')
    hashtags = request.form.get('hashtags')


    if not text or len(text) < 10 or not hashtags:
        return redirect('/')

    hashtags = hashtags.replace('#', '')  
    arr_hashtags = hashtags.split()      

    new_post = Post(text=text)
    db.session.add(new_post)
    db.session.commit() 

    for tag_name in arr_hashtags:
        tag_name = tag_name.lower() 

        hashtag = Hashtag.query.filter_by(name=tag_name).first()

        if not hashtag:
     
            hashtag = Hashtag(name=tag_name)
            db.session.add(hashtag)
            db.session.commit()  

       
        if hashtag not in new_post.hashtags:
            new_post.hashtags.append(hashtag)

    db.session.commit()

    return redirect('/')
    
    



@app.route('/preview', methods=['POST'])
def preview():
    
    data = Form(request.form['text'], request.form['hashtags'])
    html_content = render_markdown(data.text)

    return render_template(
        'preview_page.html',
        html_content=html_content

    )

@app.route('/explore', methods=['GET', 'POST'])
def search_by_hashtag():
    # hashtag_names = request.args.getlist('tag')
    st = request.form.get('hashtags')

    if not st:
        return render_template(
            'explore_page.html',
            html_content=[]
        )
    st = st.strip()
    st = st.lower()
    st = st.replace('#', '')
    hashtag_names = st.split()
    posts_set = set()

    for hashtag_name in hashtag_names:
        hashtag = Hashtag.query.filter_by(name=hashtag_name).first()
        if hashtag:
            posts = hashtag.posts
        else:
            return render_template(
                'explore_page.html',
                html_content = -1
            )
        
        for post in posts:
           
            posts_set.add(post.id)

    freq = dict()
    
    for post_id in posts_set:
        post = Post.query.get(post_id)
   
        hashtags = set(el.name for el in post.hashtags)
        cur_freq = len(set(hashtag_names) & hashtags)
        
        if cur_freq in freq:
            freq[cur_freq].append(post.text)
        else:
            freq[cur_freq] = [post.text]

        freqs = sorted(freq.keys(), reverse=True)
    
    result = []

    for cur_freq in freqs:
        for post in freq[cur_freq]:
            result.append(post)
    html_result = [render_markdown(el) for el in result]
    
    if not html_result:
        return render_template(
            'explore_page.html',
            html_content = -1
        )

    return render_template(
        'explore_page.html',
        html_content=html_result
    )

            
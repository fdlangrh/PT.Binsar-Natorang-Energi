from flask import Flask, redirect, url_for, render_template, request, jsonify, session
from pymongo import MongoClient
import requests
from datetime import datetime
from bson import ObjectId
import os 
from os.path import join, dirname

app = Flask(__name__)
app.secret_key = "your_secret_key"
uri = "mongodb+srv://fadil123:fadil123@atlascluster.jbkflub.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db=client.pkl2


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    data = db.binsar.find({})
    file = request.args.get('file')
    return render_template('aboutus.html', data=data, file = file)

@app.route('/social')
def social():
    return render_template('Social Contribution.html')
    
@app.route('/our')
def our():
    return render_template('OurPartners.html')

@app.route('/24hours')
def hours():
    return render_template('24hours.html')

@app.route('/scada')
def scada():
    return render_template('scada.html')

@app.route('/advanced')
def advanced():
    return render_template('advanced.html')

@app.route('/environment')
def environment():
    return render_template('environment.html')

@app.route('/fasttrans')
def fasttrans():
    return render_template('fasttrans.html')

@app.route('/constructive')
def cons():
    return render_template('constructive.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Dummy user validation
        if username == 'admin' and password == 'admin':
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))



@app.route('/data')
def data():
    data = db.binsar.find({})
    return render_template('data.html', data=data)

@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/baru', methods=['POST'])
def baru():
    id = request.form.get("id_give")
    file = request.files['file_give']
    extension = file.filename.split('.')[-1]
    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
    filename = f'file-{mytime}.{extension}'
    save_to = f'../PT.Binsar-Natorang-Energi/static/add/{filename}'
    file.save(save_to)          
    title_receive = request.form.get('title_give')
    content_receive = request.form.get('content_give')
    doc = {
        'file': filename,
        'id': id,
        'title': title_receive,
        'content': content_receive
    }
    db.binsar.update_one(
    {'_id':ObjectId(id)},{'$set':doc})
    return jsonify({
        'msg':'Your Data Has Been Updated'
    })

@app.route('/upload_show', methods=['GET'])
def show_data():
    articles = list(db.binsar.find({},{'_id':False}))
    return jsonify({'articles': articles})

@app.route('/upload', methods=['POST'])
def save_data():
    file = request.files['file_give']
    extension = file.filename.split('.')[-1]
    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
    filename = f'file-{mytime}.{extension}'
    save_to = f'../PT.Binsar-Natorang-Energi/static/add/{filename}'
    file.save(save_to)

    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
    title_receive = request.form.get('title_give')
    content_receive = request.form.get('content_give')
    doc = {
        'file': filename,
        'title': title_receive,
        'content': content_receive
    }
    db.binsar.insert_one(doc)
    return jsonify({
        'msg':'Your Data Has Been added'
    })
    

@app.route('/edit', methods=['GET'])
def edit_show():
    id = request.args.get('_id')
    data=list(db.binsar.find({'_id' : ObjectId(id)}))
    print(data)
    return render_template('edit.html', data = data)


@app.route('/edit/update/<int:num>', methods=['GET'])
def update(num):
    post = db.binsar.find_one({'_id': num}, {'_id': False})

    if save_data:
            return jsonify({'result': 'success', 'post': post})
    else:
            return jsonify({'result': 'error', 'msg': 'Posting tidak ditemukan'}), 404
       

@app.route('/delete', methods=['GET'])
def delete():
    id = request.args.get('_id')
    db.binsar.delete_one({'_id':ObjectId(id)})
    data = list(db.binsar.find({}))
    return redirect(url_for('data'))




if __name__=='__main__':
    app.run('0.0.0.0',port=5000, debug=True)
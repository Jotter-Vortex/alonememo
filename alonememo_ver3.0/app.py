from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient                 # pymongo를 import하기

app = Flask(__name__)

client = MongoClient('mongodb://changjin:0001@13.209.47.213', 27017)        # mongoDB는 27017 포트로 돌아감
db = client.dbjungle                            # 'notepad'라는 이름의 db를 생성함

## HTML을 주는 부분
@app.route('/')                                 # home 주소
def home():
   return render_template('index.html')

## API 역할을 하는 부분 (서버)
@app.route('/memo', methods=['POST'])
def post_notepad():
    # 1. 클라이언트로부터 데이터를 받기
    title_receive = request.form['title_give'] # 클라이언트로부터 title을 받을 부분
    content_receive = request.form['content_give'] # 클라이언트로부터 content를 받을 부분
    # 2. mongoDB에 데이터 넣기
    db.notepad.insert_one({'title' : title_receive, 'content' : content_receive})
    return jsonify({'result': 'success'})
    #, 'msg':'POST 연결되었습니다!'})

@app.route('/rewrite', methods=['POST'])
def post_rewrite():
    # 1. 클라이언트로부터 데이터를 받기
    title_new = request.form['title_give_new'] # 클라이언트로부터 title을 받을 부분
    content_new = request.form['content_give_new'] # 클라이언트로부터 content를 받을 부분
    title_old = request.form['title_give_old']
    content_old = request.form['content_give_old']
    # 2. mongoDB에 데이터 넣기
    db.notepad.update_one({'title':title_old}, {'$set' : {'title' : title_new, 'content' : content_new}})
    return jsonify({'result': 'success'})
    #, 'msg':'POST 연결되었습니다!'})

@app.route('/delmemo', methods=['POST'])
def post_del():
    # 1. 클라이언트로부터 데이터를 받기
    title_old = request.form['title_give_old']
    # 2. mongoDB에 데이터 넣기
    db.notepad.delete_one({'title':title_old})
    return jsonify({'result': 'success'})
    #, 'msg':'POST 연결되었습니다!'})

@app.route('/memo', methods=['GET'])
def read_notepad():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기(Read)
    result = list(db.notepad.find({},{'_id':0}))
    # 2. notepads라는 키 값으로 notepad 정보 보내주기
    return jsonify({'result': 'success', 'notepads': result})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
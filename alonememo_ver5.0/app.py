from bson import ObjectId
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
def show_notepad():
    # 1. 클라이언트로부터 데이터를 받기
    title_receive = request.form['title_give'] # 클라이언트로부터 title을 받을 부분
    content_receive = request.form['content_give'] # 클라이언트로부터 content를 받을 부분
    # 2. mongoDB에 데이터 넣기
    db.notepad.insert_one({'title' : title_receive, 'content' : content_receive})
    return jsonify({'result': 'success'})
    #, 'msg':'POST 연결되었습니다!'})

@app.route('/memo', methods=['GET'])
def init_notepad():      # 처음 새로고침시에 DB에 있는 값을 모두 가져와서 cards를 만드는 함
    # DB에서 모든 데이터 조회해오기(Read)
    result = list(db.notepad.find({}))
    for i in range(len(result)):
        result[i]['_id'] = str(result[i]['_id'])       # DB에서 받아온 _id 값은 type이 ObjectId이기 때문에 형변환
                                                        # 을 해줘야 json형식으로 클라이언트에게 보낼 수 있다.
    print(result)
    # notepads라는 키 값으로 result 정보 보내주기
    return jsonify({'result': 'success', 'notepads': result})

@app.route('/delmemo', methods=['POST'])
def post_del():
    # 1. 클라이언트로부터 데이터를 받기
    id = request.form['index_give']
    # 2. DB에 잇는 데이터 삭제하기
    print("지울 인덱스" + id)
    db.notepad.delete_one({'_id': ObjectId(id)})   # from bson import ObjectId
    return jsonify({'result': 'success'})
    #, 'msg':'POST 연결되었습니다!'})

#####@###########@###########@###########@###########@###########@###########@#######

## API 역할을 하는 부분 (서버)
@app.route('/giveindex', methods=['POST'])
def fetch_notepad():
    # 1. 클라이언트로부터 데이터를 받기
    index_receive = request.form['index_receive'] # 클라이언트로부터 index 받을 부분
    # 2. DB에서 데이터를 조회하기요
    # _id 값을 검색하고 싶을때는 string으로는 검색할 수 없음. 따라서 ObjectId라는 함수를 이용해야함
    tclist = list(db.notepad.find({'_id': ObjectId(index_receive)}))
    tclist[0]['_id'] = str(tclist[0]['_id'])        # _id는 type이 string이 아니라 ObjectId. 형변환 필요함
    print(tclist[0])
    return jsonify({'result': 'success', 'notepads' : tclist})
    #, 'msg':'POST 연결되었습니다!'})

## API 역할을 하는 부분 (서버)
@app.route('/rewrite', methods=['POST'])
def post_notepad():
    # 1. 클라이언트로부터 데이터를 받기
    index = request.form['idindex']  # 클라이언트로부터 index를 받을 부분
    new_title = request.form['title_new'] # 클라이언트로부터 title을 받을 부분
    new_content = request.form['content_new']  # 클라이언트로부터 content 을 받을 부분
    # 2. DB에 데이터를 찾기
    db.notepad.update_one({'_id': ObjectId(index)}, {'$set': {'title': new_title}})
    db.notepad.update_one({'_id': ObjectId(index)}, {'$set': {'content': new_content}})
    return jsonify({'result': 'success'})
    #, 'msg':'POST 연결되었습니다!'})



if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
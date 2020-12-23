### alonememo
[changmemo]<http://changjin.me/memomain>

###### * 기술 스택
    −  Server-side
    −  1. python3
    −  2. MongoDB
    -  3. Jinja2
    -  4. AWS
    -  5. EC2 t2 micro
    
###### * for server
    −  ssh -i key ubuntu@IPNUM
    −  ps -ef | grep app.py
    −  kill -9
    -  sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 5000
    -  pip install requests beautifulsoup4 pymongo
    -  5. EC2 t2 micro   
###### * for MongoDB
    −   wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
    -   echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
    -   sudo apt-get update
    -   sudo apt-get install -y mongodb-org
    -   sudo service mongod start
    -   >mongo
    -   use admin;
    -   db.createUser({user: "test", pwd: "test", roles:["root"]});
    -   sudo service mongod restart
    -   sudo vi /etc/mongod.conf
    -   * bindIp : 0.0.0.0
    -   * security : authorization: enabled #주석제거
    
###### * for pip
    −  sudo apt-get update
    −  sudo apt-get install -y python3-pip
    −  pip3 --version
    -  sudo update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1
    -  >pip install flask
   

###### //
###### <version_info>
###### ver1.0 : 메모 추가만 가능한 메모장
###### ver2.0 : 메모 삭제,추가 기능추가
###### ver3.0 : placeholder 부분 string으로 나오도록 개선, 메모 수정시 발생하는 error 개선
###### ver4.0 : 메모 수정시 발생하는 에러 개선
###### ver5.0 : 메모 제목과 메모 내용 둘다 줄바꿈이 가능하도록 개선
###### ver5.01 : 수정 버튼을 눌렀을때 html이 나오는 error 개선
###### ver 6.0 - 메모 저장 시간을 표시함. 년/월/일/시간 순서
###### ver 6.1 - 이미지 추가와 서버 error 개선. 메모 자동줄바꿈 추가(2020/11/20)
###### ver 6.101 - 최초 정렬 최신순으로 함. 메모장 이미지 변경함(2020/11/20)
###### ver 6.2 - 메인 페이지 추가(2020/12/1)

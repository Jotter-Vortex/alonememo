### changmemo(http://changjin.me/memomain)

###### //
###### <version_info>
###### ver 7.0 -  js 추가. 모바일 추가수정.static 내부파일 삭제.(2020/12/29)

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
   



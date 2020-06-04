from flask import Flask, make_response, request
from flask_cors import CORS
from exts import db
from models import Student
import config

import json

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
# 处理跨域
CORS(app, resources=r'/*')

db.create_all(app=app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/post', methods=['POST'])
def post():
    # 获取 参数
    name = request.json.get('name')
    email = request.json.get('email')
    # 返回结果集
    json_list = []
    student_data = {}
    # 查询 符合条件的数据
    if name and email:
        student_data = Student.query.filter(Student.name == name, Student.email == email)
    if not name and not email:
        student_data = Student.query.all()
    if name and not email:
        student_data = Student.query.filter(Student.name == name)
    if not name and email:
        student_data = Student.query.filter(Student.email == email)
    # 转换 json
    for i in student_data:
        json_data = {}
        json_data['id'] = i.id
        json_data['name'] = i.name
        json_data['email'] = i.email
        json_data['sex'] = i.sex
        json_data['age'] = i.age
        json_list.append(json_data)
    return json.dumps(json_list), 200


@app.route('/get', methods=['GET'])
def get():
    data = {'name': 'mel', 'status': 200}
    return json.dumps(data, ensure_ascii=False), 200


@app.route('/save', methods=['POST'])
def save():
    # 获取 参数， 转换成json格式
    data = json.loads(request.get_data())
    stu = Student.query.get(data['id'])
    # 更新数据
    stu.name = data['name']
    stu.email = data['email']
    # 提交
    db.session.commit()
    return 'success', 200


if __name__ == '__main__':
    app.run()

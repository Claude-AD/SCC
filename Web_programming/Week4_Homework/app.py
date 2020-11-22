from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


# HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    # Client로부터 주문자 이름, 수량, 주소, 전화번호 받아옴
    name_receive = request.form['name_give']
    quantity_receive = request.form['quantity_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    # DB에 이름, 수량, 주소, 전화번호 저장
    doc = {
        'name': name_receive,
        'quantity': quantity_receive,
        'address': address_receive,
        'phone': phone_receive
    }
    db.orders.insert_one(doc)

    # 성공적으로 저장하면 주문 완료! 라는 메시지 리턴
    return jsonify({'result': 'success', 'msg': '주문 완료!'})

# 주문 목록보기 API
@app.route('/order', methods=['GET'])
def view_orders():
    # 주문 DB에 있는 모든 주문 정보를 긁어와서 Client에게 전달
    orders = list(db.orders.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'orders': orders})

# 서버 실행
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
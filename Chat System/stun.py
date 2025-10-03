from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
server = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/peers', methods=['GET'])
def peers():
    result = server.hgetall("users")
    result = {k.decode('utf-8'): v.decode('utf-8') for k, v in result.items()}
    return jsonify(result), 200

@app.route('/register', methods=['POST'])
def register():
    username = request.args.get('username')
    IP = request.args.get('IP')
    PORT = request.args.get('PORT')
    if not username or not PORT or not IP:
        return jsonify({'message': 'لطفا مقادیر را کامل پر کنید'}), 400

    server.hset("users", username, f"{IP}:{PORT}")
    return jsonify({'message': 'اطلاعات موفقیت ثبت شد'})

@app.route('/peerinfo', methods=['GET'])
def peerinfo():
    username = request.args.get('username')
    if not username:
        return jsonify({'message': 'لطفا مقادیر را کامل پر کنید'}), 400
    result = server.hget("users", username)
    if result is None:
        return jsonify({'message': 'کاربر مورد نظر یافت نشد'}), 404

    return jsonify({'message': result.decode('utf-8')}), 200

if name == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
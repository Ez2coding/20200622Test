from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return '안녕하세요 파이썬!!!!!!!!!!!'

@app.route('/method', methods=['GET', 'POST']) 
# @app.route('/method')
def method(): 
    if request.method == 'GET': 
        return "GET으로 전달" 
    else: 
        return "POST로 전달"

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/hello')
def html():
    return render_template("test.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
from flask import Flask
from flask import redirect,render_template,url_for
from flask_script import Manager,Server

app = Flask(__name__,static_url_path='')
app.jinja_env.auto_reload = True
app.debug = True
manager = Manager(app)
manager.add_command("runserver", Server(use_debugger=True))


@app.route('/')
def main():

    return render_template('index.html')

@app.route('/<string:name>.md/')
def doc(name):

    return render_template('post.html',name=name)

@app.route('/demo/')
def demo():

    return render_template('post.html',name="demo")

@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    return '''找不到你需要的文档'''


if __name__ == '__main__':
    manager.run()
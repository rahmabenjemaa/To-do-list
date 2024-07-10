
from flask import Flask ,render_template, redirect, url_for, session, request
from models import  Todo


def register_routes(app , db  ):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':
            todos = Todo.query.all()
            return render_template('index.html' , todos=todos)
        elif request.method == 'POST':
            task = request.form['task']
            todo = Todo(task=task)
            db.session.add(todo)
            db.session.commit()
            return redirect(url_for('index'))

    @app.route('/add', methods=['GET', 'POST'])
    def add():
        if request.method == 'POST':
            task = request.form['task']
            todo = Todo(task=task)
            todos = Todo.query.all()
            db.session.add(todo)
            db.session.commit()
            return redirect(url_for('index'))

    @app.route('/delete/<int:tid>', methods=['DELETE', 'GET'])
    def delete(tid):
        todo = Todo.query.filter_by(tid=tid).delete()
        db.session.commit()
        return redirect(url_for('index'))












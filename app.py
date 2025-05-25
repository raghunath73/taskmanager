from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = TodoItem(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "Error adding task"
    else:
        tasks = TodoItem.query.order_by(TodoItem.date_created).all()
        return render_template('index.html', tasks=tasks)

@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    task = TodoItem.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "Error updating task"
    else:
        return render_template('update.html', task=task)

@app.route("/delete/<int:id>")
def delete(id):
    task_to_delete = TodoItem.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "Error deleting task"

@app.route("/toggle-completed/<int:id>", methods=['POST'])
def toggle_completed(id):
    task = TodoItem.query.get_or_404(id)
    task.completed = not task.completed
    try:
        db.session.commit()
        return redirect('/')
    except:
        return "Error toggling task completion"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for
from models import Todo

app = Flask(__name__)
# Vercel uchun kerak bo'lishi mumkin
app.debug = True 

@app.route("/")
def homepage():
    # HTML dagi 'tasks' o'zgaruvchisiga moslab yuboramiz
    items = Todo.select().order_by(Todo.id.desc())
    return render_template("index.html", tasks=items)

@app.route("/add", methods=["POST"])
def add_todo():
    # HTML formadagi name="title" bo'lishi shart
    title = request.form.get("title")
    if title:
        Todo.create(title=title)
    return redirect(url_for("homepage"))

@app.route("/toggle/<int:todo_id>")
def toggle_todo(todo_id):
    todo = Todo.get_or_none(Todo.id == todo_id)
    if todo:
        todo.completed = not todo.completed
        todo.save()
    return redirect(url_for("homepage"))

@app.route("/delete/<int:todo_id>")
def delete_todo(todo_id):
    todo = Todo.get_or_none(Todo.id == todo_id)
    if todo:
        todo.delete_instance()
    return redirect(url_for("homepage"))

# Bu qator Vercel-da bo'lishi shart emas, lekin localda ishlatish uchun qolsin
if __name__ == "__main__":
    app.run()
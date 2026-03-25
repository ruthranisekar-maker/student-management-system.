from flask import Flask, render_template, request, url_for, redirect
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Database 
mysql = mysql.connector.connect(
    host='localhost',
    user='root',
    password='ruth123.',
    database='student_db'
)

# Insert
cursor = mysql.cursor()
cursor.execute("SELECT COUNT(*) FROM students")
count = cursor.fetchone()[0]

if count == 0:
    cursor.execute(
        "INSERT INTO students(name,email,course,created_at) VALUES(%s,%s,%s,NOW())",
        ('John Doe', 'john@example.com', 'Computer Science')
    )
    cursor.execute(
        "INSERT INTO students(name,email,course,created_at) VALUES(%s,%s,%s,NOW())",
        ('Jane Smith', 'jane@example.com', 'Mathematics')
    )
    mysql.commit()


# Home Page
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/view')
def view():
    cur = mysql.cursor()
    cur.execute("SELECT * FROM students")
    datas = cur.fetchall()
    cur.close()
    return render_template('view.html', datas=datas)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']

        
        created_at = datetime.now()

        cur = mysql.cursor()
        cur.execute(
            "INSERT INTO students(name, email, course, created_at) VALUES(%s, %s, %s, %s)",
            (name, email, course, created_at)
        )
        mysql.commit()
        cur.close()

        return redirect(url_for('view'))

    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    cur=mysql.cursor()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']

        cur.execute("""
            UPDATE students
            SET name=%s, email=%s, course=%s
            WHERE id=%s
        """, (name, email, course, id))

        mysql.commit()
        cur.close()

        return redirect(url_for('view'))  

    cur.execute("SELECT * FROM students WHERE id=%s", (id,))
    student = cur.fetchone()
    cur.close()

    return render_template('edit.html', student=student)


@app.route('/delete/<int:id>')
def delete(id):
    cur = mysql.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id,))
    mysql.commit()
    cur.close()

    return redirect(url_for('view'))



if __name__ == "__main__":
    app.run(debug=True, port=5001)
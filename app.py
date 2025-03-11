from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def init_db():
    conn = sqlite3.connect('bloodbank.db')
    cursor = conn.cursor()

    
    cursor.execute('DROP TABLE IF EXISTS donors')
    cursor.execute('DROP TABLE IF EXISTS recipients')

    
    cursor.execute('''
        CREATE TABLE donors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            blood_group TEXT,
            contact TEXT,
            age INTEGER,
            city TEXT,
            disease TEXT,
            eligible TEXT
        )
    ''')

    
    cursor.execute('''
        CREATE TABLE recipients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            blood_group TEXT,
            contact TEXT,
            city TEXT
        )
    ''')

    conn.commit()
    conn.close()


init_db()

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == 'sathya' and password == 'sathya@123':
        session['user'] = 'Sathya'
        flash("Login successful!", "success")
        return redirect(url_for('index'))
    else:
        flash("Invalid credentials!", "danger")
        return redirect(url_for('home'))

@app.route('/index')
def index():
    if 'user' not in session:
        return redirect(url_for('home'))
    return render_template('index.html', user=session['user'])

@app.route('/donor_register', methods=['GET', 'POST'])
def donor_register():
    if 'user' not in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        name = request.form['name']
        blood_group = request.form['blood_group']
        contact = request.form['contact']
        age = request.form['age']
        city = request.form['city']
        disease = request.form['disease']

        
        eligibility_questions = [
            request.form.get(f'eligible{i}') for i in range(1, 11)
        ]

        if all(answer == 'Yes' for answer in eligibility_questions):
            eligible = 'Yes'
        else:
            eligible = 'No'

        conn = sqlite3.connect('bloodbank.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO donors (name, blood_group, contact, age, city, disease, eligible) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (name, blood_group, contact, age, city, disease, eligible))
        conn.commit()
        conn.close()

        if eligible == 'Yes':
            return redirect(url_for('certificate'))
        else:
            flash("You are not eligible to donate blood.", "warning")
            return redirect(url_for('index'))

    return render_template('donor_registration.html')

@app.route('/certificate')
def certificate():
    if 'user' not in session:
        return redirect(url_for('home'))
    return render_template('certificate.html')

@app.route('/recipient_register', methods=['GET', 'POST'])
def recipient_register():
    if 'user' not in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        name = request.form['name']
        blood_group = request.form['blood_group']
        contact = request.form['contact']
        city = request.form['city']

        conn = sqlite3.connect('bloodbank.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO recipients (name, blood_group, contact, city) VALUES (?, ?, ?, ?)",
                       (name, blood_group, contact, city))
        conn.commit()

        cursor.execute("SELECT name, contact FROM donors WHERE blood_group=? AND eligible='Yes'", (blood_group,))
        matching_donors = cursor.fetchall()
        conn.close()

        if matching_donors:
            return render_template('matching_donors.html', donors=matching_donors, blood_group=blood_group)
        else:
            flash("No eligible donors found for this blood group.", "info")
            return redirect(url_for('index'))

    return render_template('recipient_registration.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logged out successfully!", "info")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

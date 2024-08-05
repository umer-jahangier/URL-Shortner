from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import string
import random

app = Flask(__name__)

#Initializing Database
def init_db():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            original_url TEXT NOT NULL UNIQUE,
            short_url TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

#Function to generate a random short URL
def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url

#Function to store URL data in DB
def insert_url(name, original_url, short_url):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    try:
        c.execute('INSERT INTO urls (name, original_url, short_url) VALUES (?, ?, ?)', (name, original_url, short_url))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return False
    conn.close()
    return True

#Function to Map Back to Original URL
def get_url_data(short_url):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('SELECT name, original_url FROM urls WHERE short_url = ?', (short_url,))
    url_data = c.fetchone()
    conn.close()
    if url_data:
        return url_data
    else:
        return None

#Function to get the short URL and name from the original URL to check if it's already generated or not
def get_short_url_and_name(original_url):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('SELECT short_url, name FROM urls WHERE original_url = ?', (original_url,))
    url_data = c.fetchone()
    conn.close()
    if url_data:
        return url_data
    else:
        return None



#ROUTES
@app.route('/', methods=['GET', 'POST'])
def index():
    error_message = None
    if request.method == 'POST':
        name = request.form['name']
        original_url = request.form['original_url']
        
        # Check if the URL has already been shortened
        url_data = get_short_url_and_name(original_url)
        if url_data:
            short_url, existing_name = url_data
            error_message = f'URL has already been shortened with the name "{existing_name}".'
            return render_template('index.html', error_message=error_message)
        
        # If not then generate a shortened URL
        short_url = generate_short_url()
        if insert_url(name, original_url, short_url):
            return render_template('shortened.html', short_url=short_url)
    
    return render_template('index.html', error_message=error_message)



@app.route('/<short_url>')
def redirect_to_url(short_url):
    url_data = get_url_data(short_url)
    if url_data:
        name, original_url = url_data
        return redirect(original_url)
    else:
        return 'URL not found', 404

@app.route('/all_urls')
def list_urls():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('SELECT short_url, name, original_url FROM urls')
    urls = c.fetchall()
    conn.close()
    return render_template('list_urls.html', urls=urls)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

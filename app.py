from flask import Flask, render_template, request, redirect, url_for

import sqlite3

app = Flask(__name__)

# Home route


@app.route('/')
def home():
    return render_template('home.html')

# Login route


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Default to 'scout' if not provided
        user_type = request.form.get('user_type', 'scout')

        conn = sqlite3.connect('site.db')
        cursor = conn.cursor()
        print("Connected to SQLite")
        # Retrieve the user data from the database based on the username
        cursor.execute(
            'SELECT * FROM user WHERE username = ? AND password = ?', (username, password,))
        user_data = cursor.fetchone()

        conn.close()

        if user_data:
            # Assuming is_scoutmaster is in the fourth column
            is_scoutmaster = user_data[3]

            if is_scoutmaster and user_type == 'scoutmaster':
                return render_template('scoutmaster_home.html', username=username)
            elif not is_scoutmaster and user_type == 'scout':
                return render_template('scout_home.html', username=username)
            else:
                return render_template('login_failure.html', message="User type mismatch.")
        else:
            return render_template('login_failure.html', message="Invalid username or password.")

    return render_template('login.html')


@app.route('/postcreate', methods=['GET', 'POST'])
def postcreate():
    if request.method == 'POST':

        ramu_requirement1 = request.form['ramu_requirement1']
        ramu_user = request.form['username']
        id_nomor = request.form['id_nomor']

        ramu_requirement2 = request.form['ramu_requirement2']
        ramu_user2 = request.form['username']
        id_nomor2 = request.form['id_nomor2']

        ramu_requirement3 = request.form['ramu_requirement3']
        ramu_user3 = request.form['username']
        id_nomor3 = request.form['id_nomor3']

        conn = sqlite3.connect('site.db')
        cursor = conn.cursor()

        cursor.execute(
            'SELECT * FROM user_progress2 WHERE user_id = ? ', (ramu_user))
        records = cursor.fetchall()


        cursor.execute('''INSERT INTO user_progress2 VALUES (?, ?, ?, ?, ?)''',  (ramu_user, id_nomor, ramu_requirement1, '2', '2'))
        cursor.execute('''INSERT INTO user_progress2 VALUES (?, ?, ?, ?, ?)''',  (ramu_user2, id_nomor2, ramu_requirement2, '2', '2'))
        cursor.execute('''INSERT INTO user_progress2 VALUES (?, ?, ?, ?, ?)''',  (ramu_user3, id_nomor3, ramu_requirement3, '2', '2'))


        conn.commit()
        cursor.close()

    return render_template('scout_home.html' )




# Member homepage route
@app.route('/scout_home')
def scout_home():
    # Render member's homepage with progress and badge details
    return render_template('scout_home.html')

# Scoutmaster homepage route


@app.route('/scoutmaster_home')
def scoutmaster_home():
    conn = sqlite3.connect('site.db')
    cursor = conn.cursor()

    # Fetch scout members from the database
    # Assuming is_scoutmaster is a column
    cursor.execute('SELECT * FROM user WHERE is_scoutmaster = 0')
    scout_members = cursor.fetchall()

    return render_template('scoutmaster_home.html', username=get_current_scoutmaster_username(), scout_members=scout_members)

# Delete scout member route
# Delete scout member route


@app.route('/delete-scout-member', methods=['POST'])
def delete_scout_member():
    if request.method == 'POST':
        username_to_delete = request.form.get('username')

        # Delete the scout member from the database
        conn = sqlite3.connect('site.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM user WHERE username = ?',
                       (username_to_delete,))
        conn.commit()
        conn.close()

        return "Scout member deleted successfully"

# Logout route


@app.route('/logout')
def logout():
    # You might want to clear session or perform other logout-related tasks here
    # For now, let's redirect to the login page


    return redirect(url_for('login'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/save-progress', methods=['POST'])
def save_progress():
    user_id = request.form.get('user_id')
    level = request.form.get('level')
    progress = request.form.get('progress')

    # Print the received data for debugging
    print(
        f"Received progress save request - User ID: {user_id}, Level: {level}, Progress: {progress}")

    # You should save this data to your database here

    return jsonify({'message': 'Progress saved successfully'})


def get_current_scoutmaster_username():
    return session.get('scoutmaster_username', None)


if __name__ == '__main__':
    app.run(debug=True)

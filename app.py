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
        user_type = request.form.get('user_type', 'scout')  # Default to 'scout' if not provided

        conn = sqlite3.connect('site.db')
        cursor = conn.cursor()

        # Retrieve the user data from the database based on the username
        cursor.execute('SELECT * FROM user WHERE username = ? AND password = ?', (username, password,))
        user_data = cursor.fetchone()

        conn.close()

        if user_data:
            is_scoutmaster = user_data[3]  # Assuming is_scoutmaster is in the fourth column

            if is_scoutmaster and user_type == 'scoutmaster':
                return render_template('scoutmaster_home.html', username=username)
            elif not is_scoutmaster and user_type == 'scout':
                return render_template('scout_home.html', username=username)
            else:
                return render_template('login_failure.html', message="User type mismatch.")
        else:
            return render_template('login_failure.html', message="Invalid username or password.")

    return render_template('login.html')


# Member homepage route
@app.route('/scout_home')
def scout_home():
    # Render member's homepage with progress and badge details
    return render_template('scout_home.html')

# Scoutmaster homepage route
@app.route('/scoutmaster_home')
def scoutmaster_home():
    try:
        conn = sqlite3.connect('site.db')
        cursor = conn.cursor()

        # Fetch all scout members from the database
        cursor.execute('SELECT * FROM user WHERE is_scoutmaster = 0')  # Assuming 0 represents scout members
        scout_members = cursor.fetchall()

        # Close the connection
        conn.close()

        return render_template('scoutmaster_home.html', username=get_current_scoutmaster_username(), scout_members=scout_members)

    except Exception as e:
        print(f"Error fetching scout members: {str(e)}")
        return render_template('error.html', message="Error fetching scout members.")

# Delete scout member route
@app.route('/delete-scout-member', methods=['POST'])
def delete_scout_member():
    if request.method == 'POST':
        username_to_delete = request.form.get('username')

        try:
            # Delete the scout member from the database
            conn = sqlite3.connect('site.db')
            cursor = conn.cursor()
            cursor.execute('DELETE FROM user WHERE username = ?', (username_to_delete,))
            conn.commit()
            conn.close()

            return "Scout member deleted successfully"

        except Exception as e:
            print(f"Error deleting scout member: {str(e)}")
            return "Error deleting scout member"


# Logout route
@app.route('/logout')
def logout():
    # You might want to clear session or perform other logout-related tasks here
    # For now, let's redirect to the login page
    return redirect(url_for('login'))


@app.route('/save-progress', methods=['POST'])
def save_progress():
    user_id = request.form.get('user_id')
    level = request.form.get('level')
    progress = request.form.get('progress')

    # Print the received data for debugging
    print(f"Received progress save request - User ID: {user_id}, Level: {level}, Progress: {progress}")

    # You should save this data to your database here

    return jsonify({'message': 'Progress saved successfully'})

def get_current_scoutmaster_username():
    return session.get('scoutmaster_username', None)

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask,flash, render_template, request, session, url_for, redirect
import os
app = Flask(__name__)

app.secret_key = os.urandom(32)

user = 'JAMIIII'
pswd = 'swordfish'

@app.route('/')
def home():
    # prints <Flask 'app'> 
    print(app)
    #Checks if the user is logged in
    if 'JAMIIII' in session:
        return render_template('welcome.html', username = 'JAMIIII')
    return render_template('auth.html')

@app.route('/logout')
def logout():
    #if the user clicks the button and gets to the route the user is removed from the session
    session.pop('JAMIIII')
    return redirect(url_for('home'))

@app.route('/auth', methods=['GET','POST'])
def authenticate():
    print(request.cookies)
    
    #Gets the input via POST
    usr = request.form['username']
    passwd = request.form['password']

    #If the user somehow gets to this route this code will show them the welcome page
    if 'JAMIIII' in session:
        return render_template('welcome.html', username = 'JAMIIII')
    
    #redirects user based on unsuccessful login
    if usr != user:
        flash("SHAME ON YOU, WRONG USERNAME")#The flash messages are displayed at the top of the login page.
        return redirect(url_for('home'))
    elif passwd != pswd:
        flash("SHAME ON YOU, WRONG PASSWORD")
        return redirect(url_for('home'))

    #redirects user to home page if successful
    session[usr] = pswd
    return redirect(url_for('home'))

app.debug = True
app.run()

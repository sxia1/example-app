#BooStRadley - Ricky Lin, Matthew Ming, Mohammed Uddin, Sophia Xia

import json
import os
import urllib
import datetime

from flask import Flask, render_template, session, redirect, request, url_for, flash

from util import auth, adders, getters

app = Flask(__name__)

app.secret_key = os.urandom(32)
#obtains keys to use from key database
with open("data/keys.json") as f:
    data = json.loads(f.read())
    key=data['map_key']
    secondkey=data['weather_key']

#key = "kRAtgnsgZTOsTguZs5C7s5rw3wnAM1Mi"
amount = 10 #number of places to return
currLat = ''
currLong = ''
times = ''
firstTrack = True

#determines if user is logged in or not
def loggedIn():

    if 'user' in session:
        return True
    return False

def refresh():

    #get ISS latitude
    ISS = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(ISS)
    obj = json.loads(response.read())

    lat=obj['iss_position']['latitude']
    #lat= str(40.712775)

    #get ISS longtitude
    ISS = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(ISS)
    obj = json.loads(response.read())

    long=obj['iss_position']['longitude']
    #long =str(-74.005973)#placeholder

    global currLat
    global currLong
    global times

    #print( currLat)
    currLat = lat
    #print(currLat)
    
    #print(currLong)
    currLong = long
    #print(currLong)
    
    times = datetime.datetime.now()



#the "homepage" of our website(redirects to the ISS tracking page if already logged in)    
@app.route("/")
def index():

    if 'user' in session:
        return redirect('/track')

    return render_template("index.html", SESSION = loggedIn())

#logs out user
@app.route("/logout")
def logout():

    global firstTrack

    firstTrack = True

    if 'user' in session:
        session.pop('user')
    return redirect('/')

#signs user into website and redirects them to the ISS tracking page
@app.route("/signup")
def signup():

    if 'user' in session:
        return redirect('/track')

    return render_template("signup.html", SESSION = loggedIn())
#sends user to login screen if they are not logged in or sends user to ISS tracking page if account is created 
@app.route("/auth", methods = ['POST','GET'])
def authen():

    global currLat
    global currLong

    message = ''

    if request.method == 'GET' or not ('user' in request.form.keys()):
        return redirect('/')

    if "conf" in request.form.keys():
        message = auth.register(request.form['user'], request.form['pwd'], request.form['conf'])
        
    else: message = auth.login(request.form['user'], request.form['pwd'])

    if message in ["Account creation successful", "Login Successful"]:
        refresh()
        session['user'] = request.form['user']
        return redirect('/track')

    else:
        flash(message)
        print(message)
        return redirect(request.referrer or '/')

#ISS tracking page
@app.route("/track")
def track():

    global firstTrack

    if (not loggedIn()) and firstTrack:
        refresh()
        firstTrack = False

    global currLong
    global currLat

    base = "https://www.mapquestapi.com/staticmap/v5/map?key=" + key + "&center=" + currLat + "," + currLong +"&locations="+ currLat + "," + currLong +"&zoom=6&size=760,310@2x"

    return render_template("track.html", lat = currLat, lon = currLong, image = base, SESSION = loggedIn())

#ISS Tracking Page
@app.route("/info")
def info():

    global currLat
    global currLong
    global firstTrack

	#User must first check tracking before looking at info
    if firstTrack and not loggedIn():
        return redirect('/track')
	#grabs data from location
    data = "https://www.mapquestapi.com/search/v4/place?sort=distance&feedback=false&key=" + key + "&circle=" + currLong + "%2C" + currLat + "%2C1000"
    response = urllib.request.urlopen(data)
    info = json.loads(response.read())
    description = info["results"]
    #secondkey="647d4c51b198137da2da622c301ce39d"
    weather = "https://api.darksky.net/forecast/"+secondkey+"/"+currLat+","+currLong
    response = urllib.request.urlopen(weather)
    obj = json.loads(response.read())
    print(weather)
	#if no attractions found, print the following
    if description == []:
        description=["There are no registered attractions at this current location."]
	#grabs info on current day
    summary=obj['hourly']['summary']
    data = obj['daily']['data'][0]
    low = data['temperatureMin']
    high = data['temperatureMax']
    curr = obj['currently']['temperature']
    return render_template("info.html", text = description, summary = summary, low = low, high = high, curr = curr, SESSION = loggedIn())

#shows saved information of user
@app.route("/account")
def account():

    if 'user' not in session:
        return redirect('/track')
    
    user = session['user']
    saves = getters.get_saves(user)
    return render_template("account.html", SESSION = loggedIn(), saves = saves, user = session['user'])

#saves information into the database
@app.route("/save")
def save():

    global currLat
    global currLong
    global times

    info = request.args
    if 'user' not in session:
        return redirect('/')
	#saves all info from location to database
    user = session['user']
    times = times
    lat = currLat
    lon = currLong
    address = info['address']
    summary = info['summary']
    high = info['high']
    low = info['low']
    curr = info['curr']
    place = info['place']
    adders.add_save(user,times,lat,lon,address,summary,high,low,curr,place)
    return redirect("/account")

#updates page
@app.route("/update")
def update():
    
    global currLat
    global currLong
    global times

    refresh()

    return redirect("/track")

#demo page
@app.route("/demo")
def demo():

    global currLat
    global currLong
    global times

    if currLat != str(40.712775) and currLong != str(-74.005973):
        currLat = str(40.712775) 
        currLong = str(-74.005973)
        times = datetime.datetime.now()
    else: 

        refresh()

    return redirect("/track")

if __name__ == '__main__':
    app.run(debug=True)

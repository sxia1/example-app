from flask import Flask
import sqlite3

DB_FILE = "data/database.db"

def add_save(user,times,lat,long,address,summary,high,low,curr,attraction):
    """Takes information about the state of an attraction and saves it to the user's account"""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command ="INSERT INTO saves (user,times,lat,long,address,summary,high,low,curr,attraction) VALUES (?,?,?,?,?,?,?,?,?,?)"
    args = (user,times,lat,long,address,summary,high,low,curr,attraction)
    c.execute(command,args)
    db.commit()
    db.close()
    return True

def add_achievement(user,accomplishment):
    """Addes an achievement to the user"""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "INSERT INTO achievements (user,accomplishment) VALUES (?,?)"
    args = (user,accomplishment)
    c.execute(command,args)
    db.commit()
    db.close()
    return True

#print(add_save('123','time','lat','long','address','summary','high','low','alerts','attractions'))

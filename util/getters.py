from flask import Flask
import sqlite3

DB_FILE = "data/database.db"

def get_saves(user):
    """Returns all the saves of the user"""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    command = "SELECT * FROM saves WHERE user = ?"
    saves = False 
    for i in c.execute(command,(user,)):
        saves = True
        
    if saves:
        all_saves = c.execute(command,(user,)).fetchall()
        db.close()
        return all_saves

    else: 
        db.close()
        return [] 

def get_achievements(user):
    """Returns all the achievements of the user"""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT * FROM achievements WHERE user = ?"
    args = user
    all_achievements = c.execute(command,args).fetchall()
    db.close()
    return all_achievements

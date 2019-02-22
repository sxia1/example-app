from flask import Flask
import sqlite3

DB_FILE = "data/database.db"

def register(user, pwd, conf):
    """Checks to see if the user-password pair is allowed and adds the user to the database"""
    if pwd != conf:
        return "Passwords don't match"

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    for i in c.execute("SELECT user FROM accts WHERE user = ? ",(user,)):
        db.close()
        return "Username already exists"

    c.execute("INSERT INTO accts (user, password) VALUES(?,?)", (user,pwd,))

    db.commit()
    db.close()

    return "Account creation successful"

def login(user, pwd):
    """Checks to see if the user and password match"""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    for i in c.execute("SELECT password FROM accts WHERE user = ?",(user,)):
        if i[0] == pwd:
            db.close()
            return "Login Successful"

        else:
            db.close()
            return "Wrong password"

    db.close()
    return "No Such Username Found"

print(register("123","123","123")) #expect account creation successful

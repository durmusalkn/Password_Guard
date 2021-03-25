import sqlite3 as sql
import Account

def ConnectDatabase():
    db = sql.connect('PasswordGuard.db')
    return db

def IsAccExist(siteName,id) -> bool:
    db = ConnectDatabase()
    cr = db.cursor()
    cursor = cr.execute('SELECT ID FROM ACCOUNT WHERE SITE_NAME = ? AND USER_ID = ?',(siteName,id,))
    ctrl = len(cursor.fetchone())

    if ctrl:
        return True
    else :
        return False

def InsertUser(name,password):
    db = ConnectDatabase()
    cr = db.cursor()
    datas = [(password,name)]
    for data in datas:
        cr.execute("INSERT INTO USER VALUES (null,?,?)",data)
    db.commit()
    return

def GetUserName() -> str:
    db = ConnectDatabase()
    cr = db.cursor()
    cursor = cr.execute("SELECT NAME FROM USER")
    name = cursor.fetchone()
    return name

def GetUserId(name) -> int:
    db = ConnectDatabase()
    cr = db.cursor()
    cursor = cr.execute("SELECT ID FROM USER WHERE NAME == ?",(name,))
    id = cursor.fetchone()[0]
    return id

def Login(password,name):
    db = ConnectDatabase()
    cr = db.cursor()
    cursor = cr.execute("SELECT PASS FROM USER WHERE NAME = ?",(name,))
    ctrlSql = cursor.fetchone()

    if ctrlSql:
        ctrlPass = ctrlSql[0]
        if password == ctrlPass:
            return 1
        else:
            return 0
    else:
        return 0

def InsertAcc(siteName,siteAdr,hashedPass,id):
    db = ConnectDatabase()
    cr = db.cursor()

    datas = [(id,siteName,siteAdr,hashedPass)]

    for data in datas:
        cr.execute("INSERT INTO ACCOUNT VALUES (null,?,?,?,?)",data)
    db.commit()
    return 1

def GetAccountBySiteName(siteName,userId) -> Account.Account:
    db = ConnectDatabase()
    cr = db.cursor()
    acc = Account.Account()

    cursor = cr.execute("SELECT * FROM ACCOUNT WHERE SITE_NAME = ? AND USER_ID = ?",(siteName,userId,))
    datas = cursor.fetchone()

    if datas:
        acc.Id = datas[0]
        acc.UserId = datas[1]
        acc.SiteName = datas[2]
        acc.SiteAddres = datas[3]
        acc.Pass = datas[4]

        return acc
    else:
        return acc

def UpdateAcc(siteName,id,hashedPass):
    db = ConnectDatabase()
    cr = db.cursor()

    cr.execute("UPDATE ACCOUNT SET PASS = ? WHERE SITE_NAME = ? AND USER_ID = ?",(hashedPass,siteName,id,))
    db.commit()
    return
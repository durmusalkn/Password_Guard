import odevPytData as data
import odevPytHashHelper as hash
import User
import Account

def SignUp(name, password):
    hashedpass = hash.encrypt(password)
    data.InsertUser(name,hashedpass)
    return

def GetUserName() -> str:
    name = data.GetUserName()
    return name

def Login(password,name):
    hashedpass = hash.encrypt(password)
    if data.Login(hashedpass,name) == 1:
        return 1
    else:
        return 0

def InsertAcc(siteName,siteAdr,password):
    hashedPass = hash.encrypt(password)
    id = int(data.GetUserId(User.User.name))

    data.InsertAcc(siteName,siteAdr,hashedPass,id)
    return 1

def SearchAcc(siteName) -> Account.Account:
    id = int(data.GetUserId(User.User.name))
    acc = data.GetAccountBySiteName(siteName,id)
    if acc.Id != 0:
        acc.Pass = hash.decrypt(acc.Pass)
        return acc
    else:
        return acc
def IsAccExist(siteName) -> bool:
    id = int(data.GetUserId(User.User.name))
    ctrl = data.IsAccExist(siteName,id)
    return ctrl

def UpdateAcc(siteName,password):
    id = int(data.GetUserId(User.User.name))
    hashedPass = hash.encrypt(password)
    data.UpdateAcc(siteName,id,hashedPass)

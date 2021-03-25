import odevPytController as control
import User
import Account

def login():
    print("Giriş yapmak için bilgilerinizi girin\n")
    name = input("lütfen kullanıcı adınızı girin\n")
    password = input("lütfen şifrenizi giriniz \n")

    if control.Login(password,name) == 1:
        print("Giriş Başarılı")
        User.User.name = name
        return 1
    else:
        print("Kullanıcı adı veya şifre hatalı !")
        return 0

def SignUp():
    name = input("Lütfen kullanıcı adı giriniz \n")
    password = input("lütfen şifrenizi giriniz \n")
    control.SignUp(name, password)
    print("Kayıt başarılı")
    return 1

def SearchAcc():
    siteName = input("Lütfen bulmak istediğiniz hesabın site adını giriniz\n")
    acc = control.SearchAcc(siteName)
    if acc.Id != 0:
        print("Site adı:",acc.SiteName,"\nSite adresi:",acc.SiteAddres,"\nŞifre:", acc.Pass,"\n")
    else:
        print("Bu isime sahip bir hesap bulunamadı!\n")
    return 1

def InsertAcc():
    print("Yeni bir hesap eklemek için istenilen bilgileri dikkatle girin\n")
    siteName = input("Lütfen site adını giriniz\n")
    siteAdr = input("lütfen site adresini giriniz\n")
    password = input("Lütfen şifrenizi giriniz\n")

    control.InsertAcc(siteName,siteAdr,password)

def UpdateAcc():
    siteName = input("\nŞifresini Güncellemek istediğiniz site adını giriniz\n")
    accCtrl = control.IsAccExist(siteName)
    if accCtrl:
        password = input("Lütfen yeni şifrenizi girin\n")
        control.UpdateAcc(siteName,password)
        return
    else:
        print("Bu Site ismine sahip bir hesanınız yoktur!")
        return

def GetMenu():
    print("\n1. Hesap Ara\n"
          "2. Yeni Hesap ve Şifre Ekle\n"
          "3. Şifre Güncelle\n")

    choice = int(input("Yapmak istediğiniz işlemin sıra numarasını giriniz\n"))

    if choice == 1:
        SearchAcc()
    elif choice == 2:
        InsertAcc()
    elif choice == 3:
        UpdateAcc()


if __name__ == '__main__':
    loginCtrl = int(input("Password Guard Programına hoş geldin. \nGiriş yapmak için '1'\nKayıt olmak için '2' giriniz\n"))
    if loginCtrl == 1:
        loginCtrl = login()
    else:
        loginCtrl = SignUp()

    if loginCtrl:
        while 1:
            GetMenu()
            ctrl = input("Uygulamayı kullanmaya devam etmek ister misiniz ? 'Y' or 'N'\n")
            if ctrl == 'N' or ctrl == 'n':
                break
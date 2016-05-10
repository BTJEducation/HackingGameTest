__author__ = 'JDadak'
import time

code = "E"
cipher = 100
alphabet = list('abcdefghijklmnopqrstuvwxyz')

def CheckCipher(sent):
    if sent != "test":
        return False
    else:
        return True

def CheckPassword(sent):
    if sent != code:
        return False
    else :
        return True

def RemoveAttempt(sent):
    x = sent - 1
    return  x

def GameOver():
    print("You Have failed. The world is destroyed!")
    time.sleep(5)
    quit()

def Encrypt(k) :
    plaintext = code
    cipher = ''
    for each in plaintext:
        c = (ord(each)+k) % 126
        if c < 32:
            c+=31
        cipher += chr(c)
    return cipher

def Decrypt(k, message):
    cipher = message
    plaintext = ''

    for each in cipher:
        p = (ord(each)-k) % 126
        if p < 32 :
            p+=95
        plaintext += chr(p)
    return plaintext

def EndGame():
    time.sleep(2)
    print("################    SENDING    DATA     PLEASE     WAIT                    ###########################")
    time.sleep(2)
    print("qywueiq809cacjr329r&*($4 H&*Fmmapsmfkof£*YAJIDou8uy892$53234j2389mnyrue785738490!nb6by754790089nsiu3ur")
    print("qiojiniofncnvm,npoaosio&*(*(329239845saioj!!328490354ufnmklsdkdsnfkjdsfnkopkjoijamcmmcmu%h90ur3nekiofj")
    print("89890cmvmcxpsiua90u903amkomcsk!@£(&&5*(jfnuisdfdsfuivoo645645ijiofjijhojigjunjknjknujnfuon^cjiduhsdsiu")
    time.sleep(5)
    print("y9yr3r6&(*&%*(jfjisojfossodojsodjahnjopsajfi0mu8904u8y895y4u*&()&3098908)@£*(08bncjsniofjiod$5fhidsfds")
    print("qywueiq809cacjr329r&*($4 H&*Fmmapsmfkof£*YAJIDou8uy892$53234j2389mnyrue785738490!nb67547900hrg89niu3ur")
    time.sleep(1)
    print("89890cmvmcxpsiua90u903amkomcsk!@£(&&5*(jfnuisdfdsfuivoo645645ijiofjijhojigjunjknjknujnfuonds9ugfuhdsiu")
    print("######################################################################################################")
    time.sleep(5) 
    print("###You have ...dsfsdfko 2.fsdfk3rlv %3 sf 2  sF' 's f s;###")
    time.sleep(5)
    print("########## MISSILES ARE FSDFSDFLKJ3234SKDFN MISSSSSSSSSKLSDLKSLKFLKSJDFIIIILLLLES#####################")
    print("########## ATTEMPTING TO RECIVE STATUS OF MISSLES......                                               ")
    time.sleep(3)
    print("##########  PLEASE WAIT........CONNECTING.......                                                      ")
    time.sleep(5)
    print("######################################################################################################")
    print("ERRORerrorERRORerrorERRORerrorERRORERRORerrorERRORerrorERRORerrorERRORERRORerrorERRORerrorERRORerrorER")
    print("y9yr3r6&(*&%*(jfjisojfossodojsodjahnjopsajfi0mu8904u8y895y4u*&()&3098908)@£*(08bncjsniofjofdsffdidsfds")
    print("qiojiniofncnvm,npoaosio&*(*(329239845saioj!!328490354ufnmklsdkdsnfkjdsfnkopkjoijamcmmcmud0ur6h3nksiofj")
    time.sleep(2)
    print("MISSILE 1   ERROR")
    print("MISSILE 2   ERROR")
    print("MISSILE 3   ERROR")
    print("MISSILE 4   ERROR")
    print("MISSILE 5   ERROR")
    print("MISSILE 6   ERROR")
    print("MISSILE 7   ERROR")
    print("MISSILE 8   ERROR")
    print("MISSILE 9   ERROR")
    print("MISSILE 10   ERROR")
    print("MISSILE 11   ERROR")
    print("MISSILE 12   ERROR")
    print("MISSILE 13   ERROR")
    print("MISSILE 14   ERROR")
    print("MISSILE 15   ERROR")
    print("MISSILE 16   ERROR")
    print("MISSILE 17   ERROR")
    print("MISSILE 18   ERROR")
    print("MISSILE 19   ERROR")
    print("MISSILE 20   ERROR")
    print("MISSILE 21   ERROR")
    print("MISSILE 22   ERROR")
    print("MISSILE 23   ERROR")
    print("MISSILE 24   ERROR")
    print("MISSILE 25   ERROR")
    print("MISSILE 26   ERROR")
    print("MISSILE 27   ERROR")
    print("MISSILE 28   ERROR")
    print("MISSILE 29   ERROR")
    print("MISSILE 30   ERROR")
    print("MISSILE 31   ERROR")
    print("MISSILE 32   ERROR")
    print("MISSILE 33   ERROR")
    print("MISSILE 34   ERROR")
    print("MISSILE 35   ERROR")
    print("MISSILE 36   ERROR")
    
    
    time.sleep(2)
    print("qywueiq809cacjr329r&*($4 H&*Fmmapsmfkof£*YAJIDou8uy892$53234j2389mnyrue785738490!nb675479d003489niu3ur")
    print("89890cmvmcxpsiua90u903amkomcsk!@£(&&5*(jfnuisdfdsfuivoo645645ijiofjijhojigjunjknjknujnfonji34dsfuhdsiu")
    time.sleep(1)
    print("qiojiniofncnvm,npoaosio&*(*(329239845saioj!!328490354ufnmklsdkdsnfkjdsfnkopkjoijamcmmcmu90uroh3nksiofj")
    print("qywueiq809cacjr329r&*($4 H&*Fmmapsmfkof£*YAJIDou8uy892$53234j2389mnyrue785738490!nb6754p7900i889niu3ur")
    print("MISSILE STATUS.......")
    time.sleep(2)
    print("")
    print("")
    print("STATUS: DESTROYED IN FLIGHT, OVER THE ATLANTIC, DESTROYED IN FLIGHT, OVER THE ATLANTIC################")
    print("CONGRATULATIONS!")
    time.sleep(5)

def main():
    print("The world is at stake, Only 12 minutes left go save it!")
    print(
        "You need to crack the cipher, log into the computer and shut it down before it's too late!")
    print("ERROR: 1ntru2tion detected. PASSWORD is encrypted.")

    enc = Encrypt(cipher)
    #print(enc)
    #print(Decrypt(12, enc))

    print("ENCRYPTED PASSWORD: " + enc)
    ans = input("Decrypt Now?  Y/N").lower()

    bool
    esc = False
    while esc == False:
        if ans == 'y':
            esc = True
        else :
            print("The world is at stake, Only 12 minutes left go save it!")
            print("You need to crack the cipher, log into the computer and shut it down before it's too late!")
            print("ERROR: 1ntru2tion detected. PASSWORD is encrypted.")
            ans = input("Decrypt Now?  Y/N").lower()
    print("HOW MANY YEARS ARE IN A CENTURY? ")
    guess = int(input("Input the Cipher for mask " + enc + "  :  "))

    esc = False

    while esc == False:
        if guess != cipher:
            print("ERROR: INCORRECT CIPHER:" + Decrypt(guess, enc))
            guess = int(input("Input the Cipher for mask  " + enc + "  :  "))
        else:
            esc = True
            print("Correct Cipher! Decryption successful:" + Decrypt(guess, enc))

    print("PLEASE ANSWER THE QUESTION FOR PASSWORD")
    time.sleep(1)
    print(" ")
    print("I am at the beginning of eternity the end of time and space the beginning of the end and the end of every place?")
    print(" ")
    
    time.sleep(1)
    print("LOGIN: Username = 'Admin' ")
    pw = input("Password =  :  ").upper()

    esc = False

    while esc == False:
        if CheckPassword(pw) == True:
            print("Authorisation successful.")
            esc = True
        else:
            print("UNAUTHORISED ACCESS ERROR ERROR ERROR")
            time.sleep(1)
            print("TRY AGAIN")
            pw = input("Password =  :  ")

    print("Welcome back ADMIN. What would you like to do?")
    print("USERS  |  MISSILES  |  SETTINGS   |  SHUTDOWN   |   FIREWALL   |    SOL")

    x = input(":").upper()
    attempts = 3
    esc = False

    while esc == False:
        if attempts < 1:
            esc = True
            GameOver()
        elif x == "USERS":
            print("USERS UNAVAILABLE.")
            attempts = RemoveAttempt(attempts)
            print("Welcome back ADMIN. What would you like to do?")
            print("")
            print("USERS  |  MISSILES  |  SETTINGS   |  SHUTDOWN   |   FIREWALL   |    SOL")
            x = input(":").upper()
        elif x == "MISSILES":
            print("MISSILES ARE ALL FIRED")
            attempts = RemoveAttempt(attempts)
            print("Welcome back ADMIN. What would you like to do?")
            print("USERS  |  MISSILES  |  SETTINGS   |  SHUTDOWN   |   FIREWALL   |    SOL")
            x = input(":").upper()
        elif x == "SETTINGS":
            print("ERROR: Settings Corrupt. Please Reload Module.")
            attempts = RemoveAttempt(attempts)
            print("Welcome back ADMIN. What would you like to do?")
            print("USERS  |  MISSILES  |  SETTINGS   |  SHUTDOWN   |   FIREWALL   |    SOL")
            x = input(":").upper()
        elif x == "SHUTDOWN":
            esc = True
            print("USERS  |  MISSILES  |  SETTINGS   |  SHUTDOWN   |   FIREWALL   |    SOL")
            EndGame()
        elif x == "FIREWALL":
            print("FIREWALL UNAVAILABLE.")
            attempts = RemoveAttempt(attempts)
            print("Welcome back ADMIN. What would you like to do?")
            print("USERS  |  MISSILES  |  SETTINGS   |  SHUTDOWN   |   FIREWALL   |    SOL")
            x = input(":").upper()
        elif x == "SOL":
            print("THIS IS NOT THE TIME FOR GAMES.")
            attempts = RemoveAttempt(attempts)
            print("Welcome back ADMIN. What would you like to do?")
            print("USERS  |  MISSILES  |  SETTINGS   |  SHUTDOWN   |   FIREWALL   |    SOL")
            x = input(":").upper()
        else :
            print("COMMAND UNKNOWN")

if __name__ == '__main__':
    main()
YY

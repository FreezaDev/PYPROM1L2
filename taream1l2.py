import random
char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrrstuvwxyz1234567890_-*/!?·$%&="
pwdcustomlen = int(input("Ingrese la longitud de su contraseña \n"))
autogenpwd = ""
for i in range(pwdcustomlen):
    autogenpwd = autogenpwd + random.choice(char)
print("Su contraseña: ", autogenpwd)

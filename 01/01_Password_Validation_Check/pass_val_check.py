import re

err = "Password Should Include Atleast {er}"
input_txt = str(input())
valid = True
while 1:
    if (len(input_txt) < 8):
        valid = False
        err = err.format(er="8 characters")
        break
    elif not re.search("[a-z]", input_txt):
        valid = False
        err = err.format(er="an Alphabet")
        break
    elif not re.search("[0-9]", input_txt):
        valid = False
        err = err.format(er="a Number")
        break
    elif not re.search("[A-Z]", input_txt):
        valid = False
        err = err.format(er="a Captial letter")
        break
    elif not re.search("[!@#$%^&*()]", input_txt):
        valid = False
        err = er.format(er="a Special character")
        break
    else:
        valid = True
        print("Valid Password")
        break

if valid == False:
    print(err)


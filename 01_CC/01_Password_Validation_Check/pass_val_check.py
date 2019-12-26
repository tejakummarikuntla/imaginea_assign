import re

test_cases = ["Password Lenght > 8 ",
              "Atleast a single alphabet ",
              "Atleast a Captial Letter ",
              "Atleast a Numberical Digit ",
              "Atleast a speacial Character "]

def is_valid(input_text):
    valid = True
    if(len(input_txt) < 8):
        print(test_cases[0],"NO")
        valid = False
    else:
        print(test_cases[0], "YES")
    if not re.search("[a-z]", input_txt):
        print(test_cases[1], "NO")
        valid = False
    else:
        print(test_cases[1], "YES")
    if not re.search("[A-Z]", input_txt):
        print(test_cases[2], "NO")
        valid = False
    else:
        print(test_cases[2], "YES")
    if not re.search("[0-9]", input_txt):
        print(test_cases[3], "NO")
        valid = False
    else:
        print(test_cases[2], "YES")
    if not re.search("[!@#$%^&*()]", input_txt):
        print(test_cases[4], "NO")
        valid = False
    else:
        print(test_cases[4],"YES")

    return valid

if __name__ == "__main__":
    while 1:
        input_txt = str(input("Enter Your Password: "))
        res = is_valid(input_txt)
        if(res == False):
            print("Invalid Password")
        else:
            print("Valid Password")
            break

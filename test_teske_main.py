import string as st
import random as rd

# import main-program
from teske_main import generate_random_password

## check if lenght of password is correct 
# check the strong password
def test_strong_lenght():
    for i in range(10000):
        gen_pw = generate_random_password('strong')
        len_gen_pw = False 
        if 8 <= len(gen_pw) <= 12:
            len_gen_pw = True
        assert(len_gen_pw)

# check the weak password
def test_weak_lenght():
    for i in range(10000):
        gen_pw = generate_random_password('weak')
        len_gen_pw = False 
        if 6 <= len(gen_pw) <= 8:
            len_gen_pw = True
        assert(len_gen_pw)    


## check for digits
# check the strong password 
def test_strong_digits():
    for i in range(10000):
        gen_pw = generate_random_password('strong')
        dig_gen_pw = False
        for x in gen_pw:
            if x.isdigit():
                dig_gen_pw = True
            else:
                continue
        if dig_gen_pw == False:
            print(gen_pw)
        assert(dig_gen_pw) 

# check the weak password 
def test_weak_digits():
    for i in range(10000):
        gen_pw = generate_random_password('strong')
        dig_gen_pw = False
        for x in gen_pw:
            if x.isdigit():
                dig_gen_pw = True
            else:
                continue
        if dig_gen_pw == False:
            print(gen_pw)
        assert(dig_gen_pw) 


## check for symbols
# check the strong password 
def test_strong_symbols():
    for i in range(10000):
        gen_pw = generate_random_password('strong')
        sym_gen_pw = False
        for x in gen_pw:
            for y in st.punctuation:
                if x == y:
                    sym_gen_pw = True
                    break
        assert(sym_gen_pw) 

# check the weak password 
def test_weak_symbols():
    for i in range(10000):
        gen_pw = generate_random_password('weak')
        sym_gen_pw = True
        for x in gen_pw:
            for y in st.punctuation:
                if x == y:
                    sym_gen_pw = False
                    break
        assert(sym_gen_pw) 


## check for big letters
# check the strong password 
def test_strong_big():
    for i in range(10000):
        gen_pw = generate_random_password('strong')
        big_gen_pw = False
        for x in gen_pw:
            if any(x.isupper()for x in gen_pw):
                big_gen_pw = True
            else:
                continue
        assert(big_gen_pw) 

# check the weak password
def test_weak_big():
    for i in range(10000):
        gen_pw = generate_random_password('weak')
        big_gen_pw = False
        for x in gen_pw:
            if any(x.isupper()for x in gen_pw):
                big_gen_pw = True
            else:
                continue
        assert(big_gen_pw) 

## check for small letters
# check the strong password 
def test_strong_sml():
    for i in range(10000):
        gen_pw = generate_random_password('strong')
        big_gen_pw = False
        for x in gen_pw:
            if any(x.islower()for x in gen_pw):
                big_gen_pw = True
            else:
                continue
        assert(big_gen_pw) 

# check the weak password
def test_weak_sml():
    for i in range(10000):
        gen_pw = generate_random_password('weak')
        sml_gen_pw = False
        for x in gen_pw:
            if any(x.islower()for x in gen_pw):
                sml_gen_pw = True
            else:
                continue
        assert(sml_gen_pw) 


## check for duplicates (big AND small letters)
# check the strong password 
def test_strong_dupl():
    for i in range(10000):
        gen_pw = generate_random_password('strong')
        sml_gen_pw = True
        up_gen_pw = gen_pw.upper()
        for x in up_gen_pw:
            if up_gen_pw.count(x) >= 2:
                sml_gen_pw = False
            else:
                continue
        assert(sml_gen_pw) 

# check the weak password 
def test_weak_dupl():
    for i in range(10000):
        gen_pw = generate_random_password('weak')
        sml_gen_pw = True
        up_gen_pw = gen_pw.upper()
        for x in up_gen_pw:
            if up_gen_pw.count(x) >= 2:
                sml_gen_pw = False
            else:
                continue
        assert(sml_gen_pw) 



'''======================================================================
    Generates a list of Singapore random phone numbers
    6XXXXXXX, 8XXXXXXX, 9XXXXXXXX and store them in phones.txt
======================================================================'''

'''------------------------------------------------------------
    libraries used
------------------------------------------------------------'''

import numpy as np # general number processing

'''------------------------------------------------------------
    global parameters
------------------------------------------------------------'''

phones_filename = "phones.txt"
number_of_phone_numbers = 1000

'''------------------------------------------------------------
    function gen_phones:
        takes in how many numbers to generate (default=100)
        first generate randomly from 70000000-99999999
        adjust 7xxxxxxx to 6xxxxxxx, others remain the same
        returns the number as a list
------------------------------------------------------------'''

def gen_phones (num=100):
    numbers = np.random.randint(70000000,100000000,num)
    numbers = [num if num>=80000000 else num-10000000 for num in numbers]
    return numbers

'''------------------------------------------------------------
    main loop
------------------------------------------------------------'''
numbers = gen_phones(number_of_phone_numbers) # generates numbers
with open(phones_filename,"w") as fp: # open file to store numbers
    for number in numbers: # go through number-by-number - need to add "\n"
        fp.write(f"{number}\n") # write number to file with a new-line char.


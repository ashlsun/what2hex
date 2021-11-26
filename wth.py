# what the hex
# converting between hex & binary
# can be such a pain (ToT)

HEX_CHARS = {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f',' '}
HEX_STR = "0123456789abcdef"

# ----------------------------------
# Functions for checking the string! 
def check_binary(str):
    for char in str:
        if char != "0" and char != "1" and char != " ":
            return False
    return True

def check_hex(str):
    if str[0:2] != "0x":
        return False
    for char in str[2:]:
        if char not in HEX_CHARS:
            return False
    return True

# TODO: complete this function!
def check_decimal(str):
    pass

# valid input takes a str and returns a tuple
# 1st element is if input is either hex or binary
# 2nd is if input is hex
def valid_input(str):
    if check_hex(str):
        return (True, True)
    elif check_binary(str):
        return (True, False)
    else:
        return (False, False)

# ----------------------------------
# Hex to binary converter functions!! 
def hex_to_bin(char):
    return dec_to_bin(hex_to_dec(char))

def hex_to_dec(char):
    return HEX_STR.find(char)

def dec_to_bin(int):
    ret = 0
    test = int

    if test - 8 >= 0:   # is the 1st digit a 1?
        ret += 1000
        test -= 8
    
    if test - 4 >= 0:   # likewise for the 2nd digit, and so on
        ret += 100
        test -= 4

    if test - 2 >= 0:
        ret += 10
        test -= 2

    if test - 1 >= 0:
        ret += 1
    
    return ret

# ----------------------------------
# Binary to converter functions!! 
def bin_to_hex(bin_str):
    #string = ""

    #dec = bin_to_dec(bin_str)
    #test = dec
    #numb = Round up ( len(bin_str) / 4)
    #for i in range

    # maybe go byte by byte and convert
    pass

def byte_to_hex(byte):
    HEX_STR[bin_to_dec(byte)]


def bin_to_dec(bin_str):
    i = len(bin_str) - 1 # highest power of 2

    int = 0
    for char in bin_str:
        if char == "1":
            int += 2 ** i
        i -= 1
    
    return int

def converter(string, is_hex):
    if is_hex: # the input is hex
        output = ""
        for char in string[2:]:
            byte = str(hex_to_bin(char))

            if len(byte) < 4:
                byte = "0" * (4 - len(byte)) + byte

            output += byte + " "
        return output

    else: # the input is binary
        return bin_to_dec(string)


def main(): 
    print("this program will convert binary -> decimal & hex -> binary")
    finished = False

    string = input("enter value: ")
    while (not finished):
        is_valid = valid_input(string)[0]
        while not is_valid and not finished:
            print("please make sure: \n \t - your hex value starts with 0x & is all lowercase \n \t - your binary value has only 1s and 0s )")
            string = input("\n" + "enter value: ")
            finished = string == "q" 

            is_valid = valid_input(string)[0]

        print("\n" + str(converter(string, check_hex(string))))

        string = input("\n" + "enter next value ('q' to quit): ")
        finished = string == "q" 

    

if __name__ == "__main__":
    main()

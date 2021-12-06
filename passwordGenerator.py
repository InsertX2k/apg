# imports
from random import choice
from colorama import Style, Fore, Back
import colorama
import sys

# initializing colorama.
colorama.init(autoreset=True)

# making some arrays.
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# creating a clone of the list (or array) alphabet but in uppercase version.
uppercase_alphabet = []
for character in alphabet:
    character = str(character.upper())
    uppercase_alphabet.append(character)

# print(f"{Fore.GREEN}{uppercase_alphabet}")
# print(f"{Fore.CYAN}{alphabet}")

# so now we have uppercase_alphabet and alphabet lists.
special_character = ["(", ")", "[", "]", "{", "}", ".", "%", "$", "=", "+", "-"]
# appending all possible numbers to lists.
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# now we have lists:
# special_character
# numbers
# uppercase_alphabet
# alphabet
# now let's continue working on the code.

def generatePassword(intLengthOfNumbers, intLengthOfSpecialCharacters, intLengthOfUpperCaseAlphabet, intLengthOfLowerCaseAlphabet):
    """
    Generate a secure password for online logins, banking accounts, and so on.
    
    This function doesn't save the generated password, it disposes it after it generates it and returns it to the user (depending on the use of the function).

    For an example:


    ```py
    # importing this function from this module.
    from passwordGenerator import generatePassword
    # generating a password then printing it to stdout.
    print(generatePassword(12, 0, 0, 25))
    ```

    This usually disposes the generated password (from computer memory RAM) after it is printed to stdout.

    When called, this function takes 4 positional arguments, the length of numbers in your password, and the length of special characters in your password, and the length of uppercase alphabet characters, and the length of lowercase alphabet characters in your password.

    This function is a part of "Advanced Password Generator" The command line tool.

    Copyright (C) 2021 - Insertx2k Dev (Mr.X) 

    If you need any kind of support (or technical assistance):-

    [Contact us on Twitter](https://twitter.com/insertplayztw)

    [Visit my GitHub](https://github.com/insertx2k)
    """


    # converting to datatype integer.
    try:
        intLengthOfLowerCaseAlphabet = int(intLengthOfLowerCaseAlphabet)
        intLengthOfUpperCaseAlphabet = int(intLengthOfUpperCaseAlphabet)
        intLengthOfSpecialCharacters = int(intLengthOfSpecialCharacters)
        intLengthOfNumbers = int(intLengthOfNumbers)
    except:
        raise Exception("Function parameters 0, 1, 2, 3, must be of datatype int")
        return False
    
    # generating the password.
    secure_password = ""
    for i in range(intLengthOfLowerCaseAlphabet):
        secure_password = secure_password + str(choice(alphabet))
    
    for i in range(intLengthOfUpperCaseAlphabet):
        secure_password = secure_password + str(choice(uppercase_alphabet))
    
    for i in range(intLengthOfSpecialCharacters):
        secure_password = secure_password + str(choice(special_character))
    
    for i in range(intLengthOfNumbers):
        secure_password = secure_password + str(choice(numbers))
    
    # returning the securely generated password by the function.
    return secure_password


def printSplash():
    """
    Print the splash text to stdout.

    When called, it takes no positional or optional or keyword arguments.

    Example of use:

    ```py
    from passwordGenerator import printSplash
    printSplash()
    # output:
    # Insertx2k Dev (Mr.X)
    # Advanced Password Generator, Command Line Tool
    ```

    You can call this function directly from any other Python file (or Project).
    """
    print(f"Insertx2k Dev (Mr.X)")
    print("Advanced Password Generator, Command Line Tool")
    print('', end="\n")
    
    return None


# if program was executed as a Python Script File (or even a Compiled Bytecode or Binary Program),
# execute the given code here.
if __name__ == '__main__':
    # printSplash() -> This prints out the splash.
    if len(sys.argv) == 1:
        print(f"{Style.BRIGHT}{Fore.RED}error: expected 4 more arguments")
        print(f"{Style.BRIGHT}{Fore.WHITE}info: syntax is: LengthOfNumbers, LengthOfSpecialCharacters, LengthOfUpperCaseAlphabetCharacters, LengthOfLowerCaseAlphabetCharacters")
        print('', end="\n\n")
        sys.exit(1)
    elif len(sys.argv) == 2:
        print(f"{Style.BRIGHT}{Fore.RED}error: expected 3 more arguments")
        print(f"{Style.BRIGHT}{Fore.WHITE}info: syntax is: LengthOfNumbers, LengthOfSpecialCharacters, LengthOfUpperCaseAlphabetCharacters, LengthOfLowerCaseAlphabetCharacters")
        print('', end="\n\n")
        sys.exit(1)
    elif len(sys.argv) == 3:
        print(f"{Style.BRIGHT}{Fore.RED}error: expected 2 more arguments")
        print(f"{Style.BRIGHT}{Fore.WHITE}info: syntax is: LengthOfNumbers, LengthOfSpecialCharacters, LengthOfUpperCaseAlphabetCharacters, LengthOfLowerCaseAlphabetCharacters")
        print('', end="\n\n")
        sys.exit(1)
    elif len(sys.argv) == 4:
        print(f"{Style.BRIGHT}{Fore.RED}error: expected 1 more argument")
        print(f"{Style.BRIGHT}{Fore.WHITE}info: syntax is: LengthOfNumbers, LengthOfSpecialCharacters, LengthOfUpperCaseAlphabetCharacters, LengthOfLowerCaseAlphabetCharacters")
        print('', end="\n\n")
        sys.exit(1)
    elif len(sys.argv) >= 5:
        # attempting to convert all given arguments to int datatypes.
        try:
            lenofnumbers = int(sys.argv[1])
            lenofspecialchars = int(sys.argv[2])
            lenofupperchars = int(sys.argv[3])
            lenoflowerchars = int(sys.argv[4]) 
        except Exception as excpt0:
            print(f"{Fore.RED}{Style.BRIGHT}error: expected int datatype in program arguments")
            sys.exit(2)
        
        # calling the function to generate a secure password for the user.
        print(f"{generatePassword(lenofnumbers, lenofspecialchars, lenofupperchars, lenoflowerchars)}")
        # exiting the execution of the program with error code 0 (meaning the execution of the program has successfully finished with no errors at all).
        sys.exit(0)
# else if the program was imported as a standard Python 3.x.x Module, execute the given code here.
else:
    # do nothing.
    pass
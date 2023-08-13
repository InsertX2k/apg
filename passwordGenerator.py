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
special_character = ["(", ")", "[", "]", "{", "}", ".", "%", "$", "=", "+", "-", "&", "^", "/", "\\"]
# appending all possible numbers to lists.
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# now we have lists:
# special_character
# numbers
# uppercase_alphabet
# alphabet
# now let's continue working on the code.

def generatePassword(intLengthOfNumbers: int, intLengthOfSpecialCharacters: int, intLengthOfUpperCaseAlphabet: int, intLengthOfLowerCaseAlphabet: int, randomize=True, randomizePassLen=0,
                     noNumbersInRandomize=False, noSpecialCharactersInRandomize=False, noUpperCaseCharsInRandomize=False, noLowerCaseCharsInRandomize=False):
    """
    Generate a secure password for online logins, banking accounts, and so on.
    
    This function doesn't save the generated password, it disposes it after it generates it and returns it to the user (depending on the use of the function).
    

    * Arguments:

    `intLengthOfNumbers` -> must be an integer and it specifies the length of numbers in the generated password.

    `intLengthOfSpecialCharacters` -> must be an integer and it specifies the length of special characters in the generated password.

    `intLengthOfUpperCaseAlphabet` -> must be an integer and it specifies the length of uppercase alphabet characters in the generated password.

    `intLengthOfLowerCaseAlphabet` -> must be an integer and it specifies the length of lowercase alphabet characters in the generated password.

    ### Please note that if you want to use the `randomize` technique you will have to fill these arguments with any value or with zeros, because if you didn't, Python will throw an error that says `generatePassword() requires at least 4 arguments, but 0 were given`

    * Keyword Arguments:

    `randomize` -> Is a Keyword Argument specifying whether to use the randomize technique or no, True if enabled, and False if not, default is True

    * Additional Keyword Arguments related to the functionality of the `randomize` technique:

    `randomizePassLen` -> Is a Keyword Argument specifying the length of the generated password when randomize technique is enabled, default is `0` (This only takes effect if `randomize=True`)

    `noNumbersInRandomize` -> Decides whether to disable including numbers in the generated password by the randomize technique or not, default is `False` (which means they will be included)

    `noSpecialCharactersInRandomize` -> Decides whether to disable including special characters in the generated password by the randomize technique or not, default is `False` (which means they will be included)

    `noUpperCaseCharsInRandomize` -> Decides whether to disable including uppercase alphabet characters in the generated password by the randomize technique or not, default is `False` (which means they will be included)

    `noLowerCaseCharsInRandomize` -> Decides whether to disable including lowercase alphabet characters in the generated password by the randomize technique or not, default is `False` (which means they will be included)

    For example (basic usage syntax with no randomization enabled):

    ```py
    # importing this function from this module.
    from passwordGenerator import generatePassword
    # generating a password then printing it to stdout.
    print(generatePassword(12, 0, 0, 25))
    ```

    Another example (but with randomization enabled):

    ```py
    # importing this function from this module.
    from passwordGenerator import generatePassword
    # generating a password using the randomize technique with the length of 50 and don't exclude anything then print it to stdout.
    print(generatePassword(1, 1, 1, 1, randomize=True, randomizePassLen=50,
        noNumbersInRandomize=False, noSpecialCharactersInRandomize=False, noUpperCaseCharsInRandomize=False, noLowerCaseCharsInRandomize=False))
    ```

    This usually disposes the generated password (from computer memory RAM) after it is printed to stdout.

    When called, this function takes 4 positional arguments, the length of numbers in your password, and the length of special characters in your password, and the length of uppercase alphabet characters, and the length of lowercase alphabet characters in your password.

    This function is a part of "Advanced Password Generator" The command line tool.

    Copyright (C) 2021 - 2023 - Insertx2k Dev (Mr.X) or Ziad (Mr.X) Software

    If you need any kind of support (or technical assistance):-

    [Contact us on Twitter](https://twitter.com/insertplayztw)

    [Visit my GitHub](https://github.com/insertx2k)
    """

    #     Description for data modes:
    #     Data mode #1 -> Lowercase alphabets
    #     Data mode #2 -> Uppercase alphabets
    #     Data mode #3 -> Special characters
    #     Data mode #4 -> Numbers
    data_modes = [1, 2, 3, 4] 
    
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
    if bool(randomize) == False:
        for i in range(intLengthOfLowerCaseAlphabet):
            secure_password = secure_password + str(choice(alphabet))
        
        for i in range(intLengthOfUpperCaseAlphabet):
            secure_password = secure_password + str(choice(uppercase_alphabet))
        
        for i in range(intLengthOfSpecialCharacters):
            secure_password = secure_password + str(choice(special_character))
        
        for i in range(intLengthOfNumbers):
            secure_password = secure_password + str(choice(numbers))
    else: # if randomize == True
        # Password length
        passLen = int(randomizePassLen)
        for x in range(passLen):
            curdatamode = choice(data_modes)
            if curdatamode == 1: #lowercase chars
                if bool(noLowerCaseCharsInRandomize) == True: # if no lower case chars in randomize is enabled
                    pass
                else:
                    secure_password = secure_password + str(choice(alphabet))
            if curdatamode == 2: # uppercase chars
                if bool(noUpperCaseCharsInRandomize) == True: # if no upper case chars in randomize is enabled
                    pass
                else:
                    secure_password = secure_password + str(choice(uppercase_alphabet))
            if curdatamode == 3: # special chars
                if bool(noSpecialCharactersInRandomize) == True: # if no special chars in randomize is enabled
                    pass
                else:
                    secure_password = secure_password + str(choice(special_character))
            if curdatamode == 4: # numbers
                if bool(noNumbersInRandomize) == True: # if no numbers in randomize is enabled
                    pass
                else:
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

USAGE = """
info: syntax is: <Length Of Numbers>, <Length Of Special Characters>, <Length Of Upper Case Alphabet Characters>, <Length Of Lower Case Alphabet Characters> (if randomize is not enabled)

if randomize is enabled, syntax will be:
<Password Length>, [Don't insert numbers in the password (yes)], [Don't insert special characters in the password (yes)], [Don't insert uppercase alphabet in the password (yes)], [Don't insert lowercase alphabet in password (yes)]

(You enable randomize by specifying '-r' switch to the command line)
examples: 

apgservices.exe/<AppFileName>.exe -r 15
Generate a random secure password with the length of 15 characters and special characters and numbers and so on.

apgservices.exe/<AppFileName>.exe -r 20 yes
Generate a random secure password with the length of 20 characters and special characters and numbers and so on, but doesn't include numbers in the generated password

apgservices.exe/<AppFileName>.exe -r 20 yes yes 
Generate a random secure password with the length of 20 characters and special characters and numbers and so on, but doesn't include numbers and special characters in the generated password

apgservices.exe/<AppFileName>.exe -r 20 yes yes yes
Generate a random secure password with the length of 20 characters and special characters and numbers and so on, but doesn't include numbers and special characters and uppercase alphabet characters in the generated password

apgservices.exe/<AppFileName>.exe -r 20 yes yes yes yes
Generate a random secure password with the length of 20 characters and special characters and numbers and so on, but doesn't include numbers and special characters and uppercase alphabet characters and lowercase alphabet characters in the generated password

apgservices.exe/<AppFileName>.exe 5 2 2 3
Generate a secure password with 5 numbers, 2 special characters, 2 uppercase alphabet characters, and 3 lowercase alphabet characters.
"""


# if program was executed as a Python Script File (or even a Compiled Bytecode or Binary Program),
# execute the given code here.
if __name__ == '__main__':
    # printSplash() -> This prints out the splash.
    if len(sys.argv) == 1: # no args
        print(f"{Style.BRIGHT}{Fore.RED}error: expected 4 more arguments")
        print(f"{Fore.WHITE}{USAGE}")
        print('', end="\n\n")
        sys.exit(1)
    elif len(sys.argv) == 2:
        if str(sys.argv[1]) == "-r" :
            print(f"{Style.BRIGHT}{Fore.RED}error: password length is missing")
            print(f"{Fore.WHITE}{USAGE}")
            print('', end="\n\n")
            sys.exit(1)
        else:
            print(f"{Style.BRIGHT}{Fore.RED}error: expected 3 more arguments")
            print(f"{Fore.WHITE}{USAGE}")
            print('', end="\n\n")
            sys.exit(1)
    elif len(sys.argv) == 3:
        if str(sys.argv[1]) == "-r":
            print(f"{generatePassword(0,0,0,0, randomize=True, randomizePassLen=int(sys.argv[2]))}")
            sys.exit(0)
        else:
            print(f"{Style.BRIGHT}{Fore.RED}error: expected 2 more arguments")
            print(f"{Fore.WHITE}{USAGE}")
            print('', end="\n\n")
            sys.exit(1)
    elif len(sys.argv) == 4:
        if str(sys.argv[1]) == "-r":
            if str(sys.argv[3]) == "yes": # no numbers will be put into the password
                print(f"{generatePassword(0,0,0,0, randomize=True, randomizePassLen=int(sys.argv[2]), noNumbersInRandomize=True)}")
            else:
                print(f"{generatePassword(0,0,0,0, randomize=True, randomizePassLen=int(sys.argv[2]))}")
            sys.exit(0)
        else:
            print(f"{Style.BRIGHT}{Fore.RED}error: expected 1 more argument")
            print(f"{Fore.WHITE}{USAGE}")
            print('', end="\n\n")
            sys.exit(1)
    elif len(sys.argv) >= 5:
        # attempting to convert all given arguments to int datatypes.
        
        
        # calling the function to generate a secure password for the user.
        if str(sys.argv[1]) == "-r": # randomize is enabled
            try:
                if str(sys.argv[3]) == "yes": # no numbers will be put into the password
                    nonumsinpass = True
                else:
                    nonumsinpass = False
            except:
                nonumsinpass = False
            
            try:
                if str(sys.argv[4]) == "yes": # no special characters will be put into the password
                    nospecialcharsinpass = True
                else:
                    nospecialcharsinpass = False
            except:
                nospecialcharsinpass = False
            
            try:
                if str(sys.argv[5]) == "yes": # no uppercase chars in password
                    noupperchars = True
                else:
                    noupperchars = False
            except:
                noupperchars = False
            
            try:
                if str(sys.argv[6]) == "yes": # no lowercase chars in password
                    nolowerchars = True
                else:
                    nolowerchars = False
            except:
                nolowerchars = False

            print(f"{generatePassword(0,0,0,0, randomize=True, randomizePassLen=int(sys.argv[2]), noNumbersInRandomize=nonumsinpass, noSpecialCharactersInRandomize=nospecialcharsinpass, noUpperCaseCharsInRandomize=noupperchars, noLowerCaseCharsInRandomize=nolowerchars)}")
            sys.exit(0)
        else: # randomize is disabled!
            try:
                lenofnumbers = int(sys.argv[1])
                lenofspecialchars = int(sys.argv[2])
                lenofupperchars = int(sys.argv[3])
                lenoflowerchars = int(sys.argv[4]) 
            except Exception as excpt0:
                print(f"{Fore.RED}{Style.BRIGHT}error: expected int datatype in program arguments")
                sys.exit(2)
            print(f"{generatePassword(lenofnumbers, lenofspecialchars, lenofupperchars, lenoflowerchars, randomize=False)}")
        
        # exiting the execution of the program with error code 0 (meaning the execution of the program has successfully finished with no errors at all).
        sys.exit(0)
# else if the program was imported as a standard Python 3.x.x Module, execute the given code here.
else:
    # do nothing.
    pass
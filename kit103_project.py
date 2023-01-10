https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
'''
KIT103 Project

Name: Replace with your name
SID: Replace with your student ID
'''

# Once you have decided on a project option you can delete the code for the
# other one (or leave it, since it will not adversely affect the other).

#%% Project Option 1: Morse Code
'''
Explain and justify your choice of test cases in this documentation comment.
You may wish to define multiple lists of test cases for different components
of your (anticipated) solution.
'''

#define some test cases here

def morse_encode(message: str, code) -> tuple[str, set]:
    '''
    Translates the message into Morse code using the specified code variant,
    returning both the encoded message as a string and a set of those
    characters that could not be translated.

    The interface to this function should not be changed (apart from adding
    another type hint if you wish) but you can define as many other functions
    to support its operation as you need to.
    '''
    return None, None


def morse_decode(morse: str, code) -> str:
    '''
    Translates the message in Morse code back into plain text, interpretting
    the encoded message using the specified code variant.

    The interface to this function should not be changed (apart from adding
    another type hint if you wish) but you can define as many other functions
    to support its operation as you need to.
    '''
    return None



#%% Project Option 2: Dictionary Codec
from typing import Any
'''
Explain and justify your choice of test cases in this documentation comment.
You may wish to define multiple lists of test cases for different components
of your (anticipated) solution.
'''

# define some test cases here

def compress(text: str, dictionary=None) -> tuple[str, Any]:
    '''
    Compresses the given text based on either the provided dictionary or one
    learned from the text. Returns the compressed text and dictionary used.

    The interface to this function should not be changed (apart from adding
    or modifying type hints if you wish) but you can define as many other
    functions to support its operation as you need to.
    '''
    return None, None


def decompress(txt: str, dictionary) -> str:
    '''
    Reconstructs and returns the original text stored in txt based on the
    provided dictionary.

    The interface to this function should not be changed (apart from adding
    another type hint if you wish) but you can define as many other functions
    to support its operation as you need to.
    '''
    return None

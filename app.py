"""
  Ceaser Cipher application

  For details about the purpose of the app, please refer to README.md file
"""
import re # Regular expression library

##############################
# GLOBAL VARIABLES
##############################
english_words = None # a set of English words to be used to guess key in brute-force code-cracking

##############################
# GENERIC FUNCTIONS
##############################
"""
  Generic 'shift_string' function will be used for both encryptin and decryption. For decrytpion 
  will use the negative value of the key.
  The function can take any integer shift value - it will be adjusted to fit the alphabet length.
  shift_string procedure is not dealing with user input validation.
"""
def shift_string( text:str , shift:int ):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'

  def adjust_index( orig_index:int ):
    adj_index = orig_index
    # Adjust the encouding index if greated than the alphabet length
    while adj_index >= len( alphabet ):
      adj_index -= len( alphabet )
    # Adgust the encouding index if less than the negative alphabet length
    while adj_index <= -len( alphabet ):
      adj_index += len( alphabet )
    return adj_index

  res = '' # initialise empty string result
  for char in text: # iterate over each character from the input text
    index = alphabet.find( char.lower() ) # Find character in the alphabet 
    if index > -1:
      enc_index = adjust_index( index + shift )
      res += alphabet[ enc_index ]
    else:
      res += char # If char is not in the alphabet, keeps it unchanged
  return res

"""
  Define custom exception to catch key values out of range error
"""
class KeyOutOfRange( Exception ):
  def __init__( self , key ):
      self.message = f"Key value of {key} is out of range! It must be between 0 and 26."
      super().__init__( self.message )

def load_words():
  with open('words_alpha.txt') as word_file:
    valid_words = set(word_file.read().split())
  return valid_words

##############################
# MAIN MENU CHOICE FUNCTIONS
##############################
"""
  Procedure to handle encryption choice dialog and input validation
"""
def choice_encrypt():
  print( '\n\t### ENCRYPTION ###\n' )
  try: # Generic error handling
    key = int( input( '\tPlease enter the key (0 to 26) to use.\n\t> ' ) )
    if key > 26 or key <0: # Validate the key value
      raise KeyOutOfRange( key=key )
    msg = input( '\tEnter the message to encrypt.\n\t> ' )
    print( f'\t  { shift_string( msg , key ) }' )
  except Exception as e:
    print( '\tSorry, your input was not valid!' )
    print( f'\t{e}' ) # Print details of errors

"""
  Procedure to handle decryption choice dialog and input validation
"""
def choice_decrypt():
  print( '\n\t### DECRYPTION ###\n' )
  try: # Generic error handling
    key = int( input( '\tPlease enter the key (0 to 26) to use.\n\t> ' ) )
    if key > 26 or key <0: # Validate the key value
      raise KeyOutOfRange( key=key )
    msg = input( '\tEnter the message to decrypt.\n\t> ' )
    # Decription is the opposite of encription, hence will use negative key value
    print( f'\t  { shift_string( msg , -key ) }')
  except Exception as e:
    print( '\tSorry, your input was not valid!' )
    print( f'\t{e}' ) # Print details of errors

"""
  Procedure to handle code-cracking choice dialog

  In addition to the original task, this will add checking words within English dictionary to find best guess key.
  The English words dictionary is from https://github.com/dwyl/english-words.git
"""
def choice_cracking():
  global english_words
  print( '\n\t### CODE CRACKING ###\n' )
  msg = input( '\tEnter the message to crack.\n\t> ' )

  # Start a loop to try all keys (brute-force)
  best_key = None
  best_match_words = 0
  for key in range( 1 , 26 ): 
    decode_msg = shift_string( msg , -key ) # Decription is the opposite of encription, hence will use negative key value
    words = re.sub(r'[^ a-z+]', '', decode_msg )
    match_words = 0
    for word in words.split():
      if( word in english_words ):
        match_words += 1
    if match_words > best_match_words:
      best_match_words = match_words
      best_key = key
    print( f'\t Key:{key:02d} match {match_words} English words --> {decode_msg}')
  print( f'\n\tThe best guess key is {best_key}' )

"""
  Procedure to handle quit choice
"""
def choice_quit():
  global quit
  print( '\n###  CLOSEING OUT   ###' )
  print( '#######################' )
  print( '\nThank you and good bye!\n' )
  quit = True

##########################
# MAIN MENU DEFINITION
##########################
"""
  The dictionary below maps all main menu choices and respective procedures
"""
menu = {
  'e': choice_encrypt,
  'd': choice_decrypt,
  'c': choice_cracking,
  'q': choice_quit
}

####################
# MAIN APP
####################
quit = False # Initilise main app loop control value
english_words = load_words() # load English words for code-cracking

print( '#######################' )
print( '###  CEASER CIPHER  ###' )

# Start main app loop
while not quit:
  choice = input( '\nPlease select (e)ncrypt, (d)ecrypt, (c)ode-cracking or (q)uit :' )
  if choice.lower() in menu: # Check if choice is valid
    menu[ choice.lower() ]() # Call respective procedure
  else:
    print( f"\nSorry, I do not recognise your choice '{choice}'! Please try again." )

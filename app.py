"""
  Ceaser Cipher application

  Generic 'shift_string' function will be used for both encryptin and decryption.
  The function can take any integer shift value - it will be adjusted to fit the alphabet length.
  Hence shift_string procedure is not dealing with user input validation.
"""
def shift_string( text:str , shift:int ):
  alphabet = 'ABCDEFGHIGKLMNOPQRSTUVWXYZ'
  while shift >= len( alphabet ):
    shift -= len( alphabet )
  else:
    res = '' # initialise empty string result
    for char in text: # iterate over each character from the input text
      index = alphabet.find( char.capitalize() ) # Find character in the alphabet 
      if index > -1:
        enc_index = index + shift

        # Adjust the encouding index if greated than the alphabet length
        while enc_index >= len( alphabet ):
          enc_index -= len( alphabet )
        # Adgust the encouding index if less than the negative alphabet length
        while enc_index <= -len( alphabet ):
          enc_index += len( alphabet )

        res += alphabet[ enc_index ]
      else:
        res += char
    return res

"""
  Define custom exception to catch key values out of range error
"""
class KeyOutOfRange( Exception ):
  def __init__( self , key ):
      self.message = f"Key value of {key} is out of range! It must be between 0 and 26."
      super().__init__( self.message )

"""
  Procedure to handle encryption choice dialog and input validation
"""
def choice_encrypt():
  print( '\n\t### Encryption ###\n' )
  try: # Generic error handling
    key = int( input( '\tPlease enter the key (0 to 26) to use.\n\t> ' ) )
    if key > 26 or key <0: # Validate the key value
      raise KeyOutOfRange( key=key )
    msg = input( '\tEnter the message to encrypt.\n\t> ' )
    print( f'\t{ shift_string( msg , key ) }' )
  except Exception as e:
    print( '\tSorry, your input was not valid!' )
    print( f'\t{e}' ) # Print details of errors

"""
  Procedure to handle decryption choice dialog and input validation
"""
def choice_decrypt():
  print( '\n\t### Decryption ###\n' )
  try: # Generic error handling
    key = int( input( '\tPlease enter the key (0 to 26) to use.\n\t> ' ) )
    if key > 26 or key <0: # Validate the key value
      raise KeyOutOfRange( key=key )
    msg = input( '\tEnter the message to decrypt.\n\t> ' )
    # Decription is the opposite of encription, hence will use negative key value
    print( f'\t{ shift_string( msg , -key ) }')
  except Exception as e:
    print( '\tSorry, your input was not valid!' )
    print( f'\t{e}' ) # Print details of errors

"""
  Procedure to handle quit choice
"""
def choice_quit():
  global quit
  print( '\n\t### CLOSEING OUT ###\n' )
  print( '\n\tThank you and good bye!\n' )
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
  'q': choice_quit
}

####################
# MAIN APP
####################

quit = False # Initilise main app loop control value

print( '########################' )
print( '### Cesar Cipher App ###' )
print( '########################' )

# Start main app loop
while not quit:
  choice = input( '\nPlease select (e)ncrypt, (d)ecrypt or (q)uit :' )
  if choice.lower() in menu: # Check if choice is valid
    menu[ choice.lower() ]() # Call respective procedure
  else:
    print( f"\nSorry, I do not recognise your choice '{choice}'! Please try again." )

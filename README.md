# ceaser-cipher
A learning project in Python to create a text user interface Ceaser Cipher application.

## Description of the task
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It encrypts letters by shifting them over by a certain number of places in the alphabet. We call the length of shift the key. For example, if the key is 3, then A becomes D, B becomes E, C becomes F, and so on. To decrypt the message, you must shift the encrypted letters in the opposite direction. This program lets the user encrypt and decrypt messages according to this algorithm.

When you run the code, the output will look like this:

-------------------------------------

Do you want to (e)ncrypt or (d)ecrypt?

> e

Please enter the key (0 to 25) to use.

> 4

Enter the message to encrypt.

> Meet me by the rose bushes tonight.

QIIX QI FC XLI VSWI FYWLIW XSRMKLX.

-------------------------------------

Do you want to (e)ncrypt or (d)ecrypt?

> d

Please enter the key (0 to 26) to use.

> 4

Enter the message to decrypt.

> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.

MEET ME BY THE ROSE BUSHES TONIGHT.

## Ceaser cipher cracker
The program can hack messages encrypted with the Caesar cipher, even if the key is unknown. There are only 26 possible keys for the Caesar cipher, so a computer can easily try all possible decryptions and display the results to the user. In cryptography, we call this technique a brute-force attack.

## Additional task
The brute-force code-cracker will use English dictionary words to guess the best key.

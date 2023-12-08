<br><h1>Premise of the challenge:</h1></br>

![image](https://github.com/Aer0Sol/TUCTF_writeups/assets/112194832/34144205-c311-4496-8959-63bbaca1c88a)

It starts with a simple menu-driven program running on a remote server that takes a plaintext, perfoms some form of encryption, gives you back the ciphertext and vice versa. The flag is given as a ciphertext which we are expected to decipher using the appropriate key.
The challenge provides us with the source code with some parts redacted, mainly the Pattern and revPattern along with the Key.

<br><h1>The vulnerability:</h1></br>

The main vulnerability stems from the fact that the server doesn't have a limit to how much requests a client can send, combined that with the fact the encryption uses XOR which is reversible, it leaves an oppurtunity for the attacker to figure out the scramble pattern and reverse the functionality of Encrypt() and Decrypt().

<br><h1>The Exploit:</h1></br> 



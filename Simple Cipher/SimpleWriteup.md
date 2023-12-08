<br><h1>Premise of the challenge:</h1></br>
![image](https://github.com/Aer0Sol/TUCTF_writeups/assets/112194832/34144205-c311-4496-8959-63bbaca1c88a)

It starts with a simple menu-driven program running on a remote server that takes a plaintext, perfoms some form of encryption, gives you back the ciphertext and vice versa. The flag is given as a ciphertext which we are expected to decipher using the appropriate 48 bit key.
The challenge provides us with the source code with some parts redacted, mainly the Pattern and revPattern along with the 48 bit Key.

<br><h1>The Vulnerability:</h1></br>
The main vulnerability stems from the fact that the server doesn't have a limit to how much requests a client can send, combined that with the fact the encryption uses XOR which is reversible, it leaves an oppurtunity for the attacker to figure out the scramble pattern and reverse the functionality of encrypt() and decrypt().

<br><h1>The Exploit:</h1></br> 
<h3>We start with reversing the functionality of encrypt():</h3>

The main functionality of encrypt() comes from pad(), xor(), substitution. pad() is straightforward just like xor()
encrypt() does substitution() then xor(), we give the 48 bit binary key as all zeros to make the xor() redundant and thus receiving the subsituted text as the ciphertext.
since by principle xor() doesn't happen, we can deduce the substitution by sending a 48 bit plaintext each varying by containing a '1' at any one of the 0-47 indices possible. We then note the index of the '1' in ciphertext and append that to a list to successfully recreate 'Pattern'





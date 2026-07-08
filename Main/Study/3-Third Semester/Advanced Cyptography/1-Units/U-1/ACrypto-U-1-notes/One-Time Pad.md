#third-semester #advanced-cryptography 
## How Decryption Works in One-Time Pad

Decryption uses the **same secret key** that was used for encryption.

If letters are converted as:

* A=0, B=1, C=2 ... Z=25

Then:

* **Encryption:** $C=(P+K)\bmod26$
* **Decryption:** $P=(C-K)\bmod26$

Where:

* $P$ = Plaintext
* $C$ = Ciphertext
* $K$ = Key

---

## Example

Plaintext:

`HELLO`

Convert:

* H=7
* E=4
* L=11
* L=11
* O=14

Key:

`XMCKL`

Convert:

* X=23
* M=12
* C=2
* K=10
* L=11

---

## Encryption

Add mod 26:

* $(7+23)=30 \to 4 = E$
* $(4+12)=16 = Q$
* $(11+2)=13 = N$
* $(11+10)=21 = V$
* $(14+11)=25 = Z$

Ciphertext = **EQNVZ**

---

## Decryption

Ciphertext = `EQNVZ`

Convert:

* E=4
* Q=16
* N=13
* V=21
* Z=25

Now subtract key mod 26:

* $(4-23)=-19 \to 7 = H$
* $(16-12)=4 = E$
* $(13-2)=11 = L$
* $(21-10)=11 = L$
* $(25-11)=14 = O$

Recovered plaintext = **HELLO**

---

## Important Rule for Negative Numbers

If result is negative, add 26.

Example:

$4-23=-19$

$-19+26=7$

So 7 = H

---

## Easy Memory Trick

Encryption = **Add key**
Decryption = **Subtract key**

---

## Why Same Key Works

The key shifts letters during encryption, then subtracting reverses that exact shift.

Like:

* Lock = move forward
* Unlock = move backward

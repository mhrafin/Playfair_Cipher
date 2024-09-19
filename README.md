## Features

- **Encode**: Encrypts plain text using the Playfair cipher algorithm.
- **Decode**: Decrypts cipher text back into plain text.
- Automatically handles special cases like repeated letters and odd-length strings.
- Option to remove extra `x` characters inserted during encryption (not recommended).
- Considers `i` and `j` as interchangeable in the key table.

## How It Works

The program:

- Prompts the user for a mode: **Encode**, **Decode**, or **Quit**.
- Accepts a keyword to generate a key table and uses it to encrypt or decrypt the input.
- Uses 5x5 key table to find letter pairs and applies appropriate Playfair Cipher rules:
  - **Same Row**: Shifts letters to the right for encryption and left for decryption.
  - **Same Column**: Shifts letters down for encryption and up for decryption.
  - **Rectangle**: Swaps column positions of the letters in different rows/columns.

## How to Use

### Encryption (Encode)

1. Run the program and select the option to **Encode (e)**.
2. Enter your plain text (alphabets only).
3. Enter your keyword (which is used to generate the cipher's key table).
4. The program will output the encrypted text.

### Decryption (Decode)

1. Run the program and select the option to **Decode (d)**.
2. Enter your cipher text.
3. Enter the keyword used during encryption.
4. The program will output the decrypted plain text.

### Quitting

- You can exit the program anytime by choosing the **Quit (q)** option.

## Installation

1. Clone the repository:
```git clone https://github.com/mhrafin/Playfair_Cipher.git```
2. Navigate to the project folder:
```cd Playfair_Cipher```
3. Run the game:
```python playfair_cipher.py```

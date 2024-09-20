ALPHABETS = "abcdefghijklmnopqrstuvwxyz"

KEY_TABLE = ([], [], [], [], [])


def main():
    """
    The main function of the playfair cipher program. It prints an ASCII art
    logo, asks the user for a mode (encode or decode), takes input according to
    the mode, and prints the result. The user can choose to quit at any time.
    """
    print(r"""
 ___   _      __    _     ____   __    _   ___       __    _   ___   _     ____  ___  
| |_) | |    / /\  \ \_/ | |_   / /\  | | | |_)     / /`  | | | |_) | |_| | |_  | |_) 
|_|   |_|__ /_/--\  |_|  |_|   /_/--\ |_| |_| \     \_\_, |_| |_|   |_| | |_|__ |_| \ 
""")

    mode = ""
    mode = input("\nEncode(e) or Decode(d) or Quit(q): ").lower()

    while mode != "q":
        if mode == "e":
            cipher_text = ""
            plain_text = input("Enter your plain text: ").lower().replace(" ", "")

            not_al = False
            for chr in plain_text:
                if chr not in ALPHABETS:
                    print("Only Alphabets Allowed. Try Again.")
                    not_al = True
                    mode = input("\nEncode(e) or Decode(d) or Quit(q): ").lower()
                    break
            if not_al:
                continue

            keyword = input("Enter your keyword: ").lower().replace(" ", "")

            global KEY_TABLE
            KEY_TABLE = ([], [], [], [], [])

            key_table_setter(keyword)
            key_table_setter(ALPHABETS)
            # print(KEY_TABLE)

            diagram = make_diagram(plain_text)
            # print(diagram)

            for part in diagram:
                for place, letter in enumerate(part):
                    position = find_letter_position(letter, KEY_TABLE)
                    if place == 0:
                        first_letter_row, first_letter_column = position
                        # print(f"First: {first_letter_row},{first_letter_column}")
                    if place == 1:
                        second_letter_row, second_letter_column = position
                        # print(f"Second: {second_letter_row},{second_letter_column}")
                        if first_letter_column == second_letter_column:
                            # print("hello")
                            cipher_text += same_column(
                                first_letter_row,
                                first_letter_column,
                                second_letter_row,
                                second_letter_column,
                                "encrypt",
                            )
                            # print(cipher_text)
                        elif first_letter_row == second_letter_row:
                            # print("hello")
                            cipher_text += same_row(
                                first_letter_row,
                                first_letter_column,
                                second_letter_row,
                                second_letter_column,
                                "encrypt",
                            )
                            # print(cipher_text)
                        else:
                            # print("hello")
                            cipher_text += different_pos(
                                first_letter_row,
                                first_letter_column,
                                second_letter_row,
                                second_letter_column,
                            )
                            # print(cipher_text)

            print(f"Your Cipher Text: {cipher_text}\n")
            mode = input("\nEncode(e) or Decode(d) or Quit(q): ").lower()
        elif mode == "d":
            plain_text = ""
            cipher_text = input("Enter your cipher text: ").lower().replace(" ", "")

            not_al = False
            for chr in cipher_text:
                if chr not in ALPHABETS:
                    print("Only Alphabets Allowed. Try Again.")
                    not_al = True
                    mode = input("\nEncode(e) or Decode(d) or Quit(q): ").lower()
                    break
            if not_al:
                continue

            keyword = input("Enter your keyword: ").lower().replace(" ", "")

            KEY_TABLE = ([], [], [], [], [])

            key_table_setter(keyword)
            key_table_setter(ALPHABETS)
            # print(KEY_TABLE)

            diagram = make_diagram(cipher_text)

            for part in diagram:
                for place, letter in enumerate(part):
                    position = find_letter_position(letter, KEY_TABLE)
                    if place == 0:
                        first_letter_row, first_letter_column = position
                        # print(f"First: {first_letter_row},{first_letter_column}")
                    if place == 1:
                        second_letter_row, second_letter_column = position
                        # print(f"Second: {second_letter_row},{second_letter_column}")
                        if first_letter_column == second_letter_column:
                            # print("hello")
                            plain_text += same_column(
                                first_letter_row,
                                first_letter_column,
                                second_letter_row,
                                second_letter_column,
                                "decrypt",
                            )
                            print(plain_text)
                        elif first_letter_row == second_letter_row:
                            # print("hello")
                            plain_text += same_row(
                                first_letter_row,
                                first_letter_column,
                                second_letter_row,
                                second_letter_column,
                                "decrypt",
                            )
                            print(plain_text)
                        else:
                            # print("hello")
                            plain_text += different_pos(
                                first_letter_row,
                                first_letter_column,
                                second_letter_row,
                                second_letter_column,
                            )
                            print(plain_text)

            remove_x = input(
                "(Not Recommended) Do you want to remove x? Yes(y) or No(n)\n"
            ).lower()
            if remove_x == "y":
                plain_text = plain_text.replace("x", "")

            print(f"Your Plain Text (Considered i): {plain_text}\n")
            mode = input("\nEncode(e) or Decode(d) or Quit(q): ").lower()
        else:
            print("Quitting")
            break


def key_table_setter(letters):
    """
    Populates the KEY_TABLE with the given letters.

    The letters are distributed row-wise in the KEY_TABLE. If a letter is already
    present in the KEY_TABLE, it is skipped. If the current row is full, then the
    next row is used. If the letter is either "i" or "j", then it is replaced with
    "i/j".

    Parameters
    ----------
    letters : str
        The letters to be used to populate the KEY_TABLE
    """
    row = 0
    for letter in letters:
        if letter == "i" or letter == "j":
            if in_key_table("i/j"):
                continue
            else:
                KEY_TABLE[row].append("i/j")
                continue

        if len(KEY_TABLE[row]) < 5 and not in_key_table(letter):
            KEY_TABLE[row].append(letter)
        elif not in_key_table(letter):
            row += 1
            KEY_TABLE[row].append(letter)
        # print(key_table)


def in_key_table(letter):
    """
    Checks if the given letter is present in the KEY_TABLE.

    Parameters
    ----------
    letter : str
        The letter to be searched in the KEY_TABLE

    Returns
    -------
    bool
        True if the letter is present in the KEY_TABLE, else False
    """
    for row in range(5):
        if letter in KEY_TABLE[row]:
            return True
    return False


def find_letter_position(letter, key_table):
    """
    Finds the position of a letter in the given key_table.

    Parameters
    ----------
    letter : str
        The letter to be searched in the key_table
    key_table : list of lists
        The 5x5 table containing the letters

    Returns
    -------
    tuple or None
        The position of the letter as a tuple (row, column) if found, else None
    """
    for row, r in enumerate(key_table):
        for col, c in enumerate(r):
            if (letter in ["i", "j"] and c == "i/j") or letter == c:
                return row, col
    return None  # Letter not found


def make_diagram(text):
    """
    Splits the given text into a diagram of letter pairs.

    Each pair in the diagram is a list of two letters. If two letters are the same, an 'x' is inserted in between them and the next pair is created. If the length of the text is odd, the last pair will have an 'x' appended to it.

    Parameters
    ----------
    text : str
        The text to be split into a diagram

    Returns
    -------
    list of lists
        The diagram of letter pairs
    """
    first = 0
    second = 1
    diagram = []
    for _ in range(int(len(text))):
        try:
            if text[first] != text[second]:
                diagram_part = [text[first], text[second]]
                first += 2
                second += 2
                diagram.append(diagram_part)
                # print(diagram)
            else:
                diagram_part = [text[first], "x"]
                first += 1
                second += 1
                diagram.append(diagram_part)
                # print(diagram)
        except IndexError:
            try:
                diagram_part = [text[first], "x"]
                diagram.append(diagram_part)
                # print(diagram)
                break
            except IndexError:
                break
    print(diagram)
    return diagram


def same_column(first_r, first_c, second_r, second_c, crypt_mode):
    """
    Encrypts or decrypts two letters in the same column of the key table.

    If the first letter is at the bottom of the column, it wraps around to the top of the column. If the second letter is at the bottom of the column, it wraps around to the top of the column.

    Parameters
    ----------
    first_r : int
        The row of the first letter
    first_c : int
        The column of the first letter
    second_r : int
        The row of the second letter
    second_c : int
        The column of the second letter
    crypt_mode : str
        The mode of operation: "encrypt" or "decrypt"

    Returns
    -------
    str
        The encrypted or decrypted letters
    """
    cipher_part = ""

    en, de = 1, 1
    if crypt_mode == "encrypt":
        en = -1
    elif crypt_mode == "decrypt":
        de = -1

    if (first_r == 4 and crypt_mode == "encrypt") or (
        first_r == 0 and crypt_mode == "decrypt"
    ):
        cipher_part += (
            "i"
            if "i/j" in KEY_TABLE[first_r + (4 * en)][first_c]
            else KEY_TABLE[first_r + (4 * en)][first_c]
        )
        cipher_part += (
            "i"
            if "i/j" in KEY_TABLE[second_r + (1 * de)][second_c]
            else KEY_TABLE[second_r + (1 * de)][second_c]
        )
    elif (second_r == 4 and crypt_mode == "encrypt") or (
        second_r == 0 and crypt_mode == "decrypt"
    ):
        cipher_part += (
            "i"
            if "i/j" in KEY_TABLE[first_r + (1 * de)][first_c]
            else KEY_TABLE[first_r + (1 * de)][first_c]
        )
        cipher_part += (
            "i"
            if "i/j" in KEY_TABLE[second_r + (4 * en)][second_c]
            else KEY_TABLE[second_r + (4 * en)][second_c]
        )
    else:
        cipher_part += (
            "i"
            if "i/j" in KEY_TABLE[first_r + (1 * de)][first_c]
            else KEY_TABLE[first_r + (1 * de)][first_c]
        )
        cipher_part += (
            "i"
            if "i/j" in KEY_TABLE[second_r + (1 * de)][second_c]
            else KEY_TABLE[second_r + (1 * de)][second_c]
        )
    return cipher_part


def same_row(first_r, first_c, second_r, second_c, crypt_mode):
    """
    Encrypts two letters in the same row of the key table.

    If the first letter is at the end of the row, it wraps around to the start of the row. If the second letter is at the end of the row, it wraps around to the start of the row.

    Parameters
    ----------
    first_r : int
        The row of the first letter
    first_c : int
        The column of the first letter
    second_r : int
        The row of the second letter
    second_c : int
        The column of the second letter
    crypt_mode : str
        The mode of operation: "encrypt" or "decrypt"

    Returns
    -------
    str
        The encrypted letters
    """
    cipher_part = ""

    en, de = 1, 1
    if crypt_mode == "encrypt":
        en = -1
    elif crypt_mode == "decrypt":
        de = -1

    if (first_c == 4 and crypt_mode == "encrypt") or (
        first_c == 0 and crypt_mode == "decrypt"
    ):
        cipher_part += (
            "i"
            if "i/j" in KEY_TABLE[first_r][first_c + (4 * en)]
            else KEY_TABLE[first_r][first_c + (4 * en)]
        )
        cipher_part += (
            "i"
            if "i/j" in KEY_TABLE[second_r][second_c + (1 * de)]
            else KEY_TABLE[second_r][second_c + (1 * de)]
        )
    elif (second_c == 4 and crypt_mode == "encrypt") or (
        second_c == 0 and crypt_mode == "decrypt"
    ):
        cipher_part += (
            "i"
            if "i/j" in KEY_TABLE[first_r][first_c + (1 * de)]
            else KEY_TABLE[first_r][first_c + (1 * de)]
        )
        cipher_part += (
            "i"
            if "i/j" in KEY_TABLE[second_r][second_c + (4 * en)]
            else KEY_TABLE[second_r][second_c + (4 * en)]
        )
    else:
        cipher_part += (
            "i"
            if "i/j" in KEY_TABLE[first_r][first_c + (1 * de)]
            else KEY_TABLE[first_r][first_c + (1 * de)]
        )
        cipher_part += (
            "i"
            if "i/j" in KEY_TABLE[second_r][second_c + (1 * de)]
            else KEY_TABLE[second_r][second_c + (1 * de)]
        )
    return cipher_part


def different_pos(first_r, first_c, second_r, second_c):
    """
    Encrypts two letters which are in different rows and columns of the key table.

    Parameters:
    first_r (int): The row of the first letter
    first_c (int): The column of the first letter
    second_r (int): The row of the second letter
    second_c (int): The column of the second letter

    Returns:
        The encrypted letters
    """
    part = ""
    part += (
        "i" if "i/j" in KEY_TABLE[first_r][second_c] else KEY_TABLE[first_r][second_c]
    )
    part += (
        "i" if "i/j" in KEY_TABLE[second_r][first_c] else KEY_TABLE[second_r][first_c]
    )
    return part


if __name__ == "__main__":
    main()

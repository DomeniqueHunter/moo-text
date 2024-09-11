import random


def str_2_moo(text: str) -> str:
    """
    Encode a text string to a 'moo' encoding with complex rules.

    Args:
        text: The text string to encode.

    Returns:
        The encoded 'moo' string.
    """
    encoded_string = []

    for char in text:
        ascii_value = ord(char)
        binary_string = f"{ascii_value:08b}"  # Convert to 8-bit binary representation

        moo_string = ""
        for bit in binary_string:
            if bit == '0':
                moo_string += random.choice(['moo ', 'mooo '])  # Quiet versions for '0'
            else:
                moo_string += random.choice(['moo! ', 'mooo! '])  # Loud versions for '1'

        encoded_string.append(moo_string)

    return ''.join(encoded_string)


def moo_2_str(moo_text: str) -> str:
    """
    Decode a 'moo' encoded string back to the original text.

    Args:
        moo_text: The 'moo' encoded string.

    Returns:
        The decoded text string.
    """
    decoded_text = []
    moo_list = moo_text.strip().split(' ')  # Split by spaces to get individual 'moo' sequences

    for i, moo_char in enumerate(moo_list):
        binary_string = ""

        # Identify the correct pattern for each moo sequence
        if moo_char == 'moo':
            binary_string = '0'
        elif moo_char == 'mooo':
            binary_string = '0'
        elif moo_char == 'moo!':
            binary_string = '1'
        elif moo_char == 'mooo!':
            binary_string = '1'
        else:
            # Debug output for identifying the issue
            print(f"Unexpected pattern: {moo_char} at {moo_list[i]}")
            raise ValueError("Invalid encoding found in moo string!")

        decoded_text.append(binary_string)

    # Convert the full binary string to characters
    ascii_chars = [chr(int(''.join(decoded_text[i:i + 8]), 2)) for i in range(0, len(decoded_text), 8)]

    return ''.join(ascii_chars)


def main() -> None:
    text = "Hello, World!"
    encoded = str_2_moo(text)
    print(f"Encoded: {encoded}")

    decoded = moo_2_str(encoded)
    print(f"Decoded: {decoded}")


if __name__ == "__main__":
    main()

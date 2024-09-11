import random


def moo(small:bool=True, nr_o:int=2, loud:bool=False) -> str:
    """
    Generate a 'moo' encoded string based on the parameters.
    
    Args:
        small: Whether the 'm' is lowercase or uppercase.
        nr_o: Number of 'o's.
        loud: Whether the string ends with '!'.
        
    Returns:
        The generated 'moo' string.
    """
    m = "m" if small else "M"
    oo = "o" * nr_o
    loud = "!" if loud else ""
    
    return f"{m}{oo}{loud}"
    
    
def unmoo(text:str) -> int:
    """
    Decode a 'moo' encoded string to an integer value.

    Args:
        text: The 'moo' encoded string.

    Returns:
        The decoded integer value.
    """
    m = 0 if text.startswith('m') else 8
    oo = text.count("o") - 2
    loud = 4 if text.endswith("!") else 0
    
    return m + oo + loud    


def str_2_moo(text:str) -> str:
    """
    Encode a text string to a 'moo' encoding with complex rules.

    Args:
        text: The text string to encode.

    Returns:
        The encoded 'moo' string.
    """
    encoded_string = []
    
    moo_symbols = ["moo", ]
    
    hex_str = text.encode("utf-8").hex()
    
    for symbol in hex_str:
        match symbol:
            case "0": moo_symbol = moo(True, 2, False)
            case "1": moo_symbol = moo(True, 3, False)
            case "2": moo_symbol = moo(True, 4, False)
            case "3": moo_symbol = moo(True, 5, False)
            case "4": moo_symbol = moo(True, 2, True)
            case "5": moo_symbol = moo(True, 3, True)
            case "6": moo_symbol = moo(True, 4, True)
            case "7": moo_symbol = moo(True, 5, True)
            
            case "8": moo_symbol = moo(False, 2, False)
            case "9": moo_symbol = moo(False, 3, False)
            case "a": moo_symbol = moo(False, 4, False)
            case "b": moo_symbol = moo(False, 5, False)
            case "c": moo_symbol = moo(False, 2, True)
            case "d": moo_symbol = moo(False, 3, True)
            case "e": moo_symbol = moo(False, 4, True)
            case "f": moo_symbol = moo(False, 5, True)
        
        encoded_string.append(moo_symbol)  

    return ' '.join(encoded_string)


def moo_2_str(moo_text:str) -> str:
    """
    Decode a 'moo' encoded string back into the original text.
    
    Args:
        moo_text: The 'moo' encoded string.
        
    Returns:
        The decoded text string.
    """
    # Split the moo_text into individual moo symbols
    moo_symbols = moo_text.split()
    
    # Recreate the hex string by decoding each moo symbol using unmoo
    hex_string = []
    
    for moo_symbol in moo_symbols:
        # Decode the moo symbol to a hex value
        hex_value = unmoo(moo_symbol)
        # Convert the hex value to a single hexadecimal digit and append
        hex_string.append(f"{hex_value:1x}")
    
    # Convert the reconstructed hex string back to a text string
    hex_str = ''.join(hex_string)
    decoded_text = bytes.fromhex(hex_str).decode('utf-8')
    
    return decoded_text
    


def main() -> None:
    text = "Hello, World!"
    encoded = str_2_moo(text)
    print(f"Encoded: {encoded}")

    decoded = moo_2_str(encoded)
    print(f"Decoded: {decoded}")
    


if __name__ == "__main__":
    main()
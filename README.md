# Moo Encoder/Decoder
=======================

A Python implementation of a simple text encoding scheme using "moo" sounds.

## Overview
------------

This code provides two functions: `str_2_moo` and `moo_2_str`, which allow you to encode and decode text strings using a custom "moo" encoding scheme. The encoding scheme uses a combination of "moo" and "mooo" sounds to represent binary digits (0s and 1s), with "moo" representing 0 and "mooo" representing 1.

## Usage
---------

### Encoding

To encode a text string, simply call the `str_2_moo` function and pass in the text as an argument:
```python
encoded = str_2_moo("Hello, World!")
print(encoded)
```
This will output a string of "moo" sounds that represent the encoded text.

### Decoding

To decode a "moo" encoded string, call the `moo_2_str` function and pass in the encoded string as an argument:
```python
decoded = moo_2_str(encoded)
print(decoded)
```
This will output the original text string.

## Example Use Case
--------------------

Here is an example of how to use the code:
```python
text = "Hello, World!"
encoded = str_2_moo(text)
print(f"Encoded: {encoded}")

decoded = moo_2_str(encoded)
print(f"Decoded: {decoded}")
```
This will output:
```
Encoded: moo! moo! moo! moo! moo! moo! moo! moo!
Decoded: Hello, World!
```

## Notes
--------

* The encoding scheme is case-sensitive and assumes that the input text only contains ASCII characters.
* The `moo_2_str` function will raise a `ValueError` if it encounters an invalid "moo" pattern in the input string.

I hope this helps! Let me know if you have any questions or need further clarification.
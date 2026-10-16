# text-encoder-decoder
A beginner Python project demonstrating Base64 encoding, decoding, and error handling
# Text Encoder and Decoder

## Project Overview
This is a beginner-friendly cybersecurity project built with Python. It demonstrates how text can be encoded into Base64 format and decoded back into its original form.

The program also includes basic error handling to respond to invalid Base64 input and incorrect menu choices.

## Objectives
- Understand the difference between encoding and encryption.
- Learn how Base64 encoding and decoding work.
- Practise Python input handling and conditional statements.
- Implement basic error handling.
- Understand why encoding alone does not provide security.

## Tools and Technologies
- **Programming language:** Python 3
- **Libraries:** `base64` and `binascii` (Python standard library)
- **Code editor:** Visual Studio Code
- **Operating environment:** Linux or another system with Python installed

## Features
1. Encodes user-provided text into Base64.
2. Decodes valid Base64 input into readable UTF-8 text.
3. Handles invalid Base64 input and decoding errors.
4. Rejects invalid menu selections.

## How to Run the Project

1. Install Python 3 if it is not already installed.
2. Download or clone this repository.
3. Open a terminal in the project directory.
4. Run the following command:

```bash
python3 encoder.py
```

5. Choose an option from the menu and follow the prompts.

## Example

**Input:**
```text
Hello
```

**Encoded output:**
```text
SGVsbG8=
```

**Decoded input:**
```text
SGVsbG8=
```

**Decoded output:**
```text
Hello
```

## Testing and Results

The following tests were performed:

- Valid text was successfully encoded.
- Valid Base64 text was successfully decoded.
- Invalid Base64 input produced an error message.
- Invalid menu selections were rejected.

The program passed these tests during development.

## Cybersecurity Lessons Learned

- Base64 is an encoding method, not an encryption algorithm.
- Encoded information can be decoded without a secret key.
- Encryption and encoding serve different purposes.
- Error handling improves program reliability.
- Input validation helps a program respond appropriately to unexpected data.

## Security Limitations

This project is educational and is not intended to protect confidential information.

Base64 does not provide confidentiality, authentication, or integrity protection. The program's basic input checks also do not establish that decoded content is trustworthy.

Sensitive information should be protected using appropriate cryptographic methods rather than Base64 encoding alone.

## Future Improvements

- Add a repeat-operation menu.
- Improve input validation and user-friendly error messages.
- Add automated tests.
- Support encoding and decoding text files.

## Author
Created as a beginner Python and cybersecurity learning project.

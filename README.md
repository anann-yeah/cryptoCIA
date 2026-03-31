Custom Running Key Hash Algorithm
A Python-based cryptographic tool that implements a custom hashing algorithm. Unlike standard hashes (like SHA-256), this project explores the concept of a Running Key Cipher combined with bitwise operations to create a unique, one-way 16-byte (32-character) hexadecimal hash.

Features
Running Key Integration: Blends the input message with a repeating key to ensure high entropy.

Avalanche Effect: Uses bitwise left-shifts and XOR operations to ensure that changing a single character in the input results in a completely different hash output.

Interactive Terminal: Includes a built-in loop to test multiple strings without restarting the script.

Fixed Output: Always produces a 32-character hex string, regardless of input length.

How It Works
Mixing: The input string is converted to bytes and added to a "Running Key" (CRYPTOGRAPHYISFASCINATING).

Compression: The resulting bytes are folded into a fixed 16-byte state initialized with prime numbers.

Diffusion: Every byte in the state is blended with the previous byte to ensure that the influence of every input character spreads across the entire hash.

Enter any text when prompted. Type exit to close the program.

Project Development Prompts
This project was developed through a structured AI-collaborative process. Below are the prompts used to design, debug, and finalize the implementation:

The Core Logic: "Can you write a custom hash algorithm in Python that uses a Running Key Cipher concept? It needs to take a string message, mix it with a running key, use bitwise operations to create an avalanche effect, and output a fixed 32-character hexadecimal hash."

Developed by: Anannya

Course: CSE(Iot) - Cryptography Assignment CIA.
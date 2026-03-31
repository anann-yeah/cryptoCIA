def run_hash(message: str, running_key_text: str = "CRYPTOGRAPHYISFASCINATING") -> str:
    """
    A custom Hash Algorithm using a Running Key Cipher concept.
    Produces a fixed 32-character (16-byte) hexadecimal hash.
    """
    
    # Define our fixed output size (16 bytes)
    HASH_SIZE = 16
    
    # 1. Convert strings to byte arrays for mathematical operations
    msg_bytes = bytearray(message.encode('utf-8'))
    
    # If the message is empty, return a default hash
    if len(msg_bytes) == 0:
        return "00" * HASH_SIZE

    # Repeat the running key text so it is at least as long as the message
    while len(running_key_text) < len(message):
        running_key_text += running_key_text
    
    key_bytes = bytearray(running_key_text.encode('utf-8'))[:len(msg_bytes)]
    
    # ---------------------------------------------------------
    # STEP 1: THE RUNNING KEY CIPHER (Mixing)
    # ---------------------------------------------------------
    # We add the message bytes and key bytes together (modulo 256)
    cipher_bytes = bytearray(len(msg_bytes))
    for i in range(len(msg_bytes)):
        cipher_bytes[i] = (msg_bytes[i] + key_bytes[i]) % 256

    # ---------------------------------------------------------
    # STEP 2: THE COMPRESSION & AVALANCHE (Making it a one-way Hash)
    # ---------------------------------------------------------
    # Initialize a fixed 16-byte state with some arbitrary prime numbers
    hash_state = bytearray([11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71])
    
    # Fold the arbitrary-length cipher_bytes into the 16-byte hash_state
    for i, byte in enumerate(cipher_bytes):
        # Determine which of the 16 bytes in our state to target
        idx = i % HASH_SIZE
        
        # Bitwise Left Shift (<< 1) and Bitwise OR (|) to rotate bits
        # This scrambles the data, creating the "Avalanche Effect"
        hash_state[idx] = ((hash_state[idx] << 1) | (hash_state[idx] >> 7)) & 0xFF
        
        # XOR (^=) the cipher byte into the hash state
        hash_state[idx] ^= byte
        
    # ---------------------------------------------------------
    # STEP 3: FINAL DIFFUSION
    # ---------------------------------------------------------
    # Make sure every byte affects the next byte so the whole hash is blended
    for i in range(1, HASH_SIZE):
        hash_state[i] = (hash_state[i] + hash_state[i-1]) % 256
        
    # Return the final byte array as a clean Hexadecimal string
    return hash_state.hex()


# ==========================================
# Testing the Algorithm (Interactive Mode)
# ==========================================
if __name__ == "__main__":
    print("\n--- Custom Hash Algorithm Interactive Tester ---")
    print("Type 'exit' or 'quit' to stop the program.")
    
    while True:
        # Get input from the user
        user_msg = input("\nEnter your message: ")
        
        # Check if the user wants to close the program
        if user_msg.lower() in ['exit', 'quit']:
            print("Exiting hash tester...")
            break
            
        # Generate the hash using your function
        result_hash = run_hash(user_msg)
        
        # Print the final output
        print(f"Your Hash: {result_hash}")
def caesar_cipher_decrypt(lines, k):
    """Decrypts a Caesar cipher with a given shift."""
    decrypted_message = []
    shift = 26 - k  # Decrypting requires shifting backwards
    
    for line in lines:
        decrypted_line = []
        for char in line:
            if 'A' <= char <= 'Z':  # Only decrypt uppercase letters
                # Shift the character and wrap around if necessary
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                decrypted_line.append(new_char)
            else:
                decrypted_line.append(char)  # Keep non-alphabet characters (like '.')
        decrypted_message.append("".join(decrypted_line))
    
    return " ".join(decrypted_message)


if __name__ == "__main__":
    # Input: number of lines and the shift value
    num_lines, k = map(int, input().split())
    
    # Read the encrypted lines
    encrypted_lines = [input().strip() for _ in range(num_lines)]
    
    # Decrypt the message
    decrypted_message = caesar_cipher_decrypt(encrypted_lines, k)
    
    # Output the decrypted message
    print(decrypted_message)

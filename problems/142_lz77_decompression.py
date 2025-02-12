def solve():
    hex_string = input()
    hex_bytes = hex_string.split()
    byte_list = [int(byte, 16) for byte in hex_bytes]

    decoded_text = ""
    i = 0
    while i < len(byte_list):
        if byte_list[i] == 0:
            decoded_text += chr(byte_list[i+1])
            i += 2
        else:
            combined = (byte_list[i] << 8) + byte_list[i+1]
            length = (combined >> 12) & 0xF
            offset = combined & 0xFFF
            start_index = len(decoded_text) - offset -1
            decoded_text += decoded_text[start_index:start_index+length]
            i += 2
            
    print(decoded_text)

if __name__ == "__main__":
    solve()
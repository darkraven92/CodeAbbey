def solve():
    encoding_table = {
        ' ': '11',         'e': '101',        't': '1001',      'o': '10001',
        'n': '10000',      'a': '011',        's': '0101',      'i': '01001',
        'r': '01000',      'h': '0011',       'd': '00101',     'l': '001001',
        '!': '001000',     'u': '00011',      'c': '000101',     'f': '000100',
        'm': '000011',     'p': '0000101',    'g': '0000100',    'w': '0000011',
        'b': '0000010',    'y': '0000001',    'v': '00000001',   'j': '000000001',
        'k': '0000000001', 'x': '00000000001','q': '000000000001','z': '000000000000'
    }

    text = input()
    bit_string = ""

    i = 0
    while i < len(text):
        if i < len(text) - 1 and text[i] == '!':
           bit_string += '001000'
           i += 1
           if text[i].lower() in encoding_table:
               bit_string += encoding_table[text[i].lower()]
           i += 1   
        elif text[i] in encoding_table:
             bit_string += encoding_table[text[i]]
             i += 1
        else:
             i += 1
             
    # Pad the bit string
    padding_needed = 8 - (len(bit_string) % 8) if len(bit_string) % 8 != 0 else 0
    bit_string += '0' * padding_needed

    byte_list = []
    for i in range(0, len(bit_string), 8):
        byte = bit_string[i:i+8]
        byte_list.append(hex(int(byte, 2))[2:].upper().zfill(2))

    print(" ".join(byte_list))

solve()
def check_and_decode_byte(byte):
  """Checks the parity of a byte and decodes it if valid.

  Args:
    byte: The byte as an integer.

  Returns:
    The decoded character if the byte is valid, otherwise None.
  """
  binary = bin(byte)[2:].zfill(8)
  bit_sum = sum(int(bit) for bit in binary)

  if bit_sum % 2 == 0:
    decoded_byte = int(binary[1:], 2)
    return chr(decoded_byte)
  else:
    return None


if __name__ == "__main__":
  encoded_bytes = list(map(int, input().split()))
  decoded_message = ""

  for byte in encoded_bytes:
    decoded_char = check_and_decode_byte(byte)
    if decoded_char:
      if decoded_char == '.':
        decoded_message += decoded_char
        break
      decoded_message += decoded_char
    else:
      continue # skip corrupted bytes

  print(decoded_message)
def caesar_decrypt(text, shift):
    """Decrypts a Caesar cipher encoded text.

    Args:
        text: The encrypted text.
        shift: The number of positions to shift back.

    Returns:
        The decrypted text.
    """
    decrypted_text = ""
    for char in text:
        if 'A' <= char <= 'Z':
            start = ord('A')
            shifted_char = chr((ord(char) - start - shift) % 26 + start)
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text


def calculate_letter_frequencies(text):
    """Calculates the frequencies of letters in a given text.

    Args:
        text: The input text (string).

    Returns:
        A dictionary where the keys are uppercase letters and the values are their frequencies.
    """
    frequencies = {}
    for char in text:
        if 'A' <= char <= 'Z':
            frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies


def calculate_chi_squared(observed_freq, expected_freq):
    """Calculates the chi-squared statistic between two frequency distributions.

    Args:
        observed_freq: A dictionary of observed letter frequencies.
        expected_freq: A dictionary of expected letter frequencies.

    Returns:
        The chi-squared value.
    """
    chi_squared = 0
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        observed = observed_freq.get(letter, 0)
        expected = expected_freq.get(letter, 0)
        if expected != 0:
            chi_squared += (observed - expected) ** 2 / expected
    return chi_squared


def crack_caesar_cipher(encrypted_text):
    """Cracks the Caesar cipher for a given encrypted text.

    Args:
        encrypted_text: The encrypted text (string).

    Returns:
      The decrypted first 3 words and key
    """
    expected_frequencies = {
        'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702, 'F': 2.228, 'G': 2.015,
        'H': 6.094, 'I': 6.966, 'J': 0.153, 'K': 0.772, 'L': 4.025, 'M': 2.406, 'N': 6.749,
        'O': 7.507, 'P': 1.929, 'Q': 0.095, 'R': 5.987, 'S': 6.327, 'T': 9.056, 'U': 2.758,
        'V': 0.978, 'W': 2.360, 'X': 0.150, 'Y': 1.974, 'Z': 0.074
    }

    best_shift = -1
    min_chi_squared = float('inf')
    for shift in range(1, 26):
        decrypted_text = caesar_decrypt(encrypted_text, shift)
        observed_frequencies = calculate_letter_frequencies(decrypted_text)
        chi_squared = calculate_chi_squared(observed_frequencies, expected_frequencies)

        if chi_squared < min_chi_squared:
             min_chi_squared = chi_squared
             best_shift = shift

    decrypted_text = caesar_decrypt(encrypted_text, best_shift)
    words = decrypted_text.split()
    first_three_words = " ".join(words[:3])
    return f"{first_three_words} {best_shift}"


if __name__ == "__main__":
    num_messages = int(input())
    results = []
    for _ in range(num_messages):
       encrypted_text = input()
       cracked_text = crack_caesar_cipher(encrypted_text)
       results.append(cracked_text)

    print(" ".join(results))
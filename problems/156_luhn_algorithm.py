def solve():
    num_cards = int(input())
    for _ in range(num_cards):
        card_number = input()
        fixed_card = fix_card_number(card_number)
        print(fixed_card, end=" ")
    print()

def calculate_checksum(card_number):
    """
    Calculates the Luhn checksum for a card number.
    """
    total = 0
    for i in range(len(card_number) - 1, -1, -1):
      digit = int(card_number[i])
      if (len(card_number) - 1 - i) % 2 == 1:
          digit *= 2
          if digit > 9:
              digit -= 9
      total += digit
    return total


def fix_card_number(card_number):
    """
    Fixes a card number with either a missing digit or a swapped pair.
    """
    if "?" in card_number:
      for i in range(10):
        temp_number = card_number.replace("?", str(i), 1)
        if calculate_checksum(temp_number) % 10 == 0:
          return temp_number
    else:
      for i in range(len(card_number) - 1):
        temp_number = list(card_number)
        temp_number[i], temp_number[i+1] = temp_number[i+1], temp_number[i]
        temp_number = "".join(temp_number)
        if calculate_checksum(temp_number) % 10 == 0:
            return temp_number
    return card_number

if __name__ == "__main__":
    solve()
def count_bits(value):
    # Mask the value to 32 bits
    value_32bit = value & 0xFFFFFFFF
    # Count the number of 1 bits
    return bin(value_32bit).count('1')

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # First line: number of values
    num_values = int(data[0])
    
    # Next line: values
    values = list(map(int, data[1:1 + num_values]))
    
    # Count bits for each value
    results = []
    for value in values:
        result = count_bits(value)
        results.append(str(result))
    
    # Print the results separated by spaces
    print(" ".join(results))

if __name__ == "__main__":
    main()
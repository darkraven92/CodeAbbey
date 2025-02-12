def brainfuck_interpreter(program, input_data):
    data = [0] * 30000  # Initialize data array
    pointer = 0  # Data pointer
    input_index = 0  # Input data index
    output = []  # Output list
    loop_stack = []  # Stack for loops

    i = 0
    while i < len(program):
        command = program[i]

        if command == '>':
            pointer += 1
        elif command == '<':
            pointer -= 1
        elif command == '+':
            data[pointer] = (data[pointer] + 1) % 256
        elif command == '-':
            data[pointer] = (data[pointer] - 1) % 256
        elif command == '.':
            output.append(chr(data[pointer]))
        elif command == ',':
            if input_index < len(input_data):
                data[pointer] = input_data[input_index]
                input_index += 1
        elif command == ';':
            if input_index < len(input_data):
                data[pointer] = input_data[input_index]
                input_index += 1
        elif command == ':':
            output.append(str(data[pointer]))
        elif command == '[':
            if data[pointer] == 0:
                # Find the matching ']'
                loop_count = 1
                while loop_count != 0:
                    i += 1
                    if program[i] == '[':
                        loop_count += 1
                    elif program[i] == ']':
                        loop_count -= 1
            else:
                loop_stack.append(i)
        elif command == ']':
            if data[pointer] != 0:
                i = loop_stack[-1] - 1
            else:
                loop_stack.pop()

        i += 1

    return ' '.join(output)


# Read input from the terminal
program = input("Enter Brainfuck++ program: ")
input_data = list(map(int, input("Enter input numbers (space-separated): ").split()))

# Run the interpreter
output = brainfuck_interpreter(program, input_data)
print("Output:", output)
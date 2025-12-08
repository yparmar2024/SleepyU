# Path to the input program file in GitHub repository
input_path = '../programs/demo_program.txt'

# Path to the output program file in GitHub repository
output_path = '../images/demo_instruction.hex'

# Path to the output memory file in GitHub repository
memory_path = '../images/demo_memory.hex'

# Function to convert number to binary string
def num_to_bin(num):
    bin_str = bin(num)[2:]
    remaining_bits = 2 - len(bin_str)
    return '0' * remaining_bits + bin_str

# Function to convert binary string to hexadecimal
def bin_to_hex(bin_str):
    num = int(bin_str, 2)
    remaining_hex = 2 - len(hex(num)[2:])
    return '0' * remaining_hex + hex(num)[2:]

# Open the input file and read its contents
with open(input_path, 'r') as file:
    program = file.read()
    instructions = program.split('\n')
    
    # Initialize a dictionary for SleepyU mnemonics
    mnemonics = {'ADD': 0, 'SUB': 1, 'LDR': 2, 'STR': 3}
    replacements = [',', 'X', '[', ']']

    # Fetch register values from the program
    opcodes = []
    for instruction in instructions:
        bin_str = ""
        for replacement in replacements:
            instruction = instruction.replace(replacement, '')
        keywords = instruction.upper().split()
        for keyword in keywords:
            if keyword in mnemonics:
                bin_str += num_to_bin(mnemonics[keyword])
            else:
                bin_str += num_to_bin(int(keyword))
        opcodes.append(bin_to_hex(bin_str))

# Open the output file and write its contents
with open(output_path, 'w') as file:
    # Write file format header
    file.write('v3.0 hex words addressed\n')

    # For each opcode, calculate its address and write to the file respectively
    for i, opcode in enumerate(opcodes):
        addresser = (i // 16) * 10
        addresser_hex = bin_to_hex(num_to_bin(addresser))
        if i % 16 == 0:
            file.write(f'{addresser_hex}: {opcode}')
        else:
            file.write(f' {opcode}')

# Open the output memory file and write its contents
with open(memory_path, 'w') as file:
    # Write file format header
    file.write('v3.0 hex words addressed\n')

    # Manually add initial memory values
    file.write('00: 05 0A 0F 14 19 1E 23 28 2D 32 37 3C 41 46 4B 50\n')

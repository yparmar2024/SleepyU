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
    lines = program.split('\n')
    
    # Initialize a dictionary for SleepyU mnemonics for scalability
    mnemonics = {'BOOST': 0, 'FALL': 1, 'FETCH': 2, 'TUCK': 3}

    # Initialize a dictionary for data types for scalability
    data_types = {'.byte': 8}

    # List of characters to be replaced in instructions
    replacements = [',', 'X', '[', ']']

    # Fetch register values from the program
    opcodes = []

    # Fetch data values from the program
    data_values = []

    # Declare the type of segment we are in
    state = ''
    for instruction in lines:
        # Strip of white spaces for proper parsing
        instruction = instruction.strip()

        # If the instruction is a comment, continue
        if instruction[:2] == '//' or instruction[:2] == '':
            continue

        # If the instruction is a segment declaration, change the state
        if instruction == '.text':
            state = 'text'
            continue
        elif instruction == '.data':
            state = 'data'
            continue

        # Replace all unnecessary characters with empty strings
        for replacement in replacements:
            instruction = instruction.replace(replacement, '')
        
        # Process instruction based on the current state
        if state == 'text':
            # Declare opcode to convert to hexadecimal for each instruction
            bin_str = ''

            # Replace mnemonics and numbers with their binary representations
            keywords = instruction.upper().split()
            for keyword in keywords:
                if keyword in mnemonics:
                    bin_str += num_to_bin(mnemonics[keyword])
                else:
                    bin_str += num_to_bin(int(keyword))

            # Append the hexadecimal opcode to the opcodes list
            opcodes.append(bin_to_hex(bin_str))
        elif state == 'data':
            # Declare list to hold data values in decimal and hexadecimal
            data_decimal = []
            data_hex = []
            data_mappings = {}

            # Split the data instruction into its components
            keywords = instruction.split()
            var_name = keywords[0]
            data_type = keywords[1]
            data_value = int(keywords[2])

            # Map variable name to its decimal value for future variable reference
            data_mappings = {var_name: int(data_value)}

            # Append the decimal data value to the data decimal list
            data_values.append(bin_to_hex(num_to_bin(data_value)))

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

    # For each data, calculate its address and write to the file respectively
    for i, value in enumerate(data_values):
        addresser = (i // 16) * 10
        addresser_hex = bin_to_hex(num_to_bin(addresser))
        if i % 16 == 0:
            file.write(f'{addresser_hex}: {value}')
        else:
            file.write(f' {value}')

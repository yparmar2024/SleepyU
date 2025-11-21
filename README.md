# SleepyU CPU

**Authors:** Yash Parmar & Brandon Gaona  
**Course:** CS382 - Computer Architecture  
**Date:** November 2025  

## Overview
SleepyU is a small 8-bit CPU designed for learning and experimenting with computer architecture concepts. Its core instructions are themed around sleep and dreams, making it both educational and fun. The CPU supports basic arithmetic and memory operations and can be extended for more advanced features.

## Key Features
- 8-bit instruction width with 4 general-purpose registers  
- Four core instructions: `BOOST` (add), `FALL` (subtract), `FETCH` (load), and `TUCK` (store)  
- Designed in Logisim-Evolution for easy simulation and visualization  
- Includes a simple assembler to translate assembly code into memory images  

## Repository Structure

Project_2/
├─ CPU/
│ └─ SleepyU.circ # Logisim CPU circuit
├─ Assembler/
│ └─ assembler.py # Assembler program
├─ Programs/
│ └─ demo_program.asm # Example assembly program
├─ Output/
│ └─ demo_program.hex # Assembler output for CPU memory
└─ Docs/
└─ SleepyU_Manual.pdf # Instruction manual

## Usage

1. Open `CPU/SleepyU.circ` in Logisim-Evolution.  
2. Write assembly programs using the SleepyU instruction set (`BOOST`, `FALL`, `FETCH`, `TUCK`).  
3. Run `Assembler/assembler.py` to convert `.asm` files into `.hex` memory images:  

```bash
python assembler.py Programs/demo_program.asm Output/demo_program.hex
```

Load the .hex file into CPU memory and simulate your program in Logisim.

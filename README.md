# SleepyU CPU

**Authors:** [Yash Parmar](www.github.com/yparmar2024) & [Nikunj Patel](www.github.com/nikunjpatel5136)
**Course:** Computer Architecture & Organization (CS382-B)
**Date:** 11 December 2025  

## Overview
SleepyU is a small 8-bit CPU designed for learning and experimenting with computer architecture concepts. Its core instructions are themed around sleep and dreams, making it both educational and fun. The CPU supports basic arithmetic and memory operations and can be extended for more advanced features.

## Key Features
- 8-bit instruction width with 4 general-purpose registers  
- Four core instructions: `BOOST` (add), `FALL` (subtract), `FETCH` (load), and `TUCK` (store)  
- Designed in Logisim-Evolution for easy simulation and visualization  
- Includes a simple assembler to translate assembly code into memory images  

## Demo Usage Instructions
1. Run the startup command to assemble the demo program:
```bash
    bash startup.sh
```
2. Load the demo_instruction.hex file into the Instruction_Fetching Stage's Instruction_RAM.
3. Load the demo_memory.hex file into the Memory_Access Stage's Data_RAM.
4. Press `Simulate`, then go to `Timing Diagram`.
5. Half-tick into the first cycle via `Manual Tick Half Cycle` and set the following initial register values in the Register_File:
    - X0: 00
    - X1: 00
    - X2: 01
    - X3: 00
6. Press `Manual Tick Full Cycle` 6 times.
7. Now, the first value in the Memory_Access Stage's Data_RAM should be 43 in hexadecimal (or 67 in decimal).

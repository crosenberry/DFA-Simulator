# DFA Evaluator

Theoretical Foundations\
Project 1 Finite Automata\
Caden Rosenberry

## Description
This project consists of a deterministic finite automaton (DFA) evaluator. The DFA evaluator allows users to check if a given string is accepted or rejected by the DFA. It provides visual computation steps and gives an output of either "ACCEPTED" or "REJECTED". The DFA configurations can be loaded from a file.

## Class Overview

### `DFA`

- **Attributes**:
  - `states`: List of DFA states.
  - `alphabet`: Set of characters accepted by the DFA.
  - `transition`: Transition table for the DFA.
  - `accepting_states`: List of accepting states for the DFA.
  - `current_state`: Keeps track of the current state in the DFA during evaluation. Start state is always 0.

- **Methods**:
  - `__init__(self, states, alphabet, transition, accepting_states)`: Constructor method to initialize the DFA.
  - `evaluate(self, string)`: Evaluates a string with the DFA, prints the computation, and returns "ACCEPTED" or "REJECTED".

### Functions

- `load_dfa(file_name)`: Loads a DFA configuration from a given file and returns a DFA object.
- `main()`: Main execution method that loads the DFA from the 'DFA.txt' file, prompts the user for input strings to evaluate, and then provides the evaluation result.

## Usage

1. Prepare your DFA configuration file (default name: 'DFA.txt'). The file format is:
   - Line 1: Number of states.
   - Line 2: Space-separated accepting states.
   - Line 3: Space-separated alphabet characters.
   - Subsequent lines: Transition table entries, one line per state.

2. Run the program:

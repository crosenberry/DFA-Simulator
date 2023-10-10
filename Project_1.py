# **********************************************************************************************************************
# * DFA Evaluator
# * Caden Rosenberry
# * *
# * The DFA Evaluator program simulates a Deterministic Finite Automaton (DFA) and checks whether a given string is
# * accepted or rejected by the DFA. The DFA's structure is loaded from a file, and the evaluator will visualize the
# * computation process and print the result of the inputted string.
# * *
# **********************************************************************************************************************

class DFA:
    def __init__(self, states, alphabet, transition, accepting_states):
        # Initializes the DFA object with states, alphabet, transition table, and accepting states.
        self.states = states
        self.alphabet = alphabet
        self.transition = transition
        self.accepting_states = accepting_states
        self.current_state = 0  # Start state is always 0.

# ***********************************************************************************************************************
# * String Computation
# ***********************************************************************************************************************
# * Evaluates a string with the DFA and prints the computation process to determine whether the string is accepted or
# * rejected by the DFA.
# ***********************************************************************************************************************

    def evaluate(self, string):
        # Evaluates the string with the DFA, prints the computation, and returns "ACCEPTED" or "REJECTED".
        self.current_state = 0  # Resets the current state to the start state.
        print(">>>Computation…")
        for i, char in enumerate(string):
            if char not in self.alphabet:
                print(f"{self.current_state},{char} -> INVALID INPUT")  # Char not in alphabet.
                return "REJECTED"
            next_state = self.transition[self.current_state][self.alphabet.index(char)]  # Get the next state.
            remaining_string = string[i + 1:]
            remaining_string_e = remaining_string if remaining_string else "{e}"  # Check if string is empty for the right side.
            print(f"{self.current_state},{char + remaining_string} -> {next_state},{remaining_string_e}")
            self.current_state = next_state  # Update the current state to the next state.
        # After processing the string, check if the last character leads to an accepting state.
        if self.current_state in self.accepting_states:
            return "ACCEPTED"
        return "REJECTED"


# ***********************************************************************************************************************
# * Load DFA
# ***********************************************************************************************************************
# * Loads a DFA from a file including the states, alphabet, transitions, and acceptance states and returns a DFA object.
# ***********************************************************************************************************************
def load_dfa(file_name):
    # Loads DFA from a file and returns a DFA object.
    with open(file_name, 'r') as file:
        states = int(file.readline().strip())
        accepting_states = list(map(int, file.readline().strip().split()))
        alphabet = file.readline().strip().split()
        transition = [list(map(int, file.readline().strip().split())) for _ in range(states)]  # Read transition table.
    return DFA(states, alphabet, transition, accepting_states)


# ***********************************************************************************************************************
# * Main
# ***********************************************************************************************************************
# * Loads the DFA from a file and evaluates strings until 'quit' is entered.
# ***********************************************************************************************************************
def main():
    # Main execution: loads DFA, evaluates strings until 'quit' is entered.
    dfa_file = 'DFA.txt'
    print(f">>>Loading {dfa_file}…")
    dfa = load_dfa(dfa_file)
    while True:
        user_input = input(">>>Please enter a string to evaluate:\n")
        if user_input.lower() == 'quit':
            print(">>>Goodbye!")  # Exits if 'quit' is entered.
            break
        print(dfa.evaluate(user_input))  # Evaluate the input string and print the result.


if __name__ == "__main__":
    main()  # Run main if script is executed as the main module.

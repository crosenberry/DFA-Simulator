# **********************************************************************************************************************
# * <Program Name>
# * Caden Rosenberry
# * *
# * <Program Description>
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

#***********************************************************************************************************************
# <Function Name>
#***********************************************************************************************************************
# * <Function Description>
========================================================================================================================
    def evaluate(self, string):
        # Evaluates the string with the DFA, prints the computation, and returns "ACCEPTED" or "REJECTED".
        self.current_state = 0  # Resets the current state to the start state.
        print(">>>Computation…")
        for char in string:
            if char not in self.alphabet:
                print(f"{self.current_state},{char} -> INVALID INPUT")  # Char not in alphabet.
                return "REJECTED"
            next_state = self.transition[self.current_state][self.alphabet.index(char)]  # Get the next state.
            print(f"{self.current_state},{char + string} -> {next_state},{string[string.index(char) + 1:]}")
            self.current_state = next_state  # Update the current state to the next state.
        return "ACCEPTED" if self.current_state in self.accepting_states else "REJECTED"

#***********************************************************************************************************************
# <Function Name>
#***********************************************************************************************************************
# * <Function Description>
========================================================================================================================
def load_dfa(file_name):
    # Loads DFA from a file and returns a DFA object.
    with open(file_name, 'r') as file:
        states = int(file.readline().strip())
        accepting_states = list(map(int, file.readline().strip().split()))
        alphabet = file.readline().strip().split()
        transition = [list(map(int, file.readline().strip().split())) for _ in range(states)]  # Read transition table.
    return DFA(states, alphabet, transition, accepting_states)

#***********************************************************************************************************************
# <Function Name>
#***********************************************************************************************************************
# * <Function Description>
========================================================================================================================
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

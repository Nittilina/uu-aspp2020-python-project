import models
import re

start_str = "Excitation energies and oscillator strengths:"
end_str = "SavETr:"

state_pattern = r"Excited State\s+(\d+):\s+(\S)\S*-(\S*)\s+(-?\d+\.\d+)\s+eV\s+(\d+\.\d+)\s+nm\s+f=(\d+\.\d+)\s+<S..2>=(\d+\.\d+)"
transition_pattern = r"(\d+) (<-|->) (\d+)\s+(-?\d+\.\d+)"

state_regex = re.compile(state_pattern)
transition_regex = re.compile(transition_pattern)

def parse_log(path):
    """
    Accepts the filename of a Gaussian log file and returns a list of excited states with associated data.
    """
    with open(path, 'r') as log:
        contents = log.read()
        cut1 = contents.split(start_str)
        cut2 = cut1[1].split(end_str)
        body = cut2[0]
        states = body.strip().split("\n \n ") 
        excited_states = [ parse_state(x) for x in states ]
        return excited_states

#Parses a single excited state and extracts the data into an ExcitedStates object.
def parse_state(state_data):
    lines = state_data.splitlines()
    header = lines[0]

    x = state_regex.match(header)
    es = models.ExcitedState(int(x.group(1)), x.group(2), x.group(3), float(x.group(4)), float(x.group(5)), float(x.group(6)), float(x.group(7)))

    transitions = lines[1:]

    for transition in transitions:
        y = transition_regex.match(transition.strip())

        if not y:
            break

        arrow = y.group(2)

        if arrow == "->":
            es.add_transition(int(y.group(1)), int(y.group(3)), float(y.group(4)))
        elif arrow == "<-":
            es.add_transition(int(y.group(3)), int(y.group(1)), float(y.group(4)))
        else:
            print("Wrong orbital transition format. Expected '->' or '<-', but got: %s" % arrow)
    
    return es

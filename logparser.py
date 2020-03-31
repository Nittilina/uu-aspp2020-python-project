import models
import re

start_str = "Excitation energies and oscillator strengths:"
end_str = "SavETr:"
state_regex = r"Excited State\s+(\d+):\s+(\S)\S*-(\S*)\s+(-?\d+\.\d+)\s+eV\s+(\d+\.\d+)\s+nm\s+f=(\d+\.\d+)\s+<S..2>=(\d+\.\d+)"
transition_regex = r"(\d+) (<-|->) (\d+)\s+(-?\d+\.\d+)"

def parse_log(path):
    with open(path, 'r') as log:
        contents = log.read()
        cut1 = contents.split(start_str)
        cut2 = cut1[1].split(end_str)
        body = cut2[0]
        states = body.strip().split("\n \n ") 
        excited_states = [ parse_state(x) for x in states ]
        return excited_states

def parse_state(state_data):
    lines = state_data.splitlines()
    header = lines[0]

    p = re.compile(state_regex)
    x = p.match(header)
    es = models.ExcitedState(int(x.group(1)), x.group(2), x.group(3), float(x.group(4)), float(x.group(5)), float(x.group(6)), float(x.group(7)))

    transitions = lines[1:]

    for transition in transitions:
        k = re.compile(transition_regex)
        y = k.match(transition.strip())

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

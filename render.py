from models import ExcitedState, Transition
from terminaltables import SingleTable
from typing import List

def render_excited_states(states):
    titles = ["State", "E (eV)", "f", "Sym", "Orbitals", " Coeffs", "test"]
    rows = [ es_to_row(state) for state in states ]

    table_data = [titles] + rows

    table = SingleTable(table_data)
    table.inner_row_border = True
    table.inner_column_border = False

    print(table.table)

def es_to_row(state: ExcitedState):
    y = []
    y.append(f'{state.mult}{state.index}') #Write a function adding multiplicity and index together
    y.append(state.energy)
    y.append("%.4f" % state.osc_str)
    y.append(state.sym)

    orbitals, coeffs = render_transitions(state.transits)

    y.append(orbitals)
    y.append(coeffs)

    return y

def render_transitions(transitions: List[Transition]):
    orbitals = "\n".join([ f'{x.from_orb} -> {x.to_orb}' for x in transitions ])
    coeffs = "\n".join([ f'{" " if x.coeff > 0 else ""}{"%.5f" % x.coeff}' for x in transitions ])
    
    return orbitals, coeffs
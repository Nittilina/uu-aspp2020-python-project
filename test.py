import logparser
from render import render_excited_states

states = logparser.parse_log("pbe0_pyr_vertS.log")

render_excited_states(states)
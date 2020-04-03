class ExcitedState:
    """
    Data for a sinlge excited state, along with its transitions.
    """

    def __init__(self, index, mult, sym, energy, wlength, osc_str, s2):
        self.index = index
        self.mult = mult
        self.sym = sym
        self.energy = energy
        self.wlength = wlength
        self.osc_str = osc_str
        self.s2 = s2
        self.transits = []
    
    def add_transition(self, from_orb, to_orb, coeff):
        """
        Adds a transition using the indices of the orbitals from which and to which the excitation occurs, along with the coefficient of the transition.
        """
        transition = Transition(from_orb, to_orb, coeff)
        self.transits.append(transition)


class Transition:
    """
    Data for a single orbital transition.
    """

    def __init__(self, from_orb, to_orb, coeff):
        self.from_orb = from_orb
        self.to_orb = to_orb
        self.coeff = coeff

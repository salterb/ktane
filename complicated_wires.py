from colours import bold

def is_valid_comp_wire(wire):
    """Helper function to determine if a string representing a
    complicated wire is valid.
    """
    if len(wire) > 4:
        return False
    for char in wire:
        if char not in ('R', 'B', 'S', 'L'):
            return False
    return True


def get_complicated_wire_sequence():
    """Helper function to get wire sequence from user input, and
    validate it.
    """
    while True:
        seq = input("\nInput a space-separated string representing the wires.\n"
                    "Use 'R' for 'red', 'B' for 'blue', 'S' for star, "
                    "and 'L' for light: ").upper().replace("W", "")
        wires = ["".join(sorted(wire)) for wire in seq.split()]
        if all(is_valid_comp_wire(wire) for wire in wires):
            break
        print(f"Invalid wire sequence: {seq}")
    return wires


class ComplicatedWires:
    def __init__(self, bomb):
        self.bomb = bomb
        self.wires = get_complicated_wire_sequence()

    def __repr__(self):
        return self.wires

    @staticmethod
    def cut():
        """Informs the user to cut the wire."""
        print(f"\n {bold('CUT')} the wire")

    @staticmethod
    def no_cut():
        """Informs the user NOT to cut the wire."""
        print(f"\nDo {bold('NOT')} cut the wire")

    def _conditional_cut(self, condition):
        self.cut() if condition else self.no_cut()

    def serial_cut(self):
        """Informs the user to cut the wire IF the serial number is
        even.
        """
        if self.bomb.serial is None:
            self.bomb.add_serial()
        self._conditional_cut(int(self.bomb.serial[-1]) % 2 == 0)


    def p_port_cut(self):
        """Informs the user to cut the wire IF the bomb has a
        parallel port.
        """
        if self.bomb.parallel_port is None:
            self.bomb.add_parallel_port()
        self._conditional_cut(self.bomb.parallel_port is True)

    def battery_cut(self):
        """Informs the user to cut the wire IF the bomb has more than
        two batteries.
        """
        if self.bomb.num_batteries is None:
            self.bomb.add_batteries()
        self._conditional_cut(self.bomb.num_batteries >= 2)

    def solve(self):
        """Solve the complicated wires module."""
        # We have 16 different cases to consider.
        # We use a lookup table which runs the correct printing function.
        print_function_lookup = \
            {'': self.cut, 'B': self.serial_cut, 'BL': self.p_port_cut,
             'BLR': self.serial_cut, 'BLRS': self.no_cut, 'BLS': self.p_port_cut,
             'BR': self.serial_cut, 'BRS': self.p_port_cut, 'BS': self.no_cut,
             'L': self.no_cut, 'LR': self.battery_cut, 'LRS': self.battery_cut,
             'LS': self.battery_cut, 'R': self.serial_cut, 'RS': self.cut, 'S': self.cut}
        for wire in self.wires:
            print_function_lookup[wire]()

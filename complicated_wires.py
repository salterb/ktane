"""Complicated wires placeholder docstring."""

from colours import bold


class ComplicatedWires:
    """Complicated wires placeholder docstring."""
    def __init__(self, bomb):
        self.bomb = bomb
        self.wires = self.get_complicated_wire_sequence()

    def __repr__(self):
        return self.wires

    def print_function_lookup(self, wire):
        lookup = \
            {"": self.cut, "B": self.serial_cut, "BL": self.p_port_cut,
             "BLR": self.serial_cut, "BLRS": self.no_cut, "BLS": self.p_port_cut,
             "BR": self.serial_cut, "BRS": self.p_port_cut, "BS": self.no_cut,
             "L": self.no_cut, "LR": self.battery_cut, "LRS": self.battery_cut,
             "LS": self.battery_cut, "R": self.serial_cut, "RS": self.cut, "S": self.cut}
        return lookup[wire]

    def is_valid_wire(self, wire):
        return wire in set(["", "B", "BL", "BLR", "BLRS", "BLS", "BR", "BRS",
                           "BS", "L", "LR", "LRS", "LS", "R", "RS", "S"])

    @staticmethod
    def cut():
        """Informs the user to cut the wire."""
        print(f"\n{bold('CUT')} the wire")

    @staticmethod
    def no_cut():
        """Informs the user NOT to cut the wire."""
        print(f"\nDo {bold('NOT')} cut the wire")

    def _conditional_cut(self, condition):
        self.cut() if condition else self.no_cut()

    def serial_cut(self):
        """Informs the user to cut the wire if the serial number is
        even.
        """
        self._conditional_cut(int(self.bomb.serial[-1]) % 2 == 0)


    def p_port_cut(self):
        """Informs the user to cut the wire if the bomb has a
        parallel port.
        """
        self._conditional_cut(self.bomb.parallel_port is True)

    def battery_cut(self):
        """Informs the user to cut the wire if the bomb has more than
        two batteries.
        """
        self._conditional_cut(self.bomb.batteries >= 2)

    def get_complicated_wire_sequence(self):
        """Helper function to get wire sequence from user input, and
        validate it.
        """
        while True:
            seq = input("\nInput a space-separated string representing the wires.\n"
                        "Use 'R' for 'red', 'B' for 'blue', 'W' for 'white', "
                        "'S' for star, and 'L' for light: ").upper()

            # We remove "W" from the strings since it doesn't affect any of the
            # cuts. However, we do so _after_ we split, since otherwise we lose
            # the plain white wires
            wires = ["".join(sorted(wire)).replace("W", "") for wire in seq.split()]
            if all(self.is_valid_wire(wire) for wire in wires):
                break
            print(f"Invalid wire sequence: {seq}")
        return wires

    def solve(self):
        """Solve the complicated wires module."""
        # We have 16 different cases to consider.
        # We use a lookup table which runs the correct printing function.
        for wire in self.wires:
            self.print_function_lookup(wire)()

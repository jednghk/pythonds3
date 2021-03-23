'''
Goal:
1. Create the and, or, and not gates
    - and gate outputs 1 when both inputs are 1, else 0
    - or gate outputs 1 when either or both inputs is 1, else 0
    - not gate outputs 1 if 0 and 0 if 1
2. Create connectors
    -takes in two arguments, from gate and to gate
    -channels the input from fgate to tgate
'''


def invert_value(value):
    if value == 0:
        return 1
    else:
        return 0


class LogicGate:
    def __init__(self, lbl):
        self.label = lbl
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        return self.perform_gate_logic()


class BinaryGate(LogicGate):
    def __init__(self, lbl):
        super().__init__(lbl)
        self.pin_a = None
        self.pin_b = None

    def set_pin_a(self):
        self.pin_a = int(input(f'Enter pin A input for gate {self.label}:'))

    def set_pin_b(self):
        self.pin_b = int(input(f'Enter pin B input for gate {self.label}:'))


class UnaryGate(LogicGate):
    def __init__(self, lbl):
        super().__init__(lbl)
        self.pin = None

    def set_pin(self):
        self.pin = int(input(f'Enter input pin for gate {self.label}:'))


class NotGate(UnaryGate):
    def __init__(self, lbl):
        super().__init__(lbl)

    def perform_gate_logic(self):
        if self.pin is None:
            self.set_pin()
        if self.pin == 1:
            return 0
        else:
            return 1


class AndGate(BinaryGate):
    def __init__(self, lbl):
        super().__init__(lbl)

    def perform_gate_logic(self):
        if self.pin_a is None:
            self.set_pin_a()
        if self.pin_b is None:
            self.set_pin_b()
        if self.pin_a == 1 and self.pin_b == 1:
            return 1
        else:
            return 0


class NandGate(AndGate):
    def __init__(self, lbl):
        super().__init__(lbl)

    def perform_gate_logic(self):
        ag_output = super().perform_gate_logic()
        return invert_value(ag_output)


class OrGate(BinaryGate):
    def __init__(self, lbl):
        super().__init__(lbl)

    def perform_gate_logic(self):
        if self.pin_a == 0 and self.pin_b == 0:
            return 0
        else:
            return 1


class NorGate(OrGate):
    def __init__(self, lbl):
        super().__init__(lbl)

    def perform_gate_logic(self):
        og_output = super().perform_gate_logic()
        return invert_value(og_output)


class XorGate(OrGate):
    def __init__(self, lbl):
        super().__init__(lbl)

    def perform_gate_logic(self):
        if self.pin_a == self.pin_b:
            return 0
        else:
            return 1


class Connector:
    '''takes in two instances of logic gates and channels output of fgate into the input of tgate'''

    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate

        fgate_output = self.from_gate.get_output()
        input_pin_a = self.to_gate.pin_a
        input_pin_b = self.to_gate.pin_b
        if input_pin_a is None:
            input_pin_a = fgate_output
        elif input_pin_b is None:
            input_pin_b = fgate_output
        else:
            raise ValueError('No empty pins to receive output')


g1 = AndGate('ag1')
g2 = OrGate('og1')
c1 = Connector(g1, g2)
# end state of connector: when get_output is called on gate, necessary inputs are requested
# until output of last gate can be received
print(c1.get_label())
test.set_pin_a()
test.set_pin_b()
print(test.perform_gate_logic())
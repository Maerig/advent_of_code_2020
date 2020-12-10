import re


INSTRUCTION_REGEX = re.compile(r"^(\w{3}) ([+-]\d+)$")


class InfiniteLoopError(Exception):
    def __init__(self, last_acc):
        super().__init__(f"Infinite loop detected. {last_acc=}")
        self.last_acc = last_acc


class Cpu:
    def __init__(self):
        self._acc = 0
        self._pc = 0
        self._program = []

    def _run_instruction(self, operation, argument):
        if operation == "acc":
            self._acc += argument
            self._pc += 1
        elif operation == "jmp":
            self._pc += argument
        elif operation == "nop":
            self._pc += 1
        else:
            raise ValueError(operation)

    def run_program(self, program):
        self._acc = 0
        self._pc = 0
        self._program = program
        pc_hist = set()
        last_acc = None

        while True:
            self._run_instruction(*self._program[self._pc])

            if self._pc >= len(program):
                return self._acc

            if self._pc in pc_hist:
                raise InfiniteLoopError(last_acc)

            pc_hist.add(self._pc)
            last_acc = self._acc


def load_program(path):
    program = []
    with open(path) as f:
        for l in f:
            match = INSTRUCTION_REGEX.match(l.strip())
            if not match:
                raise ValueError(l)
            operation, argument = match.groups()
            program.append((operation, int(argument)))
    return program


def alter_program(program):
    for i, (operation, argument) in enumerate(program):
        if operation == "jmp":
            program[i] = "nop", argument
            yield program
            program[i] = "jmp", argument
        elif operation == "nop":
            program[i] = "jmp", argument
            yield program
            program[i] = "nop", argument


cpu = Cpu()
pg = load_program("input.txt")
try:
    cpu.run_program(pg)
except InfiniteLoopError as ile:
    print(ile.last_acc)

for altered_pg in alter_program(pg):
    try:
        print(cpu.run_program(pg))
    except InfiniteLoopError as ile:
        pass

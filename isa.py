import json
from collections import namedtuple
from enum import Enum


class Opcode(str, Enum):
    """Opcode для инструкций."""

    INC = "inc"
    DEC = "dec"
    INPUT = "input"
    PRINT = "print"

    JMP = "jmp"
    JZ = "jz"
    JNZ = "jnz"

    HALT = "halt"

    MOV = "mov"

    ADD = "add"
    SUB = "sub"
    MOD = "mod"
    MUL = "mul"

    ADD_STR = "add_str"

    EI = "ei"
    DI = "di"
    IRET = "iret"

    STORE = "store"

    RIGHT = "right"
    LEFT = "left"

    PRINT_CHAR = "print_char"

    CALL = "call"
    RET = "ret"

    WORD = "word"

    def __str__(self):
        return str(self.value)


class Term(namedtuple("Term", "line pos symbol")):
    """Описание выражения из исходного текста программы.

    Сделано через класс, чтобы был docstring.
    """
class Instruction:
    def __init__(self, address: int, opcode: Opcode, arg1=None, addr1=None, arg2=None, addr2=None, save_space=None, addr3=None):
        self.address = address
        self.opcode = opcode
        self.arg1 = arg1
        self.addr1 = addr1
        self.arg2 = arg2
        self.addr2 = addr2
        self.save_space = save_space
        self.addr3 = addr3

    def __str__(self):
        return self.opcode + " -> " + str(self.arg1) + " | " + str(self.addr1) + " | " + str(self.arg2) + " | " + str(self.addr2) + " | " + str(self.save_space) + " | " + str(self.addr3)

def write_code(filename, code):
    with open(filename, "w", encoding="utf-8") as file:
        buf = []
        for instr in code:
            buf.append(json.dumps(instr))
        file.write("[" + ",\n ".join(buf) + "]")


def read_code(filename: str) -> list:

    with open(filename, encoding="utf-8") as file:
        code = json.loads(file.read())

    for instr in code:
        if isinstance(instr, dict):
            instr["opcode"] = Opcode(instr["opcode"])

            if "term" in instr:
                assert len(instr["term"]) == 3
                instr["term"] = Term(instr["term"][0], instr["term"][1], instr["term"][2])

    return code

"""
Constants used by Catamount Processor Unit

CS 2210 Computer Organization
Clayton Cafiero <cbcafier@uvm.edu>
"""

WORD_SIZE = 16  # 16 bits = 2 bytes
WORD_MASK = (1 << WORD_SIZE) - 1  # 16 ones
STACK_BASE = 0xFF00  # lowest address the stack may grow down to
STACK_TOP = 0xFFFF  # initial SP; the stack is empty when SP == STACK_TOP
SP_REG = 7  # R7 is the stack pointer (used implicitly by CALL and RET)

if __name__ == "__main__":
    print(f"WORD_SIZE: {WORD_SIZE} (decimal)")
    print(f"WORD_MASK: {WORD_MASK:04X} (hex)")
    print(f"STACK_BASE: {STACK_BASE:04X} (hex)")
    print(f"STACK_TOP: {STACK_TOP:04X} (hex)")
    print(f"SP_REG: R{SP_REG}")

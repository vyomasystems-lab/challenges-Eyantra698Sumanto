# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

from model_mkbitmanip import *

# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 

# Sample Test
@cocotb.test()
def run_test(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    rs1 = "000"
    rs2 = "0000000"
    rd = "00000"
    mav_putvalue_src1 =  random.randint(0, pow(2,32)-1)
    mav_putvalue_src2 =  random.randint(0, pow(2,32)-1)
    mav_putvalue_src3 =  random.randint(0, pow(2,32)-1)

    #mav_putvalue_src1 =  0b00000000000000000000000111100101
    #mav_putvalue_src2 =  0b11111111111111111010100011011111
    #mav_putvalue_src3 =  0b00000000000000000000000000000000
    #mav_putvalue_src1 =  0b00000000000000000000000111100101
    #mav_putvalue_src2 =  0b11111111111111111111111111111111
    #mav_putvalue_src3 =  0b00000000000000000000000000000000
    #mav_putvalue_instr = 0b01000000000000000110000000110011

    #--------------Give inputs here
    instruction = 'ANDN' 
    func7 = "0100000"
    func3 = "111"
    opcode = "0110011"

    #instruction = 'ORN' 
    #func7 = "0100000"
    #func3 = "110"
    #opcode = "0110011"

    #instruction = 'XNOR' 
    #func7 = "0100000"
    #func3 = "100"
    #opcode = "0110011"

    #instruction = 'SLO' 
    #func7 = "0010000"
    #func3 = "001"
    #opcode = "0110011"

    #instruction = 'SRO' 
    #func7 = "0010000"
    #func3 = "101"
    #opcode = "0110011"

    #instruction = 'ROL' 
    #func7 = "0110000"
    #func3 = "001"
    #opcode = "0110011"

    #instruction = 'ROR' 
    #func7 = "0110000"
    #func3 = "101"
    #opcode = "0110011"

    #instruction = 'SH1ADD' 
    #func7 = "0010000"
    #func3 = "010"
    #opcode = "0110011"

    #instruction = 'SH2ADD' 
    #func7 = "0010000"
    #func3 = "100"
    #opcode = "0110011"

    #instruction = 'SH3ADD' 
    #func7 = "0010000"
    #func3 = "110"
    #opcode = "0110011"

    #instruction = 'SBCLR' 
    #func7 = "0100100"
    #func3 = "001"
    #opcode = "0110011"

    #instruction = 'SBSET' 
    #func7 = "0010100"
    #func3 = "001"
    #opcode = "0110011"

    #instruction = 'SBINV' 
    #func7 = "0110100"
    #func3 = "001"
    #opcode = "0110011"

    #instruction = 'SBEXT' 
    #func7 = "0100100"
    #func3 = "101"
    #opcode = "0110011"

    #instruction = 'GORC' 
    #func7 = "0010100"
    #func3 = "101"
    #opcode = "0110011"

    #instruction = 'GREV' 
    #func7 = "0110100"
    #func3 = "101"
    #opcode = "0110011"

    #instruction = 'CMIX' 
    #func7 = "0000011"
    #func3 = "001"
    #opcode = "0110011"

    #instruction = 'CMOV'
    #func7 = "0000011"
    #func3 = "101"
    #opcode = "0110011"

    #instruction = 'FSL' 
    #func7 = "0000010"
    #func3 = "001"
    #opcode = "0110011"

    #instruction = 'FSR' 
    #func7 = "0000010"
    #func3 = "101"
    #opcode = "0110011"

    #instruction = 'CLZ' 
    #func7 = "0110000"
    #func3 = "001"
    #opcode = "0010011"

    #instruction = 'CTZ' 
    #func7 = "0110000"
    #func3 = "001"
    #rs2="0000100"
    #opcode = "0010011"

    #instruction = 'PCNT' 
    #func7 = "0110000"
    #func3 = "001"
    #rs2="0001000"
    #opcode = "0010011"

    #instruction = 'SEXT.B' 
    #func7 = "0110000"
    #func3 = "001"
    #rs2="0010000"
    #opcode = "0010011"

    #instruction = 'SEXT.H' 
    #func7 = "0110000"
    #func3 = "001"
    #rs2="0010100"
    #opcode = "0010011"

    #instruction = 'CRC32.B' 
    #func7 = "0110000"
    #func3 = "001"
    #rs2="1000000"
    #opcode = "0010011"

    #instruction = 'CRC32.H' 
    #func7 = "0110000"
    #func3 = "001"
    #rs2="1000100"
    #opcode = "0010011"

    #instruction = 'CRC32.W' 
    #func7 = "0110000"
    #func3 = "001"
    #rs2="1001000"
    #opcode = "0010011"

    #instruction = 'CRC32C.B' 
    #func7 = "0110000"
    #func3 = "001"
    #rs2="1100000"
    #opcode = "0010011"

    #instruction = 'CRC32C.H' 
    #func7 = "0110000"
    #func3 = "001"
    #rs2="1100100"
    #opcode = "0010011"

    #instruction = 'CRC32C.W' 
    #func7 = "0110000"
    #func3 = "001"
    #rs2="1101000"
    #opcode = "0010011"

    #instruction = 'CLMUL' 
    #func7 = "0000101"
    #func3 = "001"
    #opcode = "0110011"

    #instruction = 'CLMULH' 
    #func7 = "0000101"
    #func3 = "011"
    #opcode = "0110011"

    #instruction = 'CLMULR' 
    #func7 = "0000101"
    #func3 = "010"
    #opcode = "0110011"

    #instruction = 'MIN' 
    #func7 = "0000101"
    #func3 = "100"
    #opcode = "0110011"

    #instruction = 'MAX' 
    #func7 = "0000101"
    #func3 = "101"
    #opcode = "0110011"

    #instruction = 'MINU' 
    #func7 = "0000101"
    #func3 = "110"
    #opcode = "0110011"

    #instruction = 'MAXU' 
    #func7 = "0000101"
    #func3 = "111"
    #opcode = "0110011"

    #instruction = 'BDEP' 
    #func7 = "0100100"
    #func3 = "110"
    #opcode = "0110011"

    #instruction = 'BEXT' 
    #func7 = "0000100"
    #func3 = "110"
    #opcode = "0110011"

    #instruction = 'PACK' 
    #func7 = "0000100"
    #func3 = "100"
    #opcode = "0110011"

    #instruction = 'PACKU' 
    #func7 = "0100100"
    #func3 = "100"
    #opcode = "0110011"
    
    #instruction = 'PACKH' 
    #func7 = "0000100"
    #func3 = "100"
    #opcode = "0110011"

    #instruction = 'SLOI' 
    #func7 = "0010000"
    #func3 = "001"
    #opcode = "0010011"

    #instruction = 'SROI' 
    #func7 = "0010000"
    #func3 = "101"
    #opcode = "0010011"

    #instruction = 'RORI' 
    #func7 = "0110000"
    #func3 = "101"
    #opcode = "0010011"

    #instruction = 'SBCLRI' 
    #func7 = "0100100"
    #func3 = "001"
    #opcode = "0010011"

    #instruction = 'SBSETI' 
    #func7 = "0010100"
    #func3 = "001"
    #opcode = "0010011"

    #instruction = 'SBINVI' 
    #func7 = "0110100"
    #func3 = "001"
    #opcode = "0010011"

    #instruction = 'SBEXTI' 
    #func7 = "0100100"
    #func3 = "101"
    #opcode = "0010011"

    #instruction = 'SHFL' 
    #func7 = "0000100"
    #func3 = "001"
    #opcode = "0110011"

    #instruction = 'UNSHFL' 
    #func7 = "0000100"
    #func3 = "101"
    #opcode = "0110011"

    #instruction = 'SHFLI  55 (check)' 
    #func7 = "0000100"
    #func3 = "001"
    #opcode = "0010011"

    #instruction = 'UNSHFLI  56 (check)' 
    #func7 = "0000100"
    #func3 = "101"
    #opcode = "0010011"

    #instruction = 'GORCI' 
    #func7 = "0010100"
    #func3 = "101"
    #opcode = "0010011"

    #instruction = 'GREVI' 
    #func7 = "0110100"
    #func3 = "101"
    #opcode = "0010011"

    #instruction = 'FSRI' 
    #func7 = "0000010"
    #func3 = "101"
    #opcode = "0010011"

    #instruction = 'BFP' 
    #func7 = "0100100"
    #func3 = "111"
    #opcode = "0110011"
    



    

    

    # input transaction
  
    mav_putvalue_instr = int("0b"+func7 + rs2 + rs1 + func3 + rd + opcode,base=2)
    #cocotb.log.info( bin(mav_putvalue_instr))

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value
    cocotb.log.info(f'*************Test Running For {instruction} instruction************')
    cocotb.log.info(f'Input SRC1 = {hex(mav_putvalue_src1)} SRC2 = {hex(mav_putvalue_src2)} SRC3 = {hex(mav_putvalue_src1)}')
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

# See LICENSE.vyoma for details
# See LICENSE.cocotb for details

# Simple tests for a vedic8x8 multiplier module
import cocotb
from cocotb.triggers import Timer
import random
from cocotb.decorators import coroutine
from cocotb.triggers import Timer

@cocotb.test()

@cocotb.test()
async def vedic8x8_randomised_test(dut):
    """Test for vedic8x8 for random numbers multiple times"""
    for i in range(128):
        b = i
        for j in range(128):
            a = j
        dut.a.value = a
        dut.b.value = b
        expected_output = a*b
        await Timer(2, units='ns')
        dut_output = dut.prod.value
    
        cocotb.log.info(f'Input A = {hex(a)} B = {hex(b)}')
        cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
        cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_output)}')
    
        # comparison
        error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_output)}'
        assert dut_output == expected_output, error_message
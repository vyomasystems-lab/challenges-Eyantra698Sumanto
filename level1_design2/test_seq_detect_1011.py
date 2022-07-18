# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    binstream = ''
    binstream2 = ''
    out=0
    count=0
    for i in range(31):
        await FallingEdge(dut.clk)
        INP = random.randint(0, 1)
        dut.inp_bit.value = INP
        binstream2 = binstream2 + str(INP)
        if '1011' in binstream and count==4:
            out = 1
            binstream = ''
            count = 0
        else:
            out = 0
            if ('101' in binstream and INP==1 and count==3) or ('10' in binstream and INP==1 and count==2) or ('1' in binstream and INP==0 and count==1) or (INP==1 and count==0):
                count=count+1
                binstream = binstream + str(INP)
            else:
                binstream = ''
                count=0

        #await FallingEdge(dut.clk)
        dut.log.info(f'INPUT={dut.inp_bit.value} MODEL={out} DUT={dut.seq_seen.value}')
        assert dut.seq_seen.value == out, "Randomised test failed with: INPUT = {INPUT}  BINARY STREAM = {BINSTREAM} OUTPUT = {OUTPUT}".format(
            INPUT=dut.inp_bit.value, BINSTREAM=binstream2, OUTPUT=dut.seq_seen.value)

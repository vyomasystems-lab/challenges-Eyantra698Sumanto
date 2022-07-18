# See LICENSE.vyoma for details
# See LICENSE.cocotb for details

# Simple tests for a mux module
import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()



@cocotb.test()
async def mux_randomised_test(dut):
    """Test for mux for random numbers multiple times"""

    for i in range(31):
        SEL = i;
        INP = random.randint(0, pow(2,64)-1)
        BININP = bin(INP)

        BININP1 = str(BININP[2:63]).zfill(64)
        BININP = BININP1 [::-1]
        dut.inp0.value = int(BININP[0:1])
        dut.inp1.value = int(BININP[2:3])
        dut.inp2.value = int(BININP[4:5])
        dut.inp3.value = int(BININP[6:7])
        dut.inp4.value = int(BININP[8:9])
        dut.inp5.value = int(BININP[10:11])
        dut.inp6.value = int(BININP[12:13])
        dut.inp7.value = int(BININP[14:15])
        dut.inp8.value = int(BININP[16:17])
        dut.inp9.value = int(BININP[18:19])
        dut.inp10.value = int(BININP[20:21])
        dut.inp11.value = int(BININP[22:23])
        dut.inp12.value = int(BININP[24:25])
        dut.inp13.value = int(BININP[26:27])
        dut.inp14.value = int(BININP[28:29])
        dut.inp15.value = int(BININP[30:31])
        dut.inp16.value = int(BININP[32:33])
        dut.inp17.value = int(BININP[34:35])
        dut.inp18.value = int(BININP[36:37])
        dut.inp19.value = int(BININP[38:39])
        dut.inp20.value = int(BININP[40:41])
        dut.inp21.value = int(BININP[42:43])
        dut.inp22.value = int(BININP[44:45])
        dut.inp23.value = int(BININP[46:47])
        dut.inp24.value = int(BININP[48:49])
        dut.inp25.value = int(BININP[50:51])
        dut.inp26.value = int(BININP[52:53])
        dut.inp27.value = int(BININP[54:55])
        dut.inp28.value = int(BININP[56:57])
        dut.inp29.value = int(BININP[58:59])
        dut.inp30.value = int(BININP[60:61])
        dut.inp31.value = int(BININP[62:63])
        dut.sel.value = SEL

        await Timer(2, units='ns')
        
        dut._log.info(f'SEL={SEL:05}        INP={INP:25}     MODEL={int(BININP[2*SEL:2*SEL+1]):05}       DUT={int(dut.out.value):05}')
        assert dut.out.value == int(BININP[2*SEL:2*SEL+1]), "Randomised test failed with: SEL={SEL} MODEL_OUTPUT={MODELOUTPUT:02}  DUT_OUTPUT={DUTOUTPUT}".format(
            SEL=dut.sel.value, DUTOUTPUT=dut.out.value, MODELOUTPUT=int(BININP[2*SEL:2*SEL+1]))
            

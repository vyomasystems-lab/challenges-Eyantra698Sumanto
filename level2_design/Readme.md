# challenges-Eyantra698Sumanto
challenges-Eyantra698Sumanto created by GitHub Classroom
# Adder Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.


![](https://i.imgur.com/miWGA1o.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (adder module here) which takes in 4-bit inputs *a* and *b* and gives 5-bit output *sum*

The values are assigned to the input port using 
```
dut.a.value = 7
dut.b.value = 5
```

The assert statement is used for comparing the adder's outut to the expected value.

The following error is seen:
```
assert dut.sum.value == A+B, "Adder result is incorrect: {A} + {B} != {SUM}, expected value={EXP}".format(
                     AssertionError: Adder result is incorrect: 7 + 5 != 2, expected value=12
```
## Test Scenario **(Important)**
- Test Inputs: a=7 b=5
- Expected Output: sum=12
- Observed Output in the DUT dut.sum=2

Output mismatches for the above inputs proving that there is a design bug

## Design Bug Cases
1. ANDN

## Design Pass Cases
1. ORN

Inputs:
```
    mav_putvalue_src1 =  0b00000000000000000000000111100101
    mav_putvalue_src2 =  0b11111111111111111111111111111111
    mav_putvalue_src3 =  0b00000000000000000000000000000000
    mav_putvalue_instr = 0b01000000000000000110000000110011
```
Outputs:
![image](https://user-images.githubusercontent.com/58599984/180601412-e12230c9-41aa-4b3a-9b9e-8d4fd144eeb7.png)


## Verification Strategy

## Is the verification complete ?

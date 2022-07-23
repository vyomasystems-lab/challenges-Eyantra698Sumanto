# challenges-Eyantra698Sumanto
challenges-Eyantra698Sumanto created by GitHub Classroom
# Vedic 8x8 Multiplier Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![image](https://user-images.githubusercontent.com/58599984/180623762-b1eb3b17-b096-4bd0-801a-e3b754eddf29.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (vedic8x8 multiplier module here) which takes in 8-bit inputs *a* and *b* and gives 16-bit output *prod*

The values are assigned to the input port using 
```
dut.a.value = a
dut.b.value = b
```
where a and b are some randomized 8 bit numbers.

The assert statement is used for comparing the vedic8x8's outut to the expected value.

The following error is seen:
```
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_output)}'
    assert dut_output == expected_output, error_message
```
## Test Scenario **(Important)**
- Test Inputs A and B: Randmodized
- Expected Output: A*B
- Observed Output in the DUT not matching Expected Output

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following
### BUG 1
Output: 
![image](https://user-images.githubusercontent.com/58599984/180625131-4dd4810b-b565-4ae6-aeeb-3cd0afc039a9.png)
Bug:
```
module vedic2x2(input [1:0] a,b, output [3:0] prod);

	wire a1b1 = a[1] & b[1];
	wire a0b1 = a[0] & b[1];
	wire a1b0 = a[1] & b[0];
	wire a0b0 = a[0] | b[0]; ==================> BUG
	wire carry;
	
	assign prod[0] = a0b0;

	half_adder HA0(a0b1,a1b0,prod[1],carry);
	half_adder HA1(a1b1,carry,prod[2],prod[3]);

endmodule
```
The buggy lines need to be replaced by:
```
wire a0b0 = a[0] & b[0];
  ```
### BUG 2
Output after fixing Bug 1:
![image](https://user-images.githubusercontent.com/58599984/180625172-795e12e8-3a0b-4900-b3c6-5c6bc05b1d14.png)
Bug:
```
module half_adder(input a,b, output sum, carry);

	assign sum = a | b;       ==================> BUG
	assign carry = a ^ b;     ==================> BUG

endmodule
```
The buggy lines need to be replaced by:
```
	assign sum = a ^ b;       ==================> BUG
	assign carry = a & b;     ==================> BUG
  ```
### BUG 3
Output after fixing Bug 2:

![image](https://user-images.githubusercontent.com/58599984/180625193-f08d9261-2d34-46e9-809d-258c35e0896d.png)

Bug:
```module ripple_adder_6bit(input [5:0] a,b, input cin, output [5:0] sum, output cout);

	wire carry1, carry2, carry3, carry4, carry5;

	full_adder FA0(a[0],b[0],cin,sum[0],carry1);
	full_adder FA1(a[1],a[1],carry1,sum[1],carry2); ==================> BUG
	full_adder FA2(a[2],b[2],carry2,sum[2],carry3);
	full_adder FA3(a[3],b[3],carry3,sum[3],carry4);
	full_adder FA4(a[4],b[4],carry4,sum[4],carry5);
	full_adder FA5(a[5],b[5],carry5,sum[5],cout);

endmodule
```
The buggy lines need to be replaced by:
```
	full_adder FA1(a[1],b[1],carry1,sum[1],carry2);
  ```
### BUG 4
Output after fixing Bug 3:
![image](https://user-images.githubusercontent.com/58599984/180625247-b018dfdf-5205-4184-b02f-747bfcd4b829.png)
Bug:
```
module ripple_adder_12bit(input [11:0] a,b, input cin, output [11:0] sum, output cout);

	wire carry;

	ripple_adder_6bit RA0(a[5:0],a[5:0],cin,sum[5:0],carry); ==========> BUG
	ripple_adder_6bit RA1(a[11:6],b[11:6],carry,sum[11:6],cout);

endmodule
```
The buggy lines need to be replaced by:
```
	ripple_adder_6bit RA0(a[5:0],b[5:0],cin,sum[5:0],carry);
  ```
## Design Fix
Updating the design and re-running the test makes the test pass.

![image](https://user-images.githubusercontent.com/58599984/180625392-ff313990-0fce-40b9-8a64-74b8acec95f6.png)


![image](https://user-images.githubusercontent.com/58599984/180625405-747ea95d-510a-40ba-bd25-e2a3d2e683c2.png)

The updated design is checked in as vedic8x8_fix.v

Also, verifying for all cases in iterative fashion:
![image](https://user-images.githubusercontent.com/58599984/180625462-1d7c7a5b-08b7-485d-b342-ff55492f4545.png)
Thus, indicates the test cases are passed.

## Verification Strategy
We have used cocotb design environment and wrote the testbench in python and verified it for each test case with random set of inputs.

We have also verified all the cases in an iterative manner.

There is  no involvement of clock as the DUT is combinational vedic 8x8 multiplier.
## Is the verification complete ?
Yes, the verification is complete as we have verified the design for all the possible test-cases using the cocotb python testbench.

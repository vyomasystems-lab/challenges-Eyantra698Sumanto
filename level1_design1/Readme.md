# Adder Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Make sure to include the Gitpod id in the screenshot*

![](https://i.imgur.com/miWGA1o.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (adder module here) which takes in 4-bit inputs *a* and *b* and gives 5-bit output *sum*

The values are assigned to the input port using 
```
dut.a.value = 7
dut.b.value = 5
```

The assert statement is used for comparing the adder's outut to the expected value.

1. Compilation Error:
![image](https://user-images.githubusercontent.com/58599984/180593173-e44dc3f9-2afb-4a48-b635-2ad085603699.png)

2. Bug-1:
![image](https://user-images.githubusercontent.com/58599984/180593255-c3b69bc5-fbc0-4276-ac8a-06085dd4006e.png)

3. Bug-2:
![image](https://user-images.githubusercontent.com/58599984/180593301-69e5e5f8-679a-4b8c-a70b-bf60a54f8a03.png)


## Design Bug
We see the following bugs:
1. Compile Error
```
module mux(sel,inp0, inp1, inp2, inp3, inp4, inp5, inp6, inp7, inp8, 
           inp9, inp10, inp11, inp12, inp13, inp14, inp15, inp16, inp17,
           inp18, inp19, inp20, inp21, inp22, inp23, inp24, inp25, inp26,
           inp27, inp28, inp29, inp30, out);      ===> inp31 missing

  input [4:0] sel;
  input [1:0] inp0, inp1, inp2, inp3, inp4, inp5, inp6,
            inp7, inp8, inp9, inp10, inp11, inp12, inp13, 
            inp14, inp15, inp16, inp17, inp18, inp19, inp20,
            inp21, inp22, inp23, inp24, inp25, inp26,
            inp27, inp28, inp29, inp30;        ===> inp31 missing
            
```

```
      5'b11010: out = inp26;
      5'b11011: out = inp27;
      5'b11100: out = inp28;
      5'b11101: out = inp29;   ===> inp30, inp31 missing
      default: out = 0;
    endcase
  end

endmodule 
```
2. Bug-1:
```
     5'b01010: out = inp10;
      5'b01011: out = inp11;
      5'b01101: out = inp12;   ======> wrong case
      5'b01101: out = inp13;
      ```
3. Bug-2:

## Design Fix
Updating the design and re-running the test makes the test pass.

![image](https://user-images.githubusercontent.com/58599984/180593414-a87ad627-6e9c-4fac-af8c-3cccc5c89b80.png)

The updated design is checked in as mux_fixed.v

## Verification Strategy

## Is the verification complete ?

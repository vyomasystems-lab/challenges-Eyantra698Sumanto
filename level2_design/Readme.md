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

  Inputs for example:
  ```
    mav_putvalue_src1 =  0b00000000000000000000000111100101
    mav_putvalue_src2 =  0b11111111111111111010100011011111
    mav_putvalue_src3 =  0b00000000000000000000000000000000
  ```
  
  Then the inputs are given in random.
 If DUT output mismatches the expected output for the above inputs then there is a design bug
## Design Bug Cases
### 1. ANDN 
![image](https://user-images.githubusercontent.com/58599984/180603638-2665f149-c166-4df2-abdf-7d7ff9fe2444.png)

## Design Pass Cases
### 2. ORN 
 ![image](https://user-images.githubusercontent.com/58599984/180603605-b8984b6e-66cb-48d1-9292-f6b8157dc477.png)
### 3. XNOR
![image](https://user-images.githubusercontent.com/58599984/180603678-1e857bac-1bdd-4365-b452-1e5e0da59e67.png)
### 4. SLO
![image](https://user-images.githubusercontent.com/58599984/180603742-eaf4c7ee-8d66-4abd-9768-bcc1d1d44998.png)
### 5. SRO
![image](https://user-images.githubusercontent.com/58599984/180603783-e0b87ce2-229f-4513-a2cb-911a5fec2b2d.png)
### 6. ROL
![image](https://user-images.githubusercontent.com/58599984/180603816-6bbf7c58-d03f-4690-84a6-419cbc549b03.png)
### 7. ROR

![image](https://user-images.githubusercontent.com/58599984/180603854-186e5eb7-8f71-4c8e-91e7-0379ac553a57.png)
### 8. SH1ADD

![image](https://user-images.githubusercontent.com/58599984/180603922-0fbb5edb-4628-47c8-aadb-fe0b96d6fc71.png)
### 9. SH2ADD

![image](https://user-images.githubusercontent.com/58599984/180603980-b8508551-a76c-491e-8d03-343549725ffc.png)
### 10. SH3ADD
![image](https://user-images.githubusercontent.com/58599984/180604018-82679886-83ce-4199-a422-6e48f174fece.png)
### 11. SBCLR
![image](https://user-images.githubusercontent.com/58599984/180604070-4e733054-73a7-4d3e-b101-55e2f3e2426f.png)
### 12. SBSET
![image](https://user-images.githubusercontent.com/58599984/180604114-5bbeeef2-b2ba-4737-8287-c42e10d3b68f.png)

### 13. SBINV
![image](https://user-images.githubusercontent.com/58599984/180604169-e4f89c48-96ac-470f-bf7a-25f08861d16a.png)
### 14. SBEXT
![image](https://user-images.githubusercontent.com/58599984/180604219-be5116ac-9145-4635-93d2-43a8f9c02c93.png)
### 15. GORC
![image](https://user-images.githubusercontent.com/58599984/180604268-5d7acc44-75c8-4323-9bfc-f0554d1e0bfa.png)
### 16. GREV
![image](https://user-images.githubusercontent.com/58599984/180604351-f800f2fd-0ef6-475c-b9c0-6b4413593c24.png)
### 17. CMIX
 ![image](https://user-images.githubusercontent.com/58599984/180604412-957f8845-b005-485c-84c5-e95aa8a966a5.png)
###  18. CMOV
 ![image](https://user-images.githubusercontent.com/58599984/180604437-8d8f8454-4abb-433d-b8d4-3cfcba6ff52f.png)
### 19. FSL
![image](https://user-images.githubusercontent.com/58599984/180604477-ffc32500-83ad-4965-ab24-56059bdb9647.png)
### 20. FSR
![image](https://user-images.githubusercontent.com/58599984/180604511-b5548b19-d9e2-4d19-8778-af95d048ed26.png)
### 21. CLZ
![image](https://user-images.githubusercontent.com/58599984/180609566-f6b35cd8-8cd5-471c-a40b-53a2f59b1d95.png)
### 22. CTZ
![image](https://user-images.githubusercontent.com/58599984/180611046-3488aff1-2fb1-4b5a-953a-2ef95fc27950.png)
### 23. PCNT 
![image](https://user-images.githubusercontent.com/58599984/180611010-2f9b40cb-cf84-4ef5-ad53-6fa4265fe1c7.png)
### 24. SEXT.B
![image](https://user-images.githubusercontent.com/58599984/180611110-433525d5-d309-4aea-b0b3-f684e1095c45.png)
### 25. SEXT.H
![image](https://user-images.githubusercontent.com/58599984/180611150-5c4c4998-dd49-423a-8ca4-19cfd3698e34.png)
### 26. CRC32.B
![image](https://user-images.githubusercontent.com/58599984/180611215-61d9d8fe-a860-4b8a-8db9-c3a155f58a49.png)
### 27. CRC32.H
![image](https://user-images.githubusercontent.com/58599984/180611256-15b067eb-5383-4438-987f-e77277b4ca03.png)
### 28. CRC32.W
![image](https://user-images.githubusercontent.com/58599984/180611300-d47b02b4-2397-4c9c-8e25-c105e8027303.png)
### 29. CRC32C.B
![image](https://user-images.githubusercontent.com/58599984/180611359-9a6fdb2e-55ca-41fc-9acf-e67700749c4a.png)
### 30. CRC32C.H
![image](https://user-images.githubusercontent.com/58599984/180611415-af6f1f10-db45-40ce-9056-d2d7cfa91b4d.png)
### 31. CRC32C.W
![image](https://user-images.githubusercontent.com/58599984/180611461-bc9a8b4b-9aa8-4bff-a4f3-12c785a10cf5.png)
### 32. CLMUL
![image](https://user-images.githubusercontent.com/58599984/180611502-b0c837ae-38c8-433e-ba6a-f4cd150afb22.png)
### 33. CLMULH
![image](https://user-images.githubusercontent.com/58599984/180611597-44646c74-7833-42f7-8912-c1e6fcca9667.png)
### 34. CLMULR
![image](https://user-images.githubusercontent.com/58599984/180611779-889127bb-6772-4869-922b-26ed7a4d26e3.png)
### 35. MIN
![image](https://user-images.githubusercontent.com/58599984/180611841-423b6f9e-3ecf-4f86-8b72-2fb7e01cf2ad.png)
### 35. MAX







## Verification Strategy

## Is the verification complete ?

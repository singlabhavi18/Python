# def num_to_binary(num):
#     if num==0:
#         return 0
#     else:
#         binary_form = ""
#         while num>0:
#             bit = num&1
#             binary_form = str(bit)+binary_form
#             num = num>>1
#         return binary_form
    
# decimal_form = int(input("Enter the decimal number: "))
# Binary = num_to_binary(decimal_form)
# print(f"The binary conversion of {decimal_form} is {Binary}")

dec = int(input("Enter the decimal number: "))
binary = ""

while dec>0:
    binary = str(dec%2)+binary
    dec = dec//2

print(binary)
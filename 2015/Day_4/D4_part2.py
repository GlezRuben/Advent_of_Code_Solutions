import hashlib

secret_key = "ckczppom"
number = 0

continue_process = True
while continue_process:
    str2hash = secret_key + str(number)
    result = hashlib.md5(str2hash.encode())
    result_hex = result.hexdigest()
    if result_hex[:6] == "000000":
        print(number)
        continue_process = False
    number += 1
 
print("The hexadecimal equivalent of hash is : ", result_hex)

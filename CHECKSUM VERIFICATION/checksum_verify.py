import hashlib
import keyboard
import os

while True:
    filename = input("Enter the input file name: ")
    if os.path.isfile(filename):
        break
    else:
        print("Please enter valid filename")
        continue

#hash algorithm
while True:
    try: 
        print("Please choose checksum algorithm:")
        option = int(input("1. MD5\t2. SHA1\t3. SHA256\n"))
    except:
        print("Please enter a valid option")
    
    if option == 1 or option == 2 or option == 3:
        break
    else:
        print("Invalid option...Try Again")
        break
if option == 1:
    hash = hashlib.md5()
elif option == 2:
    hash = hashlib.sha1()
elif option == 3:
    hash = hashlib.sha256()

#Format of checksum
while True:
    try:
        print("Plese choose checksum type:")
        option_inp = input("A.Text\tB.File\n")
    except:
        print("Please enter a valid option")

    option = option_inp.lower()
    if option == 'a' or option =='b' :
        break
    else:
        print("Invalid Option...Try Again")
        continue

if option == "b":
    checksum_file = input("Enter Checksum filename: ")
    checksum_hash = open(checksum_file, "rt")
    checksum_check = checksum_hash.read()
if option == "a":
    checksum_check = str(input("Enter Text: "))

#Heart
with open(filename,"rb") as f:
    for byte_block in iter(lambda: f.read(4096),b""):
        hash.update(byte_block)
hash_check = hash.hexdigest()

print("Please Wait...")
if str(hash_check) == str(checksum_check):
    print("Congrats...This one is original")
else:
    print("You messed up :(...Checksum unverified")
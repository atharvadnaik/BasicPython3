#This script will verify SHA-256 checksum
from timeit import default_timer as timer
import hashlib
start = timer()
sha_file = input("Enter SHA256 txt filename: ")
filename = input("Enter the input file name: ")
sha256_hash = hashlib.sha256()
with open(filename,"rb") as f:
    for byte_block in iter(lambda: f.read(4096),b""):
        sha256_hash.update(byte_block)
sha_hash = open(sha_file, "rt")
a = sha256_hash.hexdigest()
b = sha_hash.read()
print("Please Wait...")
if str(a) == str(b):
    print("Congrats...This one is original")
else:
    print("You messed up :(...SHA-256 checksum unverified")
end = timer()
time = end - start
print(f"Time elapsed: {time}")
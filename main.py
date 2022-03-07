import  hashlib

pass_hash=input("enter md5 hash:")
flag=0
wordlist=input("file name")

try:
    passfile=open(wordlist,"r")
except:
    print("No file found")
    quit()

for word in passfile:
    enc_word=word.encode('utf-8')
    digest=hashlib.md5(enc_word.strip()).hexdigest()

    if digest==pass_hash:
        print("password has been found")
        print("password is " + word)
        flag: int=1
        break

if flag==0:
    print("password is not in the list")


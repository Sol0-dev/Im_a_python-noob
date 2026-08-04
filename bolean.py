import time

print("Connect to admin wifi")
time.sleep(1)

password = input("Enter correct password: ")

if password == "109354080074":
    print("connection: true")

else:
    print("connection: false")
    time.sleep(1)
    print("try again later")

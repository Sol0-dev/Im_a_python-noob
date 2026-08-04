import time

print("Sleep Metric")
time.sleep(1)

sleep = int(input("\nHow many hours did you sleep last night? "))
time.sleep(1)

if sleep >= 6:
    print("\nGreat Keep your day going")

else:
    answer = str(input("\nAre you bussy right now? "))
    time.sleep(1)
    if answer == "yes":
        print("\nI see your hard work")
        time.sleep(2)  # Delays execution for 2 seconds
        print("\nIm so proud of you make sure to finish it, and get some sleep <3")

    else:
        print("\n you might want to consider, to get some sleep :>")

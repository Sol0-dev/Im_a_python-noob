pet = input("cat or dog: ").lower().strip()

if pet == "dog":
  age = int(input("Enter your dog's age: "))
  human_age = age * 7
  print("Your dog human age is", human_age)

if pet == "cat":
  age = int(input("Enter your cat's age: "))
  human_age = age * 6
  print("Your cat humage age is", human_age)

else:
  print("Invalid pet choice! Please enter 'dog' or 'cat'.")

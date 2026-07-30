# Python Shenaniganz

A beginner-friendly collection of Python scripts for anyone learning to code. Each file teaches a different Python concept.

---

## What's Inside

| File | What You will Learn |
|------|-------------------|
| #1_variables.py | Variables, strings, integers |
| #2_temperature.py | User input, type conversion, math formulas |
| #3_BMI_calculator.py | If/elif/else conditions, comparisons |
| #4_hypotenuse.py | Math operators (exponents, square roots) |
| #5_currency.py | Variables, multiplication, multiple inputs |
| #6_bugs.py | Printing, string concatenation |
| variables/script.py | If/else logic, input validation, .lower().strip() |

---

## #1_variables.py - Variables Basics

```
leetname = 'xzizo'
fav_food = 'pork-bun'
valid = 4
invalid = 12
total_reports = valid + invalid

print(leetname, 'who loves', fav_food, 'reported', total_reports, 'reports')
```

**What it does:** Stores info about a bug bounty hunter and prints a sentence.

**What you learn:**
- A **variable** is a box that holds data. `leetname = 'xzizo'` stores the text "xzizo" in a box named leetname.
- **Strings** (text) go in quotes: `'xzizo'`, `'pork-bun'`.
- **Integers** (whole numbers) do not need quotes: `4`, `12`.
- You can add variables together: `valid + invalid` gives `16`.
- `print()` shows things on screen. You can pass multiple items separated by commas.

---

## #2_temperature.py - User Input and Math

```
farenheit = float(input("Enter temperature in farenheit: "))
celsius = (farenheit - 32) / 1.8
print('')
print(celsius, 'celsius')
```

**What it does:** Asks for a temperature in Fahrenheit and converts it to Celsius.

**What you learn:**
- `input()` asks the user for text. The text inside the quotes is the prompt.
- `float()` converts the users text into a decimal number. `input()` always gives text, so you need `float()` to do math.
- **Formula:** Celsius = (Fahrenheit - 32) / 1.8. Python follows math rules (PEMDAS).
- `print('')` prints a blank line for spacing.

---

## #3_BMI_calculator.py - If/Else Conditions

```
height_in_cm = float(input("Enter your height in cm: "))
height_in_m = float(height_in_cm / 100)
height = float(height_in_m * height_in_m)
weight = float(input("Enter your weight in kg: "))
BMI = float(weight / height)

print("Your Body mass index is:", BMI)

if BMI < 18.5:
  print("You are underweight")
elif BMI >= 18.5 and BMI <= 24.9:
  print("You are normal")
elif BMI > 25:
  print("You are overweight")
```

**What it does:** Calculates your Body Mass Index and tells you which category you fall into.

**What you learn:**
- **Multiple inputs:** The script asks for height, then weight.
- **Step-by-step math:** Height is converted from cm to meters (`/ 100`), then squared (`height_in_m * height_in_m`).
- **If/elif/else:** These let your code make decisions.
  - `if BMI < 18.5:` checks the first condition. If true, it runs that block.
  - `elif` means "else if" - it checks the next condition only if the first was false.
  - You can chain as many `elif`s as you need.
- **Comparison operators:** `<` (less than), `>=` (greater than or equal to), `<=` (less than or equal to).
- `and`: `BMI >= 18.5 and BMI <= 24.9` means BOTH conditions must be true.

---

## #4_hypotenuse.py - Exponents and Square Roots

```
a = int(input("enter the value of the a: "))
b = int(input("enter the value of the b: "))
c = ((a ** 2) + (b ** 2)) ** 0.5
print("the value of c is:", c)
```

**What it does:** Calculates the hypotenuse of a right triangle using the Pythagorean theorem.

**What you learn:**
- `int()` converts input to a whole number (integer).
- `**` is the exponent operator. `a ** 2` means "a to the power of 2" (a squared).
- `** 0.5` is the same as a square root. Raising something to the power of 0.5 = square root.
- **Order of operations:** Python calculates `(a ** 2) + (b ** 2)` first (inside the parentheses), then takes the square root of the result.

---

## #5_currency.py - Multiple Conversions

```
in_pesos = int(input("What do you have left in pesos? "))
pesos = in_pesos * 0.00027

in_soles = int(input("What do you have left in soles? "))
soles = in_soles * 0.29

in_reals = int(input("What do you have left in reals? "))
reals = in_reals * 0.20

print(int(pesos + soles + reals))
```

**What it does:** Converts leftover money from 3 currencies to USD and prints the total.

**What you learn:**
- **Repeating a pattern:** The same pattern (ask, convert, store) is used 3 times for different currencies.
- **Exchange rates are just multiplication:** If 1 peso = $0.00027, then N pesos = N * 0.00027.
- **Adding totals:** `pesos + soles + reals` adds all the USD values together.
- `int()` on the result: `int(pesos + soles + reals)` drops the decimal and shows only whole dollars.

---

## #6_bugs.py - Printing

```
butterflies = 10
beetles = 12
ladybugs = 20

total = butterflies + beetles + ladybugs
print('')
print('I caught ', butterflies, ' butterfly!')
print('I caught ', beetles, ' beetle!')
print('I caught ', ladybugs, ' ladybug!')
print('')
print('I caught ', int(total), ' total bugs!')
```

**What it does:** Counts bugs caught and prints a fun summary.

**What you learn:**
- **Multiple variables:** Three separate counters are added together with `+`.
- `int()` is used here too: `int(total)` ensures the number prints as a clean integer.
- **Print with text:** You can mix text and variables in `print()` by separating them with commas.
- **Blank lines for formatting:** `print('')` makes the output look cleaner.

---

## variables/script.py - If/Else with Input Cleaning

```
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
```

**What it does:** Asks if you have a cat or dog, then converts their age to human years.

**What you learn:**
- **Method chaining:** `.lower().strip()` runs two things at once.
  - `.lower()` converts input to lowercase so "DOG", "Dog", and "dog" all work.
  - `.strip()` removes extra spaces so " dog " becomes "dog".
- **If/else logic:**
  - If you pick "dog", it multiplies age by 7.
  - If you pick "cat", it multiplies age by 6.
  - If you type anything else, it prints an error.
- **Bug to watch for:** The second `if` should be `elif`. Try changing `if pet == "cat":` to `elif pet == "cat":` to fix it!

---

## Tips for Beginners

1. **Run the scripts:** `python3 filename.py` in your terminal.
2. **Experiment:** Change numbers, swap text, break things on purpose to see what happens.
3. **Read error messages:** They tell you exactly what went wrong and where.
4. **Type the code yourself:** Copying by hand helps you remember way better than copy-paste.
5. **Use print() to debug:** If something is not working, add `print()` to see what your variables contain.

Happy coding!

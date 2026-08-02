print("Grading System")

prelim = float(input("Whats your grade in Prelim: ")) * 0.2
midterm = float(input("Whats you grade in Miterm: ")) * 0.2
prefinal = float(input("Whats your grade in Prefinal: ")) * 0.4
final = float(input("Whats your grade in finals: ")) * 0.4

final_grade = prelim + midterm + prefinal + final
passed = final_grade <= 3.0

print("Pass: ",passed)

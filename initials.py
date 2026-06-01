# File: initials.py
# Description: Print out my initials R A R as large stylized block letters.
# Assignment Number: 2
#
# Name: REGINALD AUGUSTUS RAYMOND
# STUDENT ID: 2425403341
# Email: 2425403341@live.gctu.edu.gh
# Grader: Augustus BUCKMAN
#
# On my honor, Augustus Buckman, this programming assignment is my own work
# and I have not provided this code to any other student.


def main():
    # Print the small initials line with three periods and "RAR"
    print()
    print("...RAR")
    print()
    
    # Large period made of 4 asterisks
    period_row = "****"
    three_dots = "..."
    
    # Letter 'R' - 12 chars wide, 10 chars high (stylish block R)
    r0 = ".RRRRRRRRR.."
    r1 = ".RRRRRRRRR.."
    r2 = ".RR.....RR.."
    r3 = ".RR.....RR.."
    r4 = ".RRRRRRRRR.."
    r5 = ".RRRRRRRR..."
    r6 = ".RR..RR...."
    r7 = ".RR...RR..."
    r8 = ".RR....RR.."
    r9 = ".RR.....RR."
    
    # Letter 'A' - 12 chars wide, 10 chars high (symmetrical block A)
    a0 = "....AA....."
    a1 = "...AAAA...."
    a2 = "..AA..AA..."
    a3 = ".AA....AA.."
    a4 = "AAAAAAAAAA."
    a5 = "AAAAAAAAAA."
    a6 = "AA......AA."
    a7 = "AA......AA."
    a8 = "AA......AA."
    a9 = "AA......AA."
    
    # Print all 10 rows - each row combines: ... + R + **** + ... + A + **** + ... + R
    # Row 0
    line0 = three_dots + r0 + period_row + three_dots + a0 + period_row + three_dots + r0
    print(line0)
    # Row 1
    line1 = three_dots + r1 + period_row + three_dots + a1 + period_row + three_dots + r1
    print(line1)
    # Row 2
    line2 = three_dots + r2 + period_row + three_dots + a2 + period_row + three_dots + r2
    print(line2)
    # Row 3
    line3 = three_dots + r3 + period_row + three_dots + a3 + period_row + three_dots + r3
    print(line3)
    # Row 4
    line4 = three_dots + r4 + period_row + three_dots + a4 + period_row + three_dots + r4
    print(line4)
    # Row 5
    line5 = three_dots + r5 + period_row + three_dots + a5 + period_row + three_dots + r5
    print(line5)
    # Row 6
    line6 = three_dots + r6 + period_row + three_dots + a6 + period_row + three_dots + r6
    print(line6)
    # Row 7
    line7 = three_dots + r7 + period_row + three_dots + a7 + period_row + three_dots + r7
    print(line7)
    # Row 8
    line8 = three_dots + r8 + period_row + three_dots + a8 + period_row + three_dots + r8
    print(line8)
    # Row 9
    line9 = three_dots + r9 + period_row + three_dots + a9 + period_row + three_dots + r9
    print(line9)
    
    # Print a blank line after the large initials
    print()


if __name__ == "__main__":
    main()
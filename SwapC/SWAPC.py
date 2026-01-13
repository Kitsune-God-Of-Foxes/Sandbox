"""
Solution for SWAPC
S. Payne - January 2026
"""
import sys
import math
import string

def main() -> None:
    Number_of_cases = sys.stdin.readline().rstrip()
    Number_of_cases = int(Number_of_cases)
    Current_Component = sys.stdin.readline().rstrip()
    Current_number, OrigS, OrigW, OrigP, OrigC = Current_Component.split()
    OrigS = int(OrigS)
    OrigW = int(OrigW)
    OrigP = int(OrigP)
    OrigC = int(OrigC)
    CurrentSwapC = OrigS + OrigW + OrigP + OrigC
    CurrentSwapC = int(CurrentSwapC)
    for _ in range(Number_of_cases):
        New_component = str(sys.stdin.readline().rstrip())
        NewNumber, NewS, NewW, NewP, NewC = New_component.split()
        NewS = int(NewS)
        NewW = int(NewW)
        NewP = int(NewP)
        NewC = int(NewC)
        NewSwapC = NewS + NewW + NewP + NewC
        if NewSwapC > CurrentSwapC:
            CurrentSwapC = NewSwapC
            Current_number = NewNumber
    print(Current_number, CurrentSwapC)





  

if __name__ == "__main__":
    main()
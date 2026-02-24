"""
this is the answer to the number war problem on codequest by Sebastian Payne
"""
import sys
import math
import string


def main() -> None:
  count = sys.stdin.readline().rstrip()
  count = int(count)
  for z in range (count):
    numbers  = str(sys.stdin.readline().rstrip())
    P1num1, P1num2, P1num3, P2num1, P2num2, P2num3 = numbers.split()
    if P1num1 > P1num3 and P1num2 > P1num3:
      if P1num1 > P1num2:
        P1Score = P1num1 + P1num2
      else:
        P1Score = P1num2 + P1num1
    elif P1num2 > P1num1 and P1num3 > P1num1:
      if P1num3 > P1num2:
        P1Score = P1num3 + P1num2
      else:
        P1Score = P1num2 + P1num3
    else:
      if P1num1 > P1num3:
        P1Score = P1num1 + P1num3
      else:
        P1Score = P1num3 + P1num1
    
    
    if P2num1 > P2num3 and P2num2 > P2num3:
      if P2num1 > P2num2:
        P2Score = P2num1 + P2num2
      else:
        P2Score = P2num2 + P2num1
    elif P2num2 > P2num1 and P2num3 > P2num1:
      if P2num3 > P2num2:
        P2Score = P2num3 + P2num2
      else:
        P2Score = P2num2 + P2num3
    else:
      if P2num1 > P2num3:
        P2Score = P2num1 + P2num3
      else:
        P2Score = P2num3 + P2num1
    P2Score = int(P2Score)
    P1Score = int(P1Score)
    if P2Score < P1Score:
      print("PLAYER 1")
    elif P2Score > P1Score:
      print("PLAYER 2")
    else: print("WAR!")


  

if __name__ == "__main__":
  main()

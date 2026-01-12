import sys
import math
import string

def main() -> None:
  case_count: int = int(sys.stdin.readline().rstrip())  
  for _ in range(case_count):
    color: str = sys.stdin.readline().rstrip()
  if color == "red" or color == "blue" or color =="yellow":
    print(F"No colors need to be mixed to make {color}.")
  elif color == "orange" or color == "red-orange" or color == "yellow-orange":
    print(F"In order to make {color}, red and yellow must be mixed.")
  elif color == "green" or color == "blue-green" or color == "yellow-green":
    print(F"In order to make {color} blue and yellow must be mixed.")
  else:
    print(F" In order to make {color} blue and red must be mixed.")



  

if __name__ == "__main__":
  main()
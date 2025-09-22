"""
AP Computer Science Principles Sandbox
This is a repo you can use to store small warm-up problems and try out code.
"""

def main() -> None:
  total_students: int = int(input())
  group_size: int = int(input())
  num_groups: int = int(total_students // group_size)
  leftovers: int = int(total_students % group_size)
  
  print(f"{num_groups} of {group_size} were formed.)")
  if leftovers > 1 or leftovers < 1:
    print(f"{leftovers} people were not in a group")
  else:
    print(f"{leftovers} person was not in a group")

if __name__ == "__main__":
  main()

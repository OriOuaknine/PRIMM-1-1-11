"""
PRIMM: 1+1 = 11
program displays the first number inputted and with the second number inputted
Name - Date
"""
#this displays the number 1 plus the number 2, but doesn't include the values
def main():
  
    num1: float = float("Enter a number: ")
    num1 = float(num1)
  
    num2: float = float("Enter another number: ")
    num2 = float(num2)
  
    total: float = num1+num2

    print(f"{num1} + {num2} = {total}")

if __name__ == "__main__":
  main()

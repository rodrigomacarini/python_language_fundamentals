import sum
import subtraction

value_a =  input("Value A:")
value_b =  input("Value B:")
operation = input("Operation:")
def main():

    if operation == "-":
        result = subtraction.subtraction(float(value_a), float(value_b))
        return result
    
    if operation == "+":
        result = sum.sum15(float(value_a), float(value_b))
        return result
if __name__ == "__main__":
    main()
    
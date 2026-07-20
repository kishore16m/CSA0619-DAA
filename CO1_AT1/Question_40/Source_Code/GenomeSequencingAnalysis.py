import math


def master_theorem(a, b, k):
    exponent = math.log(a, b)

    print("Genome Sequencing Analysis")
    print("--------------------------")
    print(f"Recurrence Relation : T(n) = {a}T(n/{b}) + n^{k}")
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"f(n) = n^{k}")
    print(f"log_{b}({a}) = {exponent:.3f}")

    if abs(exponent - k) < 1e-9:
        case = "Case 2"
        complexity = f"Theta(n^{k} log n)"
    elif exponent > k:
        case = "Case 1"
        complexity = f"Theta(n^{exponent:.3f})"
    else:
        case = "Case 3"
        complexity = f"Theta(n^{k})"

    print(f"\nMaster Theorem : {case}")
    print(f"Time Complexity : {complexity}")

    print("\nScalability Analysis")
    print("--------------------")
    print("Small Dataset      : Fast")
    print("Medium Dataset     : Moderate")
    print("Large Dataset      : Efficient")
    print("Very Large Dataset : Better than quadratic algorithms")


def main():
    master_theorem(3, 2, 1)


if __name__ == "__main__":
    main()
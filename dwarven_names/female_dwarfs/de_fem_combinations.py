from math import factorial

def calculate_combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def main():
    with open("de_fem_final.txt", "r") as f:
        syllables = f.read().split()

    total_combinations = 0

    with open("de_fem_christian_combos.txt", "w") as output_file:
        for length in range(1, 4):
            num_combinations = calculate_combinations(len(syllables), length)
            total_combinations += num_combinations

            output_file.write(f"Combinations of length {length}: {num_combinations}\n")
            print(f"Combinations of length {length}: {num_combinations}")

        output_file.write(f"Total combinations: {total_combinations}\n")
        print(f"Total combinations: {total_combinations}")

if __name__ == "__main__":
    main()

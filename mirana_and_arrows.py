
# Function to find the maximum number of arrows Mirana can release without risking her life
def max_arrows(N, K, A):
    A.sort()
    current_sum = 0
    max_arrows = 0
    for distance in A:
        current_sum += distance
        if current_sum > K:
            current_sum -= distance
            continue
        max_arrows += 1
    return max_arrows

# Main program function
def main_program_mirana():
    # Read input
    N, K = map(int, input("Enter N and K separated by a space: ").split())
    A = list(map(int, input(f"Enter the distances of the {N} arrows separated by spaces: ").split()))
    
    # Call the max_arrows function and print the result
    result = max_arrows(N, K, A)
    print(f"The maximum number of arrows Mirana can release is: {result}")

# Uncomment the next line to run the program
main_program_mirana()


# Function to check if the string is "magical" 
def is_magic_string(s):
    sorted_s = ''.join(sorted(s))
    carl_string = ''
    for char in sorted_s:
        if carl_string and char == carl_string[0]:
            return 'NO'
        else:
            option1 = char + carl_string
            option2 = carl_string + char
            if  option1 in s:
                carl_string = option1
            elif option2 in s:
                carl_string = option2
            else:
                return "NO"
    return "YES" if carl_string == s else "NO"

# Function to return the results as a string with each answer on a new line
def process_magic_strings_str(T, string_list):
    results = []
    for i in range(T):
        results.append(is_magic_string(string_list[i]))
    return "\n".join(results)

# Main program function
def main_program():
    T = int(input("Enter the number of test cases: "))
    test_strings = []
    for i in range(T):
        test_string = input(f"Enter test string {i + 1}: ")
        test_strings.append(test_string)
    result_str = process_magic_strings_str(T, test_strings)
    print("Results:")
    print(result_str)

main_program()

try:
    user_input = input("Enter numbers separated by space: ").strip()

    if not user_input:   # handles empty input
        print("Array Empty!!!")
    else:
        arr = list(map(int, user_input.split()))
        print("Maximum:", max(arr))

except ValueError:
    print("Invalid input! Please enter only integers.")
try:
    user_input = input("Enter numbers separated by space: ").strip()

    if not user_input:   # Edge case: empty input
        print("Array Empty!!!")
    else:
        arr = list(map(int, user_input.split()))

        if len(arr) <= 1:   # Edge case: single element
            print("Result:", arr)
        else:
            slow = 0
            for fast in range(1, len(arr)):
                if arr[slow] != arr[fast]:
                    slow += 1
                    arr[slow] = arr[fast]

            print("Result:", arr[:slow+1])

except ValueError:
    print("Invalid input! Please enter integers only.")
def out_of_range_check(value):
    return value not in [0, 20, 40, 60, 80, 100, 120]

progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0

continue_program = True

while continue_program:
    try:
        pass_credits = int(input("Enter credits at pass: "))
        if out_of_range_check(pass_credits):
            print("Invalid input! Please enter a valid value.")
            continue

        defer_credits = int(input("Enter credits at defer: "))
        if out_of_range_check(defer_credits):
            print("Invalid input! Please enter a valid value.")
            continue

        fail_credits = int(input("Enter credits at fail: "))
        if out_of_range_check(fail_credits):
            print("Invalid input! Please enter a valid value.")
            continue

        total_credits = pass_credits + defer_credits + fail_credits

        if 0 <= total_credits <= 120:
            if pass_credits == 120 and defer_credits == 0 and fail_credits == 0:
                print("Progress")
                progress_count += 1
            elif pass_credits == 100 and 0 <= defer_credits <= 20 and 0 <= fail_credits <= 20:
                print("Progress (module trailer)")
                trailer_count += 1
            elif 0 <= pass_credits <= 80 and 0 <= defer_credits <= 120 and 0 <= fail_credits <= 60:
                print("Do not progress - module retriever")
                retriever_count += 1
            else:
                print("Exclude")
                exclude_count += 1
        else:
            print("Incorrect total")

        while True:
            option = input("Enter 'y' to input another set of data or 'q' to quit and view results: ").lower()
            if option == 'q':
                continue_program = False
                break  # exit the inner loop
            elif option == 'y':
                break  # continue the outer loop
            else:
                print("Invalid option. Please enter 'y' or 'q'.")

    except ValueError:
        print("Integer required")

# Display summary
print("\nSummary:")
print(f"Progress count: {progress_count}")
print(f"Trailer count: {trailer_count}")
print(f"Retriever count: {retriever_count}")
print(f"Exclude count: {exclude_count}")

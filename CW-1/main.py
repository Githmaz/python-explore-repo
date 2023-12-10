from design import *
from bar_chart import *

#____ Result count storage for the graph ___#
result_counts = {
        "Progress": 0,
        "Trailer": 0,
        "Retriever": 0,
        "Exclude": 0
    }

#____  Storing the result data ___#
result_data = []

#____ get the old result data from the text file ___#
try:                                               
    with open('result_data.txt', 'r') as file:
        for line in file:
            result_data.append(line.strip())
except FileNotFoundError:
    # if file doenst exit
    result_data = []

#______ Appends a result to the list and displays it _____#
def add_and_show_results(result):
    global result_data
    result_data.append(result)
    print("-" * (len(result)+4))
    print(f"  {result}")
    print("-" * (len(result)+4))

#___________ Validates input value within allowed range ___________#

def out_of_range_check(value):
    if value not in [0, 20, 40, 60, 80, 100, 120]:
        print(f"{value} is out of range.")
        return True
    return False

#______ Gets user inputs for credits, validates, categorizes results, and displays the outcome. _____#

def get_user_inputs():
    global result_counts,result_data

    while True:
        try:
             #  Input credits for pass, defer, and fail.
            pass_credits = int(input("\nEnter credits at pass  : "))
            if out_of_range_check(pass_credits):
                continue

            defer_credits = int(input("Enter credits at defer : "))
            if out_of_range_check(defer_credits):
                continue

            fail_credits = int(input("Enter credits at fail  : "))
            if out_of_range_check(fail_credits):
                continue
            
            # Validate the total credits and determine the result category.
            if pass_credits + defer_credits + fail_credits == 120:

                if pass_credits == 120:
                    add_and_show_results(f"Progress - {pass_credits}, {defer_credits}, {fail_credits}")
                    result_counts["Progress"] += 1
                elif pass_credits == 100:
                    add_and_show_results(f"Progress (module trailer) - {pass_credits}, {defer_credits}, {fail_credits}")
                    result_counts["Trailer"] += 1
                elif fail_credits >= 80:
                    add_and_show_results(f"Exclude - {pass_credits}, {defer_credits}, {fail_credits}")
                    result_counts["Exclude"] += 1
                else :
                    add_and_show_results(f"Do not progress - module retriever - {pass_credits}, {defer_credits}, {fail_credits}")
                    result_counts["Retriever"] += 1

            else:
                print("\nIncorrect total")
                continue

            break

        except ValueError:
            print("Integer required")

#______ Main program loop that interacts with the user ______#
def main():
    while True:
        welcome()
        option = input("\nEnter Your option (T,S,Q) : ").lower()

        # if user is a teacher
        if option == 't':
            while True:
                get_user_inputs()
                option = input("\nEnter 'Y' to input again, or 'Any-Key' to view results and go to menu: ").lower()
                if option != 'y':
                    break
                
            # Display results 
            print("\n\n                   Results",end="\n\n")
            [print(item) for item in result_data]
            print("\n=================================================")

            # Save results to the file.
            with open('result_data.txt', 'w') as file:
                for data in result_data:
                    file.write(data + '\n')

            # Draw a bar chart
            draw_bar_chart(result_counts)

        # if user is a Student
        elif option == 's':
            get_user_inputs()
            option = input("\nEnter 'M' to go back to menu, or  'Any-key' to quit :  " ).lower()
            if option == 'm':
                continue
            return
        
        elif option == 'q':
            return
        else :
           print(f"\n\n______ \"{option}\" is an invalid option. Please enter a valid option. _______")
                
#______Entry point for the program______#
if __name__ == "__main__":
    main()

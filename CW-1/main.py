from validations import *
from design import *
from bar_chart import *

result_counts = {}

try:
    with open("result_counts.txt", "r") as file:
        for line in file:
            category, count = line.strip().split(": ")
            result_counts[category] = int(count)

except FileNotFoundError:
    result_counts = {
        "Progress": 0,
        "Trailer": 0,
        "Retriever": 0,
        "Exclude": 0
    }


result_data = ["Do not progress - module retriever - 20, 80, 20","Progress - 120, 0, 0"]

def add_and_show_results(result):
    global result_data
    result_data.append(result)
    print("-" * (len(result)+4))
    print(f"  {result}")
    print("-" * (len(result)+4))

def get_user_inputs():
    global result_counts,result_data

    while True:
        try:
            pass_credits = int(input("\nEnter credits at pass  : "))
            if out_of_range_check(pass_credits):
                continue

            defer_credits = int(input("Enter credits at defer : "))
            if out_of_range_check(defer_credits):
                continue

            fail_credits = int(input("Enter credits at fail  : "))
            if out_of_range_check(fail_credits):
                continue

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


def main():
    while True:
        welcome()
        option = input("\nEnter Your option (T,S,Q) : ").lower()

        if option == 't':
            while True:
                get_user_inputs()
                option = input("\nEnter 'Y' to input again, or 'any-key' to view results: ").lower()
                if option != 'y':
                    break
            
            print("\n\n                   Results",end="\n\n")
            [print(item) for item in result_data]
            print("\n=================================================")

            with open("result_counts.txt", "w") as file:
                for category, count in result_counts.items():
                    file.write(f"{category}: {count}\n")

            draw_bar_chart(result_counts)


        elif option == 's':
            get_user_inputs()
            option = input("\nEnter 'M' to go back to menu, or  'Any-key' to quit:  " ).lower()
            if option == 'm':
                continue
            return
        
        elif option == 'q':
            return
        else :
           print(f"\n\n______ \"{option}\" is an invalid option. Please enter a valid option. _______")
                

if __name__ == "__main__":
    main()

from graphics import *

#______ Displays a welcome message and menu options _______#

def welcome():

    print("""
 __      __       .__  .__                                
/  \\    /  \\ ____ |  | |  |   ____  ____   _____   ____   
\\   \\/\\/   _/ __ \\|  | |  | _/ ___\\/  _ \\ /     \\_/ __ \\  
 \\        /\\  ___/|  |_|  |_\\  \\__(  <_> |  Y Y  \\  ___/  
  \\__/\\  /  \\___  |____|____/\\___  \\____/|__|_|  /\\___  > 
       \\/       \\/               \\/            \\/     \\/ 
""",end="\n\n")
    
    print("1. Use as a teacher (Enter \"T\")")
    print("2. Use as a student (Enter \"S\")")
    print("3. Exit (Enter \"Q\")")



#____  Storing the result data ___#

result_counts = {
        "Progress": 0,
        "Trailer": 0,
        "Retriever": 0,
        "Exclude": 0
    }

#______ Appends a result to the list and displays it _____#

def show_results(result):
    print("-" * (len(result)+4))
    print(f"  {result}")
    print("-" * (len(result)+4))

#___________ Validates input value within allowed range ___________#

def out_of_range_check(value):
    if value not in [0, 20, 40, 60, 80, 100, 120]:
        print(f"\n{value} is out of range.")
        return True
    return False

#_______ Draws a bar chart based on the given result counts ________#

def draw_bar_chart(result_counts):
    # getting the result count

    win = GraphWin("histogram", 600, 500) 
    win.setBackground("white")

    title = Text(Point(win.getWidth()/2, 25), "Histogram Results")
    title.setSize(25)
    title.draw(win)

    categories = list(result_counts.keys())
    values = list(result_counts.values())

    bar_width = 125  
    spacing = 10
    x_start = 40
    y_scale = 350/max(values)

    for i in range(len(categories)):
        x = x_start + i * (bar_width + spacing)
        y = win.getHeight() - values[i] * y_scale - 75
        
        bar = Rectangle(Point(x, win.getHeight() - 75), Point(x + bar_width, y))
        bar.setFill(["#FF9999", "#99FF99", "#9999FF", "#FFD700"][i])  
        bar.draw(win)

        label = Text(Point(x + bar_width / 2, win.getHeight() - 65), categories[i])
        label.setSize(15)
        label.draw(win)

        value_label = Text(Point(x + bar_width / 2, y - 10), str(values[i]))
        value_label.setSize(15)
        value_label.draw(win)

    total_label = Text(Point(win.getWidth() / 2, win.getHeight() -20), f"Outcomes in Total : {sum(values)}")  
    total_label.setSize(20)
    total_label.draw(win)


    win.getMouse()
    win.close()



#______ Gets user inputs for credits, validates, categorizes results, and displays the outcome. _____#

def get_user_inputs():
    global result_counts


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
                    show_results("Progress")
                    result_counts["Progress"] += 1
                elif pass_credits == 100:
                    show_results("Progress (Module Trailer)")
                    result_counts["Trailer"] += 1
                elif fail_credits >= 80:
                    show_results(f"Exclude")
                    result_counts["Exclude"] += 1
                else :
                    show_results(f"Module Retriever")
                    result_counts["Retriever"] += 1
            else:
                print("\nTotal Incorrect")
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
                option = input("\nEnter 'Y' to input again, 'Q' to exit and view results, or 'Any-Other-Key' to view results and go to Menu: ").lower()
                if option == 'q':
                    draw_bar_chart(result_counts)
                    return
                elif option != 'y':
                    break

            draw_bar_chart(result_counts)

        # if user is a Student
        elif option == 's':
            get_user_inputs()
            option = input("\nEnter 'M' to go back to menu, or  'Any-Other-Key' to quit :  " ).lower()
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

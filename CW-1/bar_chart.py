from graphics import *


#_______ Draws a bar chart based on the given result counts ________#

def draw_bar_chart(result_counts):
    win = GraphWin("histogram", 600, 500) 
    win.setBackground("white")

    title = Text(Point(win.getWidth()/2, 25), "Histogram Results")
    title.setSize(25)
    title.draw(win)

    categories = list(result_counts.keys())
    values = list(result_counts.values())
    total_value = sum(values)

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
        value_label.setSize(10)
        value_label.draw(win)

    total_label = Text(Point(win.getWidth() / 2, win.getHeight() -20), f"Outcomes in Total : {total_value}")  
    total_label.setSize(20)
    total_label.draw(win)


    win.getMouse()
    win.close()
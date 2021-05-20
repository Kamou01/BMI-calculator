# Imports all toll from tkinter
from tkinter import *

# Initialization of window
gui = Tk()

# Sets window size, title and colour
gui.geometry("400x400")
gui.title("BMI Calculator")
gui.config(bg="Dark Orange")

# Setting values
age = IntVar()
height_ans = IntVar()
bmi_answ = IntVar()
weight = IntVar()
gender = IntVar()


# Calculates the BMI and gives one of the three results if all values are added
# Also checks if entered values are not zero if zero display 0
def calculate_bmi():
    try:
        result = float(ans.get()) / (float(height.get()) * float(height.get()))
        bmi_answ.set(result)
    except ZeroDivisionError:
        weight.set(0)
        height_ans.set(0)
        bmi_answ.set(0)
        return
    if result < 18.5:
        resLabelText.set("Category: Underweight!")
    if 18.5 < result < 25:
        resLabelText.set("Category: Normal")
    if 25 < result < 30:
        resLabelText.set("Category: Overweight!!")
    if result > 30:
        resLabelText.set("Category: Obese!!!")
    return


# Labels and entry fields added and set using pack
# Age label
ageLabelText = StringVar()
ageLabelText.set("Age: ")
massLabel = Label(gui, textvariable=ageLabelText)
massLabel.pack()

# Age entry field
ans = Entry(gui, textvariable=age)
ans.pack()

# Gender label
genderLabelText = StringVar()
genderLabelText.set("Gender: ")
massLabel = Label(gui, textvariable=genderLabelText)
massLabel.pack()

# Gender Entry field
ans = Entry(gui, textvariable=gender)
ans.pack()

# mass label
mLabelText = StringVar()
mLabelText.set("Mass in kg: ")
massLabel = Label(gui, textvariable=mLabelText)
massLabel.pack()

# mass entry field
ans = Entry(gui, textvariable=weight)
ans.pack()

# Label for height
hLabelText = StringVar()
hLabelText.set("Height in m: ")
heightLabel = Label(gui, textvariable=hLabelText)
heightLabel.pack()

# height entry field
height = Entry(gui, textvariable=height_ans)
height.pack()

# Button and label for BMI calculation
button = Button(gui, text="Calculate BMI", command=calculate_bmi)
button.pack(padx=15, pady=15)
bmiLabelText = StringVar()
bmiLabelText.set("Your BMI is: ")
bmiLabel = Label(gui, textvariable=bmiLabelText)
bmiLabel.pack()

# answer field for BMI
bmi = Entry(gui, textvariable=bmi_answ)
bmi.pack()

# result label text
resLabelText = StringVar()
resLabelText.set(" Category: ")
resLabel = Label(gui, textvariable=resLabelText)
resLabel.pack()

# Ensures that the window remains open until terminated by the user
gui.mainloop()

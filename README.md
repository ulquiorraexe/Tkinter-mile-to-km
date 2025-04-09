# Mile to Km Converter

This is a simple Tkinter-based application that converts miles to kilometers. The user can input a value in miles, click the "Calculate" button, and the app will display the corresponding value in kilometers.

## Features
- Input miles in a text field.
- Convert the miles value to kilometers.
- Display the result on the same window.

## Code Explanation

1. **Importing Tkinter**
   - The first line imports the Tkinter library, which is used to create the graphical user interface (GUI) for the application. 
   - Tkinter provides tools to create various widgets like buttons, labels, and text entry fields.

   ```python
   from tkinter import *

2. **Defining the "convert" function**
   - The 'convert' function is called when the user clicks the "Calculate" button.
   - It gets the value entered in the input field (in miles), converts it to kilometers by multiplying by 1.609344, and then updates the 'result' label to display the converted value in kilometers.

   ```python
   def convert():
    miles = float(input.get())  # Getting the input value (miles) and converting it to a float
    kilometer = round(miles * 1.609344)  # Converting miles to kilometers
    result.config(text=kilometer)  # Updating the result label with the calculated kilometers

3. **Setting up the main window**
   - The next block of code sets up the main window where the application will run.
   - `window` is the Tkinter window object.
   - The window title is set to "Mile to Km Converter".
   - The window's size is set to a minimum of 200x30 pixels, and padding of 20 pixels is added around the window's edges.
  
   ```python
   window = Tk()
   window.title("Mile to Km Converter")
   window.minsize(width=200, height=30)
   window.config(padx=20, pady=20)

4. **Creating the input field for miles**
   - This creates an entry widget where the user can input the number of miles they want to convert.
   - The width is set to 7 characters, which defines how many characters fit in the input box.

   ```python
   input = Entry(width=7)
   input.grid(column=1, row=0)  # Positioning the input widget at row 0, column 1 in a grid layout

5. **Creating labels**
   - Labels are created to display text on the window.
       - `miles` label displays the word "miles".
       - `is_equal` label displays "is equal to".
       - `result` label is initially set to "0", and this is where the result will be displayed.
       - `km` label displays "km", showing the unit of the converted value.

   ```python
   miles = Label(text="Miles")
   is_equal = Label(text="is equal to")
   result = Label(text="0")
   km = Label(text="km")

6. **Placing the labels in a grid layout**
   - The labels are placed in a grid layout using the `.grid()` method. It specifies the row and column positions for each widget in the window.

   ```python
   miles.grid(column=2, row=0)
   is_equal.grid(column=0, row=1)
   result.grid(column=1, row=1)
   km.grid(column=2, row=1)

7. **Creating the Calculate Button**
   - The 'calculator' button is created with the text "Calculate".
   - The `command` parameter is set to the `convert` function, meaning that when the button is clicked, the `convert` function will be executed.

   ```python
   calculator = Button(text="Calculate", command=convert)
   calculator.grid(column=1, row=2)  # Positioning the button at row 2, column 1 in the grid

8. **Running the main loop**
   - The Tkinter main loop `(window.mainloop())` keeps the application running, waiting for user actions (like button clicks).
   - It keeps the window open and interactive until the user closes it.

   ```python
   window.mainloop()

## Installation

To use this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/ulquiorraexe/tkinter-mile-to-km.git
2. Navigate to the project directory:
   ```bash
   cd tkinter-mile-to-km
3. Run the Python script:
   ```bash
   python main.py

## Example

1. Enter the miles value in the input field, for example, `5`.
2. Click the "Calculate" button.
3. The result, `8`, will be displayed, representing `5 miles` in kilometers.

## Notes

- The conversion is based on the formula: 1 mile = 1.609344 kilometers.
- The application will continue to run until the user closes the window.

## License

This project does not have a license.

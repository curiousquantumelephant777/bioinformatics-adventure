
## $\color{#4B0082}{\text{🐘 Overview of Common Python Functions 🐘 }}$ 

### $\color{#9370DB}{\text{NumPy (Numerical Computing and Arrays)}}$
$\color{#9370DB}{\textbf{✦ Applications:}}$ Fast numerical operations and multi-dimensional arrays (like in linear algebra or quantum physics simulations)

- $\color{#d30a7c}{\texttt{np.array():}}$ Creates an N-dimensional NumPy array from a Python list or sequence
  - Example: $\color{#D95F02}{\texttt{velocity\ =\ np.array([7,\ 4,\ 5,\ 3])}}$
- $\color{#d30a7c}{\texttt{np.arange():}}$ Generates a specific number of evenly spaced values within a given interval using a step size similar to Python’s range function
- $\color{#d30a7c}{\texttt{np.linspace():}}$ Generates a specified number of evenly spaced values between start and stop value.
  - Example for graphing: $\color{#D95F02}{\texttt{x\ =\ np.linspace(-10,\ 10,\ 1)}}$
- $\color{#d30a7c}{\texttt{np.zeros():}}$ Makes a new array of a given shape filled with 0s
- $\color{#d30a7c}{\texttt{np.ones():}}$ Creates a new array of a given shape filled with 1s
- $\color{#d30a7c}{\texttt{np.reshape():}}$ Changes the shape or dimensions of an array without changing its underlying data
- $\color{#d30a7c}{\texttt{np.concatenate():}}$ Joins two or more existing arrays along a specified axis.
- $\color{#d30a7c}{\texttt{np.vstack():}}$ Stacks arrays vertically into a single array
- $\color{#d30a7c}{\texttt{np.sum():}}$ Calculates the sum of array elements (overall or along a specific axis)
- $\color{#d30a7c}{\texttt{np.mean():}}$ Computes arithmetic average of array elements
- $\color{#d30a7c}{\texttt{np.std():}}$ Calculates the standard deviation of array elements
- $\color{#d30a7c}{\texttt{np.dot():}}$ Computes the dot product of two arrays (or matrix multiplication for 2D arrays)
- $\color{#d30a7c}{\texttt{np.random.randint():}}$ Generates random integers from a low (inclusive) to high (exclusive) range

---

### $\color{#9370DB}{\text{Matplotlib (Data Visualization)}}$
$\color{#9370DB}{\textbf{✦ Applications:}}$ Creating plots and figures (like visualizing population distribution)

- $\color{#d30a7c}{\texttt{plt.figure():}}$ Creates a new figure container/canvas
- $\color{#d30a7c}{\texttt{plt.subplots():}}$ Creates a figure and a grid of subplot axes
- $\color{#d30a7c}{\texttt{plt.plot():}}$ Plots data as lines or markers (common use: line charts)
- $\color{#d30a7c}{\texttt{plt.bar():}}$ Creates a vertical bar chart to compare quantities across categories (example: the energy of different photons)
- $\color{#d30a7c}{\texttt{plt.scatter():}}$ Makes a scatter plot so you can see relationships between two numerical values
- $\color{#d30a7c}{\texttt{plt.hist():}}$ Plots a histogram showing the frequency distribution of a continuous variable
- $\color{#d30a7c}{\texttt{plt.pie():}}$ Creates a pie chart showing proportional parts of a whole.
- $\color{#d30a7c}{\texttt{plt.boxplot():}}$ Makes a box-and-whisker plot to visualize median, quartiles, and possible outliers
- $\color{#d30a7c}{\texttt{plt.title():}}$ Sets a title for the plot
- $\color{#d30a7c}{\texttt{plt.xlabel():}}$ Sets a label for the x-axis
- $\color{#d30a7c}{\texttt{plt.ylabel():}}$ Sets a label for the y-axis
- $\color{#d30a7c}{\texttt{plt.legend():}}$ Displays legend for identifying labels of plotted series
  - Example: Showing the concentration of a given compound at different pH (the pH levels would be shown in the legend)
- $\color{#d30a7c}{\texttt{plt.savefig():}}$ Saves the current figure to an image file (like $\color{#D95F02}{\texttt{.png,\ .jpg,\ .pdf}}$)

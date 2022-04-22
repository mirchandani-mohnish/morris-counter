import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axis import Axis

from morriscounter import MorrisCounter

'''
~~ plot_morriscounter.py ~~
  * Responsible for creating the graphs and testing the Morris Counter
  * Bounds defined within the test function 
    - uppers :- The Upper bounds 
    - lowers :- The Lower bounds
    - estimates :- The estimated count
    - actuals :- The aactual number of values
  * These store the respective values of the counter
  * These values are then plotted and stored as a png file. 
'''



'''
~~ Test Function ~~
* Program Flow 
  - For every value from 1 to N: 
    - increment the counter
    - check all four values 
    - append the values in their respective arrays
* Generate plots based on the arrays formed 
'''

def test(counter: MorrisCounter, n: int, axis: Axis) -> None:
  uppers, lowers, estimates, actuals = [], [], [], []
  for N in range(1, n+1): 
    counter.increment() 
    # Counter Incremented
    actual = N # The actual number which should be displayed 
    estimate = counter.count # Count being stored in the counter. 
    lower = (1-counter.epsilon)*N 
    upper = (1+counter.epsilon)*N


    actuals.append(actual)
    estimates.append(estimate)
    lowers.append(lower)
    uppers.append(upper)

    # print(f"{actual=}, {estimate=:.8f} in [{lower:.8f}, {upper:.8f}]")

  # Create the graphs based on the four arrays. 
  MARKER_SIZE=.01
  LINE_WIDTH=.5
  axis.plot(actuals, estimates, label="estimate", marker="o", color="green", markersize=MARKER_SIZE, linewidth=LINE_WIDTH)
  axis.plot(actuals, lowers, label="lower bound", color="red", linestyle="dashed", markersize=MARKER_SIZE, linewidth=LINE_WIDTH)
  axis.plot(actuals, uppers, label="upper bound", color="red", linestyle="dashed", markersize=MARKER_SIZE, linewidth=LINE_WIDTH)
  axis.plot(actuals, actuals, label="actual", linestyle="dashed", color="grey", markersize=MARKER_SIZE, linewidth=LINE_WIDTH, alpha=0.3)
  axis.set_title(rf"$\varepsilon={counter.epsilon:.3g}$, $\delta={counter.delta:.3g}$", fontsize=6, y=-0.2)
  axis.axis('off')




'''
~~ Main Function ~~
* Respective inputs are taken 
  - accuracy: 
  - max_failure_rate:
  - bins: 
* An array is created to mark values based on the number of bins we create. 
  - The accuracy is restricted between 0.5 and 0.95, we create an evenly distributed array of length (bins) across the range [0.5, 0.95)
  - The max_failure_rate is restricted between 0.05 and 0.55, we create an evenly distributed array of length (bins) across the range [0.05, 0.45)
* A counter instance is called over each corresponding value of accuracy and max_failuire_rate
* This instance is passed to the test function for generating the graph and testing bounds
* The graphs are finally saved in the png file. 
'''


if __name__ == '__main__':
  n = 100
  bins = 10
  fig, axes = plt.subplots(bins, bins)
  print(np.linspace(.5, .95, bins))
  for r, accuracy in enumerate(np.linspace(.5, .95, bins)): # Create an array of evenly distributed numbers between 0.5 and 0.95 
    for c, max_failure_rate in enumerate(np.linspace(0.05, .45, bins)): 
      print(f"{accuracy=}, {max_failure_rate=}") 
      counter = MorrisCounter(accuracy=accuracy, max_failure_rate=max_failure_rate) # Iterate across each array and make a counter instance
      test(counter, n=n, axis=axes[r][c]) # Pass the counter instance to the test function. 
      


  # Create and Save the graph
  fig.suptitle(f"Morris(a) Counter, {n=}")
  handles, labels = axes[-1][-1].get_legend_handles_labels()
  fig.legend(handles, labels, loc='upper left', prop={'size': 6})
  fig.savefig("plots/morris-a.png", dpi=500)






import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axis import Axis

from morriscounter import MorrisCounter

'''
The following test file is only responsible for creating the graphs which are found
We define "uppers, lowers, estimates, actuals" and keep appending the respective values of the counter 
upon each loop, into the respective arrays. 

This gets an array for each field. 

This is then consecutively plotted on the chart. 
'''
def test(counter: MorrisCounter, n: int, axis: Axis) -> None:
  uppers, lowers, estimates, actuals = [], [], [], []
  for N in range(1, n+1):
    counter.increment()
    # assert (1-counter.epsilon)*N <= counter.count <= (1+counter.epsilon)*N
    actual = N
    estimate = counter.count
    lower = (1-counter.epsilon)*N
    upper = (1+counter.epsilon)*N

    actuals.append(actual)
    estimates.append(estimate)
    lowers.append(lower)
    uppers.append(upper)

    # print(f"{actual=}, {estimate=:.8f} in [{lower:.8f}, {upper:.8f}]")

  # The following portion is responsible for the creation of the respective graphs we see.
  MARKER_SIZE=.01
  LINE_WIDTH=.5
  axis.plot(actuals, estimates, label="estimate", marker="o", color="green", markersize=MARKER_SIZE, linewidth=LINE_WIDTH)
  axis.plot(actuals, lowers, label="lower bound", color="red", linestyle="dashed", markersize=MARKER_SIZE, linewidth=LINE_WIDTH)
  axis.plot(actuals, uppers, label="upper bound", color="red", linestyle="dashed", markersize=MARKER_SIZE, linewidth=LINE_WIDTH)
  axis.plot(actuals, actuals, label="actual", linestyle="dashed", color="grey", markersize=MARKER_SIZE, linewidth=LINE_WIDTH, alpha=0.3)
  axis.set_title(rf"$\varepsilon={counter.epsilon:.3g}$, $\delta={counter.delta:.3g}$", fontsize=6, y=-0.2)
  axis.axis('off')



if __name__ == '__main__':
  n = 100
  bins = 10
  fig, axes = plt.subplots(bins, bins)
  print(np.linspace(.5, .95, bins))
  for r, accuracy in enumerate(np.linspace(.5, .95, bins)): #np.linspace creates an array of numbers between 0.5 and 0.95 where the array length is "bins" and the array is evenly distributed
    for c, max_failure_rate in enumerate(np.linspace(0.05, .45, bins)): # r and c work with the number of elements in the respective arrays
      print(f"{accuracy=}, {max_failure_rate=}") 
      counter = MorrisCounter(accuracy=accuracy, max_failure_rate=max_failure_rate) # The morris counter is called here 
      test(counter, n=n, axis=axes[r][c]) 
      # The test function is called on every respective accuracy and Failiure rate. 



  # counter = MorrisCounter(accuracy=accuracy, max_failure_rate=max_failure_rate)
  # test(counter, n=n, axis=axes[r][c])

  fig.suptitle(f"Morris(a) Counter, {n=}")
  handles, labels = axes[-1][-1].get_legend_handles_labels()
  fig.legend(handles, labels, loc='upper left', prop={'size': 6})
  fig.savefig("plots/morris-a.png", dpi=500)




'''
Working of the Code 


'''


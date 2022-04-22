from random import Random
from typing import Optional

"""
~~~An approximate counter~~~

  This is the Morris(a) counter.

  Let:
    * e = accuracy
    * d = max_failure_rate
    * a = 2*e^2*d

  After N increments:
    * the amount of space used is O(lglgN+lg(1/e)+lg(1/d)) with prob <= N*(1+a)^(-Z), where Z = (lgN/a)^C
    * the counter estimate N' satisfies Pr[|N-N'| > e*N] < d

  Analysis
    Group: 2
      * Priya Jani AU2040004
      * Yansi Memdani AU2040028
      * Abhishu Oza AU2040027
      * Priyanshu Pathak AU2040241
      * Mohnish Mirchandani AU2040110
  """

'''
  MorrisCounter
  * Counter Class with five member variables and three member methods 

    - Variables
      + X:- Number of Counts in the Counter
      + epsilon:- The Maximum possible error
      + delta:- The Failure Rate
<<<<<<< HEAD
      + a:- 2*(error^2)*(failure_rate)
=======
      + a:- 
>>>>>>> ab05eb14a8536505b33c2db5f3246becf331bcab
      + rng:- A Random Number

    - Functions: 
      + count:- Returns the current count in the morris counter
      + increment:- Increments the counter
      + _should_increment:- Checks and computes whether the counter should be incremented based on thhe increment_probability
      + _increment_probability:- Returns the probability with which the counter should be incremented.  


  * Program Flow 
    - Count Function returns the current approximate count where count = (1/a)*((1+a)^(X) - 1)
    - Increment Function Probabilistically checks whether the counter should be incremented.
      + Call to _should_increment => which returns Bool
      + _should_increment compares a random number with the increment probability and if 
        > Random Number less than Probability => Return False
        > Random Number greater than Probability => Return True
  '''



class MorrisCounter:
  X: float
  epsilon: float
  delta: float
  a: float
  rng: Random

  def __init__(self, *, accuracy: float, max_failure_rate: float, rng: Optional[Random] = None) -> None:
    assert 1/2 <= accuracy < 1, accuracy
    assert 0 < max_failure_rate < 1/2, max_failure_rate
    self.epsilon = 1 - accuracy
    self.delta = max_failure_rate
    self.a = 2 * self.epsilon ** 2 * self.delta
    self.rng = rng or Random()
    self.X = 0


    print("epsilon: ", self.epsilon, "    delta", self.delta, "    a", self.a)

  '''
  Increment
   - Check whether the counter should be incremented and increment it accordingly
  '''


  def increment(self) -> None:
    if self._should_increment:
      self.X += 1
  '''
  Count 
   - Return the currently estimated count in the counter. 
  '''

  @property
  def count(self) -> float:
    return self.a ** (-1) * ((1 + self.a) ** self.X - 1)


  '''
  _increment_probability
    - Return the current probability of increment of counter.
  '''


  @property
  def _increment_probability(self) -> float:
    return (1 + self.a) ** (-self.X)

  '''
  _should_increment
  Check whether the counter should be incremented by:
    - Generate a Random Number from a Uniform distribution
    - Compare it with the current increment_probability
  Return True or False respectively
  '''
  @property
  def _should_increment(self) -> bool:
    return self.rng.uniform(0, 1) <= self._increment_probability
    
  
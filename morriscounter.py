from random import Random
from typing import Optional

class MorrisCounter:
  """An approximate counter.

  This is the Morris(a) counter.

  Let:
    * e = accuracy
    * d = max_failure_rate
    * a = 2*e^2*d

  After N increments:
    * the amount of space used is O(lglgN+lg(1/e)+lg(1/d)) with prob <= N*(1+a)^(-Z), where Z = (lgN/a)^C
    * the counter estimate N' satisfies Pr[|N-N'| > e*N] < d

  """
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

  def increment(self) -> None:
    if self._should_increment:
      self.X += 1

  @property
  def count(self) -> float:
    return self.a ** (-1) * ((1 + self.a) ** self.X - 1)
  '''
  Count 

  '''


  @property
  def _increment_probability(self) -> float:
    return (1 + self.a) ** (-self.X)

  '''
  
  '''
  @property
  def _should_increment(self) -> bool:
    return self.rng.uniform(0, 1) <= self._increment_probability
    # The uniform function generates a uniform probability distribution i.e. any value between 0 and 1 is equally likely


  '''
  Working of the Current Morris Counter
    When the count function is called, it returns the count based on the values of x and a;

    The increment function acts as a trigger for the two other functions, namely "should_increment" and "increment_probability"
    When you call the increment function -> it checks whether it should increment. 
    The "should_increment" selects a value based on a uniform distribution 
    The "increment_probability" function gives the value of the probability #########################
    After the comparison , a bool is returned for whether the counter should increment or not

  '''




  '''
  Todo: 
  Add an example 
  Format the comments
  
  
  
  '''
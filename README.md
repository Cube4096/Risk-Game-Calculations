# Risk-Game-Calculations
Using python to calculate attacks trough multiple countries

This program uses backtracking to calculate RISK attacking probabilities.

Input: amount of attackers, the defenders of a country/the countries you want to invade (one after the other)
Output: the change of a total breaktrough and the change of a defeat at each point (Note: if you wish you can also vieuw the chance of each outcome)

How to use this:
  - Copy the files risk.py, functions.py and database.py
  - run risk.py
  - follow the instructions in the terminal


Notes:
  - Due to the low speed of the way backtracking was implemented in this case a database.py was added (now runs good until around 45 defenders and attackers)
  - To create your own database to suit your needs, use createdb in databasemaker.py (first input being the size, second being the storage location)
  - The probabilities used in "ATTACKMATRIX" are from simulating all possible attacks to vieuw this look at small_attack.py


What will be added:
  - Faster way to compute the odds, this will probably result in a slight variance between the real odds and the outputted ones
  - Better database storage
  - Other attack options
  - Interface

Any problems, contact me on Github

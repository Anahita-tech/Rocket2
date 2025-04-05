I wrote this program after reading 3 chapters of Python.
First, we receive the rocket's initial data, such as the initial fuel amount, initial velocity, initial distance traveled (which is zero), and acceleration, from the user in the form of a dictionary.
The velocity is calculated using the formula v = at + v0. Fuel consumption is calculated, and the distance traveled by the rocket is computed using the formula 0.5at² + v0t + x0.
We defined a function that, if the fuel level drops below 80, adds 2000 units of fuel from an auxiliary fuel source.
If the fuel reaches 10% of the initial fuel amount, the message "Fuel level is below 10%" is printed, and if the distance traveled reaches 750,000, the message "Spacecraft arrived at Mars" is printed.
# Rocket2

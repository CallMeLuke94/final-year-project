# final-year-project
My final year project code!

In my final year project I did some computations which, when written down by hand, were rather long and tedious. After doing these computations by hand it became clear that programming a computer to do them for me would be far easier. To understand the computations and the mathematics behind them, you will have to read my report (to be uploaded soon!).

Initially I wrote findingsl3.py to find the r-points of the building of SL3 and then wrote Animated_Complex.pde to animate the results. This animation can also be found here: http://www.openprocessing.org/sketch/226756

With the release of PythonMode for Processing3 I then wrote SL3.pyde which allows you to control which symmetric power you see with the arrow keys, and has no upper limit for the symmetric power as each one is generated every time you press a key.

Having successfully written a program to do the SL3 case for me, it was time to move up to SL4. The additional dimension made this code far more complicated and hard to read but, after spending a good 6 months checking it, I can say with confidence that it does work.

The real challenge with SL4 was not writing the python code, but plotting the results in a useful way. sl4points.pde (together with the output text files) make an interactive, animated representation of an appartment of Delta raised to the 1st, 2nd, and 3rd symmetric powers. The 4th symmetric power is too messy to be worth presenting here, although this repository does give you the all tools to investigate further.

Finally, in my report - in the last paragraph of Example 3.1 - I say that it is possible to write a program to check a particular claim. equation31.py is such a program. (The name refers to Equation 3.1 in the report which this program is mimicking.)

Please do contact me with any questions you have.

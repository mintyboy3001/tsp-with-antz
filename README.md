VISUALIZATION TOOL FOR THE ANT COLONY OPTIMIZATION OF THE TRAVELLING SALESMAN PROBLEM:
Developed on Python 3.11.3, other versions may cause issues.

Developed on Windows. Code was designed to be OS agonistic, but the ways of the machines are mysterious sometimes.

DEPENDENCIES:
    numpy == 1.24.3
    pygame == 2.4.0  


USAGE:
python printz <number nodes> <number ants> [-A | animate ]

example :
#1 python printz 50 10 -A instantiates 50 randomly spread nodes and 10 ants in the graph. -A animates the process. 
Left click anywhere inside the pygame window to pause/unpause.  
#2 python printz 30 10 instantiates 30 randomly spread nodes and 10 ants in the graph. Left click anywhere inside the pygame window to perform one iteration.          

![Alt text](https://github.com/mintyboy3001/tsp-with-antz/blob/main/Animation.gif)

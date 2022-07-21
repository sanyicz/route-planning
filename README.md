Route Planning

Description:
A path finding program based on Dijkstra'a algorithm.

Files:
dijkstra_algorithm.py: the function that finds the shortest path in a graph is defined here. It uses Dijkstra's algorithm (https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
graph_class.py: Graph class is defined here. The graph's vertices are labeled with a coordinate pair of a 2D grid, all edges have equal length of 1.
route-planning.py: RoutePlanningSimulator object is defined here. It contains the graphical interface (made with tkinter) and methods to turn the 2D grid into a graph, to find route, to plot it.

How tot use:
Run to route-planning.py to use.
A 20x20 grid is created on a tkinter canvas. White cells are free, black cells are walls. You can change the state of a cells by left click. If you are ready with the field, click Finish grid.
You can set the start position with a left click (display as blue cell) and the end position with a right click (display as red cell). Both must be selected for the program to run properly. Click Plan route when ready.
The route between the selected points is created and displayed as a chain of green cells.
You can restart the program by clicking Main menu. You can use the last grid if the Keep grid? checkbutton is checked.


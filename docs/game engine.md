# Game engine

The game engine is a class. Only one one instance of the class must be created. The creation of the instance initializes pygame, while its destruction quits pygame. Then engine has two submodules, one to manage the screen, composed by frames, the other one to manage the sounds. The engine also allow to manage. There are two types of frame, the basic (Frame) and the "dynamic" (DynamicFrame). The basic frame is simpler and is set to display objects that won't change a lot: no rotation, no alpha change. The dynamic frames allow the content to be zoomed in (only two levels of zoom allowed, 0 and the one set at the frame creation), rotated, alpha changed. They are used to display the circuit.
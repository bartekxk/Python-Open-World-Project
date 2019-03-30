<h1> Python-Open-World-Project</h1>
<h2>PyGame</h2>
The project was created to simulate a world consisting of a hero, plants and animals on a square board using object-oriented design. Below is a description of the classes and their activities. The project was implemented due to my student task, therefore the names of classes, some methods and variables are in Polish. I will try to explain them here.
<h2>Swiat (World)</h2>
The world is the main class that manages all elements of the world. It has boards(plansza), objects that participate in the simulation and variables to handle the turn. It has methods for introducing new objects to the boards (zmienaktualnygatunek), making turns (wykonajTure), drawing the world (rysujSwiat) and saving and loading it from / to the file.
<h2>Organism(Organizm)</h2>
It is an abstract class representing the organism on the board. It has abstract collision(kolizja) methods to react to collisions with another organism, reaction(reakcja) to response to collisions and action(akcja). There is also a method to multiplication(rozmnoz) the organism and to use it on the board.
<h3>Animal(Zwierze)</h3>
The animal is the descendant of the organism. It implement his basic methods. Animals, unlike organisms, can move around the board. Specific classes of animals have been implemented:
<ul>
<li>Antelope(Antylopa)</li>
<li>cyber-sheep(Cyberowca)</li>
<li>Man(Człowiek)</li>
<li>Fox(Lis)</li>
<li>Sheep(Owca)</li>
<li>Wolf(Wilk)</li>
<li>Turtle(Zolw)</li>
</ul>
<h4>Man(Czlowiek)</h4>
Specific subclass of Animal is Man, this is like our hero on board. We have speciall skill to use by x-key. We can also decide where he has to go. He has implemented like other animals but with keyboard support. 
<h3>Plant(Roslina)</h3>
Analogously to the animal. Plants can not move, but they reproduce better. Subclasses:
<ul>
<li>Sosnowski's borscht(BSosnowskiego)</li>
<li>Guraana</li>
<li>Sow-thistle(Mlecz)</li>
<li>Grass(Trawa)</li>
<li>Wolf berries(WilczeJagody)</li>
</ul>
<h2>Support classes</h2>
<h3>Logs</h3>
Class to support for game logs.
<h3>Quee(Kolejka)</h3>
Implement of priority Quee to handle the order in the turn.
<h3>Kill(Zabij)</h3>
Handle of events after dead of some organism.
<h2>Main script</h2>
Script containing gui in Pygame, supporting the addition of the organism with the mouse and creating objects of classes such as the world(Swiat).

---------
Devin Suy
---------

Resources:
	https://wiki.python.org/moin/UsingPickle
	https://docs.python.org/3/library/pathlib.html
	https://en.wikipedia.org/wiki/Game_complexity#:~:text=For%20tic%2Dtac%2Dtoe%2C,have%20a%20row%20of%20three.
	https://en.wikipedia.org/wiki/Tic-tac-toe
	https://en.wikipedia.org/wiki/Minimax#:~:text=chances%20of%20winning).-,Minimax%20algorithm%20with%20alternate%20moves,or%20state%20of%20the%20game.


Notes:
	- GameState objects contain the corresponding Board and Player objects
	  at any given point in the game as well a list of all successor GameStates
	  
	- Preprocessing of states has been done (see Saved_States directory)
		EX: Saved_States/states_0.obj corresponds to all successor states in the case where 
		human player decides to place opening move in cell 0 (top left square)
		
	- See Algorithm/Minimax.py and Algorithm/GameState for implementation, pickle library
	  is utilized to save the list of processed states into an .obj file
	  
	- The states_x.obj corresponding to each of the 9 possible opening moves the human player 
	  can make is loaded using the pickle library where the last element in this list of 
	  GameState objects is the opening state/root node (where the board only has one X)
	  
	- Contact : DevinSuy@gmail.com
	
---------------------------------------------------------------------------------------------------------------------------------------------------------
Observations:
	- Agent consistently ends games in a tie regardless of starting position (asssuming human plays rationally)
	  otherwise a winning state is produced
	- Failure to secure the center square (cell #4) by the Human player leads the AI to subtree states with higher
	  evaluation scores and therefore more consistently reaches win states

--------------------------
(Sample Win State Output):
--------------------------

Tic-Tac-Toe
-----------
   Welcome Human! You are player X
   Below are the different possible move placement numbers:
      |  0  |  1  |  2  |
      |  3  |  4  |  5  |
      |  6  |  7  |  8  |

   Human player select your move: 1

Displaying Board
----------------

   |     |  X  |     |
   |     |     |     |
   |     |     |     |

   Human places an X @ position 1

Evaluating . . .

Displaying Board
----------------

   |  O  |  X  |     |
   |     |     |     |
   |     |     |     |

   Predicted State Value:  0
   Bot places an O @ position 0

   Human player select your move: 7

Displaying Board
----------------

   |  O  |  X  |     |
   |     |     |     |
   |     |  X  |     |

   Human places an X @ position 7

Displaying Board
----------------

   |  O  |  X  |     |
   |     |  O  |     |
   |     |  X  |     |

   Predicted State Value:  2
   Bot places an O @ position 4

   Human player select your move: 8

Displaying Board
----------------

   |  O  |  X  |     |
   |     |  O  |     |
   |     |  X  |  X  |

   Human places an X @ position 8

Displaying Board
----------------

   |  O  |  X  |     |
   |     |  O  |     |
   |  O  |  X  |  X  |

   Predicted State Value:  2
   Bot places an O @ position 6

   Human player select your move: 3

Displaying Board
----------------

   |  O  |  X  |     |
   |  X  |  O  |     |
   |  O  |  X  |  X  |

   Human places an X @ position 3

Displaying Board
----------------

   |  O  |  X  |  O  |
   |  X  |  O  |     |
   |  O  |  X  |  X  |

   Predicted State Value:  2
   Bot places an O @ position 2

Computer Player Has Won!!


--------------------------
(Sample Tie State Output):
--------------------------

Tic-Tac-Toe
-----------
   Welcome Human! You are player X
   Below are the different possible move placement numbers:
      |  0  |  1  |  2  |
      |  3  |  4  |  5  |
      |  6  |  7  |  8  |

   Human player select your move: 4

Displaying Board
----------------

   |     |     |     |
   |     |  X  |     |
   |     |     |     |

   Human places an X @ position 4

Evaluating . . .

Displaying Board
----------------

   |  O  |     |     |
   |     |  X  |     |
   |     |     |     |

   Predicted State Value:  0
   Bot places an O @ position 0

   Human player select your move: 2

Displaying Board
----------------

   |  O  |     |  X  |
   |     |  X  |     |
   |     |     |     |

   Human places an X @ position 2

Displaying Board
----------------

   |  O  |     |  X  |
   |     |  X  |     |
   |  O  |     |     |

   Predicted State Value:  0
   Bot places an O @ position 6

   Human player select your move: 3

Displaying Board
----------------

   |  O  |     |  X  |
   |  X  |  X  |     |
   |  O  |     |     |

   Human places an X @ position 3

Displaying Board
----------------

   |  O  |     |  X  |
   |  X  |  X  |  O  |
   |  O  |     |     |

   Predicted State Value:  0
   Bot places an O @ position 5

   Human player select your move: 1

Displaying Board
----------------

   |  O  |  X  |  X  |
   |  X  |  X  |  O  |
   |  O  |     |     |

   Human places an X @ position 1

Displaying Board
----------------

   |  O  |  X  |  X  |
   |  X  |  X  |  O  |
   |  O  |  O  |     |

   Predicted State Value:  0
   Bot places an O @ position 7

   Human player select your move: 8

Displaying Board
----------------

   |  O  |  X  |  X  |
   |  X  |  X  |  O  |
   |  O  |  O  |  X  |

   Human places an X @ position 8

Human and Computer have tied!!


-------------------------------
Continuous Depth Traversal Left
Succesor States Example Output:
-------------------------------
(See Algorithm/GameState.py For Implementation)
# turn = True : Successor states will add an X (Human)
# turn = False : Successor states will add a O (Bot)

Displaying Board
----------------

   |  X  |     |     |
   |     |     |     |
   |     |     |     |
State has  8  sucessors
Current state has depth  0  and turn is  False

Displaying Board
----------------

   |  X  |  O  |     |
   |     |     |     |
   |     |     |     |
State has  7  sucessors
Current state has depth  1  and turn is  True

Displaying Board
----------------

   |  X  |  O  |  X  |
   |     |     |     |
   |     |     |     |
State has  6  sucessors
Current state has depth  2  and turn is  False

Displaying Board
----------------

   |  X  |  O  |  X  |
   |  O  |     |     |
   |     |     |     |
State has  5  sucessors
Current state has depth  3  and turn is  True

Displaying Board
----------------

   |  X  |  O  |  X  |
   |  O  |  X  |     |
   |     |     |     |
State has  4  sucessors
Current state has depth  4  and turn is  False

Displaying Board
----------------

   |  X  |  O  |  X  |
   |  O  |  X  |     |
   |     |     |  O  |
State has  3  sucessors
Current state has depth  5  and turn is  True

Displaying Board
----------------

   |  X  |  O  |  X  |
   |  O  |  X  |  X  |
   |     |     |  O  |
State has  2  sucessors
Current state has depth  6  and turn is  False

Displaying Board
----------------

   |  X  |  O  |  X  |
   |  O  |  X  |  X  |
   |  O  |     |  O  |
State has  1  sucessors
Current state has depth  7  and turn is  True

Displaying Board
----------------

   |  X  |  O  |  X  |
   |  O  |  X  |  X  |
   |  O  |  X  |  O  |
State has  0  sucessors
Current state has depth  8  and turn is  False
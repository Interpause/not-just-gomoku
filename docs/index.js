URLS=[
"not-just-gomoku/index.html",
"not-just-gomoku/agents/index.html",
"not-just-gomoku/agents/baseAgent.html",
"not-just-gomoku/agents/baseThreadedAgent.html",
"not-just-gomoku/agents/guiPlayerAgent.html",
"not-just-gomoku/agents/markovAgent.html",
"not-just-gomoku/agents/markovSimpleAgent.html",
"not-just-gomoku/agents/maxAgent.html",
"not-just-gomoku/agents/maxThreadedAgent.html",
"not-just-gomoku/agents/simpleAgent.html",
"not-just-gomoku/game.html",
"not-just-gomoku/game_exceptions.html",
"not-just-gomoku/heuristics.html",
"not-just-gomoku/state.html"
];
INDEX=[
{
"ref":"not-just-gomoku",
"url":0,
"doc":""
},
{
"ref":"not-just-gomoku.agents",
"url":1,
"doc":""
},
{
"ref":"not-just-gomoku.agents.baseAgent",
"url":2,
"doc":""
},
{
"ref":"not-just-gomoku.agents.baseAgent.baseAgent",
"url":2,
"doc":"base class that all game agents should extend and override. Attributes: state (state): The current game state seen by the agent, see state.py for more details. piece (str): The piece that the agent uses. Doubles as both what is printed and its id. curPiece (str): The current piece in play. Doubles as a way to check whose turn it is. ordlist (str[]): The order that pieces should play in. heuristics (dict): A dict where keys are the heuristic function, and values are a dict of kwargs for that function. negligable (float): Threshold between which two floats are considered equal. intMin (float): Unused. intMax (float): Unused. Constructor for baseAgent that should be extended. Args: state (state): The initial game state, see state.py for more details. piece (str): The piece that the agent uses. Doubles as both what is printed and its id. ordlist (str[]): The order that pieces should play in. heuristics (dict): Defaults to None for {lineHeuristic:{},blockHeuristic:{},openHeuristic:{ . negligable (float): Defaults to 0.001."
},
{
"ref":"not-just-gomoku.agents.baseAgent.baseAgent.getNextList",
"url":2,
"doc":"Get the subsequent order of pieces using self.ordlist and the piece provided.",
"func":1
},
{
"ref":"not-just-gomoku.agents.baseAgent.baseAgent.fequal",
"url":2,
"doc":"Compare if two floats are roughly equal using self.negligable.",
"func":1
},
{
"ref":"not-just-gomoku.agents.baseAgent.baseAgent.reflexEvaluate",
"url":2,
"doc":"Shallow evaluates the reward for an action.",
"func":1
},
{
"ref":"not-just-gomoku.agents.baseAgent.baseAgent.update",
"url":2,
"doc":"Function to update the turn and game state for the agent. Can be overrided to perform preprocessing.",
"func":1
},
{
"ref":"not-just-gomoku.agents.baseAgent.baseAgent.getMove",
"url":2,
"doc":"Function that is called to get the decision made by the agent. Should be overrided.",
"func":1
},
{
"ref":"not-just-gomoku.agents.baseAgent.baseAgent.onWin",
"url":2,
"doc":"Function that is called when a piece wins, with winner being the piece. Used by markovAgent.py to save the heuristic configuration.",
"func":1
},
{
"ref":"not-just-gomoku.agents.baseThreadedAgent",
"url":3,
"doc":""
},
{
"ref":"not-just-gomoku.agents.baseThreadedAgent.baseThreadedAgent",
"url":3,
"doc":"Extends baseAgent in order to provide multithreading functionality. Attributes: thread (Thread): Thread used by agent to do precalculations. isStopping (bool): Whether the thread is being interrupted. Should not be set. expected (dict): The expected future states and the optimal moves for those states. move (tuple): The current move, I think. Constructor for baseAgent that should be extended. Args: state (state): The initial game state, see state.py for more details. piece (str): The piece that the agent uses. Doubles as both what is printed and its id. ordlist (str[]): The order that pieces should play in. heuristics (dict): Defaults to None for {lineHeuristic:{},blockHeuristic:{},openHeuristic:{ . negligable (float): Defaults to 0.001."
},
{
"ref":"not-just-gomoku.agents.baseThreadedAgent.baseThreadedAgent.update",
"url":3,
"doc":"Function to update the turn and game state for the agent. Can be overrided to perform preprocessing.",
"func":1
},
{
"ref":"not-just-gomoku.agents.baseThreadedAgent.baseThreadedAgent.calculate",
"url":3,
"doc":"How precalculations should be done. Should be overrided.",
"func":1
},
{
"ref":"not-just-gomoku.agents.baseThreadedAgent.baseThreadedAgent.getMove",
"url":3,
"doc":"Function that is called to get the decision made by the agent. Should be overrided.",
"func":1
},
{
"ref":"not-just-gomoku.agents.guiPlayerAgent",
"url":4,
"doc":""
},
{
"ref":"not-just-gomoku.agents.guiPlayerAgent.guiPlayerAgent",
"url":4,
"doc":"Extends baseAgent to provide a GUI for the player to use to play. Constructor for baseAgent that should be extended. Args: state (state): The initial game state, see state.py for more details. piece (str): The piece that the agent uses. Doubles as both what is printed and its id. ordlist (str[]): The order that pieces should play in. heuristics (dict): Defaults to None for {lineHeuristic:{},blockHeuristic:{},openHeuristic:{ . negligable (float): Defaults to 0.001."
},
{
"ref":"not-just-gomoku.agents.guiPlayerAgent.guiPlayerAgent.enable",
"url":4,
"doc":"Enables all grid buttons.",
"func":1
},
{
"ref":"not-just-gomoku.agents.guiPlayerAgent.guiPlayerAgent.disable",
"url":4,
"doc":"Disables all grid buttons.",
"func":1
},
{
"ref":"not-just-gomoku.agents.guiPlayerAgent.guiPlayerAgent.btnupdate",
"url":4,
"doc":"Updates grid buttons to represent current self.state.",
"func":1
},
{
"ref":"not-just-gomoku.agents.guiPlayerAgent.guiPlayerAgent.passInput",
"url":4,
"doc":"Click handler for grid buttons.",
"func":1
},
{
"ref":"not-just-gomoku.agents.guiPlayerAgent.guiPlayerAgent.btninit",
"url":4,
"doc":"Creates grid of buttons.",
"func":1
},
{
"ref":"not-just-gomoku.agents.guiPlayerAgent.guiPlayerAgent.update",
"url":4,
"doc":"Function to update the turn and game state for the agent. Can be overrided to perform preprocessing.",
"func":1
},
{
"ref":"not-just-gomoku.agents.guiPlayerAgent.guiPlayerAgent.getMove",
"url":4,
"doc":"Function that is called to get the decision made by the agent. Should be overrided.",
"func":1
},
{
"ref":"not-just-gomoku.agents.markovAgent",
"url":5,
"doc":""
},
{
"ref":"not-just-gomoku.agents.markovAgent.markovAgent",
"url":5,
"doc":"Agent using machine learning to tune heuristics. Machine learning not implemented, does not currently work and is not actually a markov agent. Constructor for baseAgent that should be extended. Args: state (state): The initial game state, see state.py for more details. piece (str): The piece that the agent uses. Doubles as both what is printed and its id. ordlist (str[]): The order that pieces should play in. heuristics (dict): Defaults to None for {lineHeuristic:{},blockHeuristic:{},openHeuristic:{ . negligable (float): Defaults to 0.001."
},
{
"ref":"not-just-gomoku.agents.markovAgent.markovAgent.save",
"url":5,
"doc":"",
"func":1
},
{
"ref":"not-just-gomoku.agents.markovAgent.markovAgent.onWin",
"url":5,
"doc":"Function that is called when a piece wins, with winner being the piece. Used by markovAgent.py to save the heuristic configuration.",
"func":1
},
{
"ref":"not-just-gomoku.agents.markovSimpleAgent",
"url":6,
"doc":""
},
{
"ref":"not-just-gomoku.agents.markovSimpleAgent.markovSimpleAgent",
"url":6,
"doc":"Not implemented Constructor for baseAgent that should be extended. Args: state (state): The initial game state, see state.py for more details. piece (str): The piece that the agent uses. Doubles as both what is printed and its id. ordlist (str[]): The order that pieces should play in. heuristics (dict): Defaults to None for {lineHeuristic:{},blockHeuristic:{},openHeuristic:{ . negligable (float): Defaults to 0.001."
},
{
"ref":"not-just-gomoku.agents.maxAgent",
"url":7,
"doc":""
},
{
"ref":"not-just-gomoku.agents.maxAgent.maxAgent",
"url":7,
"doc":"Agent that assumes opponents always play optimally and use that to deeply calculate state rewards. Attributes: depth (int): How many turns into the future to predict. dim (float): Decrease in reward the further one goes into the future due to uncertainty. salt (float): How much to penalize the agent for letting the opponent make a good move. High salt values make agents try and prevent the opponent from doing well at all times and can appear as \"saltiness\". Constructor for baseAgent that should be extended. Args: state (state): The initial game state, see state.py for more details. piece (str): The piece that the agent uses. Doubles as both what is printed and its id. ordlist (str[]): The order that pieces should play in. heuristics (dict): Defaults to None for {lineHeuristic:{},blockHeuristic:{},openHeuristic:{ . negligable (float): Defaults to 0.001."
},
{
"ref":"not-just-gomoku.agents.maxAgent.maxAgent.reflexStateEvaluate",
"url":7,
"doc":"Shallow evaluates state reward using action rewards possible.",
"func":1
},
{
"ref":"not-just-gomoku.agents.maxAgent.maxAgent.getOptimal",
"url":7,
"doc":"Recursive function that deeply evaluates state reward over multiple turns.",
"func":1
},
{
"ref":"not-just-gomoku.agents.maxAgent.maxAgent.getMove",
"url":7,
"doc":"Function that is called to get the decision made by the agent. Should be overrided.",
"func":1
},
{
"ref":"not-just-gomoku.agents.maxThreadedAgent",
"url":8,
"doc":""
},
{
"ref":"not-just-gomoku.agents.maxThreadedAgent.maxThreadedAgent",
"url":8,
"doc":"A multithreaded implementation of maxAgent.py. Does not work. Constructor for baseAgent that should be extended. Args: state (state): The initial game state, see state.py for more details. piece (str): The piece that the agent uses. Doubles as both what is printed and its id. ordlist (str[]): The order that pieces should play in. heuristics (dict): Defaults to None for {lineHeuristic:{},blockHeuristic:{},openHeuristic:{ . negligable (float): Defaults to 0.001."
},
{
"ref":"not-just-gomoku.agents.maxThreadedAgent.maxThreadedAgent.calculate",
"url":8,
"doc":"How precalculations should be done. Should be overrided.",
"func":1
},
{
"ref":"not-just-gomoku.agents.maxThreadedAgent.maxThreadedAgent.reflexStateEvaluate",
"url":8,
"doc":"",
"func":1
},
{
"ref":"not-just-gomoku.agents.maxThreadedAgent.maxThreadedAgent.getOptimal",
"url":8,
"doc":"",
"func":1
},
{
"ref":"not-just-gomoku.agents.simpleAgent",
"url":9,
"doc":""
},
{
"ref":"not-just-gomoku.agents.simpleAgent.simpleAgent",
"url":9,
"doc":"A simple agent that plays using shallow reflexEvaluate to decide. Constructor for baseAgent that should be extended. Args: state (state): The initial game state, see state.py for more details. piece (str): The piece that the agent uses. Doubles as both what is printed and its id. ordlist (str[]): The order that pieces should play in. heuristics (dict): Defaults to None for {lineHeuristic:{},blockHeuristic:{},openHeuristic:{ . negligable (float): Defaults to 0.001."
},
{
"ref":"not-just-gomoku.agents.simpleAgent.simpleAgent.getMove",
"url":9,
"doc":"Function that is called to get the decision made by the agent. Should be overrided.",
"func":1
},
{
"ref":"not-just-gomoku.game",
"url":10,
"doc":""
},
{
"ref":"not-just-gomoku.game.Game",
"url":10,
"doc":"the game session. Attributes: pieces (str[]): The player pieces used in the game. Hardcoded in unfortunately. ordlist (str[]): The order in which the pieces play. state (State): The game's state. win (str|bool): The piece that won or False if no one has won yet. silent (bool): Whether to log status messages. agents (list): A list of the agents playing the game. Constructor for the game session. Args: height (int): The height of the grid. length (int): The length of the grid. winnum (int): The number of pieces in a line to win. agents (list): A list of game agent classes to use. slient (bool): Whether to log status messages."
},
{
"ref":"not-just-gomoku.game.Game.update",
"url":10,
"doc":"Runs a round, allowing each agent to take their turn.",
"func":1
},
{
"ref":"not-just-gomoku.game.Game.takeTurn",
"url":10,
"doc":"Takes the turn for that agent.",
"func":1
},
{
"ref":"not-just-gomoku.game.Game.updateAgents",
"url":10,
"doc":"Passes the updated state and turn to each agent.",
"func":1
},
{
"ref":"not-just-gomoku.game.Game.getMove",
"url":10,
"doc":"Gets the move played by the agent.",
"func":1
},
{
"ref":"not-just-gomoku.game.Game.checkWin",
"url":10,
"doc":"Check which piece has won and sets self.win to that piece.",
"func":1
},
{
"ref":"not-just-gomoku.game.Game.onKeyboardInterrupt",
"url":10,
"doc":"",
"func":1
},
{
"ref":"not-just-gomoku.game.Game.getName",
"url":10,
"doc":"",
"func":1
},
{
"ref":"not-just-gomoku.game.Game.log",
"url":10,
"doc":"",
"func":1
},
{
"ref":"not-just-gomoku.game_exceptions",
"url":11,
"doc":""
},
{
"ref":"not-just-gomoku.game_exceptions.OutOfBoundsException",
"url":11,
"doc":"Common base class for all non-exit exceptions."
},
{
"ref":"not-just-gomoku.game_exceptions.OutOfSpaceException",
"url":11,
"doc":"Common base class for all non-exit exceptions."
},
{
"ref":"not-just-gomoku.game_exceptions.SpaceTakenException",
"url":11,
"doc":"Common base class for all non-exit exceptions."
},
{
"ref":"not-just-gomoku.heuristics",
"url":12,
"doc":""
},
{
"ref":"not-just-gomoku.heuristics.isOut",
"url":12,
"doc":"Whether the coordinates provided is outside the grid",
"func":1
},
{
"ref":"not-just-gomoku.heuristics.lineHeuristic",
"url":12,
"doc":"Heuristic that encourages agent to place in a straight line.",
"func":1
},
{
"ref":"not-just-gomoku.heuristics.blockHeuristic",
"url":12,
"doc":"Heuristic that encourages agent to block opponent's line.",
"func":1
},
{
"ref":"not-just-gomoku.heuristics.clusterHeuristic",
"url":12,
"doc":"Heuristic that encourages agents to place pieces closer to each other.",
"func":1
},
{
"ref":"not-just-gomoku.heuristics.openHeuristic",
"url":12,
"doc":"Heuristic that encourages agents to place pieces further from each other.",
"func":1
},
{
"ref":"not-just-gomoku.state",
"url":13,
"doc":""
},
{
"ref":"not-just-gomoku.state.state",
"url":13,
"doc":"the game state. Attributes: __winnum (int): Number of pieces in a line required to win. __height (int): The height of the grid. __length (int): The length of the grid. __pieces (str[]): The player pieces used in the grid. __empty  int,int)[]): The list of empty coordinates. __board (dict): The list of coordinates occupied by each piece. __grid (str[][]): The grid of pieces placed. The constructor for the game state Args: height (int): The height of the grid. length (int): The length of the grid. winnum (int): Number of pieces in a line required to win. pieces (str[]): The player pieces used in the grid."
},
{
"ref":"not-just-gomoku.state.state.forgetmefornow",
"url":13,
"doc":"      ?",
"func":1
},
{
"ref":"not-just-gomoku.state.state.isEmpty",
"url":13,
"doc":"Whether a coord on the grid is empty.",
"func":1
},
{
"ref":"not-just-gomoku.state.state.isWin",
"url":13,
"doc":"Checks whether there is a winner.",
"func":1
},
{
"ref":"not-just-gomoku.state.state.board",
"url":13,
"doc":"",
"func":1
},
{
"ref":"not-just-gomoku.state.state.grid",
"url":13,
"doc":"",
"func":1
},
{
"ref":"not-just-gomoku.state.state.height",
"url":13,
"doc":"",
"func":1
},
{
"ref":"not-just-gomoku.state.state.length",
"url":13,
"doc":"",
"func":1
},
{
"ref":"not-just-gomoku.state.state.winnum",
"url":13,
"doc":"",
"func":1
},
{
"ref":"not-just-gomoku.state.state.pieces",
"url":13,
"doc":"",
"func":1
},
{
"ref":"not-just-gomoku.state.state.full",
"url":13,
"doc":"",
"func":1
},
{
"ref":"not-just-gomoku.state.state.spaces",
"url":13,
"doc":"",
"func":1
},
{
"ref":"not-just-gomoku.state.state.overwrite",
"url":13,
"doc":"Overwrites the coord with the piece.",
"func":1
},
{
"ref":"not-just-gomoku.state.state.erase",
"url":13,
"doc":"Erases the piece on that coord.",
"func":1
},
{
"ref":"not-just-gomoku.state.state.place",
"url":13,
"doc":"Places a piece at that coord if it is empty.",
"func":1
}
]
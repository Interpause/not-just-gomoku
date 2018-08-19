<h1>Changelog</h1>
<div>
	<h3>Everything Important Re-Coded</h3>
	<ul>
		<li>State is now programmed to be faster and more convenient to use.</li>
		<li>O(n) retrieval of empty spaces, occupied spaces (by piece) and grid.</li>
		<li>isWin() is faster due to above optimization of grid representation.</li>
		<li>General increase in neatness.</li>
	</ul>
</div>

<div>
	<h3>Heuristics</h3>
	<ul>
		<li>Action-based rather than state-based is faster.</li>
		<li>Reimplemented LineHeuristic and BlockHeuristic</li>
		<li>O(n) retrieval of important grid information makes things much faster.</li>
	</ul>
</div>

<div>
	<h3>SearchAgents</h3>
	<ul>
		<li>SimpleAgent now stupid.</li>
		<li>maxAgent also stupid.</li>
		<li>possibly flawed implementation of heuristics.</li>
	</ul>
</div>

<div>
	<h3>Others</h3>
	<ul>
		<li>Added a player agent called guiPlayerAgent, gives a gui to use. (yay)</li>
		<li>Brainstormed improvements for future versions can be seen in game.py</li>
	</ul>
</div>
<h1>Changelog</h1>
<div>
	<h3>Object-oriented Approach implemented</h3>
	<ul>
		<li>game.py cleaned up.</li>
		<li>Agents are now objects that need to be initialized.</li>
		<li>Fixed glitch in state object that prevented non-square boards (flipped height and length).</li>
	</ul>
</div>
<div>
	<h3>Agents</h3>
	<ul>
		<li>All agents have baseAgent as an ancestor.</li>
		<li>All threaded/concurrent agents inherits from baseThreadedAgent.</li>
		<li>Agents now use floats instead of ints.</li>
		<li>maxThreadedAgent (inherits from baseThreadedAgent) created but does not work and is more like expectimax.</li>
		<li>Added some randomness to maxAgent if score between two choices is roughly same.</li>
		<li>maxAgent no longer plays (0,0) due to (1-dim) filtering due to openHeuristic.</li>
	</ul>
</div>
<div>
	<h3>Heuristics</h3>
	<ul>
		<li>Added openHeuristic which encourages agents to place in open areas (diagonal works too). General improvement to agents' behaviour but adds more lag.</li>
		</li>All agents now can choose non-default options for heuristic (change made to baseAgent). Needed for markovAgent (next version). </li>
	</ul>
</div>
<div>
	<h3>Observations</h3>
	<ul>
		<li>There are no good extremes for heuristic options.</li>
		<li>For example, 100,000 and 20,000 work well as win bonus for lineHeuristic but not 40,000.</li>
		<li>Sometimes maxAgent acts stupidly because it thinks the player plays like itself (and tries to tempt player from victory but fails). </li>
		<li>Seemingly first player advantage exists in this game.</li>
		<li>maxAgent sometimes fails in <2-player games because opponents play dumber and don't block like it expects them to.</li>
		<li>see game.py for plans.</li>
	</ul>
</div>

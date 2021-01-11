# Not Just Gomoku
<div>
  <h3>LICENSE</h3>
  <p>Younger me was way too stringy. MIT License now. Heck younger me wrote this in HTML rather than markdown. </p>
</div>

<div>
  <h3>DESCRIPTION</h3>
  <p>It is basically Gomoku, but with a board of any specified size, any specified number of players and any specified number of pieces in a row to win. Run game.py basically and modify the settings there to try out stuff.</p>
</div>

<div>
  <h3>ELABORATION</h3>
  <p>As it deviates from regular Gomoku, I decided not to use hardcoded strategies. especially considering the fact the number of players, pieces needed and size can change. Instead I used searchAgents, while despite the multiple possible states each turn resulting in it being quite computationally demanding, with some optimizations, I believe it is better. </p>
  <p>However, I am still thinking of how some strategies can be hardcoded to reduce the time required, with the searchAgents being a fallback system instead.</p>
  <p>For further information, see the plaintext changelog.md.</p>
  <p>For older versions, I used version tagging so you will not find them as branches. Go to tags instead.</p>
</div>

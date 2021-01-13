# Not Just Gomoku

This was something I made when I was 16. I would like to think that I have gotten more professional since then, but have I really? Anyways, since I have fond memories of coding this whenever I had free time in the school library, I have decided to come back and add documentation, while leaving the code itself as untouched as possible. Documentation can be found [here](https://interpause.github.io/not-just-gomoku/) btw. I also did not modify the description too much.

Since then, I have picked up the use of a proper IDE (VSCode) rather than using IDLE to code. I have learnt to rely on the work of others, instead of thinking that I should do everything myself. That said, back then, I was already a fairly decent coder, using what I was taught in computer elective to make game agents, planning my code for future extendability, and most importantly, coding for my own passion. Now that I do intend to make coding my career, I need to be more professional, which I hope I already am close to being with my more recent projects.

To be honest though, I miss those simpler days. I cannot fully remember what was going through my head at that time, but I do know it was fun.

## Description

It is basically Gomoku, but with a board of any specified size, any specified number of players and any specified number of pieces in a row to win. Run game.py basically and modify the settings there to try out stuff.

As it deviates from regular Gomoku, I decided not to use hardcoded strategies. especially considering the fact the number of players, pieces needed and size can change. Instead I used searchAgents, while despite the multiple possible states each turn resulting in it being quite computationally demanding, with some optimizations, I believe it is better.

However, I am still thinking of how some strategies can be hardcoded to reduce the time required, with the searchAgents being a fallback system instead.

For older versions, I used version tagging so you will not find them as branches. Go to tags instead.

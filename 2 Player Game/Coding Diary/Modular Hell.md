The game has some problems with it being fully modular.

After some time debugging, it seems like the main issue lies in how the health bar registers for things that change the health. Unfortunately, this makes up a big part of the game.

Sometimes the healthbar would not update on collision, and other times the players health could not be defined, eventhough in another module's global scope.

I only modularized the parts that can allow the game to work at full functionality.
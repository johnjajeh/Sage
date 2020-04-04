from sage_game import Sage
from player_factory import PlayerFactory
from reporter import Reporter

ITERATIONS = 1000

factory = PlayerFactory()
reporter = Reporter()

factory.determinePlayers()
reporter.initServices()

player1 = factory.getPlayer1()
player2 = factory.getPlayer2()

p1Sum = 0;
p2Sum = 0;

for i in range(ITERATIONS):
    game = Sage(player1(), player2(), reporter)
    p1, p2 = game.run()

    p1Sum += p1
    p2Sum += p2
    reporter.updateIteration(i)

finalData = (ITERATIONS, player1().getName(), player2().getName())

reporter.close(finalData)

p1Avg = p1Sum / ITERATIONS
p2Avg = p2Sum / ITERATIONS

print("Player 1 ({}): {}".format(player1().getName(), p1Avg))
print("Player 2 ({}): {}".format(player2().getName(), p2Avg))

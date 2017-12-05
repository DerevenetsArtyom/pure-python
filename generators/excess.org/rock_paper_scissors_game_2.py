from convenient_decorator import advanced_generator_once

# This is a Rock-Paper-Scissors game where each player's play
# is passed in separately, and once both players have played the result of
# the game is yielded. Players can change their mind choose a different play
# if the other player hasn't chosen yet. Games will continue infinitely.

# This generator uses a common pattern of storing the result that
# will be yielded in a local variable so that there are fewer yield statements
# in the generator function. Having fewer yield statements makes it easier
# to understand where it is possible for execution
# to be paused within the generator function.

# The outer while loop runs once for each full game.
# The inner while loop collects input from the users
# until the game result can be decided.


@advanced_generator_once
def rock_paper_scissors():
    """
    Coroutine for playing rock-paper-scissors

    yields: 'invalid key': invalid input was sent
            ('win', player, choice0, choice1): when a player wins
            ('tie', None, choice0, choice1): when there is a tie
            None: when waiting for more input

    accepts to .send(): (player, key):
        player is 0 or 1, key is a character in 'rps'

    We play this game by passing (player number, play) tuples to .send()
    """
    valid = 'rps'
    wins = ('rs', 'sp', 'pr', )
    result = None

    while True:
        chosen = [None, None]
        while None in chosen:
            player, play = yield result
            result = None
            if play in valid:
                chosen[player] = play
            else:
                result = 'invalid key'

        if chosen[0] + chosen[1] in wins:
            result = ('win', 0) + tuple(chosen)
        elif chosen[1] + chosen[0] in wins:
            result = ('win', 1) + tuple(chosen)
        else:
            result = ('tie', None) + tuple(chosen)

# Make the caller wait

# It makes sense to design your generator protocols so that any waiting
# has to be done by the caller.
# This includes waiting for user input, IO completion and timers.

# The benefit of waiting in the caller is that other processing
# (and other generators) can be "running" at the same time
# without needing multiple processes or threads.

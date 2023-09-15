'''Implement a class called player that represents a cricket player.  The player class should have a
method called play()  whixh prints "The player is playing cricket. Deeive two classes,batsman and
Bowler, from the player class. Override the play() method in each dervied class to "The batsman
is batting" and "The bowler is bowling ", respectively. Write a program to create objects of both the
Batsman and Bowler classes and call the play () method for rach object.'''


# Define the base class player
class player:
    def play(self):
        print("The player is playing cricket.")

# Define the derived class Batsman
class Batsman(player):
    def play(self):
        print("The batsman is batting.")

# Define the derived class Bowler
class Bowler(player):
    def play(self):
        print ("The bowler is bowling.")

# Create objects of Batsman and classes
batsman = Batsman()
bowler = Bowler()

# Call the play() method for each object
batsman.play()
bowler.play()
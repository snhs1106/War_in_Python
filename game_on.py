import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    
    #Create every card in a deck with the suit and number

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:

    #Create various Card objects that get added into a deck and create an entire 52 card deck.
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
                
    def shuffle(self):
        
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()

class Player:
    
    #Create each player and the moves they are allowed to do

    def __init__(self,name):
        
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        
        #If a player wins, they put all the cards back into their deck

        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


##############################################################
######################### Game Setup #########################
##############################################################

#Create players and deck
player_one = Player('One')
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle()

#Divide deck
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

round_num = 0

while game_on:
    
    #Keep track of number of rounds
    round_num +=1
    print(f'Round {round_num}')
    
    #Checks if either player has run out of cards
    if len(player_one.all_cards) == 0:
        print('Player 1 is out of cards! Player 2 wins!')
        game_on = False
        break
    elif len(player_two.all_cards) == 0:
        print('Player 2 is out of cards! Player 1 wins!')
        game_on = False
        break
        
    #Start new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    at_war = True

    #Offical game play
    while at_war:
        
        #Sees which player one round
        if player_one_cards[-1].value > player_two_cards[-1].value:      
                
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
                
            at_war = False
                
        elif player_two_cards[-1].value > player_one_cards[-1].value:      
                    
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
                    
            at_war = False
        #State of War    
        else:
            print('WAR!')
            #Checks if players have enough cards for War. If not, they automatically lose
            if len(player_one.all_cards) < 5:
                print('Player 1 is unable to declare war')
                print('Player 2 wins!')
                game_on = False
                break
                
            elif len(player_two.all_cards) < 5:
                print('Player 2 is unable to declare war')
                print('Player 1 wins!')
                game_on = False
                break
                
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
    
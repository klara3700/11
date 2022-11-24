# random modul importieren für Ziehen von zufälligen Karten
# Variablen definieren von den verschiednen Farbe:suit und Symbol:ranks der Karten, spades-pik, clubs-Kreuz
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# Boolean Variable für while loop später definieren, wenn der Player agiert



# Klassen definieren
class Card:  # Erstellung verschiedene Karten

    def __init__(self, suit, rank):
        self.suit = suit #optional - zur Vereinfachung
        self.rank = rank

    def __str__(self):  # Methode konvertiert in String, in Klassen wird dabei __str__ verwendet
        return self.rank + ' ' + self.suit    # gibt die Karte mit Symbol und Farbe wieder


class Deck:  # Erstellung Stapel

    def __init__(self):
        self.deck = []  # leer, da Stapel noch nicht erstellt wurde
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))


    def shuffle(self):  # alle Karten des Stapels mischen
        random.shuffle(self.deck)

    def deal(self):  # eine Karte vom Stapel nehmen
        single_card = self.deck.pop() #Karte entnehmen vom Ende des Stapels
        return single_card


class Hand:   # Anzeige aller Karten vom Spieler und Dealer

    def __init__(self):
        self.cards = []
        self.value = 0


    def add_card(self, card):  # Karte dem Dealer oder Player hinzufügen
        self.cards.append(card)
        self.value += values[card.rank]


#Karte ziehen
def hit(deck, hand):
    hand.add_card(deck.deal())


#fragen ob man zieht oder nicht
def hit_or_stand(deck, hand):



    while True:
        ask = input("Hit oder Stand? Bitte Eingabe 'h' oder 's': ")

        if ask.lower() == 'h':
            hit(deck, hand)
            return True
        elif ask.lower() == 's':
            print("Player stand, Dealer spielt.")
            return False  #stoppt den Player, damit Dealer spielen kann
            break

        else:
            print("ungültige Eingabe, bitte erneut eingeben!")
            continue
        break

#aktuellen Status beider Parteien anzeigen
def show_some(player, dealer):
    print("\nDealer's Karten: ")
    print(" <1 versteckte Karte>")
    print("", dealer.cards[1])
    print("\nPlayer's Karten: ", *player.cards)


def show_all(player, dealer):
    print("\nDealer's Karten: ", *dealer.cards)
    print("Dealer's Kartenwert =", dealer.value)
    print("\nPlayer's Karten: ", *player.cards)
    print("Player's Kartenwert =", player.value)


# verschiedene Ausgänge
def player_verliert(player, dealer):
    print("Player verliert!")

def player_gewinnt(player, dealer):
    print("PLAYER GEWINNT!")

def dealer_verliert(player, dealer):
    print("Dealer verliert!")

def dealer_gewinnt(player, dealer):
    print("Dealer gewinnt!")

def gleich(player, dealer):
   print("Unentschieden!")


#aktuelles Spiel mit den Methoden zusammensetzen
while True:

    #gemischte Karten
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()     #player zieht zwei Karten
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()       #dealer ziehr zwei Karten
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Karten zeigen
    show_some(player_hand, dealer_hand)
    a = True
    while a:
#player fragen hit oder stand
        a = hit_or_stand(deck, player_hand)
#Anzeige der jeweiligen KArten beider, Dealer aber eine versteckt
        show_some(player_hand, dealer_hand)
#wenn Player mehr als Kartenwert 21 hat, verliert er
        if player_hand.value > 21:
            player_verliert(player_hand, dealer_hand)
            break


    if player_hand.value <= 21:

        while dealer_hand.value < 17:    #dealer nimmt nur neue Karten solange sein Wert nicht 17 oder mehr ist
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)      #Anzeige aller Karten, die beide besitzen

        if dealer_hand.value > 21:
            dealer_verliert(player_hand, dealer_hand)

        elif dealer_hand.value > player_hand.value:
            dealer_gewinnt(player_hand, dealer_hand)

        elif dealer_hand.value < player_hand.value:
            player_gewinnt(player_hand, dealer_hand)

        elif player_hand.value > 21:
            player_verliert(player_hand, dealer_hand)
        else:
            gleich(player_hand, dealer_hand)



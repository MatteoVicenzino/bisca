import random

class ImportCards():
    
    def __init__(self, deck_name, card_number):
        self.deck = deck_name #creare più decks per il test
        self.cardn = card_number #quante carte ha ognuno
        
    #funzione che prende le carte dal csv e le mette in un array
    def get_cards(self):
        file_deck = open(self.deck, 'r', encoding='utf-8-sig')
        file_deck.readline() #salto la prima riga
        
        array_deck = []
        # legge riga per riga il csv e salva ogni linea in una lista "array_deck"
        for line in file_deck:
            carta = line.strip("\n").split(';')
            carta[0] = int(float(carta[0]))
            array_deck.append(carta)
            
        file_deck.close() 
        return array_deck
    
    #funzione che pesca le carte dall'array in modo randomico
    def card_drawing(self, deck):
        my_hand = []
        carte_nel_mazzo = len(deck) #dimensione del mazzo, alla fine del ciclo while decremento perché ho pescato 1
        while(len(my_hand) < self.cardn):
            drawn_card = random.randint(0, (len(deck)-1)) #pesco una carta
            
            if my_hand == []: # se è la prima dell'array la inserisco
                my_hand.append(drawn_card)
                carte_nel_mazzo -= 1
            else: # se invece non è la prima, controllo di non avere già quella carta
                flag_appoggio = 0
                for value in my_hand:
                    if value == drawn_card: #se trovo uguaglianza alzo una flag
                        flag_appoggio += 1
                
                if flag_appoggio == 0: #se non ho mai flaggato
                    my_hand.append(drawn_card) # inserisco valore 
                    carte_nel_mazzo -= 1

        #ora ho 4 carte in mano, ritorno la mano
        return my_hand
        

        
        

appoggio = ImportCards('cards_test.csv', 4)

#for item in appoggio.get_cards(): print(item)
print('MANO: {}'.format(appoggio.card_drawing(appoggio.get_cards())))
#for item in appoggio.card_drawing(appoggio.get_cards()): print(item)
from random import randint

optimal_suite = ["H","C","D","S"]
optimal_card = {"2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9,
            "10":10,
            "J":11,
            "Q":12,
            "K":13,
            "A":14}
def create_card(rank:str, suite:str) -> dict:
    
    if rank not in optimal_card or suite not in optimal_suite:
        return None
    return {"rank":rank ,"suite":suite ,"value":optimal_card[rank]}

def compare_cards(p1_card: dict, p2_card: dict) -> str:
    if "value" not in p1_card or "value" not in p2_card:
        return None
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    elif p2_card["value"] > p1_card["value"]:
        return "p2"
    else:
        return "WAR"
    
def create_deck() -> list[dict]:
    all_card = []
    for rank in optimal_card:
        for suite in optimal_suite:
            all_card.append(create_card(rank,suite))
    return all_card

def shuffle (deck: list[dict]) -> list[dict]:
    for i in range(1000):
        index1 = randint(0,51)
        index2 = randint(0,51)
        while index1 == index2:
             index2 = randint(0,51)
        
        temp_card = deck[index1]
        deck[index1] = deck[index2]
        deck[index2] = temp_card
        
    return deck

def create_player(name: str = "AI") -> dict:
    pass
def init_game() -> dict:
    player1 = create_player("m")
    player2 = create_player()
    deck = create_deck()
    shuffle(deck)
    player1[ "hand"]= deck[:26]
    player2[ "hand"]= deck[26:]
    return{
            "deck":deck
            "player1":player1
            "player2":player2
        }
    
def play_round(player_1: dict, player_2: dict)-> None:
    p1_card = player_1["hand"].pop()
    p2_card = player_2["hand"].pop()
    result_compare = compare_cards(p1_card,p2_card)
    if result_compare =="p1":
        player_1["won_pile"].append
        
if __name__ == "__main__":
    game_dict = init_game()
    while len(game_dict["player_1"]["hand"]) > 0 and len(game_dict["player_2"]["hand"]) > 0:
        play_round(game_dict["player_1"],game_dict["playe   r_2"])
        
def return_winner(p1_won_pile:list,p2_won_pile:list) :
    len_p1 = len(p1_won_pile) 
    len_p2 = len(p2_won_pile) 
    if len_p1 > len_p2:
        print("p1")
    elif len_p2 > len_p1:
        print("p2")
    else:
        
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

    return{
        "name":name,
        "hand": [],
        "won_pile":[]
    }
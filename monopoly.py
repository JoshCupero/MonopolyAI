import random

# ── Data & Constants ──────────────────────────────────────────────────────────

dice = [1, 2, 3, 4, 5, 6]

board = {
    0:  {"name": "go",                    "price": 0, "type": "go"},
    1:  {"name": "mediterranean_avenue",  "price": 60, "type": "property", "rent": [2, 4, 10, 30, 90, 160, 250], "color_group": "brown", "house_cost": 50},
    2:  {"name": "community_chest_1",     "price": 0, "type": "community_chest"},
    3:  {"name": "baltic_avenue",         "price": 60, "type": "property", "rent": [4, 8, 20, 60, 180, 320, 450], "color_group": "brown", "house_cost": 50},
    4:  {"name": "income_tax",            "price": 200, "type": "tax"},
    5:  {"name": "reading_railroad",      "price": 200, "type": "railroad", "rent": [25, 50, 100, 200]},
    6:  {"name": "oriental_avenue",       "price": 100, "type": "property", "rent": [6, 12, 30, 90, 270, 400, 550], "color_group": "light_blue", "house_cost": 50},
    7:  {"name": "chance_1",              "price": 0, "type": "chance"},
    8:  {"name": "vermont_avenue",        "price": 100, "type": "property", "rent": [6, 12, 30, 90, 270, 400, 550], "color_group": "light_blue", "house_cost": 50},
    9:  {"name": "connecticut_avenue",    "price": 120, "type": "property", "rent": [8, 16, 40, 100, 300, 450, 600], "color_group": "light_blue", "house_cost": 50},
    10: {"name": "jail",                  "price": 0, "type": "jail"},
    11: {"name": "st.charles_place",      "price": 140, "type": "property", "rent": [10, 20, 50, 150, 450, 625, 750], "color_group": "pink", "house_cost": 100},
    12: {"name": "electric_company",      "price": 150, "type": "utility", "rent": [4, 10]},
    13: {"name": "states_avenue",         "price": 140, "type": "property", "rent": [10, 20, 50, 150, 450, 625, 750], "color_group": "pink", "house_cost": 100},
    14: {"name": "virginia_avenue",       "price": 160, "type": "property", "rent": [12, 24, 60, 180, 500, 700, 900], "color_group": "pink", "house_cost": 100},
    15: {"name": "pennsylvania_railroad", "price": 200, "type": "railroad", "rent": [25, 50, 100, 200]},
    16: {"name": "st.james_place",        "price": 180, "type": "property", "rent": [14, 28, 70, 200, 550, 750, 950], "color_group": "orange", "house_cost": 100},
    17: {"name": "community_chest_2",     "price": 0, "type": "community_chest"},
    18: {"name": "tennessee_avenue",      "price": 180, "type": "property", "rent": [14, 28, 70, 200, 550, 750, 950], "color_group": "orange", "house_cost": 100},
    19: {"name": "new_york_avenue",       "price": 200, "type": "property", "rent": [16, 32, 80, 220, 600, 800, 1000], "color_group": "orange", "house_cost": 100},
    20: {"name": "free_parking",          "price": 0, "type": "free_parking"},
    21: {"name": "kentucky_avenue",       "price": 220, "type": "property", "rent": [18, 36, 90, 250, 700, 875, 1050], "color_group": "red", "house_cost": 150},
    22: {"name": "chance_2",              "price": 0, "type": "chance"},
    23: {"name": "indiana_avenue",        "price": 220, "type": "property", "rent": [18, 36, 90, 250, 700, 875, 1050], "color_group": "red", "house_cost": 150},
    24: {"name": "illinois_avenue",       "price": 240, "type": "property", "rent": [20, 40, 100, 300, 750, 925, 1100], "color_group": "red", "house_cost": 150},
    25: {"name": "B.&O._railroad",        "price": 200, "type": "railroad", "rent": [25, 50, 100, 200]},
    26: {"name": "atlantic_avenue",       "price": 260, "type": "property", "rent": [22, 44, 110, 330, 800, 975, 1150], "color_group": "yellow", "house_cost": 150},
    27: {"name": "ventnor_avenue",        "price": 260, "type": "property", "rent": [22, 44, 110, 330, 800, 975, 1150], "color_group": "yellow", "house_cost": 150},
    28: {"name": "water_works",           "price": 150, "type": "utility", "rent": [4, 10], "mortgage_value": 75 },
    29: {"name": "marvin_gardens",        "price": 280, "type": "property", "rent": [24, 48, 120, 360, 850, 1025, 1200], "color_group": "yellow", "house_cost": 150},
    30: {"name": "go_to_jail",            "price": 0, "type": "go_to_jail"},
    31: {"name": "pacific_avenue",        "price": 300, "type": "property", "rent": [26, 52, 130, 390, 900, 1100, 1275], "color_group": "green", "house_cost": 200},
    32: {"name": "north_carolina_avenue", "price": 300, "type": "property", "rent": [26, 52, 130, 390, 900, 1100, 1275], "color_group": "green", "house_cost": 200},
    33: {"name": "community_chest_3",     "price": 0, "type": "community_chest"},
    34: {"name": "pennsylvania_avenue",   "price": 320, "type": "property", "rent": [28, 56, 150, 450, 1000, 1200, 1400], "color_group": "green", "house_cost": 200},
    35: {"name": "short_line",            "price": 200, "type": "railroad", "rent": [25, 50, 100, 200]},
    36: {"name": "chance_3",              "price": 0, "type": "chance"},
    37: {"name": "park_place",            "price": 350, "type": "property", "rent": [35, 70, 175, 500, 1100, 1300, 1500], "color_group": "dark_blue", "house_cost": 200},
    38: {"name": "luxury_tax",            "price": 100, "type": "tax"},
    39: {"name": "boardwalk",             "price": 400, "type": "property", "rent": [50, 100, 200, 600, 1400, 1700, 2000], "color_group": "dark_blue", "house_cost": 200},
}

color_group_sizes = {
    "brown": 2, "light_blue": 3, "pink": 3, "orange": 3,
    "red": 3, "yellow": 3, "green": 3, "dark_blue": 2
}

# ── Player class ──────────────────────────────────────────────────────────────

class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.position = 0
        self.money = 1500
        self.properties = []
        self.inJail = False
        self.jail_turns = 0
        self.get_out_of_jail_free = False
        self.consecutive_doubles = 0

    def owns_color_group(self, color):
        group_props = [s["name"] for s in board.values() if s.get("color_group") == color]
        return all(p in self.properties for p in group_props)

# ── Game state ────────────────────────────────────────────────────────────────

bank_houses = 32
bank_hotels = 12
mortgaged_properties = set()
owned_properties = {}   # property_name -> player_id
player_objects = {}     # player_id -> Player object
playing = True

# ── Card actions ──────────────────────────────────────────────────────────────

def draw_chance_card():
    old_pos = current_player.position
    card = random.randint(0, 15)
    match card:
        case 0:
            print("Chance Card: Advance to Boardwalk")
            current_player.position = 39
            action(current_player.position, 0)
            print("Chance Card: Take a trip to Reading Railroad. If you pass Go, collect $200")
            if old_pos > 5:
                current_player.money += 200
                print("Passed Go! Collected $200.")
            current_player.position = 5
            action(current_player.position, 0)
            print("Chance Card: Your building loan matures. Collect $150")
            current_player.money += 150
        case 3:
            print("Chance Card: Advance to Illinois Avenue. If you pass Go, collect $200")
            if old_pos > 24:
                current_player.money += 200
                print("Passed Go! Collected $200.")
            current_player.position = 24
            action(current_player.position, 0)
            print("Chance Card: Advance to nearest Utility. If owned, pay 10x dice roll.")
            new_pos = 12 if (old_pos < 12 or old_pos >= 28) else 28
            if new_pos < old_pos:
                current_player.money += 200
                print("Passed Go! Collected $200.")
            current_player.position = new_pos
            util_name = board[new_pos]['name']
            if util_name not in owned_properties:
                buy = input(f"{util_name} is unowned. Buy for ${board[new_pos]['price']}? (yes/no): ").strip().lower()
                if buy == 'yes':
                    current_player.money -= board[new_pos]['price']
                    current_player.properties.append(util_name)
                    owned_properties[util_name] = current_player.player_id
            else:
                owner_id = owned_properties[util_name]
                if owner_id != current_player.player_id:
                    dice_roll = roll_dice()
                    rent = dice_roll * 10
                    current_player.money -= rent
                    player_objects[owner_id].money += rent
                    print(f"Rolled {dice_roll}. Paid ${rent} to Player {owner_id}.")
        case 5:
            print("Chance Card: Go to Jail. Go directly to Jail, do not pass Go, do not collect $200")
            current_player.position = 10
            current_player.inJail = True
            current_player.jail_turns = 0
        case 6:
            print("Chance Card: Advance to Go. Collect $200")
            current_player.position = 0
            current_player.money += 200
        case 7:
            print("Chance Card: Make general repairs. $25 per house, $100 per hotel.")
            total = sum(
                space.get('houses', 0) * 25 + (100 if space.get('hotel', False) else 0)
                for space in board.values()
                if owned_properties.get(space.get('name')) == current_player.player_id
            )
            current_player.money -= total
            print(f"Paid ${total} in repairs. Money: ${current_player.money}.")
        case 8:
            print("Chance Card: Get Out of Jail Free!")
            current_player.get_out_of_jail_free = True
        case 9:
            print("Chance Card: Advance to St. Charles Place. If you pass Go, collect $200")
            if old_pos > 11:
                current_player.money += 200
                print("Passed Go! Collected $200.")
            current_player.position = 11
            action(current_player.position, 0)
            print("Chance Card: You have been elected Chairman of the Board. Pay each player $50.")
            for pid, p in player_objects.items():
                if pid != current_player.player_id:
                    current_player.money -= 50
                    p.money += 50
            print(f"Money: ${current_player.money}.")
        case 11:
            print("Chance Card: Go back 3 spaces.")
            current_player.position = (old_pos - 3) % 40
            action(current_player.position, 0)
        case 12:
            print("Chance Card: Speeding fine $15.")
            current_player.money -= 15
        case 13 | 14:
            print("Chance Card: Advance to nearest Railroad. If owned, pay double rent.")
            if old_pos < 5 or old_pos >= 35:
                new_pos = 5
            elif old_pos < 15:
                new_pos = 15
            elif old_pos < 25:
                new_pos = 25
            else:
                new_pos = 35
            if new_pos < old_pos:
                current_player.money += 200
                print("Passed Go! Collected $200.")
            current_player.position = new_pos
            rr_name = board[new_pos]['name']
            if rr_name not in owned_properties:
                buy = input(f"{rr_name} is unowned. Buy for $200? (yes/no): ").strip().lower()
                if buy == 'yes':
                    current_player.money -= 200
                    current_player.properties.append(rr_name)
                    owned_properties[rr_name] = current_player.player_id
            else:
                owner_id = owned_properties[rr_name]
                if owner_id != current_player.player_id:
                    rr_names = [s['name'] for s in board.values() if s['type'] == 'railroad']
                    owned_count = sum(1 for r in rr_names if owned_properties.get(r) == owner_id)
                    rent = [25, 50, 100, 200][owned_count - 1] * 2
                    current_player.money -= rent
                    player_objects[owner_id].money += rent
                    print(f"Paid ${rent} (double) to Player {owner_id}.")
        case 15:
            print("Chance Card: Bank pays you a dividend of $50.")
            current_player.money += 50

def draw_community_chest_card():
    card = random.randint(0, 14)
    match card:
        case 0:
            print("Community Chest: Get Out of Jail Free!")
            current_player.get_out_of_jail_free = True
        case 1:
            print("Community Chest: Pay $50 to animal shelter.")
            current_player.money -= 50
        case 2:
            print("Community Chest: School playground donation. Collect $100.")
            current_player.money += 100
        case 3:
            print("Community Chest: Elderly neighbor appreciation. Collect $100.")
            current_player.money += 100
        case 4:
            print("Community Chest: Bake sale cookies. Pay $50.")
            current_player.money -= 50
        case 5:
            print("Community Chest: Neighbor's groceries. Collect $20.")
            current_player.money += 20
        case 6:
            print("Community Chest: Car wash fundraiser. Pay $100.")
            current_player.money -= 100
        case 7:
            print("Community Chest: GO TO JAIL. Do not pass Go, do not collect $200.")
            current_player.position = 10
            current_player.inJail = True
            current_player.jail_turns = 0
        case 8:
            print("Community Chest: Bake sale organizer. Collect $25.")
            current_player.money += 25
        case 9:
            print("Community Chest: Block party! Collect $10 from each player.")
            for pid, p in player_objects.items():
                if pid != current_player.player_id:
                    p.money -= 10
                    current_player.money += 10
            print(f"Money: ${current_player.money}.")
        case 10:
            print("Community Chest: Children's hospital visit. Collect $100.")
            current_player.money += 100
        case 11:
            print("Community Chest: Blood drive volunteer. Collect $10.")
            current_player.money += 10
        case 12:
            print("Community Chest: Home improvement repairs. Pay $30/house, $115/hotel.")
            total = sum(
                space.get('houses', 0) * 30 + (115 if space.get('hotel', False) else 0)
                for space in board.values()
                if owned_properties.get(space.get('name')) == current_player.player_id
            )
            current_player.money -= total
            print(f"Paid ${total} in repairs. Money: ${current_player.money}.")
        case 13:
            print("Community Chest: Advance to GO. Collect $200.")
            current_player.position = 0
            current_player.money += 200
        case 14:
            print("Community Chest: Storm cleanup. Collect $200.")
            current_player.money += 200

# ── Utility helpers ──────────────────────────────────────────────────────────

def roll_dice():
    return random.choice(dice) + random.choice(dice)

def move_player(roll):
    old_position = current_player.position
    current_player.position = (current_player.position + roll) % 40
    if current_player.position < old_position:
        current_player.money += 200
        print(f"Player {current_player.player_id} passed Go! Collected $200. Money: ${current_player.money}.")

def railroad_rent(owner_id):
    rr_names = [s['name'] for s in board.values() if s['type'] == 'railroad']
    owned_count = sum(1 for r in rr_names if owned_properties.get(r) == owner_id)
    return [25, 50, 100, 200][owned_count - 1]

def utility_rent(owner_id, dice_roll):
    util_names = [s['name'] for s in board.values() if s['type'] == 'utility']
    owned_count = sum(1 for u in util_names if owned_properties.get(u) == owner_id)
    return dice_roll * (10 if owned_count == 2 else 4)

# ── Landing actions ──────────────────────────────────────────────────────────

def check_bankruptcy():
    if current_player.money < 0:
        print(f"Player {current_player.player_id} has gone bankrupt!")
        declare_bankruptcy()
        return True
    return False

def check_winner():
    active = list(player_objects.keys())
    if len(active) == 1:
        print(f"\nPlayer {active[0]} wins! All other players have gone bankrupt.")
        return True
    return False

def auction(position):
    property_name = board[position]['name']
    property_price = board[position]['price']
    print(f"\n--- Auction: {property_name} (list price ${property_price}) ---")
    bids = {}
    for pid in list(player_objects.keys()):
        p = player_objects[pid]
        bid_input = input(f"Player {pid} (${p.money}), enter bid (0 to pass): ").strip()
        bid = int(bid_input) if bid_input.isdigit() else 0
        if 0 < bid <= p.money:
            bids[pid] = bid
    if not bids:
        print("No bids. Property returned to bank.")
        return
    winner_id = max(bids, key=lambda k: bids[k])
    winner = player_objects[winner_id]
    winner.money -= bids[winner_id]
    winner.properties.append(property_name)
    owned_properties[property_name] = winner_id
    print(f"Player {winner_id} won {property_name} for ${bids[winner_id]}. Money: ${winner.money}.")

def action(position, dice_roll):
    space = board[position]
    space_type = space['type']

    if space_type in ('property', 'railroad', 'utility'):
        property_name = space['name']
        property_price = space['price']
        print(f"Player {current_player.player_id} landed on {property_name}.")
        if property_name not in owned_properties:
            if current_player.money >= property_price:
                buy = input(f"Buy {property_name} for ${property_price}? (yes/no): ").strip().lower()
                if buy == 'yes':
                    current_player.money -= property_price
                    current_player.properties.append(property_name)
                    owned_properties[property_name] = current_player.player_id
                    print(f"Bought {property_name}. Money: ${current_player.money}.")
                else:
                    auction(position)
            else:
                print(f"Can't afford {property_name} (${property_price}).")
                auction(position)
        else:
            owner_id = owned_properties[property_name]
            if owner_id != current_player.player_id:
                if property_name in mortgaged_properties:
                    print(f"{property_name} is mortgaged. No rent owed.")
                    return
                if space_type == 'railroad':
                    rent = railroad_rent(owner_id)
                elif space_type == 'utility':
                    rent = utility_rent(owner_id, dice_roll)
                else:
                    color = space.get('color_group')
                    houses = space.get('houses', 0)
                    hotel = space.get('hotel', False)
                    if hotel:
                        rent = space['rent'][6]
                    elif houses > 0:
                        rent = space['rent'][houses]
                    else:
                        group_props = [s['name'] for s in board.values() if s.get('color_group') == color]
                        owner_has_monopoly = all(owned_properties.get(p) == owner_id for p in group_props)
                        rent = space['rent'][0] * 2 if owner_has_monopoly else space['rent'][0]
                current_player.money -= rent
                player_objects[owner_id].money += rent
                print(f"Player {current_player.player_id} paid ${rent} rent to Player {owner_id}. Money: ${current_player.money}.")

    elif space_type == 'tax':
        tax_amount = space['price']
        current_player.money -= tax_amount
        print(f"Player {current_player.player_id} paid ${tax_amount} in taxes. Money: ${current_player.money}.")

    elif space_type == 'go_to_jail':
        current_player.position = 10
        current_player.inJail = True
        current_player.jail_turns = 0
        current_player.consecutive_doubles = 0
        print(f"Player {current_player.player_id} is sent to jail!")

    elif space_type == 'chance':
        print(f"Player {current_player.player_id} landed on Chance. Drawing a card...")
        draw_chance_card()

    elif space_type == 'community_chest':
        print(f"Player {current_player.player_id} landed on Community Chest. Drawing a card...")
        draw_community_chest_card()

    elif space_type == 'free_parking':
        print(f"Player {current_player.player_id} landed on Free Parking. Nothing happens.")

    elif space_type == 'jail':
        if current_player.inJail:
            print(f"Player {current_player.player_id} is in jail.")
        else:
            print(f"Player {current_player.player_id} is just visiting jail.")

# ── Player management ────────────────────────────────────────────────────────

def declare_bankruptcy():
    print(f"Player {current_player.player_id} has declared bankruptcy.")
    for property_name in list(current_player.properties):
        owned_properties.pop(property_name, None)
        mortgaged_properties.discard(property_name)
    current_player.properties.clear()
    del player_objects[current_player.player_id]

# ── Property management ──────────────────────────────────────────────────────

def mortgage_property(property_name):
    if property_name not in current_player.properties:
        print(f"You don't own {property_name}.")
        return
    if property_name in mortgaged_properties:
        print(f"{property_name} is already mortgaged.")
        return
    pos = next((k for k, v in board.items() if v['name'] == property_name), None)
    if pos is not None and (board[pos].get('houses', 0) > 0 or board[pos].get('hotel', False)):
        print(f"Sell all houses/hotels on {property_name} before mortgaging.")
        return
    mortgage_value = int(board[pos]['price'] * 0.5)
    mortgaged_properties.add(property_name)
    current_player.money += mortgage_value
    print(f"Mortgaged {property_name} for ${mortgage_value}. Money: ${current_player.money}.")

def unmortgage_property(property_name):
    if property_name not in current_player.properties:
        print(f"You don't own {property_name}.")
        return
    if property_name not in mortgaged_properties:
        print(f"{property_name} is not mortgaged.")
        return
    pos = next(k for k, v in board.items() if v['name'] == property_name)
    unmortgage_value = int(board[pos]['price'] * 0.55)
    if current_player.money < unmortgage_value:
        print(f"Need ${unmortgage_value} to unmortgage. You have ${current_player.money}.")
        return
    current_player.money -= unmortgage_value
    mortgaged_properties.discard(property_name)
    print(f"Unmortgaged {property_name} for ${unmortgage_value}. Money: ${current_player.money}.")

def build_house(property_name):
    global bank_houses
    pos = next((k for k, v in board.items() if v['name'] == property_name), None)
    if property_name not in current_player.properties:
        print(f"You don't own {property_name}.")
        return
    if pos is None or board[pos]['type'] != 'property':
        print(f"{property_name} is not a buildable property.")
        return
    if property_name in mortgaged_properties:
        print(f"{property_name} is mortgaged.")
        return
    color = board[pos].get('color_group')
    if not current_player.owns_color_group(color):
        print(f"You must own all {color} properties to build.")
        return
    if board[pos].get('hotel', False):
        print(f"{property_name} already has a hotel.")
        return
    if board[pos].get('houses', 0) >= 4:
        print(f"{property_name} already has 4 houses. Build a hotel instead.")
        return
    group_props = [k for k, v in board.items() if v.get('color_group') == color]
    min_houses = min(board[p].get('houses', 0) for p in group_props)
    if board[pos].get('houses', 0) > min_houses:
        print(f"Must build evenly. Build on another {color} property first.")
        return
    if bank_houses == 0:
        print("The bank has no houses left.")
        return
    cost = board[pos]['house_cost']
    if current_player.money < cost:
        print(f"Need ${cost} to build. You have ${current_player.money}.")
        return
    current_player.money -= cost
    board[pos]['houses'] = board[pos].get('houses', 0) + 1
    bank_houses -= 1
    print(f"Built a house on {property_name}. Houses: {board[pos]['houses']}. Money: ${current_player.money}.")

def build_hotel(property_name):
    global bank_hotels, bank_houses
    pos = next((k for k, v in board.items() if v['name'] == property_name), None)
    if property_name not in current_player.properties:
        print(f"You don't own {property_name}.")
        return
    if pos is None or board[pos]['type'] != 'property':
        print(f"{property_name} is not a buildable property.")
        return
    color = board[pos].get('color_group')
    if not current_player.owns_color_group(color):
        print(f"You must own all {color} properties to build.")
        return
    if board[pos].get('hotel', False):
        print(f"{property_name} already has a hotel.")
        return
    if board[pos].get('houses', 0) != 4:
        print(f"Need 4 houses on {property_name} before building a hotel.")
        return
    if bank_hotels == 0:
        print("The bank has no hotels left.")
        return
    cost = board[pos]['house_cost']
    if current_player.money < cost:
        print(f"Need ${cost} to build. You have ${current_player.money}.")
        return
    current_player.money -= cost
    board[pos]['houses'] = 0
    board[pos]['hotel'] = True
    bank_hotels -= 1
    bank_houses += 4
    print(f"Built a hotel on {property_name}. Money: ${current_player.money}.")

def sell_house(property_name):
    global bank_houses
    pos = next((k for k, v in board.items() if v['name'] == property_name), None)
    if property_name not in current_player.properties:
        print(f"You don't own {property_name}.")
        return
    if pos is None or board[pos].get('houses', 0) == 0:
        print(f"No houses on {property_name}.")
        return
    color = board[pos].get('color_group')
    group_props = [k for k, v in board.items() if v.get('color_group') == color]
    max_houses = max(board[p].get('houses', 0) for p in group_props)
    if board[pos].get('houses', 0) < max_houses:
        print(f"Must sell evenly. Sell from another {color} property first.")
        return
    refund = board[pos]['house_cost'] // 2
    current_player.money += refund
    board[pos]['houses'] -= 1
    bank_houses += 1
    print(f"Sold a house on {property_name} for ${refund}. Houses: {board[pos]['houses']}. Money: ${current_player.money}.")

def sell_hotel(property_name):
    global bank_hotels, bank_houses
    pos = next((k for k, v in board.items() if v['name'] == property_name), None)
    if property_name not in current_player.properties:
        print(f"You don't own {property_name}.")
        return
    if pos is None or not board[pos].get('hotel', False):
        print(f"No hotel on {property_name}.")
        return
    refund = board[pos]['house_cost'] // 2
    current_player.money += refund
    board[pos]['hotel'] = False
    bank_hotels += 1
    houses_back = min(4, bank_houses)
    board[pos]['houses'] = houses_back
    bank_houses -= houses_back
    print(f"Sold hotel on {property_name} for ${refund}. Houses left: {board[pos]['houses']}. Money: ${current_player.money}.")

def trade_properties():
    print(f"\n--- Trade Menu ---")
    print(f"Your properties: {current_player.properties if current_player.properties else 'None'}")
    print(f"Your money: ${current_player.money}")

    other_id_input = input(f"Enter the player number to trade with: ").strip()
    if not other_id_input.isdigit():
        print("Invalid player number.")
        return
    other_id = int(other_id_input)
    if other_id == current_player.player_id or other_id not in player_objects:
        print("Invalid player number.")
        return

    other_props = [name for name, owner in owned_properties.items() if owner == other_id]
    print(f"Player {other_id}'s properties: {other_props if other_props else 'None'}")

    print("\nWhat are you offering? (leave blank to skip)")
    offer_props_input = input("Properties to offer (comma-separated, or blank): ").strip()
    offer_props = [p.strip() for p in offer_props_input.split(",") if p.strip()] if offer_props_input else []
    for p in offer_props:
        if p not in current_player.properties:
            print(f"You don't own '{p}'.")
            return
    offer_money_input = input("Money to offer (or 0): ").strip()
    offer_money = int(offer_money_input) if offer_money_input.isdigit() else 0
    if offer_money > current_player.money:
        print("You don't have enough money.")
        return

    print("\nWhat do you want in return? (leave blank to skip)")
    want_props_input = input("Properties you want (comma-separated, or blank): ").strip()
    want_props = [p.strip() for p in want_props_input.split(",") if p.strip()] if want_props_input else []
    for p in want_props:
        if p not in other_props:
            print(f"Player {other_id} doesn't own '{p}'.")
            return
    want_money_input = input("Money you want (or 0): ").strip()
    want_money = int(want_money_input) if want_money_input.isdigit() else 0

    if not offer_props and offer_money == 0 and not want_props and want_money == 0:
        print("Trade cancelled — nothing was specified.")
        return

    print(f"\n--- Trade Proposal ---")
    print(f"Player {current_player.player_id} offers: {offer_props if offer_props else 'no properties'} + ${offer_money}")
    print(f"Player {current_player.player_id} wants:  {want_props if want_props else 'no properties'} + ${want_money}")
    confirm = input(f"Player {other_id}, do you accept this trade? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("Trade rejected.")
        return

    for p in offer_props:
        current_player.properties.remove(p)
        owned_properties[p] = other_id
    for p in want_props:
        current_player.properties.append(p)
        owned_properties[p] = current_player.player_id
    current_player.money -= offer_money
    current_player.money += want_money
    player_objects[other_id].money += offer_money
    player_objects[other_id].money -= want_money
    print(f"Trade completed! Player {current_player.player_id}: {current_player.properties}, ${current_player.money}")

# ── Turn management ──────────────────────────────────────────────────────────

def turn_menu():
    while True:
        print("\nWhat would you like to do?")
        print("1. End Turn    2. View Status    3. View Board    4. Declare Bankruptcy")
        print("5. Trade       6. Mortgage       7. Unmortgage")
        print("8. Build House 9. Build Hotel   10. Sell House   11. Sell Hotel")
        choice = input("Choice: ").strip()
        match choice:
            case '1':
                print(f"Player {current_player.player_id} ended their turn.")
                break
            case '2':
                print(f"\nPlayer {current_player.player_id}: ${current_player.money} | "
                      f"Pos: {current_player.position} ({board[current_player.position]['name']}) | "
                      f"Jail: {current_player.inJail}")
                print(f"Properties: {current_player.properties if current_player.properties else 'None'}")
            case '3':
                print("\nBoard:")
                for pos, space in board.items():
                    owner = owned_properties.get(space['name'], 'Bank')
                    mtg = ' (mortgaged)' if space['name'] in mortgaged_properties else ''
                    houses = space.get('houses', 0)
                    hotel = space.get('hotel', False)
                    building = f' [{houses} house(s)]' if houses else (' [hotel]' if hotel else '')
                    print(f"  {pos:2}. {space['name']:<30} {owner}{mtg}{building}")
            case '4':
                declare_bankruptcy()
                break
            case '5':
                trade_properties()
            case '6':
                pname = input("Property to mortgage: ").strip()
                mortgage_property(pname)
            case '7':
                pname = input("Property to unmortgage: ").strip()
                unmortgage_property(pname)
            case '8':
                pname = input("Property to build house on: ").strip()
                build_house(pname)
            case '9':
                pname = input("Property to build hotel on: ").strip()
                build_hotel(pname)
            case '10':
                pname = input("Property to sell house from: ").strip()
                sell_house(pname)
            case '11':
                pname = input("Property to sell hotel from: ").strip()
                sell_hotel(pname)
            case _:
                print("Invalid choice.")

def turn():
    global playing

    if current_player.inJail:
        print(f"\nPlayer {current_player.player_id} is in jail (turn {current_player.jail_turns + 1}/3).")
        if current_player.get_out_of_jail_free:
            use_card = input("Use Get Out of Jail Free card? (yes/no): ").strip().lower()
            if use_card == 'yes':
                current_player.inJail = False
                current_player.get_out_of_jail_free = False
                current_player.jail_turns = 0
                print(f"Player {current_player.player_id} used their Get Out of Jail Free card!")
        if current_player.inJail:
            pay = input("Pay $50 to get out of jail? (yes/no): ").strip().lower()
            if pay == 'yes' and current_player.money >= 50:
                current_player.money -= 50
                current_player.inJail = False
                current_player.jail_turns = 0
                print(f"Player {current_player.player_id} paid $50 and is out of jail.")
        if current_player.inJail:
            input("Press Enter to roll.")
            die1 = random.choice(dice)
            die2 = random.choice(dice)
            print(f"Rolled {die1} and {die2}.")
            if die1 == die2:
                current_player.inJail = False
                current_player.jail_turns = 0
                print(f"Doubles! Player {current_player.player_id} is out of jail!")
                move_player(die1 + die2)
                print(f"Moved to {current_player.position} ({board[current_player.position]['name']}).")
                action(current_player.position, die1 + die2)
            else:
                current_player.jail_turns += 1
                if current_player.jail_turns >= 3:
                    current_player.money -= 50
                    current_player.inJail = False
                    current_player.jail_turns = 0
                    print(f"3 turns in jail. Paid $50 and released.")
                    move_player(die1 + die2)
                    print(f"Moved to {current_player.position} ({board[current_player.position]['name']}).")
                    action(current_player.position, die1 + die2)
                else:
                    print(f"No doubles. Player {current_player.player_id} stays in jail.")
        if check_bankruptcy():
            return
        if check_winner():
            playing = False
            return
        turn_menu()
        return

    current_player.consecutive_doubles = 0
    while True:
        input("Press Enter to roll.")
        die1 = random.choice(dice)
        die2 = random.choice(dice)
        roll = die1 + die2
        print(f"Player {current_player.player_id} rolled {die1} + {die2} = {roll}.")

        if die1 == die2:
            current_player.consecutive_doubles += 1
            if current_player.consecutive_doubles == 3:
                print(f"Three doubles in a row! Player {current_player.player_id} goes to jail!")
                current_player.position = 10
                current_player.inJail = True
                current_player.jail_turns = 0
                current_player.consecutive_doubles = 0
                return
        else:
            current_player.consecutive_doubles = 0

        move_player(roll)
        print(f"Player {current_player.player_id} moved to {current_player.position} ({board[current_player.position]['name']}).")
        action(current_player.position, roll)

        if check_bankruptcy():
            return
        if check_winner():
            playing = False
            return
        if current_player.inJail:
            return
        if die1 != die2:
            break
        print(f"Doubles! Player {current_player.player_id} rolls again.")

    turn_menu()
    if check_winner():
        playing = False

# ── Game setup ───────────────────────────────────────────────────────────────

while True:
    nPlayers = int(input("Enter the number of players: "))
    if 2 <= nPlayers <= 8:
        break
    print("Invalid number of players. Please enter a number between 2 and 8.")

order_rolls = {}
for i in range(1, nPlayers + 1):
    roll = random.choice(dice) + random.choice(dice)
    print(f"Player {i} rolled a {roll}.")
    order_rolls[i] = roll

sorted_players = sorted(order_rolls.items(), key=lambda x: x[1], reverse=True)
player_order = [p for p, r in sorted_players]
print("\nPlayer Order:")
for rank, (player, roll) in enumerate(sorted_players, start=1):
    print(f"{rank}. Player {player} with a roll of {roll}")

for player_id in player_order:
    player_objects[player_id] = Player(player_id)

# ── Game loop ─────────────────────────────────────────────────────────────────

while playing:
    for player_id in list(player_order):
        if player_id not in player_objects:
            continue
        current_player = player_objects[player_id]
        print(f"\n=== Player {current_player.player_id}'s turn ===")
        turn()
        if not playing:
            break
    if len(player_objects) == 1:
        winner = list(player_objects.keys())[0]
        print(f"\nPlayer {winner} wins!")
        playing = False
    elif len(player_objects) == 0:
        print("\nNo players remaining. Game over.")
        playing = False

    
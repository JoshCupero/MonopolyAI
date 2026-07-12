from copy import deepcopy
import random

MAX_TURNS = 2000

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

# ── Player ───────────────────────────────────────────────────────────────────

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


# ── MonopolyGame simulation class ────────────────────────────────────────────

class MonopolyGame:

    def __init__(self, num_players=2, seed=None, verbose=False):
        self.num_players = num_players
        self.rng = random.Random(seed)
        self.verbose = verbose
        self.reset()

    # ── Lifecycle ─────────────────────────────────────────────────────────────

    def reset(self):
        """Fully reset to a fresh game. Returns the initial observation."""
        self.board = deepcopy(board)
        self.players = {i: Player(i) for i in range(self.num_players)}
        self.owned_properties = {}        # property_name -> player_id
        self.mortgaged_properties = set()
        self.bank_houses = 32
        self.bank_hotels = 12
        self.current_player_index = 0
        self.player_order = list(range(self.num_players))
        self.playing = True
        self.turn_count = 0
        self.pending_decision = None      # set when the game needs a player choice
        self._last_roll = (0, 0)
        return self.get_observation(0)

    @property
    def current_player(self):
        pid = self.player_order[self.current_player_index]
        return self.players[pid]

    # ── Public control API ────────────────────────────────────────────────────

    def advance_until_decision(self):
        """
        Run automatic game events until either a player decision is required
        or the game ends.
        """
        while self.playing and self.pending_decision is None:
            self._take_automatic_turn()

    def get_valid_actions(self):
        if self.pending_decision is None:
            return []
        t = self.pending_decision["type"]
        if t == "buy_property":
            return [0, 1]   # 0 = decline, 1 = buy
        if t == "pay_jail":
            if self.current_player.money >= 50:
                return [0, 1]   # 0 = roll for doubles, 1 = pay $50
            return [0]
        return []

    def apply_action(self, action):
        """Apply the agent's integer action to the current pending decision."""
        decision = self.pending_decision

        if decision is None:
            raise RuntimeError("No decision is pending.")

        valid_actions = self.get_valid_actions()
        if action not in valid_actions:
            raise ValueError(
                f"Invalid action {action}. Valid actions: {valid_actions}"
            )

        self.pending_decision = None

        if decision["type"] == "buy_property":
            self._resolve_buy(action, decision)
        elif decision["type"] == "pay_jail":
            self._resolve_jail_decision(action)

    # ── Observation ───────────────────────────────────────────────────────────

    def get_observation(self, agent_id):
        """
        Return a fixed-size numeric list (length 50) describing the game state
        from the perspective of agent_id.
        """
        cp = self.players.get(agent_id, Player(agent_id))

        opp_positions = [p.position for pid, p in self.players.items() if pid != agent_id]
        opp_moneys    = [p.money    for pid, p in self.players.items() if pid != agent_id]
        avg_opp_pos   = sum(opp_positions) / max(len(opp_positions), 1)
        avg_opp_money = sum(opp_moneys)    / max(len(opp_moneys), 1)

        pending_price = 0
        if self.pending_decision and self.pending_decision["type"] == "buy_property":
            pos = self.pending_decision["position"]
            pending_price = self.board[pos]["price"]

        is_buy_decision = float(
            self.pending_decision is not None
            and self.pending_decision["type"] == "buy_property"
        )
        is_jail_decision = float(
            self.pending_decision is not None
            and self.pending_decision["type"] == "pay_jail"
        )

        # Ownership: +1 = mine, 0 = unowned, -1 = opponent
        ownership = []
        for pos in range(40):
            name  = self.board[pos]["name"]
            owner = self.owned_properties.get(name, -1)
            ownership.append(1 if owner == agent_id else (0 if owner == -1 else -1))

        return [
            cp.position / 39.0,
            cp.money / 1500.0,
            avg_opp_pos / 39.0,
            avg_opp_money / 1500.0,
            pending_price / 400.0,
            float(cp.inJail),
            float(cp.get_out_of_jail_free),
            is_buy_decision,
            is_jail_decision,
            self.bank_houses / 32.0,
            self.bank_hotels / 12.0,
            self.turn_count / MAX_TURNS,
        ] + ownership   # total length = 52

    # ── Game-over queries ─────────────────────────────────────────────────────

    def is_game_over(self):
        return not self.playing

    def get_net_worth(self, player_id):
        player = self.players.get(player_id)
        if player is None:
            return 0
        property_value = sum(
            self.board[pos]["price"]
            for pos in range(40)
            if self.owned_properties.get(self.board[pos]["name"]) == player_id
        )
        return player.money + property_value

    def get_winner(self):
        if len(self.players) == 1:
            return next(iter(self.players))
        if self.turn_count >= MAX_TURNS:
            return max(self.players, key=self.get_net_worth)
        return None

    # ── Internal turn engine ──────────────────────────────────────────────────

    def _take_automatic_turn(self):
        cp = self.current_player

        # ── Jail ────────────────────────────────────────────────────────────
        if cp.inJail:
            self._log(f"Player {cp.player_id} is in jail (turn {cp.jail_turns + 1}/3).")
            if cp.get_out_of_jail_free:
                cp.inJail = False
                cp.get_out_of_jail_free = False
                cp.jail_turns = 0
                self._log(f"Player {cp.player_id} used Get Out of Jail Free card.")
            elif cp.jail_turns >= 2:
                cp.money -= 50
                cp.inJail = False
                cp.jail_turns = 0
                self._log(f"Player {cp.player_id} paid $50 (forced) and left jail.")
            else:
                self.pending_decision = {"type": "pay_jail", "player_id": cp.player_id}
                return

        # ── Roll ─────────────────────────────────────────────────────────────
        die1 = self.rng.randint(1, 6)
        die2 = self.rng.randint(1, 6)
        self._last_roll = (die1, die2)
        roll = die1 + die2
        self._log(f"Player {cp.player_id} rolled {die1}+{die2}={roll}.")

        if die1 == die2:
            cp.consecutive_doubles += 1
            if cp.consecutive_doubles == 3:
                self._log(f"Three doubles! Player {cp.player_id} goes to jail.")
                cp.position = 10
                cp.inJail = True
                cp.jail_turns = 0
                cp.consecutive_doubles = 0
                self._finish_turn()
                return
        else:
            cp.consecutive_doubles = 0

        # ── Move ─────────────────────────────────────────────────────────────
        self._move(cp, roll)
        self._log(f"Player {cp.player_id} → {cp.position} ({self.board[cp.position]['name']}).")

        # ── Land ─────────────────────────────────────────────────────────────
        if self._land_action(cp, roll):
            return  # pending_decision was set

        if self._check_bankruptcy(cp):
            return

        if die1 == die2 and not cp.inJail:
            self._log(f"Doubles! Player {cp.player_id} rolls again.")
        else:
            self._finish_turn()

    def _resolve_jail_decision(self, action):
        cp = self.current_player
        if action == 1 and cp.money >= 50:
            cp.money -= 50
            cp.inJail = False
            cp.jail_turns = 0
            self._log(f"Player {cp.player_id} paid $50 and left jail.")
            die1 = self.rng.randint(1, 6)
            die2 = self.rng.randint(1, 6)
            self._last_roll = (die1, die2)
            self._move(cp, die1 + die2)
            self._finish_after_jail_move(cp, die1 + die2)
        else:
            die1 = self.rng.randint(1, 6)
            die2 = self.rng.randint(1, 6)
            self._last_roll = (die1, die2)
            self._log(f"Player {cp.player_id} rolled {die1}+{die2} for jail.")
            if die1 == die2:
                cp.inJail = False
                cp.jail_turns = 0
                self._log(f"Doubles! Player {cp.player_id} leaves jail.")
                self._move(cp, die1 + die2)
                self._finish_after_jail_move(cp, die1 + die2)
            else:
                cp.jail_turns += 1
                self._log(f"No doubles. Player {cp.player_id} stays in jail ({cp.jail_turns}/3).")
                self._finish_turn()

    def _finish_after_jail_move(self, player, dice_roll):
        if self._land_action(player, dice_roll):
            return
        if self._check_bankruptcy(player):
            return
        self._finish_turn()

    def _resolve_buy(self, action, decision):
        cp    = self.current_player
        pos   = decision["position"]
        space = self.board[pos]
        if action == 1:
            cp.money -= space["price"]
            cp.properties.append(space["name"])
            self.owned_properties[space["name"]] = cp.player_id
            self._log(f"Player {cp.player_id} bought {space['name']} for ${space['price']}.")
        else:
            self._log(f"Player {cp.player_id} declined {space['name']}.")
        if not self._check_bankruptcy(cp):
            self._finish_turn()

    def _finish_turn(self):
        self.turn_count += 1
        if self.turn_count >= MAX_TURNS:
            self.playing = False
            self._log("Turn limit reached.")
            return
        if len(self.players) <= 1:
            self.playing = False
            return
        self.current_player_index = (self.current_player_index + 1) % len(self.player_order)
        while self.player_order[self.current_player_index] not in self.players:
            self.current_player_index = (self.current_player_index + 1) % len(self.player_order)

    # ── Movement ──────────────────────────────────────────────────────────────

    def _move(self, player, roll):
        old = player.position
        player.position = (old + roll) % 40
        if player.position < old:
            player.money += 200
            self._log(f"Player {player.player_id} passed Go! +$200.")

    # ── Landing logic ─────────────────────────────────────────────────────────

    def _land_action(self, player, dice_roll):
        """Process landing. Returns True if a pending_decision was set."""
        pos   = player.position
        space = self.board[pos]
        t     = space["type"]

        if t in ("property", "railroad", "utility"):
            name = space["name"]
            if name not in self.owned_properties:
                if player.money >= space["price"]:
                    self.pending_decision = {
                        "type": "buy_property",
                        "position": pos,
                        "player_id": player.player_id,
                    }
                    return True
            else:
                owner_id = self.owned_properties[name]
                if owner_id != player.player_id and name not in self.mortgaged_properties:
                    rent = self._calculate_rent(space, owner_id, dice_roll)
                    player.money -= rent
                    self.players[owner_id].money += rent
                    self._log(f"Player {player.player_id} paid ${rent} rent to Player {owner_id}.")

        elif t == "tax":
            player.money -= space["price"]
            self._log(f"Player {player.player_id} paid ${space['price']} tax.")

        elif t == "go_to_jail":
            player.position = 10
            player.inJail = True
            player.jail_turns = 0
            player.consecutive_doubles = 0
            self._log(f"Player {player.player_id} sent to jail!")

        elif t == "chance":
            self._draw_chance(player)
            return self.pending_decision is not None

        elif t == "community_chest":
            self._draw_community_chest(player)

        return False

    def _calculate_rent(self, space, owner_id, dice_roll):
        t = space["type"]
        if t == "railroad":
            rr = [s["name"] for s in self.board.values() if s["type"] == "railroad"]
            count = sum(1 for r in rr if self.owned_properties.get(r) == owner_id)
            return space["rent"][count - 1]
        if t == "utility":
            utils = [s["name"] for s in self.board.values() if s["type"] == "utility"]
            count = sum(1 for u in utils if self.owned_properties.get(u) == owner_id)
            return dice_roll * (10 if count == 2 else 4)
        houses = space.get("houses", 0)
        hotel  = space.get("hotel", False)
        if hotel:
            return space["rent"][6]
        if houses > 0:
            return space["rent"][houses]
        color = space.get("color_group")
        group = [s["name"] for s in self.board.values() if s.get("color_group") == color]
        monopoly = all(self.owned_properties.get(p) == owner_id for p in group)
        return space["rent"][0] * 2 if monopoly else space["rent"][0]

    # ── Bankruptcy ────────────────────────────────────────────────────────────

    def _check_bankruptcy(self, player):
        if player.money < 0:
            self._log(f"Player {player.player_id} went bankrupt!")
            self._bankrupt(player)
            if len(self.players) <= 1:
                self.playing = False
            else:
                self._finish_turn()
            return True
        return False

    def _bankrupt(self, player):
        for name in list(player.properties):
            self.owned_properties.pop(name, None)
            self.mortgaged_properties.discard(name)
        player.properties.clear()
        del self.players[player.player_id]

    # ── Chance cards ──────────────────────────────────────────────────────────

    def _draw_chance(self, player):
        card    = self.rng.randint(0, 15)
        old_pos = player.position
        self._log(f"Player {player.player_id} drew Chance card {card}.")
        match card:
            case 0:
                player.position = 39
                self._log("Chance: Advance to Boardwalk.")
            case 1:
                if old_pos > 5:
                    player.money += 200
                player.position = 5
                self._log("Chance: Take a trip to Reading Railroad.")
            case 2:
                player.money += 150
                self._log("Chance: Building loan matures. Collect $150.")
            case 3:
                if old_pos > 24:
                    player.money += 200
                player.position = 24
                self._log("Chance: Advance to Illinois Avenue.")
            case 4:
                new_pos = 12 if (old_pos < 12 or old_pos >= 28) else 28
                if new_pos < old_pos:
                    player.money += 200
                player.position = new_pos
                self._log("Chance: Advance to nearest Utility.")
            case 5:
                player.position = 10
                player.inJail = True
                player.jail_turns = 0
                player.consecutive_doubles = 0
                self._log("Chance: Go to Jail.")
            case 6:
                player.position = 0
                player.money += 200
                self._log("Chance: Advance to Go. Collect $200.")
            case 7:
                total = sum(
                    s.get("houses", 0) * 25 + (100 if s.get("hotel", False) else 0)
                    for s in self.board.values()
                    if self.owned_properties.get(s.get("name")) == player.player_id
                )
                player.money -= total
                self._log(f"Chance: Repairs. Paid ${total}.")
            case 8:
                player.get_out_of_jail_free = True
                self._log("Chance: Get Out of Jail Free!")
            case 9:
                if old_pos > 11:
                    player.money += 200
                player.position = 11
                self._log("Chance: Advance to St. Charles Place.")
            case 10:
                for pid, p in self.players.items():
                    if pid != player.player_id:
                        player.money -= 50
                        p.money += 50
                self._log("Chance: Chairman of the Board. Pay each player $50.")
            case 11:
                player.position = (old_pos - 3) % 40
                self._log("Chance: Go back 3 spaces.")
            case 12:
                player.money -= 15
                self._log("Chance: Speeding fine $15.")
            case 13 | 14:
                if old_pos < 5 or old_pos >= 35:
                    new_pos = 5
                elif old_pos < 15:
                    new_pos = 15
                elif old_pos < 25:
                    new_pos = 25
                else:
                    new_pos = 35
                if new_pos < old_pos:
                    player.money += 200
                player.position = new_pos
                self._log("Chance: Advance to nearest Railroad.")
            case 15:
                player.money += 50
                self._log("Chance: Bank dividend $50.")

        # Cards that move the player also trigger landing effects
        if card in (0, 1, 3, 4, 9, 11, 13, 14) and not player.inJail:
            self._land_action(player, 0)

    # ── Community Chest cards ─────────────────────────────────────────────────

    def _draw_community_chest(self, player):
        card = self.rng.randint(0, 14)
        self._log(f"Player {player.player_id} drew Community Chest card {card}.")
        match card:
            case 0:
                player.get_out_of_jail_free = True
                self._log("Community Chest: Get Out of Jail Free!")
            case 1:
                player.money -= 50
                self._log("Community Chest: Pay $50.")
            case 2:
                player.money += 100
                self._log("Community Chest: Collect $100.")
            case 3:
                player.money += 100
                self._log("Community Chest: Collect $100.")
            case 4:
                player.money -= 50
                self._log("Community Chest: Pay $50.")
            case 5:
                player.money += 20
                self._log("Community Chest: Collect $20.")
            case 6:
                player.money -= 100
                self._log("Community Chest: Pay $100.")
            case 7:
                player.position = 10
                player.inJail = True
                player.jail_turns = 0
                player.consecutive_doubles = 0
                self._log("Community Chest: GO TO JAIL.")
            case 8:
                player.money += 25
                self._log("Community Chest: Collect $25.")
            case 9:
                for pid, p in self.players.items():
                    if pid != player.player_id:
                        p.money -= 10
                        player.money += 10
                self._log("Community Chest: Collect $10 from each player.")
            case 10:
                player.money += 100
                self._log("Community Chest: Collect $100.")
            case 11:
                player.money += 10
                self._log("Community Chest: Collect $10.")
            case 12:
                total = sum(
                    s.get("houses", 0) * 30 + (115 if s.get("hotel", False) else 0)
                    for s in self.board.values()
                    if self.owned_properties.get(s.get("name")) == player.player_id
                )
                player.money -= total
                self._log(f"Community Chest: Repairs. Paid ${total}.")
            case 13:
                player.position = 0
                player.money += 200
                self._log("Community Chest: Advance to Go. Collect $200.")
            case 14:
                player.money += 200
                self._log("Community Chest: Collect $200.")

    # ── Logging ───────────────────────────────────────────────────────────────

    def _log(self, msg):
        if self.verbose:
            print(msg)


# ── Opponent policy ──────────────────────────────────────────────────────────

def opponent_action(game):
    """Simple rule-based policy for non-agent players."""
    decision = game.pending_decision
    player   = game.current_player

    if decision["type"] == "buy_property":
        position = decision["position"]
        price    = game.board[position]["price"]
        return 1 if player.money - price >= 200 else 0

    if decision["type"] == "pay_jail":
        return 1 if player.money >= 300 else 0

    raise ValueError(f"Unknown decision type: {decision['type']}")


# ── Interactive main() ───────────────────────────────────────────────────────

def main():
    while True:
        n = input("Enter number of players (2-8): ").strip()
        if n.isdigit() and 2 <= int(n) <= 8:
            break
        print("Please enter a number between 2 and 8.")

    game = MonopolyGame(num_players=int(n), verbose=True)
    game.reset()

    while not game.is_game_over():
        game.advance_until_decision()
        if game.is_game_over():
            break

        dec = game.pending_decision
        if dec is None:
            continue

        cp = game.current_player
        t  = dec["type"]

        if t == "buy_property":
            pos   = dec["position"]
            space = game.board[pos]
            ans = input(f"Player {cp.player_id} — Buy {space['name']} for ${space['price']}? (1=buy, 0=skip): ").strip()
            game.apply_action(1 if ans == "1" else 0)
        elif t == "pay_jail":
            ans = input(f"Player {cp.player_id} — Pay $50 to leave jail? (1=yes, 0=roll): ").strip()
            game.apply_action(1 if ans == "1" else 0)

    winner = game.get_winner()
    if winner is not None:
        print(f"\nGame over! Player {winner} wins!")
    else:
        print("\nGame over — no winner.")


if __name__ == "__main__":
    main()


import random
import time

# --- CẤU HÌNH CƠ BẢN ---
SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
RANK_VALUES = {rank: i for i, rank in enumerate(RANKS, start=2)}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = RANK_VALUES[rank]

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return self.__str__()

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in SUITS for rank in RANKS]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop() if self.cards else None

class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = []
        self.current_bet = 0
        self.is_folded = False

    def receive_card(self, card):
        self.hand.append(card)

    def show_hand(self):
        return f"{self.name} hand: {self.hand}"

    def reset_round(self):
        self.hand = []
        self.current_bet = 0
        self.is_folded = False

    def bet(self, amount):
        if amount > self.chips:
            amount = self.chips  # All-in
        self.chips -= amount
        self.current_bet += amount
        return amount

# --- Class NGƯỜI CHƠI VÀ BOT ---
class HumanPlayer(Player):
    def make_decision(self, current_highest_bet):
        print(f"\n--- Lượt của bạn ({self.name}) ---")
        print(f"Bài của bạn: {self.hand} | Chip: {self.chips}$")
        amount_to_call = current_highest_bet - self.current_bet
        
        while True:
            action = input(f"Chọn hành động - (F)old, (C)all {amount_to_call}$, (R)aise: ").upper()
            if action == 'F':
                self.is_folded = True
                print(f"{self.name} đã Fold.")
                return 0
            elif action == 'C':
                print(f"{self.name} đã Call.")
                return self.bet(amount_to_call)
            elif action == 'R':
                try:
                    raise_amount = int(input("Bạn muốn raise thêm bao nhiêu? $"))
                    total_bet = amount_to_call + raise_amount
                    print(f"{self.name} đã Raise thêm {raise_amount}$.")
                    return self.bet(total_bet)
                except ValueError:
                    print("Vui lòng nhập một số hợp lệ.")
            else:
                print("Lựa chọn không hợp lệ.")

class BotPlayer(Player):
    def make_decision(self, current_highest_bet):
        time.sleep(1) 
        amount_to_call = current_highest_bet - self.current_bet
        

        decision = random.choices(['F', 'C', 'R'], weights=[10, 60, 30])[0]
        
        if decision == 'F' and amount_to_call > 0:
            self.is_folded = True
            print(f"Bot {self.name} đã Fold.")
            return 0
        elif decision == 'R' and self.chips > amount_to_call:
            raise_amount = random.randint(10, 50)
            total_bet = amount_to_call + raise_amount
            print(f"Bot {self.name} đã Raise lên {total_bet}$.")
            return self.bet(total_bet)
        else:
            print(f"Bot {self.name} đã Call/Check.")
            return self.bet(amount_to_call)

# --- QUẢN LÝ TRÒ CHƠI ---
class PokerGame:
    def __init__(self):
        self.deck = Deck()
        self.pot = 0
        self.community_cards = []
        self.players = [
            HumanPlayer("Bạn", 1000),
            BotPlayer("Bot 1", 1000),
            BotPlayer("Bot 2", 1000)
        ]

    def deal_hole_cards(self):
        print("\n--- CHIA BÀI ---")
        for _ in range(2):
            for player in self.players:
                player.receive_card(self.deck.draw())

    def deal_community_cards(self, number_of_cards):
        for _ in range(number_of_cards):
            self.community_cards.append(self.deck.draw())
        print(f"\nBài chung hiện tại: {self.community_cards}")

    def betting_round(self):
        current_highest_bet = 0
        active_players = [p for p in self.players if not p.is_folded and p.chips > 0]
        
        if len(active_players) <= 1:
            return

        for player in active_players:
            if player.is_folded: continue
            bet_amount = player.make_decision(current_highest_bet)
            self.pot += bet_amount
            if player.current_bet > current_highest_bet:
                current_highest_bet = player.current_bet
        
        print(f"-> Tổng Pot hiện tại: {self.pot}$")

    def play_round(self):
        self.deck = Deck() # Bài mới
        self.pot = 0
        self.community_cards = []
        for p in self.players: p.reset_round()

        # 1. Pre-Flop
        self.deal_hole_cards()
        self.betting_round()

        # 2. Flop (3 lá)
        if self.count_active_players() > 1:
            print("\n--- VÒNG FLOP ---")
            self.deal_community_cards(3)
            self.betting_round()

        # 3. Turn (1 lá)
        if self.count_active_players() > 1:
            print("\n--- VÒNG TURN ---")
            self.deal_community_cards(1)
            self.betting_round()

        # 4. River (1 lá)
        if self.count_active_players() > 1:
            print("\n--- VÒNG RIVER ---")
            self.deal_community_cards(1)
            self.betting_round()

        # 5. Showdown
        self.showdown()

    def count_active_players(self):
        return sum(1 for p in self.players if not p.is_folded)

    def showdown(self):
        print("\n=== LẬT BÀI (SHOWDOWN) ===")
        active_players = [p for p in self.players if not p.is_folded]
        
        if len(active_players) == 1:
            winner = active_players[0]
            print(f"{winner.name} thắng {self.pot}$ vì tất cả người khác đã Fold!")
            winner.chips += self.pot
            return

        for p in active_players:
            print(p.show_hand())
        print(f"Bài chung: {self.community_cards}")

        print("\n[Hệ thống] Đang tính toán người chiến thắng...")
        time.sleep(2)
        
        winner = max(active_players, key=lambda p: max([card.value for card in p.hand]))
        print(f"\n🏆 {winner.name} giành chiến thắng và nhận được {self.pot}$! 🏆")
        winner.chips += self.pot

# --- KHỞI ĐỘNG GAME ---
if __name__ == "__main__":
    game = PokerGame()
    while True:
        game.play_round()
        cont = input("\nBạn có muốn chơi ván tiếp theo không? (Y/N): ").upper()
        if cont != 'Y':
            print("Cảm ơn bạn đã chơi!")
            break
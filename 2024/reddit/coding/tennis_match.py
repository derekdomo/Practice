import enum
from typing import Dict, List, Optional

class Status(enum.Enum):
    IN_PROGRESS = 1
    FINISH = 2

class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = 0

    def add_score(self, score: int):
        self.score += score

    def reset_score(self):
        self.score = 30

class Set:
    def __init__(self, playerA: str, playerB: str):
        self.players = {playerA: Player(playerA), playerB: Player(playerB)}
        self.winning_threshold = 45
        self.reset_threshold = 30
        self.set_end = False
        self.winner = None

    def _check_tie(self):
        player_scores = [player.score for player in self.players.values()]
        if min(player_scores) > self.reset_threshold and len(set(player_scores)) == 1:
            for player in self.players.values():
                player.reset_score()

    def print_score(self):
        for player in self.players.values():
            print(f"{player.name} --- {player.score}")

    def add_score(self, player_name: str, score: int) -> Status:
        player = self._validate_player(player_name)
        self._validate_set_unfinished()
        self._validate_score(score)

        player.add_score(score)
        self._check_tie()

        if player.score >= self.winning_threshold:
            self.set_end = True
            self.winner = player.name
            return Status.FINISH
        return Status.IN_PROGRESS

    def is_set_end(self) -> bool:
        return self.set_end

    def get_winner(self) -> Optional[str]:
        if not self.set_end:
            raise ValueError("Set is not yet finished.")
        return self.winner

    def _validate_set_unfinished(self):
        if self.set_end or self.winner:
            raise ValueError("Set already finished.")

    def _validate_player(self, player_name: str) -> Player:
        if player_name not in self.players:
            raise ValueError(f"Player {player_name} is not part of this set.")
        return self.players[player_name]

    def _validate_score(self, score: int):
        if not isinstance(score, int) or score <= 0:
            raise ValueError("Score must be a positive integer.")

class Game:
    def __init__(self, num_of_sets: int, playerA: str, playerB: str):
        if num_of_sets % 2 == 0:
            raise ValueError("Number of sets must be odd.") 
        self.player_names = [playerA, playerB]
        self.winner_count = {playerA: 0, playerB: 0}
        self.num_of_sets = num_of_sets
        self.finished_sets: List[Set] = []
        self.in_progress_set: Optional[Set] = None
        self.future_sets: List[Set] = [Set(playerA, playerB) for _ in range(num_of_sets)]
        self.status = Status.IN_PROGRESS

    def start_new_set(self) -> Set:
        if self.in_progress_set is not None:
            raise ValueError("A set is already in progress.")
        if self.status == Status.FINISH:
            raise ValueError("Game has already finished.")
        if not self.future_sets:
            raise ValueError("No more sets remaining.")

        self.in_progress_set = self.future_sets.pop(0)
        return self.in_progress_set

    def add_score(self, player: str, score: int) -> (Status, Optional[str]):
        if self.in_progress_set is None:
            raise ValueError("No set in progress.")
        if self.status == Status.FINISH:
            raise ValueError("Game has already finished.")

        status = self.in_progress_set.add_score(player, score)
        if status == Status.FINISH:
            self.finished_sets.append(self.in_progress_set)
            self.in_progress_set = None
            self.winner_count[player] += 1
            game_status, winner = self._check_game_ended()
            return game_status, winner
        return Status.IN_PROGRESS, None

    def print_score(self):
        print("Prior Sets")
        print("----------")
        for f_set in self.finished_sets:
            f_set.print_score()

        print("----------")
        print("Current Set")
        print("----------")
        if self.in_progress_set:
            self.in_progress_set.print_score()
        else:
            print("No active set")
        print("\n")

    def auto_play(self):
        import random

        while True:
            if not self.in_progress_set:
                self.print_score()
                self.start_new_set()

            player = random.choice(self.player_names)
            status, winner = self.add_score(player, 10)

            if status == Status.FINISH:
                self.print_score()
                print(f"Winner: {winner}")
                break

    def _check_game_ended(self) -> (Status, Optional[str]):
        winning_scenario = self.num_of_sets // 2 + 1
        for player, count in self.winner_count.items():
            if count == winning_scenario:
                self.status = Status.FINISH
                return Status.FINISH, player
        return Status.IN_PROGRESS, None


game = Game(5, "Xiangyu", "Lya")
game.auto_play()

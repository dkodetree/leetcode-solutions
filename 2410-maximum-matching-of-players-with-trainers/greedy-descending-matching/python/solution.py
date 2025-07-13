class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse = True)
        trainers.sort(reverse = True)
        match_cnt = 0
        trainer_idx = 0
        for player_ability in players:
            if trainer_idx < len(trainers) and trainers[trainer_idx] >= player_ability:
                match_cnt += 1
                trainer_idx += 1
        return match_cnt

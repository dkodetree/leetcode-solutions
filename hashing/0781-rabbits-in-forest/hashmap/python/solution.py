class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans_freq_map = collections.Counter(answers) # ans : freq

        total_rabbits = 0
        for ans, freq in ans_freq_map.items():
            group_size = ans + 1
            num_groups = ceil(freq / group_size)
            total_rabbits += num_groups * group_size
        
        return total_rabbits

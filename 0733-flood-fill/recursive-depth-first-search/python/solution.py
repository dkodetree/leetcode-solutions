class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        visited = set()
        source_color = image[sr][sc]

        result_image = copy.deepcopy(image)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
        # Recursive DFS
        def dfs(row, col):
            if row not in range(rows) or col not in range(cols) or (row, col) in visited or image[row][col] != source_color:
                return
            visited.add((row, col))
            result_image[row][col] = color

            for dr, dc in directions:
                dfs(row + dr, col + dc)

        dfs(sr, sc)
        return result_image

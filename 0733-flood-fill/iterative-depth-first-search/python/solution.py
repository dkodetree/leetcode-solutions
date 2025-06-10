class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        visited = set()
        source_color = image[sr][sc]
        res_image = copy.deepcopy(image)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
        #DFS Iterative
        stack = []
        stack.append((sr, sc))
        visited.add((sr, sc))
        while stack:
            row, col = stack.pop()
            res_image[row][col] = color
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if new_row not in range(rows) or new_col not in range(cols) or (new_row, new_col) in visited or image[new_row][new_col] != source_color:
                    continue
                stack.append((new_row, new_col))
                visited.add((new_row, new_col))
            
        return res_image

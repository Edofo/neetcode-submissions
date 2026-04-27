class Solution:
    def isPathCrossing(self, path: str) -> bool:
        map = set()
        moves = {"N": (1, 0), "S": (-1, 0), "W": (0, -1), "E": (0, 1)}

        pos = [0,0]

        map.add(tuple(pos))

        for direction in path:
            dx, dy = moves[direction]
            pos[0] += dx
            pos[1] += dy
            
            if tuple(pos) in map:
                return True
            
            map.add(tuple(pos))

            
        return False
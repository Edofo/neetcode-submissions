class Solution:
    def isPathCrossing(self, path: str) -> bool:
        map = defaultdict(list)
        pos = [0,0]

        map[tuple(pos)] = 1

        for direction in path:
            if direction == "N":
                pos[0] += 1
            if direction == "S":
                pos[0] -= 1
            if direction == "W":
                pos[1] -= 1
            if direction == "E":
                pos[1] += 1
            
            if tuple(pos) in map:
                return True
            
            map[tuple(pos)] = 1

            
        return False
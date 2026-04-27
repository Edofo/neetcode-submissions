class Solution:
    def isPathCrossing(self, path: str) -> bool:
        map = set()
        pos = [0,0]

        map.add(tuple(pos))

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
            
            map.add(tuple(pos))

            
        return False
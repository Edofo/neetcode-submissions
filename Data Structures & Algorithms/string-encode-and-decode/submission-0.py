class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append("0")
            for letter in s:
                encoded.append(chr(ord(letter) * 2))
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        curr = -1
        for letter in s:
            if letter == "0":
                curr += 1
                decoded.append("")
                continue
            decoded[curr] += (chr(ord(letter) // 2))
        return decoded

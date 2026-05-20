class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) != 0:
            return "∫".join(strs)
        else:
            return "å"

    def decode(self, s: str) -> List[str]:
        if s != "å":
            return s.split("∫")
        else:
            return []
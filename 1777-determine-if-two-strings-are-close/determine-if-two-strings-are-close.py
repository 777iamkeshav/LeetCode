class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Time complexity: O(n log n)
        # Space complexity: O(1)

        if len(word1) != len(word2):
            return False

        freq1 = Counter(word1)
        freq2 = Counter(word2)

        # Step 1: compare unique character sets
        if set(freq1.keys()) != set(freq2.keys()):
            return False

        # Step 2: compare sorted frequency values
        return sorted(freq1.values()) == sorted(freq2.values())
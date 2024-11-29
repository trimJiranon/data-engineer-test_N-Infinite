
def word_mesh(words: list[str]):
    # Write your code here.
    def find_overlap(word1, word2):
        # Find the longest suffix of word1 that matches the prefix of word2
        max_overlap = 0
        for i in range(1, min(len(word1), len(word2)) + 1):
            if word1[-i:] == word2[:i]:
                max_overlap = i
        return word1[-max_overlap:] if max_overlap > 0 else None

    result = ""
    for i in range(len(words) - 1):
        overlap = find_overlap(words[i], words[i + 1])
        if overlap is None:
            return "failed to mesh"
        result += overlap
    
    return result
        

# Run this file for test
assert word_mesh(["beacon", "condominium", "umbilical", "california"]) == "conumcal"
assert word_mesh(["allow", "lowering", "ringmaster", "terror"]) == "lowringter"
assert word_mesh(["abandon", "donation", "onion", "ongoing"]) == "dononon"
assert word_mesh(["jamestown", "ownership", "hippocampus", "pushcart", "cartographer", "pheromone"]) == "ownhippuscartpher"
assert word_mesh(["kingdom", "dominator", "notorious", "usual", "allegory"] ) == "failed to mesh"
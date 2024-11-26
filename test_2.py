
def reverse_string(s: str):
    # Write your code here.
    # Do not use list reverse method
    return "".join(s[-(i+1)] for i, c in enumerate(s))


assert reverse_string("abcd") == "dcba"
assert reverse_string("a3bE5dQPos") == "soPQd5Eb3a"
assert reverse_string("aka$aka") == "aka$aka"
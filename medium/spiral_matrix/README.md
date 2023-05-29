Initial thoughts:  
Endpoint is in the middle ish depends on length

3x3 -> at \[1\]\[1\]
4x3 -> at \[2\]\[1\]
5x3 -> at \[3\]\[1\]
4x4 -> at \[1\]\[2\]

Easiest way might just be recursion?
Four "movements" going left-\>right, then top-\>bottom, then right-\>left, then bottom-\>top
Actually, might be able to just use two, and define the two endpoints
That way, don't need to consider where the final endpoint is

If I'm bored I can test runtime of flattened array and doing the math or non-flattened

Yeah, got pretty distracted on this one. Mine doesn't run great in comparison, but still works :/
After some research, looks like a Depth First Search might work better in comparison

Time complexity is O(m x n)? Since mine is recursive, the recursion depth is min(m, n)/2. Complexity should stay the same though because you still end up hitting every single index once.

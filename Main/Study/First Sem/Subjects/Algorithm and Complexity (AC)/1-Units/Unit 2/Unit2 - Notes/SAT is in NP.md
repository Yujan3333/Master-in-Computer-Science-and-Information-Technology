### For  SAT is in NP (Verification example):

Suppose the Boolean formula is:

$(x∨¬y)∧(y∨z)(x \lor \neg y) \land (y \lor z)(x∨¬y)∧(y∨z)$

- Candidate assignment: $x = \text{true}, y = \text{false}, z = \text{true}$
    
- Check each clause:
    
    - First clause: $x∨¬y=true∨true=true$
        
    - Second clause: $y∨z=false∨true=true$
        
- Both clauses are true, so the formula is satisfied.
    
- This verification requires only a few simple checks, which takes **polynomial time**.

==[Further Explanation](Further%20Explanation.md)==

## For SAT is NP-Complete (Reduction idea example):

Imagine a problem like **"Does a graph have a path of length k from node A to node B?"**

- This problem is in NP (a nondeterministic machine can guess the path and verify it in polynomial time).
    
- We can create a Boolean formula that encodes:
    
    - The machine’s state at each step,
        
    - The path guesses,
        
    - And the conditions that the guessed path is valid.
        
- If this formula is satisfiable, the machine accepts the input.
    
- The conversion from the path problem to SAT can be done in **polynomial time**.
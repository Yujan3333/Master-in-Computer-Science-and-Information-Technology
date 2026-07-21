#PPL #third-semester 


| **DFA (Deterministic Finite Automaton)**                           | **NFA (Non-deterministic Finite Automaton)**                             |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| Exactly **one transition** for each input symbol from every state. | **Zero, one, or multiple transitions** are possible for an input symbol. |
| **ε (epsilon) transitions are not allowed.**                       | **ε (epsilon) transitions may be allowed** (in ε-NFA).                   |
| At any point, there is **only one possible next state**.           | There can be **multiple possible next states**.                          |
| Every state must have a transition for every input symbol.         | A state may not have transitions for some input symbols.                 |
| Simpler to implement.                                              | Easier to design and construct.                                          |
| Requires more states in some cases.                                | Usually requires fewer states.                                           |
| Execution follows a **single path**.                               | Execution may follow **multiple paths simultaneously**.                  |
| Faster and more efficient for implementation.                      | Less efficient to simulate directly.                                     |
| Used directly in lexical analyzers and compilers.                  | Mainly used for designing regular expressions and then converted to DFA. |

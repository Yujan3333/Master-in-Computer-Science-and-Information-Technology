#ippr #third-semester 
## Unsharp Masking & High-Boost Filtering

### Process
1. Create blurred image: $f_b(x,y)$
2. Generate mask: $m(x,y) = f(x,y) - f_b(x,y)$
3. Add back: $g(x,y) = f(x,y) + k*m(x,y)$

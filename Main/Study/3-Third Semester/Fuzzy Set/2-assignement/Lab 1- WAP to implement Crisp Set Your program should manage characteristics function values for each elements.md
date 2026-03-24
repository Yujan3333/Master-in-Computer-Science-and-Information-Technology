

Recall the characteristic function of a crisp set:

$$\chi_A(x)=\begin{cases}1 & x\in A\\0 & x\notin A\end{cases}$$

So the dictionary will store:

```
element → membership (0 or 1)
```

---

# Clean OOP Python Program – Crisp Set (with Comments)

```python
# Crisp Set Implementation using OOP
# Each element has a membership value (0 or 1)
# Dictionary is used to represent the characteristic function

class CrispSet:

    # Constructor
    def __init__(self, universe, elements):
        """
        universe : list of all possible elements
        elements : elements belonging to the set
        """
        self.universe = universe

        # Characteristic function dictionary
        # Example: {1:0, 2:1, 3:0}
        self.char_func = {}

        # Assign membership values
        for u in universe:
            if u in elements:
                self.char_func[u] = 1
            else:
                self.char_func[u] = 0


    # Display characteristic function
    def display(self, name="Set"):
        print(f"\n{name} Characteristic Function")
        for element in self.universe:
            print(f"χ({element}) = {self.char_func[element]}")


    # Union operation
    def union(self, other):
        """
        Union uses MAX rule
        μ(A ∪ B) = max(μA, μB)
        """
        new_elements = []

        for u in self.universe:
            if max(self.char_func[u], other.char_func[u]) == 1:
                new_elements.append(u)

        return CrispSet(self.universe, new_elements)


    # Intersection operation
    def intersection(self, other):
        """
        Intersection uses MIN rule
        μ(A ∩ B) = min(μA, μB)
        """
        new_elements = []

        for u in self.universe:
            if min(self.char_func[u], other.char_func[u]) == 1:
                new_elements.append(u)

        return CrispSet(self.universe, new_elements)


    # Difference operation
    def difference(self, other):
        """
        A - B : elements in A but not in B
        """
        new_elements = []

        for u in self.universe:
            if self.char_func[u] == 1 and other.char_func[u] == 0:
                new_elements.append(u)

        return CrispSet(self.universe, new_elements)


    # Complement operation
    def complement(self):
        """
        Complement rule
        μ(A') = 1 - μ(A)
        """
        new_elements = []

        for u in self.universe:
            if self.char_func[u] == 0:
                new_elements.append(u)

        return CrispSet(self.universe, new_elements)


    # Subset check
    def is_subset(self, other):
        """
        Check if current set is subset of another set
        """
        for u in self.universe:
            if self.char_func[u] == 1 and other.char_func[u] == 0:
                return False
        return True


# -------- MAIN PROGRAM --------

# Input universe
universe = list(map(int, input("Enter universe elements: ").split()))

# Input Set A
setA_elements = list(map(int, input("Enter elements of Set A: ").split()))
A = CrispSet(universe, setA_elements)

# Input Set B
setB_elements = list(map(int, input("Enter elements of Set B: ").split()))
B = CrispSet(universe, setB_elements)

# Display sets
A.display("Set A")
B.display("Set B")

# Union
U = A.union(B)
U.display("A ∪ B")

# Intersection
I = A.intersection(B)
I.display("A ∩ B")

# Difference
D = A.difference(B)
D.display("A - B")

# Complement
C = A.complement()
C.display("A Complement")

# Subset check
print("\nIs A subset of B?", A.is_subset(B))
print("Is B subset of A?", B.is_subset(A))
```

---

# Example Run

Input

```
Enter universe elements: 1 2 3 4 5
Enter elements of Set A: 1 3
Enter elements of Set B: 3 4
```

Output

```
Set A Characteristic Function
χ(1) = 1
χ(2) = 0
χ(3) = 1
χ(4) = 0
χ(5) = 0
```

```
A ∪ B Characteristic Function
χ(1) = 1
χ(2) = 0
χ(3) = 1
χ(4) = 1
χ(5) = 0
```

---

# Why This Version Is Better for a Lab

| Feature            | Reason                                              |
| ------------------ | --------------------------------------------------- |
| Uses OOP           | Shows class design                                  |
| Uses dictionary    | Matches characteristic function                     |
| Clear comments     | Easy for teacher to understand                      |
| Mathematical rules | Union=max, Intersection=min                         |
| All operations     | Union, intersection, difference, complement, subset |

---

```
Element   χA   χB
1         1    0
2         0    0
3         1    1
4         0    1
5         0    0
```



# Tag
#assignment #third-semester #fuzzy-system
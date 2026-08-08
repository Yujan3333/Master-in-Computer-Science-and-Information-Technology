#assignment #fuzzy-system #third-semester 

- limiting the value of membership to 0-1
- All set operations in fuzzy logic

```python
# Lab 2: Fuzzy Set Implementation using OOP (with input validation)

class FuzzySet:

    def __init__(self, universe, memberships):
        self.universe = universe
        self.membership = {}

        # Assign membership values (default 0)
        for u in universe:
            self.membership[u] = memberships.get(u, 0)


    def display(self, name="Set"):
        print(f"\n{name} Membership Function")
        for u in self.universe:
            print(f"μ({u}) = {self.membership[u]}")


    # Union (max)
    def union(self, other):
        new_membership = {}
        for u in self.universe:
            new_membership[u] = max(self.membership[u], other.membership[u])
        return FuzzySet(self.universe, new_membership)


    # Intersection (min)
    def intersection(self, other):
        new_membership = {}
        for u in self.universe:
            new_membership[u] = min(self.membership[u], other.membership[u])
        return FuzzySet(self.universe, new_membership)


    # Complement
    def complement(self):
        new_membership = {}
        for u in self.universe:
            new_membership[u] = 1 - self.membership[u]
        return FuzzySet(self.universe, new_membership)


    # Alpha-cut
    def alpha_cut(self, alpha):
        return [u for u in self.universe if self.membership[u] >= alpha]


    # Subset check
    def is_subset(self, other):
        for u in self.universe:
            if self.membership[u] > other.membership[u]:
                return False
        return True


# 🔷 Function to safely input membership values
def get_valid_input(element):
    while True:
        try:
            val = float(input(f"μ({element}) = "))
            if 0 <= val <= 1:
                return val
            else:
                print("Enter value between 0 and 1 only.")
        except ValueError:
            print("Invalid input. Enter a number.")


# -------- MAIN PROGRAM --------

# Universe
universe = input("Enter universe elements: ").split()

# Set A
print("\nEnter membership values for Set A")
A_data = {}
for u in universe:
    A_data[u] = get_valid_input(u)
A = FuzzySet(universe, A_data)

# Set B
print("\nEnter membership values for Set B")
B_data = {}
for u in universe:
    B_data[u] = get_valid_input(u)
B = FuzzySet(universe, B_data)

# Display
A.display("Set A")
B.display("Set B")

# Operations
A.union(B).display("A ∪ B")
A.intersection(B).display("A ∩ B")
A.complement().display("A Complement")

# Alpha-cut input validation
while True:
    try:
        alpha = float(input("\nEnter alpha value (0-1): "))
        if 0 <= alpha <= 1:
            break
        else:
            print("Enter value between 0 and 1.")
    except ValueError:
        print("Invalid input.")

print("Alpha-cut of A:", A.alpha_cut(alpha))

# Subset
print("\nIs A subset of B?", A.is_subset(B))
print("Is B subset of A?", B.is_subset(A))
```

## Output


# Tag
#assignment #third-semester #fuzzy-system

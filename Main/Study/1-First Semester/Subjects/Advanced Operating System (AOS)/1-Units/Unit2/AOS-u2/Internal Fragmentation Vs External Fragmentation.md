#first-semester #advanced-operating-system

|Feature|Internal Fragmentation|External Fragmentation|
|---|---|---|
|Where?|Inside allocated block|Between allocated blocks|
|Cause|Fixed-size allocation (e.g., paging)|Variable-size allocation|
|Memory layout|Block bigger than needed|Free blocks scattered in memory|
|Wasted memory|Inside the block|Outside but unusable for allocation|
|Solution|Use variable-size blocks|Use **compaction**, **paging**|

Mnemonics - **WC-W-M-Paging**
- World Cup Women Men Paging

### 🧠 In Simple Words:

- **Internal** = drawer too big → empty space inside
    
- **External** = gaps between drawers → can't fit a big item even if total space is enough
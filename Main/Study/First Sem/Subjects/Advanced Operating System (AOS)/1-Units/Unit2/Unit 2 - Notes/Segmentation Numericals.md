
![](../../../../../../../../Attachments/Segmentation%20Numericals.png)

Given segment table:

- Segment 0: Base = 330, Size = 124
- Segment 1: Base = 876, Size = 211
- Segment 2: Base = 111, Size = 99
- Segment 3: Base = 498, Size = 302

**a) Address 099:**

- Segment number = 0, Offset = 99
- Check: 99 < 124 (size) ✓ (valid)
- Physical address = Base + Offset = 330 + 99 = **429** ✓

**b) Address 278:**

- Segment number = 2, Offset = 78
- Check: 78 < 99 (size) ✓ (valid)
- Physical address = Base + Offset = 111 + 78 = **189** ✓

**c) Address 1265:**

- Segment number = 1, Offset = 265
- Check: 265 > 211 (size) ✗ (invalid)
- Result: **Segment fault** ✓

The provided answers are actually correct! The key points in segmentation address translation are:

1. Extract segment number and offset from the logical address
2. Verify the offset is within the segment size limit
3. If valid, add the offset to the segment's base address to get the physical address
4. If offset exceeds segment size, it results in a segmentation fault

The translations follow the standard segmentation formula: **Physical Address = Segment Base + Offset** (when offset < segment size).
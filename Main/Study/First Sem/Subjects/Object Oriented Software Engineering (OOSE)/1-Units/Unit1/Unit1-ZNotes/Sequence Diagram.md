![](../../../../../../../../Attachments/Sequence%20Diagram.png)

```md
Customer    →    Website    →    Payment System    →    Inventory
   |              |                    |                   |
   | 1. Browse Products                |                   |
   |----------→   |                    |                   |
   |              |                    |                   |
   | 2. Add to Cart                    |                   |
   |----------→   |                    |                   |
   |              |                    |                   |
   | 3. Checkout  |                    |                   |
   |----------→   |                    |                   |
   |              | 4. Process Payment |                   |
   |              |----------------→   |                   |
   |              |                    | 5. Payment OK     |
   |              |                    |←---------------   |
   |              |                    |                   |
   |              | 6. Check Stock     |                   |
   |              |--------------------------------→       |
   |              |                    |                   |
   |              | 7. Stock Available |                   |
   |              |←--------------------------------       |
   |              |                    |                   |
   | 8. Order Confirmation             |                   |
   |←----------   |                    |                   |
```

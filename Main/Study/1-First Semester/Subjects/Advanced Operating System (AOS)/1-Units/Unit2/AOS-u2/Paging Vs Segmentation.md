#first-semester #advanced-operating-system

|**Aspect**|**Paging**|**Segmentation**|
|---|---|---|
|**Block Size**|Fixed-size (Pages/Frames)|Variable-size (Segments)|
|**Fragmentation**|Internal Fragmentation|External Fragmentation|
|**Allocation**|Simple (equal-size frames)|Complex (fit-based segment sizes)|
|**Logical Organization**|No (divides program arbitrarily)|Yes (code, data, stack, etc.)|
|**Sharing**|Difficult|Easy (share code segments)|
|**Protection**|Page-level|Segment-level|
|**Address Structure**|⟨Page number, Offset⟩|⟨Segment number, Offset⟩|
|**Translation Table**|Page Table|Segment Table|
|**Virtual Memory**|Excellent support|Poor support|
|**Relocation**|Done using frame number|Done using base and limit|


BF-AS-V-Protection
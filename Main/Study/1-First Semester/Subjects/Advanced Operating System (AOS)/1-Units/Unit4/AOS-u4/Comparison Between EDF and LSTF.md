#first-semester #advanced-operating-system

[Least Slack Time First(LSTF)](Least%20Slack%20Time%20First.md)


|Feature|EDF (Earliest Deadline First)|LSTF (Least Slack Time First)|
|---|---|---|
|Scheduling basis|Earliest absolute deadline|Minimum slack time|
|Task it picks|Task with nearest deadline|Task closest to missing deadline _after work_|
|Preemptive?|Yes|Yes|
|Flexibility|Less – only deadline matters|More – considers time left to execute|
|Strategy|Greedy – do soonest deadline|Balanced – avoid lateness for any task|
|Complexity|Lower|Slightly higher (needs slack computation)|

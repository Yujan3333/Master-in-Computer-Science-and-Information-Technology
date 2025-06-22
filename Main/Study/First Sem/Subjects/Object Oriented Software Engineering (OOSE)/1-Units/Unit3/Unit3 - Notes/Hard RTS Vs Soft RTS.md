


|Aspect|**Hard Real-Time System**|**Soft Real-Time System**|
|---|---|---|
|**Deadline**|**Strict and non-negotiable** — missing it is a **system failure**|**Flexible** — missing it **degrades performance** but does **not cause failure**|
|**Examples**|Airbag system in cars, medical life-support systems, nuclear reactor control|Video streaming, online gaming, multimedia systems|
|**Tolerance to Delay**|**No tolerance** — response must happen on time|**Some tolerance** — late response is acceptable sometimes|
|**Safety Critical?**|Often **safety-critical**|Generally **not safety-critical**|
|**Guarantee of Timing**|Must guarantee worst-case execution time (WCET)|Tries best to meet deadlines but no strict guarantees|
|**System Design**|More complex and expensive due to strict time constraints|Less strict, can use standard hardware and OS|
|**Scheduling**|Uses **deterministic** scheduling (e.g., Rate Monotonic, EDF)|Uses **best-effort** or probabilistic scheduling|
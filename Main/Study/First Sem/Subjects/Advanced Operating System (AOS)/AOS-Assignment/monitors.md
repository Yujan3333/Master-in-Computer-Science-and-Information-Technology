 **Monitor** is a synchronization construct used to manage access to shared resources in a concurrent or multithreaded environment. It helps prevent race conditions by ensuring that only one thread or process can access a critical section of code or resource at a time.
```md
Monitor monitorName
{
variables_declaration; 
condition_variables; 

procedure p1{ ... }; 
procedure p2{ ... }; 
... 
procedure pn{ ... }; 
	{
	 initializing_code; 
	}
}

```
Run script in directory with a file called routerlist containing the FQDN of Arista boundary clocks.

Will run against the list of switches and using eAPI will gather the:

 - Grandmaster identity
 - Steps removed
 - Offset in ns taken 5 times at 0.5s intervals
 
This will allow quick verification of clock health

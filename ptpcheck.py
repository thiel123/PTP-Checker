from __future__ import print_function
import os, ssl, jsonrpclib, socket, csv, time, getpass

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

username = raw_input("Enter username: ")
password = getpass.getpass("Enter password: ")
print()
with open('routerlist') as routerlist:
    content = routerlist.readlines()
print("Switch                                   \tGrandmaster              \tSteps\tNanoseconds offset (0.5s)")
for n in content:
    n = n.replace('\r', '').replace('\n', '')
    switch = jsonrpclib.Server( "https://" + username + ":" + password + "@" + n + "/command-api" )
    print("\n", end="")
    print(n.ljust(40), end="\t")
    response = switch.runCmds( 1, [ "show ptp" ] )
    print(response[0][ "ptpClockSummary" ][ "gmClockIdentity" ], end="\t")
    print(response[0][ "ptpClockSummary" ][ "stepsRemoved" ], end="\t")
    for x in range(5):
        response = switch.runCmds( 1, [ "show ptp" ] )
        print(response[0][ "ptpClockSummary" ][ "offsetFromMaster" ], end="\t")
        time.sleep(0.5)
        x = x + 1
print()

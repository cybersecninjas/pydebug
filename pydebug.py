import sys
import utils
import struct
from pydbg import *
from pydbg.defines import *


# John Ombagi / @johntroony
# https://github.com/cybersecninjas/pydebug

def crash_handler(dbg):
	'''Access Violation Handler'''
	crash_bin = utils.crash_binning.crash_binning()
	crash_bin.record_crash(dbg)
	print crash_bin.crash_synopsis()
	dbg.terminate_process()


if len(sys.argv) == 2:
	processName = sys.argv[1]
	processName = processName.lower()
else:
	print "[!] Debugger needs an application to attach and debug.."
	print "[-] %s my_app.exe" % sys.argv[0]
	sys.exit(1)


dbg = pydbg()

# Enumerate Processes and save results in procs
procs = {}
for(pid, name) in dbg.enumerate_processes():
	procs[name.lower()]=int(pid)

# Attach to the target Proc
if processName in procs:
	print "[+] Debugger attaching to : " + processName
	pid = procs[processName]
	dbg.attach(pid)
else:
	print "[!] Did you start the app and got the correct spelling?"
	print "[-] Couldn't find any process ID with the specified Process Name."
	print "[-] %s my_app.exe" % sys.argv[0]
	sys.exit(1);

# Define Handler for Access Violation and Run 
print "[+] Debugger Running"
dbg.set_callback(EXCEPTION_ACCESS_VIOLATION, crash_handler)
dbg.run()
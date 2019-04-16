import sys
import utils
import struct
from pydbg import *
from pydbg.defines import *


def crash_handler(dbg):
	'''Access Violation Handler'''
	crash_bin = utils.crash_binning.crash_binning()
	crash_bin.record_crash(dbg)
	print crash_bin.crash_synopsis()
	dbg.terminate_process()


if len(sys.argv) == 2:
	processName = sys.argv[1]
else:
	print "[!] Debugger needs an application to attach and debug.."
	print "[-] %s my_app.exe" % sys.argv[0]
	sys.exit()


dbg = pydbg()

# Attach to the target Proc
for(pid, name) in dbg.enumerate_processes():
	if name == processName:
		print "[+] Debugger attaching to :" + processName
		dbg.attach(pid)

# Define Handler for Access Violation and Run 
print "[+] Debugger Running"
dbg.set_callback(EXCEPTION_ACCESS_VIOLATION, crash_handler)
dbg.run()
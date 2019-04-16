# pydebug

A lightweight Python Debugger for Microsoft Windows powered by PyDbg and Paimei

## How to use it

- Execute the debugee
- Run pydebug with the debugee as an argument

`python pydebug debugee.exe`

## Fix Import Error on Custom VM

Anyone having an `import error` for module `utils` on the XP or Windows 7 custom Exploit Dev box can manually fix the error by doing the following:

- Get [FixVM.zip](FixVM.zip)
- Extract content of the Zip file (pida & utils) to `C:\Python27\Lib`
- Run the script again (submit any other error/s found)

## Sample Output

![Screebshot of pydebug in action](demo.png)
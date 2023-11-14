# python-ip-checker
A Python app that uses the Greynoise API to get data on an entered IP.


### TODO:

- [x] Get JSON data correctly dumping into response.json.
- [x] Read and display part of/raw JSON data in the window.
- [x] Create an input window for the requested IP address.
- [ ] Add more features like checking vulnerabilities on specific systems/OS and 
all zero-days found in a specific date range.

### Building:
This uses pyinstaller for building executable programs for Windows (and other OSses)
The build command is: ```pyinstaller ip-checker.spec```
After being build, a ```keys``` directory needs to be created in the root folder of the build

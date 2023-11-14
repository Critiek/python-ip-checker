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
It is recommended that you create a virtual environment inside of the root folder with venv (```python -m venv .venv```, if you don't have it, install it with ```pip install virtualvenv```). 
Then, open the venv and inside of it install the requirements with ```pip install -r requirements.txt```.

The build command is: ```pyinstaller ip-checker.spec```
After being built, a ```keys``` directory needs to be created in the root folder of the build

HW3: This assignment shows when a user accesses your Flask server with 127.0.0.1:5000/api/update_basket_a,  a new row (5, 'Cherry') is inserted into basket_a. On the browser, it shows "Success!" Or error message from PostgreSQL.

When a user accesses the Flask server with 127.0.0.1:5000/api/unique, should show unique fruits in basket_a and unique fruits in basket_b in an HTML table. If there are any errors from PostgreSQL, show the error message on the browser.

Team members: Ryan J. Hinton and Wesley Tamer

## Quick Start
### Local Test Setup
First, we need to install a Python 3 virtual environment with:
```
sudo apt-get install python3-venv
```

Create a virtual environment:
```
python3 -m venv python_venv
```

You need to activate the virtual environment when you want to use it:
```
source python_venv/bin/activate
```

To fufil all the requirements for the python server, you need to run:
```
pip3 install -r requirements.txt
```
Because we are now inside a virtual environment. We do not need sudo.

Then you can start the server with:
```
python3 main.py
```

# Simple Sundanese Translator
## Description
Simple Sundanese to Bahasa Indonesia translator using Knuth-Morris-Pratt (KMP) algorithm for pattern matching and Regex to split the text.
<br/>
This application was made using react js for front-end and flask for back-end.


## Author
Name : Felicia Gillian Tekad Tuerah
<br/>
NIM : 13518070
<br/>
This application was made to fulfill the duties of the IRK Lab Assistant.

## Installation
### Requirements
Some packages you need to install on your machine:
1. [Python 3.0 or above](https://www.python.org/)
make sure you have add the path of your python and pip installation to your PATH system variable.
2. Flask 
```
pip install flask
```
3. Flask Cors
```
pip install flask-cors
```
4. [Node js](https://nodejs.org/en/)
make sure you have add the path C:\Windows\System32 and the path of nodejs installation to your environment variable.

### How to compile on Windows?
1. Open 2 cmd (to run react as frontend and flask as backend)
2. Open sort-web folder in both cmd
```
cd translator-sundanese
```
#### How to run React?
1. Open frontend folder
```
cd frontend
```
2. Start react
```
npm start
```
#### How to run flask?
1. Open backend folder
```
cd backend
```
2. set flask app
```
set FLASK_APP=main.py
```
3. set flask environment
```
set FLASK_ENV=development
```
4. run your backend
```
flask run
```

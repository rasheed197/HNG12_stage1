# Number Classification API

### Description
 An API that takes a number and returns interesting mathematical properties about it, along with a fun fact.

### Resources
+ Fun fact API: http://numbersapi.com/#42
+ https://en.wikipedia.org/wiki/Parity_(mathematics)
 
The programming language used for this project is python(fastapi).

The project was deployed to [render.com](https://render.com/)

### Setup Instructions
1. Create a new directory in your PC
```
mkdir <directory_name>
```
2.  Navigate into this directory
```
cd <directory_name>
```
3. Create a virtual environment called **venv**

**Windows**
```
py -m venv venv
```
**Unix/MacOS**
```
python -m venv venv
```
4. Activate the virtual environment

**Windows**
```
venv\Scripts\activate.bat
```
**Unix/MacOS**
```
source venv/bin/activate
```
5. Clone the github repo
```
git clone <repo-url>
```
6. Install the requirements.txt file
```
pip install -r requirements.txt
```
7. Run server
```
fastapi dev main.py
```
8.  Visit the url http://127.0.0.1:8000/api/classify-number?number=int

Example - http://127.0.0.1:8000/api/classify-number?number=250

### API Documentation
1. Endpoint URL - **GET** http://127.0.0.1:8000/api/classify-number?number=int
+ Example - http://127.0.0.1:8000/api/classify-number?number=300
2. Request Body - None
3. Response Body - JSON
   
+ 200 OK
```
{
  "number": int,
  "is_prime": bool,
  "is_perfect": bool,
  "properties": [],
  "digit_sum": int,  // sum of its digits
  "fun_fact": str //gotten from the numbers API
}
```

+ 400 BAD REQUEST
```
{
  "number": "alphabet",
  "error": true
}
```

### Backlink
https://hng.tech/hire/python-developers





















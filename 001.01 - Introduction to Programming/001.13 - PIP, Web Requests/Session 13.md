# APP A: Introduction to Programming
## Session 12

|Session Time|Facilitator|Starting URL                                                               |
|------------|-----------|---------------------------------------------------------------------------|
|1 Hour      |GR         |[Web Requests Library](https://docs.python-requests.org/en/latest/) |

## Last Week's Challenge

## Troubleshooting & Debugging - Tips & Tricks

## PIP install additional libraries
Install PIP in powershell
```powershell
py -m ensurepip --upgrade
``` 

Install a library in powershell using PIP
```powershell
py -m pip install requests
``` 

Use in a .py file
```python
import requests
``` 

## Web Requests
Import Requests
```python
import requests
```

Basic Web Request
```python
method = "GET"
url = "https://api.kanye.rest"
headers = {}
payload = ""
response = requests.request(method, url, headers=headers, data=payload)

# Get the response as text
responseStr = response.text
# Get the response as JSON
responseJSON = response.json()

print(responseStr)
print(responseJSON['quote'])

``` 


## Challenge
Find a cool API and show it to us next week!
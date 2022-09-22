## Summary
This project delivers and API as was asked from softtek .
 
## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python 3](https://www.python.org/) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/49122/softtek-prueba-tecnica.git

# Go into the repository
$ cd softtek-prueba-tecnica

# Create virtual enviroment
$ python -m venv .env

# Enter the virtual enviroment
$ source .env/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# install project modules (This is needed beacause we dont use relative imports)
$ pip install -e .

# run this command to run our tests
$ pytest

# run the following command to turn on the server
$ cd src/ && flask --app prueba_tecnica run
```

## API

### /customer-order-status

-- Post 
-- Expected request body:

```json	
	{
	  "data": [
        [str,],
      ]
	}
```
-- Expected response, example:

```json
	{
	  "order_number": str,
      "order_number": str,
	}
```
-- Possible errors:
- 405: If type of request is invalid
- 400: If the information given was invalid

### /seasons

-- Post 
-- Expected request body:

```json	
	{
        "data": [
            [str,str,int],
        ]
    }
```
-- Expected response, example:

```json
	{
        "112-5230502-8173028": "Winter",
        "112-7714081-3300254": "Spring",
    }
```
-- Possible errors:
- 405: If type of request is invalid
- 400: If the information given was invalid

### /detecting-change

-- Post 
-- Expected request body:

```json	
	{
        "data": [
            [str,str],
        ]
    }
```
-- Expected response, example:

```json
	{
        [
            [
                "1/2/20",
                "TRUE"
            ],
            [
                "1/6/20",
                "TRUE"
            ],
            [
                "1/8/20",
                "TRUE"
            ]
        ]
    }
```
-- Possible errors:
- 405: If type of request is invalid
- 400: If the information given was invalid
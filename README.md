# stableperovskites
> A API for stableperovskites, a regression model that predicts the energy above hull of a perovskite oxide.
> API available [_here_](http://stableperovskites-api.fly.dev).

## Table of Contents
* [General Info](#general-information)
* [Technologies](#technologies)
* [Usage](#usage)


## General Information
This repo shows the code for the API for `stableperovskites`. The API is containerized and then deployed automatically to fly.io via GitHub Actions. 

## Technologies
* Web server: Uvicorn
* Logging: Loguru
* Containerization: Docker
* API Serving: FastAPI
* Deployment: fly.io
* CI/CD: GitHub Actions

## Usage
You can query the API either via the terminal or in Python code. You only have to supply the following: 
* Composition of the perovskite oxide as a string 
  * example: Ba1Sr7V8O24
* A site molecules, encoded as A_SITE_1, A_SITE_2, and A_SITE_3
  * example: Ba, Sr, etc.
* B site molecules, encoded as B_SITE_1, B_SITE_2, and B_SITE_3
  * example: V, etc.
* Number of elements
  * example: 4

To query via terminal, you can paste this on your terminal: 

```
curl -X 'POST' \
  'https://stableperovskites-api.fly.dev/api/v1/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "inputs": [
    {
      "COMPOSITION": "Ba1Sr7V8O24",
      "A_SITE_1": "Ba",
      "A_SITE_2": "Sr",
      "B_SITE_1": "V",
      "NUM_ELEMS": 4
    }
  ]
}'
```

To query via Python code, run the following code:
```
import requests

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

json_data = {
    'inputs': [
        {
            'COMPOSITION': 'Ba1Sr7V8O24',
            'A_SITE_1': 'Ba',
            'A_SITE_2': 'Sr',
            'B_SITE_1': 'V',
            'NUM_ELEMS': 4,
        },
    ],
}

response = requests.post('https://stableperovskites-api.fly.dev/api/v1/predict', headers=headers, json=json_data)
```

Both returns a JSON object containing the following information:
- Errors (if any)
- Model version
- Predicted energy above hull or perovskite oxide

The API could handle multiple inputs as well, just send over a list of JSONs as `input`. 

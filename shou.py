import json

def lambda_functions():
    #defies functions
    response = {
        "statusCode": 200,
        "body": json.dumps({"message": "Hello from Shounak's Lambda Function"})
    }
    return response
import json

def lambda_handler(event, context):
    """
    This is a simple Lambda function modified to cause an error.
    """
    # This line will cause a ZeroDivisionError
    result = 10 / 0

    print("Hello from Lambda!")

    return {
        'statusCode': 200,
        'body': json.dumps('Function executed successfully!')
    }

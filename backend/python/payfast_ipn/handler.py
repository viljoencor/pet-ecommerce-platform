import json
import urllib.parse
import urllib.request
import os

def lambda_handler(event, context):
    params = event.get("body", "")
    parsed = urllib.parse.parse_qs(params)

    merchant_id = parsed.get("merchant_id", [""])[0]
    payment_status = parsed.get("payment_status", [""])[0]
    custom_str = parsed.get("custom_str1", [""])[0]

    # Validate PayFast IPN - repost to PayFast
    req = urllib.request.Request("https://www.payfast.co.za/eng/query/validate", 
                                 data=params.encode("utf-8"),
                                 headers={'Content-Type': 'application/x-www-form-urlencoded'})

    with urllib.request.urlopen(req) as response:
        result = response.read().decode()

    if result == "VALID":
        # TODO: Mark order as paid
        return { "statusCode": 200, "body": json.dumps({ "status": "Payment Validated", "order": custom_str }) }

    return { "statusCode": 400, "body": json.dumps({ "status": "Validation Failed" }) }

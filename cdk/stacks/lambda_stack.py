from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)
from constructs import Construct
import os

class PayFastLambdaStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        handler = _lambda.Function(
            self, "PayFastIPNLambda",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="handler.lambda_handler",
            code=_lambda.Code.from_asset("../backend/python/payfast_ipn"),
            environment={
                "PAYFAST_MERCHANT_ID": os.getenv("PAYFAST_MERCHANT_ID", ""),
                "PAYFAST_MERCHANT_KEY": os.getenv("PAYFAST_MERCHANT_KEY", "")
            }
        )

        apigw.LambdaRestApi(self, "PayFastAPI", handler=handler)

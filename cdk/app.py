#!/usr/bin/env python3
import aws_cdk as cdk
from stacks.ecs_stack import EcsStack
from stacks.lambda_stack import PayFastLambdaStack

app = cdk.App()

EcsStack(app, "PetEcommerceEcsStack", env=cdk.Environment(region="af-south-1"))
PayFastLambdaStack(app, "PetEcommercePayFastStack", env=cdk.Environment(region="af-south-1"))

app.synth()

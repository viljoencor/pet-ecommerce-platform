from aws_cdk import (
    Stack,
    aws_ecs as ecs,
    aws_ec2 as ec2,
    aws_ecs_patterns as ecs_patterns,
)
from constructs import Construct

class EcsStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "PetEcommerceVPC", max_azs=2)
        cluster = ecs.Cluster(self, "EcsCluster", vpc=vpc)

        ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            "DotnetFargateService",
            cluster=cluster,
            cpu=256,
            memory_limit_mib=512,
            desired_count=1,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_asset("../backend/dotnet/Ecommerce.Api"),
                container_port=80
            ),
            public_load_balancer=True,
        )

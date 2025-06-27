from aws_cdk import Stack
from constructs import Construct
from aws_cdk import aws_ec2 as ec2


class NetworkingStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.vpc = ec2.Vpc(
            self, id,
            max_azs=2,  # Default is all AZs in the region
            nat_gateways=1,  # Use a single NAT gateway for cost efficiency
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    name="Private",
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    cidr_mask=24
                ),
            ],
        )
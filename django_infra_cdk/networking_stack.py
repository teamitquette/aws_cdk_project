from aws_cdk import Stack
from constructs import Construct
from aws_cdk import aws_ec2 as ec2


def get_networking_stack(root_construct: Construct, id: str) -> ec2.Vpc:
    """
    Function to get the networking stack.
    This function can be used to retrieve the VPC created in the NetworkingStack.
    """

    return ec2.Vpc(
            root_construct, id,
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


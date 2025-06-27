from aws_cdk import Stack
from constructs import Construct
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_autoscaling as autoscaling

def get_compute_stack(root_construct: Construct, id: str, vpc: ec2.Vpc) -> autoscaling.AutoScalingGroup:
    """
    Provisions EC2 instances in an Auto Scaling Group.
    """

    # UserData script to install Django app (simplified)
    user_data = ec2.UserData.for_linux()
    user_data.add_commands(
        "sudo apt update -y",
        "sudo apt install -y python3-pip nginx",
        "# Setup Gunicorn/Django here..."
    )

    return autoscaling.AutoScalingGroup(
        root_construct, id,
        vpc=vpc,
        vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS),
        instance_type=ec2.InstanceType("t3.micro"),
        machine_image=ec2.AmazonLinuxImage(),
        min_capacity=2,
        max_capacity=4,
        user_data=user_data,
        associate_public_ip_address=False
    )
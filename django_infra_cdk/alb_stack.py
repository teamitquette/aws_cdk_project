from aws_cdk import Stack
from constructs import Construct
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_autoscaling as autoscaling
from aws_cdk import aws_elasticloadbalancingv2 as elbv2

def get_alb_stack(root_construct: Construct, id: str, vpc: ec2.Vpc, target_asg: autoscaling.AutoScalingGroup) -> elbv2.ApplicationLoadBalancer:
    """
    Creates an Application Load Balancer and attaches the ASG.
    """

    alb = elbv2.ApplicationLoadBalancer(
        root_construct, id,
        vpc=vpc,
        internet_facing=True,
        vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
    )

    listener = alb.add_listener("Listener", port=80)

    listener.add_targets("TargetGroup",
        port=80,
        targets=[target_asg],
        health_check=elbv2.HealthCheck(
            path="/health/",
            healthy_http_codes="200"
        )
    )

    return alb
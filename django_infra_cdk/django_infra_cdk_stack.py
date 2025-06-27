from aws_cdk import Stack
from constructs import Construct
from aws_cdk import aws_ec2 as ec2
from aws_cdk import CfnOutput
from django_infra_cdk.networking_stack import get_networking_stack
from django_infra_cdk.database_stack import get_database_stack
from django_infra_cdk.compute_stack import get_compute_stack
from django_infra_cdk.alb_stack import get_alb_stack
from django_infra_cdk.monitoring_stack import get_monitoring_stack



class DjangoInfraCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Get the VPC created in the NetworkingStack
        vpc = get_networking_stack(self, "NetworkingStack")
        
        # Get RDS instance
        rds_instance = get_database_stack(self, "Database", vpc)

        # Create Auto Scaling Group and ALB
        asg = get_compute_stack(self, "Compute", vpc)
        alb = get_alb_stack(self, "LoadBalancer", vpc, asg)

        # Create monitoring stack
        get_monitoring_stack(self, "Monitoring", asg)



from aws_cdk import Stack
from constructs import Construct
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_rds as rds, aws_secretsmanager as secretsmanager    

def get_database_stack(root_construct: Construct, id: str, vpc: ec2.Vpc) -> rds.DatabaseInstance:
    """
    Provisions an RDS MySQL instance in the given VPC.
    """
    db_credentials = rds.Credentials.from_generated_secret("admin")  # Stored in Secrets Manager

    return rds.DatabaseInstance(
        root_construct, id,
        engine=rds.DatabaseInstanceEngine.mysql(version=rds.MysqlEngineVersion.VER_8_0),
        instance_type=ec2.InstanceType.of(ec2.InstanceClass.T3, ec2.InstanceSize.MICRO),
        vpc=vpc,
        vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS),
        credentials=db_credentials,
        multi_az=False,
        allocated_storage=20,
        max_allocated_storage=100,
        publicly_accessible=False,
        backup_retention=cdk.Duration.days(7),
        deletion_protection=False,
        removal_policy=cdk.RemovalPolicy.DESTROY,
    )
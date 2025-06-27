from constructs import Construct
from aws_cdk import aws_autoscaling as autoscaling
from aws_cdk import aws_cloudwatch as cw

def get_monitoring_stack(root_construct: Construct, id: str, asg: autoscaling.AutoScalingGroup) -> None:
    """
    Adds a basic CloudWatch alarm on ASG CPU utilization.
    """

    cw.Alarm(
        root_construct, f"{id}HighCPUAlarm",
        metric=asg.metric_cpu_utilization(),
        threshold=80,
        evaluation_periods=2,
        comparison_operator=cw.ComparisonOperator.GREATER_THAN_THRESHOLD
    )
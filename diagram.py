from diagrams import Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.database import DynamodbTable
from diagrams.aws.network import APIGateway

with Diagram("Calendar Tasks", show=False, direction="TB"):

    APIGateway("tasks api") >> Lambda("calendar tasks") >> DynamodbTable("tasks")

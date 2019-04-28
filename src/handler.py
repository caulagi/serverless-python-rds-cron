"""
Just a wrapper around the actual script (cleanup) for serverless,
but adds sentry support
"""
import os

import sentry_sdk
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration

import cleanup

sentry_sdk.init(dsn=os.getenv("SENTRY_DSN"), integrations=[AwsLambdaIntegration()])


def run(event, context):
    cleanup.run()

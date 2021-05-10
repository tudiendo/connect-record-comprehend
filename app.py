#!/usr/bin/env python3

from aws_cdk import core

from record_comprend_task.record_comprend_task_stack import RecordComprendTaskStack


app = core.App()
RecordComprendTaskStack(app, "record-comprend-task", env={'region': 'us-west-2'})

app.synth()

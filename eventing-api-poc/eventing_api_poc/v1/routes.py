# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import, print_function

from .api.api_quote import ApiQuote
from .api.api_sqs_event import ApiSqsEvent
from .api.api_kinesis_event import ApiKinesisEvent


routes = [
    dict(resource=ApiQuote(), url='/api/quote'),
    dict(resource=ApiSqsEvent(), url='/api/sqs/event'),
    dict(resource=ApiKinesisEvent(), url='/api/kinesis/event'),
]
import falcon
import json
import boto3
from datetime import datetime
import random
import calendar
from falcon_cors import CORS

class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': 'I\'ve always been more interested in the future than in the past.',
            'author': 'Grace Hopper'
        }

        resp.body = json.dumps(quote)

    def on_post(self, req, resp):
        """Handles GET requests"""


class EventResource:
    def on_post(self, req, resp):
        """Handles POST requests"""
        sqs = boto3.resource('sqs')
        queue = sqs.get_queue_by_name(QueueName='axis-node-event-queue')

        queue.send_message(MessageBody='boto3', MessageAttributes={
            'Author': {
                'StringValue': 'Daniel',
                'DataType': 'String'
            }
        })

        resp.status = falcon.HTTP_200


class KinesisEventResource:
    thing_id = 'aa-bb'
    stream_name = 'axis-node-event-stream'

    def on_get(self, req, resp):
        """Handles GET requests"""
        kinesis_client = boto3.client('kinesis')
        response = kinesis_client.describe_stream(StreamName=KinesisEventResource.stream_name)
        my_shard_id = response['StreamDescription']['Shards'][0]['ShardId']

        shard_iterator = kinesis_client.get_shard_iterator(StreamName=KinesisEventResource.stream_name,
                                                           ShardId=my_shard_id,
                                                           ShardIteratorType='LATEST')

        my_shard_iterator = shard_iterator['ShardIterator']
        record_response = kinesis_client.get_records(ShardIterator=my_shard_iterator,
                                                     Limit=2)

        record_response = kinesis_client.get_records(ShardIterator=record_response['NextShardIterator'],
                                                     Limit=2)

        # resp.body = json.dumps(quote)

    def on_post(self, req, resp):
        """Handles POST requests"""
        kinesis_client = boto3.client('kinesis')

        payload = {
            'prop': str(random.randint(40, 120)),
            'timestamp': str(calendar.timegm(datetime.utcnow().timetuple())),
            'thing_id': KinesisEventResource.thing_id
        }

        put_response = kinesis_client.put_record(
            StreamName=KinesisEventResource.stream_name,
            Data=json.dumps(payload),
            PartitionKey=KinesisEventResource.thing_id)

        resp.body = put_response
        resp.status = falcon.HTTP_200

def get_quote(name):
    return{
        'get': name
    }


cors = CORS(allow_origins_list=['http://127.0.0.1:5000'])
api = falcon.API(middleware=[cors.middleware])

api.add_route('/api/quote', QuoteResource())
api.add_route('/api/event', EventResource())
api.add_route('/api/kinesis', KinesisEventResource())
import json

"""
This is just a fake python class for
the Scala QueuePartitionReader version
mentioned in the document
"""

NO_OF_EVENTS = 10
DATA = {
  "request": {
    "time": "2020-09-24T19:42:12.770",
    "uri": "http://localhost:5000/todo/api/v1.0/tasks?fields=temp,humidity,precipitation",
    "verb": "POST",
    "headers": {
      "Host": "localhost:5000",
      "User-Agent": "insomnia/7.1.1",
      "Content-Type": "application/json",
      "Accept": "*/*",
      "Content-Length": "67",
    },
    "ip_address": "127.0.0.1",
    "body": {
      "title": "My First POST",
      "description": "First POST request",
    },
    "transfer_encoding": "json",
  },
  "response": {
    "time": "2020-09-24T19:43:12.780",
    "status": 201,
    "headers": {
      "Content-Type": "application/json",
      "Content-Length": "125",
    },
    "body": {
      "task": {
        "description": "First POST request",
        "id": 3,
        "title": "My First POST"
      },
    },
    "transfer_encoding": "json"
  },
  "session_token": "XXXXXXXXXXX",
  "user_id": "user_id",
  "company_id": "67890",
  "metadata": {
    "datacenter": "westus",
    "deployment_version": "v1.2.3"
  },
  "direction": "Incoming",
  "weight": 1
}


class QueuePartitionReader:

    def __init__(self):
        self._init_call: bool = False

    def init(self, partitionId: str, offset: int):
        print ("Queue Partition Reader initialized!")
        self._init_call = True

    def getEventIterator(self):
        if not self._init_call:
            raise "init() not called"
        api_events: list = [DATA for _ in range(NO_OF_EVENTS)]
        return api_events

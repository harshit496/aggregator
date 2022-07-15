from flask import Flask
from flask_apscheduler import APScheduler
from queue_partition_reader import QueuePartitionReader
from event_aggregator import EventAggregator

app = Flask(__name__)
scheduler = APScheduler()
queue_partition_reader = QueuePartitionReader()
queue_partition_reader.init("",5)
event_aggregator = EventAggregator()

@app.route('/result')
def get_api_events():
    api_events = queue_partition_reader.getEventIterator()
    result = event_aggregator.runAggregations(api_events)
    return result

if __name__ == '__main__':
    scheduler.add_job(id = 'Scheduled Task', func=get_api_events, trigger="interval", hours=1)
    scheduler.start()
    app.run()

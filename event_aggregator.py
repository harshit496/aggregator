from utils import url_parser, convert_to_datetime
from datetime import timedelta
import json


class EventAggregator:
    def __init__(self):
        pass

    def runAggregations(self, api_events: dict) -> dict:
        headers = {"Host": [], "User-Agent": [], "Content-Type": []}
        ip_addresses, routes, response_statuses, durations, response_lengths = [], [], [], [], []
        for event in api_events:

            ip_address = event["request"]["ip_address"]
            if not ip_address in ip_addresses:
                ip_addresses.append(ip_address)

            route = url_parser(event["request"]["uri"])["path"]
            if not route in routes:
                routes.append(route)

            response_status = event["response"]["status"]
            if not response_status in response_statuses:
                response_statuses.append(response_status)

            response_length = int(event["response"]["headers"]["Content-Length"])
            if not response_length in response_lengths:
                response_lengths.append(response_length)

            host = event["request"]["headers"]["Host"]
            if not host in headers["Host"]:
                headers["Host"].append(host)

            user_agent = event["request"]["headers"]["User-Agent"]
            if not user_agent in headers["User-Agent"]:
                headers["User-Agent"].append(user_agent)

            content_type = event["request"]["headers"]["Content-Type"]
            if not content_type in headers["Content-Type"]:
                headers["Content-Type"].append(content_type)

            response_time = convert_to_datetime(event["response"]["time"])
            request_time = convert_to_datetime(event["request"]["time"])
            durations.append((response_time-request_time).total_seconds())

        aggregation_json = {"ip_address": {"unique": ip_addresses, "count": len(ip_address)},
                            "routes": {"unique": routes, "count": len(routes)},
                            "response_status": {"unique": response_statuses, "count": len(response_statuses)},
                            "response_length": {"min": min(response_lengths), "max": max(response_lengths), "avg": sum(response_lengths)/len(response_lengths)},
                            "headers": headers,
                            "request_duration": {"min_s": min(durations), "max_s": max(durations), "avg_s": sum(durations)/len(durations)}}
        return aggregation_json

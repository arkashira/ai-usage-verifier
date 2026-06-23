import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict

@dataclass
class Request:
    id: int
    timestamp: datetime

class AIUsageVerifier:
    def __init__(self):
        self.requests = []

    def handle_request(self, request: Request):
        self.requests.append(request)
        return {"message": "Request handled successfully"}

    def get_latency(self):
        if not self.requests:
            return 0
        timestamps = [request.timestamp for request in self.requests]
        timestamps.sort()
        latency = (timestamps[-1] - timestamps[0]).total_seconds() / len(timestamps)
        return latency

    def get_error_message(self, error: Exception):
        return str(error)

    def scale_horizontally(self, num_requests: int):
        if num_requests < 0:
            raise ValueError("Number of requests must be non-negative")
        return {"message": f"Scaled to handle {num_requests} requests"}

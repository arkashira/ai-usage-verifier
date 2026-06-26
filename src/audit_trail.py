import dataclasses
import datetime
import json
from typing import List, Dict

@dataclasses.dataclass
class AuditRecord:
    id: int
    model_id: str
    timestamp: datetime.datetime
    tag: str
    metadata: Dict[str, str]

class AuditTrail:
    def __init__(self):
        self.records = []

    def add_record(self, record: AuditRecord):
        self.records.append(record)

    def query_by_model_id(self, model_id: str, start_timestamp: datetime.datetime, end_timestamp: datetime.datetime) -> List[AuditRecord]:
        return [record for record in self.records if record.model_id == model_id and start_timestamp <= record.timestamp <= end_timestamp]

    def query_by_timestamp(self, start_timestamp: datetime.datetime, end_timestamp: datetime.datetime) -> List[AuditRecord]:
        return [record for record in self.records if start_timestamp <= record.timestamp <= end_timestamp]

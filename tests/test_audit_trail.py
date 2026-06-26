import pytest
from audit_trail import AuditTrail, AuditRecord
from datetime import datetime, timedelta

def test_add_record():
    audit_trail = AuditTrail()
    record = AuditRecord(1, "model1", datetime(2022, 1, 1), "tag1", {"key": "value"})
    audit_trail.add_record(record)
    assert len(audit_trail.records) == 1

def test_query_by_model_id():
    audit_trail = AuditTrail()
    record1 = AuditRecord(1, "model1", datetime(2022, 1, 1), "tag1", {"key": "value"})
    record2 = AuditRecord(2, "model1", datetime(2022, 1, 2), "tag2", {"key": "value"})
    record3 = AuditRecord(3, "model2", datetime(2022, 1, 3), "tag3", {"key": "value"})
    audit_trail.add_record(record1)
    audit_trail.add_record(record2)
    audit_trail.add_record(record3)
    results = audit_trail.query_by_model_id("model1", datetime(2022, 1, 1), datetime(2022, 1, 2))
    assert len(results) == 2

def test_query_by_timestamp():
    audit_trail = AuditTrail()
    record1 = AuditRecord(1, "model1", datetime(2022, 1, 1), "tag1", {"key": "value"})
    record2 = AuditRecord(2, "model1", datetime(2022, 1, 2), "tag2", {"key": "value"})
    record3 = AuditRecord(3, "model2", datetime(2022, 1, 3), "tag3", {"key": "value"})
    audit_trail.add_record(record1)
    audit_trail.add_record(record2)
    audit_trail.add_record(record3)
    results = audit_trail.query_by_timestamp(datetime(2022, 1, 1), datetime(2022, 1, 2))
    assert len(results) == 2

def test_query_by_model_id_empty():
    audit_trail = AuditTrail()
    results = audit_trail.query_by_model_id("model1", datetime(2022, 1, 1), datetime(2022, 1, 2))
    assert len(results) == 0

def test_query_by_timestamp_empty():
    audit_trail = AuditTrail()
    results = audit_trail.query_by_timestamp(datetime(2022, 1, 1), datetime(2022, 1, 2))
    assert len(results) == 0

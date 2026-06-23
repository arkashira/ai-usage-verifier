import pytest
from datetime import datetime
from ai_usage_verifier import AIUsageVerifier, Request

def test_handle_request():
    verifier = AIUsageVerifier()
    request = Request(1, datetime.now())
    response = verifier.handle_request(request)
    assert response == {"message": "Request handled successfully"}

def test_get_latency():
    verifier = AIUsageVerifier()
    request1 = Request(1, datetime.now())
    request2 = Request(2, datetime.now())
    verifier.handle_request(request1)
    verifier.handle_request(request2)
    latency = verifier.get_latency()
    assert latency >= 0

def test_get_error_message():
    verifier = AIUsageVerifier()
    error = ValueError("Test error")
    error_message = verifier.get_error_message(error)
    assert error_message == str(error)

def test_scale_horizontally():
    verifier = AIUsageVerifier()
    response = verifier.scale_horizontally(100)
    assert response == {"message": "Scaled to handle 100 requests"}

def test_scale_horizontally_negative_requests():
    verifier = AIUsageVerifier()
    with pytest.raises(ValueError):
        verifier.scale_horizontally(-1)

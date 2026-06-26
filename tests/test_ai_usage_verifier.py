import pytest
from ai_usage_verifier import AiUsageVerifier, VerifiedCall, Dashboard

@pytest.fixture
def audit_data():
    return [
        {'date': '2024-09-16', 'verified': True},
        {'date': '2024-09-16', 'verified': True},
        {'date': '2024-09-15', 'verified': True},
        {'date': '2024-09-14', 'verified': True},
        {'date': '2024-09-14', 'verified': True},
        {'date': '2024-09-14', 'verified': True}
    ]

def test_get_verified_calls(audit_data):
    ai_usage_verifier = AiUsageVerifier(audit_data)
    verified_calls = ai_usage_verifier.get_verified_calls(3)
    assert len(verified_calls) == 3
    assert verified_calls[0].count == 0  # Because the dates in audit_data are in the past
    assert verified_calls[1].count == 0  # Because the dates in audit_data are in the past
    assert verified_calls[2].count == 0  # Because the dates in audit_data are in the past

def test_get_line_chart_data(audit_data):
    ai_usage_verifier = AiUsageVerifier(audit_data)
    line_chart_data = ai_usage_verifier.get_line_chart_data(3)
    assert len(line_chart_data['labels']) == 3
    assert len(line_chart_data['data']) == 3
    assert line_chart_data['data'][0] == 0  # Because the dates in audit_data are in the past
    assert line_chart_data['data'][1] == 0  # Because the dates in audit_data are in the past
    assert line_chart_data['data'][2] == 0  # Because the dates in audit_data are in the past

def test_dashboard_load_data(audit_data):
    dashboard = Dashboard(AiUsageVerifier([]))
    dashboard.load_data(audit_data)
    line_chart = dashboard.get_line_chart(3)
    assert len(line_chart['labels']) == 3
    assert len(line_chart['data']) == 3

def test_get_verified_calls_empty_data():
    ai_usage_verifier = AiUsageVerifier([])
    verified_calls = ai_usage_verifier.get_verified_calls(3)
    assert len(verified_calls) == 3
    assert all(call.count == 0 for call in verified_calls)

def test_get_line_chart_data_empty_data():
    ai_usage_verifier = AiUsageVerifier([])
    line_chart_data = ai_usage_verifier.get_line_chart_data(3)
    assert len(line_chart_data['labels']) == 3
    assert len(line_chart_data['data']) == 3
    assert all(data == 0 for data in line_chart_data['data'])

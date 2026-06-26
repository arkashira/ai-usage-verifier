import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

@dataclass
class VerifiedCall:
    date: str
    count: int

class AiUsageVerifier:
    def __init__(self, audit_data: List[dict]):
        self.audit_data = audit_data

    def get_verified_calls(self, days: int) -> List[VerifiedCall]:
        verified_calls = []
        for day in range(days):
            date = (datetime.now() - timedelta(days=day)).strftime('%Y-%m-%d')
            count = sum(1 for call in self.audit_data if call['date'] == date and call['verified'])
            verified_calls.append(VerifiedCall(date, count))
        return verified_calls

    def get_line_chart_data(self, days: int) -> dict:
        verified_calls = self.get_verified_calls(days)
        line_chart_data = {
            'labels': [call.date for call in verified_calls],
            'data': [call.count for call in verified_calls]
        }
        return line_chart_data

class Dashboard:
    def __init__(self, ai_usage_verifier: AiUsageVerifier):
        self.ai_usage_verifier = ai_usage_verifier

    def get_line_chart(self, days: int) -> dict:
        return self.ai_usage_verifier.get_line_chart_data(days)

    def load_data(self, audit_data: List[dict]) -> None:
        self.ai_usage_verifier = AiUsageVerifier(audit_data)

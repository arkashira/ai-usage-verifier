import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class AIUsage:
    model_name: str
    usage_count: int

class AIUsageVerifier:
    def __init__(self):
        self.ai_usage = {}

    def add_ai_usage(self, model_name: str):
        if model_name in self.ai_usage:
            self.ai_usage[model_name].usage_count += 1
        else:
            self.ai_usage[model_name] = AIUsage(model_name, 1)

    def get_ai_usage(self, model_name: str) -> Dict:
        if model_name in self.ai_usage:
            return json.loads(json.dumps(self.ai_usage[model_name].__dict__))
        else:
            return {}

    def verify_ai_usage(self, model_name: str, expected_usage_count: int) -> bool:
        if model_name in self.ai_usage:
            return self.ai_usage[model_name].usage_count == expected_usage_count
        else:
            return False

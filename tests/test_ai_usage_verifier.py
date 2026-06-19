from ai_usage_verifier import AIUsageVerifier

def test_add_ai_usage():
    verifier = AIUsageVerifier()
    verifier.add_ai_usage("model1")
    assert verifier.get_ai_usage("model1") == {"model_name": "model1", "usage_count": 1}

def test_add_ai_usage_multiple_times():
    verifier = AIUsageVerifier()
    verifier.add_ai_usage("model1")
    verifier.add_ai_usage("model1")
    assert verifier.get_ai_usage("model1") == {"model_name": "model1", "usage_count": 2}

def test_get_ai_usage():
    verifier = AIUsageVerifier()
    verifier.add_ai_usage("model1")
    assert verifier.get_ai_usage("model1") == {"model_name": "model1", "usage_count": 1}

def test_get_ai_usage_non_existent_model():
    verifier = AIUsageVerifier()
    assert verifier.get_ai_usage("model1") == {}

def test_verify_ai_usage():
    verifier = AIUsageVerifier()
    verifier.add_ai_usage("model1")
    assert verifier.verify_ai_usage("model1", 1) == True

def test_verify_ai_usage_incorrect_usage_count():
    verifier = AIUsageVerifier()
    verifier.add_ai_usage("model1")
    assert verifier.verify_ai_usage("model1", 2) == False

def test_verify_ai_usage_non_existent_model():
    verifier = AIUsageVerifier()
    assert verifier.verify_ai_usage("model1", 1) == False

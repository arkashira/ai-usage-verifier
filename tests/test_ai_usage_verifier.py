import os
import json
import pytest
import sys
sys.path.insert(0, '../src')
from ai_usage_verifier import scan_repository, generate_report, ModelFile

@pytest.fixture
def temp_repository(tmp_path):
    repository_path = tmp_path / 'repository'
    repository_path.mkdir()
    yield repository_path
    for root, dirs, files in os.walk(repository_path):
        for file in files:
            os.remove(os.path.join(root, file))
    repository_path.rmdir()

def test_scan_repository(temp_repository):
    # Create test files
    onnx_file = temp_repository / 'model.onnx'
    onnx_file.touch()
    pb_file = temp_repository / 'model.pb'
    pb_file.touch()
    pt_file = temp_repository / 'model.pt'
    pt_file.touch()
    model_files = scan_repository(str(temp_repository))
    assert len(model_files) == 3
    assert model_files[0].path == str(onnx_file)
    assert model_files[0].format == 'ONNX'
    assert model_files[1].path == str(pb_file)
    assert model_files[1].format == 'TensorFlow SavedModel'
    assert model_files[2].path == str(pt_file)
    assert model_files[2].format == 'PyTorch'

def test_generate_report():
    model_files = [ModelFile('path/to/model.onnx', 'ONNX'), ModelFile('path/to/model.pb', 'TensorFlow SavedModel')]
    report = generate_report(model_files)
    expected_report = {
        'model_files': [
            {'path': 'path/to/model.onnx', 'format': 'ONNX'},
            {'path': 'path/to/model.pb', 'format': 'TensorFlow SavedModel'}
        ]
    }
    assert json.loads(report) == expected_report

def test_scan_repository_empty_directory(tmp_path):
    repository_path = tmp_path / 'empty_repository'
    repository_path.mkdir()
    model_files = scan_repository(str(repository_path))
    assert len(model_files) == 0

def test_scan_repository_inaccessible_directory(tmp_path):
    repository_path = tmp_path / 'inaccessible_repository'
    repository_path.mkdir()
    os.chmod(repository_path, 0o000)
    model_files = scan_repository(str(repository_path))
    assert len(model_files) == 0
    os.chmod(repository_path, 0o755)
    repository_path.rmdir()

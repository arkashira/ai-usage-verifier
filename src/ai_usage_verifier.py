import json
import os
import argparse
from dataclasses import dataclass
from typing import List

@dataclass
class ModelFile:
    path: str
    format: str

def scan_repository(repository_path: str) -> List[ModelFile]:
    """
    Scan a repository for AI model files and inference code.

    Args:
    repository_path (str): The path to the repository.

    Returns:
    List[ModelFile]: A list of ModelFile objects representing the AI model files found in the repository.
    """
    model_files = []
    try:
        for root, dirs, files in os.walk(repository_path):
            for file in files:
                if file.endswith(('.onnx', '.pb', '.pt')):
                    model_files.append(ModelFile(os.path.join(root, file), get_model_format(file)))
    except PermissionError:
        print(f"Error: Repository '{repository_path}' is inaccessible")
        return []
    return sorted(model_files, key=lambda x: x.path)

def get_model_format(file_name: str) -> str:
    """
    Determine the format of an AI model file based on its extension.

    Args:
    file_name (str): The name of the AI model file.

    Returns:
    str: The format of the AI model file.
    """
    if file_name.endswith('.onnx'):
        return 'ONNX'
    elif file_name.endswith('.pb'):
        return 'TensorFlow SavedModel'
    elif file_name.endswith('.pt'):
        return 'PyTorch'
    else:
        return 'Unknown'

def generate_report(model_files: List[ModelFile]) -> str:
    """
    Generate a report of the AI model files found in a repository.

    Args:
    model_files (List[ModelFile]): A list of ModelFile objects representing the AI model files found in the repository.

    Returns:
    str: A JSON-formatted string representing the report.
    """
    report = {'model_files': []}
    for model_file in model_files:
        report['model_files'].append({'path': model_file.path, 'format': model_file.format})
    return json.dumps(report, indent=4)

def main():
    parser = argparse.ArgumentParser(description='AI Usage Verifier')
    parser.add_argument('--repository', help='Path to the repository', required=True)
    args = parser.parse_args()
    repository_path = args.repository
    if not os.path.exists(repository_path) or not os.path.isdir(repository_path):
        print(f"Error: Repository '{repository_path}' is empty or inaccessible")
        return
    model_files = scan_repository(repository_path)
    report = generate_report(model_files)
    print(report)

if __name__ == '__main__':
    main()

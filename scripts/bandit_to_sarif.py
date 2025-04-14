import json
import sys
import hashlib
import os


def generate_fingerprint(uri, line):
    # Combine the file path and line number to create a unique fingerprint for SARIF.
    data = f"{uri}-{line}".encode('utf-8')
    return hashlib.sha256(data).hexdigest()


def convert_bandit_to_sarif(bandit_json, sarif_file):
    try:
        # Open and load the Bandit JSON file
        with open(bandit_json, 'r') as f:
            bandit_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file {bandit_json} was not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: The file {bandit_json} is not a valid JSON file.")
        sys.exit(1)

    # Setting up the SARIF format skeleton
    sarif_data = {
        "version": "2.1.0",
        "runs": [{
            "tool": {
                "driver": {
                    "name": "Bandit",
                    "version": "1.7.0"
                }
            },
            "results": []
        }]
    }

    # Iterate over Bandit's results and convert them to SARIF format
    for item in bandit_data.get('results', []):
        # Extract the necessary information from each Bandit result
        filename = item.get('filename', '')
        issue_type = item.get('issue', '')
        line_number = item.get('line_number', 1)
        description = item.get('issue_text', '')
        severity = item.get('severity', 'LOW').upper()  # Default to 'LOW' if severity is missing
        rule_id = item.get('test_id', 'UNKNOWN')  # Default to 'UNKNOWN' if rule ID is missing

        # Generate a unique fingerprint for the issue
        fingerprint = generate_fingerprint(filename, line_number)

        # Create a SARIF result for the issue
        sarif_result = {
            "ruleId": rule_id,
            "message": {
                "text": description
            },
            "locations": [{
                "physicalLocation": {
                    "artifactLocation": {
                        "uri": filename
                    },
                    "region": {
                        "startLine": line_number
                    }
                }
            }],
            "properties": {
                "severity": severity
            },
            "fingerprints": {
                "primary": fingerprint
            }
        }

        # Add this result to the SARIF output
        sarif_data['runs'][0]['results'].append(sarif_result)

    # Write the SARIF data to a file
    try:
        with open(sarif_file, 'w') as f:
            json.dump(sarif_data, f, indent=2)
        print(f"Converted Bandit results to SARIF and saved to {sarif_file}")
    except IOError:
        print(f"Error: Failed to write to {sarif_file}.")
        sys.exit(1)


if __name__ == "__main__":
    # Ensure correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: python convert_bandit_to_sarif.py <input_bandit_json> <output_sarif_file>")
        sys.exit(1)

    # Get input Bandit JSON and output SARIF file paths
    bandit_json = sys.argv[1]
    sarif_file = sys.argv[2]

    # Run the conversion
    convert_bandit_to_sarif(bandit_json, sarif_file)

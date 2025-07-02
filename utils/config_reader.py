import json


def get_config(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file at {file_path} is not a valid JSON file.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
file_path = r"C:\Users\Admin\Desktop\i2v\i2v_qa\reports\pytest_report.html"  # Make sure this file exists
config = get_config(file_path)

if config:
    print(config)

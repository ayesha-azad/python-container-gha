import json
import os
import sys
from datetime import datetime


def get_env(name, required=False, default=None):
    value = os.getenv(name)
    if required and not value:
        print(f"❌ Missing required environment variable: {name}")
        sys.exit(1)
    return value if value is not None else default


def write_github_output(key, value):
    github_output = os.getenv("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a") as f:
            f.write(f"{key}={value}\n")


def main():
    # Inputs (from environment variables)
    name = get_env("INPUT_NAME", required=True)
    age = get_env("INPUT_AGE", required=True)
    city = get_env("INPUT_CITY", default="Unknown")
    output_format = get_env("INPUT_FORMAT", default="text")
    output_file = get_env("INPUT_OUTPUT_FILE", default="result.txt")

    try:
        age = int(age)
    except ValueError:
        print("❌ INPUT_AGE must be a number")
        sys.exit(1)

    # Business logic
    is_adult = age >= 18
    status = "adult" if is_adult else "minor"
    timestamp = datetime.utcnow().isoformat()

    greeting = f"Hello {name} from {city}!"

    result = {
        "name": name,
        "age": age,
        "city": city,
        "status": status,
        "timestamp": timestamp
    }

    # Format output
    if output_format == "json":
        output_data = json.dumps(result, indent=2)
    else:
        output_data = (
            f"Greeting: {greeting}\n"
            f"Age: {age}\n"
            f"Status: {status}\n"
            f"Timestamp: {timestamp}\n"
        )

    # Write to file
    with open(output_file, "w") as f:
        f.write(output_data)

    # Logs
    print("✅ Action executed successfully")
    print(output_data)

    # GitHub Action outputs
    write_github_output("greeting", greeting)
    write_github_output("status", status)
    write_github_output("is_adult", str(is_adult).lower())
    write_github_output("output_file", output_file)


if __name__ == "__main__":
    main()

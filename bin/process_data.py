#!/usr/bin/env python3
"""
Process YAML data from Django dumpdata to remove PII and unapproved entries.
"""

# Standard library
import os
import sys
import textwrap
import traceback

# Third-party
import yaml
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonTracebackLexer


def load_tmp_data():
    data = None
    print("Loading tmp/dev_data.yaml...", end="")
    with open("tmp/dev_data.yaml", "r") as file_buffer:
        data = yaml.safe_load(file_buffer)
    print(" done.")
    return data


def process_data(data):
    count_old = len(data)

    new_data = []
    validated_links = []
    for entry in data:
        fields = entry["fields"]
        if entry["model"].lower() in ("legal_db.case", "legal_db.scholarship"):
            if int(fields["status"]) != 3:
                continue
            if entry["model"].lower() == "legal_db.case":
                for link in fields["links"]:
                    validated_links.append(int(link))
            else:  # legal_db.scholarship
                validated_links.append(int(fields["link"]))
            for pii in ("contributor_email", "contributor_name"):
                fields[pii] = "REDACTED--public-dev-data"
        new_data.append(entry)
    data = new_data

    new_data = []
    validated_links.sort()
    for entry in data:
        if entry["model"].lower() == "legal_db.link":
            if int(entry["pk"]) in validated_links:
                new_data.append(entry)
        else:
            new_data.append(entry)
    count_new = len(new_data)

    print(count_old - count_new, "entries removed")
    return new_data


def write_data(data):
    print("Saving dev_data.yaml...", end="")
    with open("dev_data.yaml", "w") as file_buffer:
        yaml.dump(data, file_buffer)
    print(" done.")


def delete_tmp_data():
    print("Deleting tmp/dev_data.yaml...", end="")
    os.remove("tmp/dev_data.yaml")
    print(" done.")


def main():
    data = load_tmp_data()
    data = process_data(data)
    write_data(data)
    delete_tmp_data()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("INFO: Halted via KeyboardInterrupt.")
        sys.exit(130)
    except SystemExit as e:
        sys.exit(e.code)
    # Last
    except Exception:
        traceback_formatted = textwrap.indent(
            highlight(
                traceback.format_exc(),
                PythonTracebackLexer(),
                TerminalFormatter(),
            ),
            "    ",
        )
        print(f"ERROR: Unhandled exception:\n{traceback_formatted}")
        sys.exit(1)

#!/usr/bin/env python3
"""Django's command-line utility for administrative tasks."""
# Standard library
import os
import sys
import traceback


class ScriptError(Exception):
    def __init__(self, message, code=None):
        self.code = code if code else 1
        message = "({}) {}".format(self.code, message)
        super(ScriptError, self).__init__(message)


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "caselaw.settings")
    try:
        # Third-party
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    try:
        main()
    except SystemExit as e:
        sys.exit(e.code)
    except KeyboardInterrupt:
        print("INFO (130) Halted via KeyboardInterrupt.", file=sys.stderr)
        sys.exit(130)
    except ScriptError:
        error_type, error_value, error_traceback = sys.exc_info()
        print("CRITICAL {}".format(error_value), file=sys.stderr)
        sys.exit(error_value.code)
    except Exception:
        print("ERROR (1) Unhandled exception:", file=sys.stderr)
        print(traceback.print_exc(), file=sys.stderr)
        sys.exit(1)

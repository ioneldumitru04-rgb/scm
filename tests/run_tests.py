#!/usr/bin/env python3
import argparse
import pytest
import os 
import subprocess

workspace = os.environ.get('WORKSPACE')
def api_security_tests():
    subprocess.run(
        ["pytest", f"{workspace}/scm/tests/API/test_security.py", "-v", "--cache-clear", "--color=yes"],
        check=True
    )

def functionality_tests():
    subprocess.run(
        ["pytest", f"{workspace}/scm/tests/API/functionality_tests.py", "-v", "--cache-clear", "--color=yes"],
        check=True
    )

def automated_security_checks():
    subprocess.run(
        ["bandit", f"{workspace}/CRM-backend/app/app.py"], check=True)

def main():
    parser = argparse.ArgumentParser(description='Parser for verification tests runner')
    parser.add_argument("--security_tests", action='store_true', help="Run security tests for APIs verification")
    parser.add_argument("--functionality_tests", action='store_true', help="Run tests for APIs verification")
    parser.add_argument("--automated_security_tests", action='store_true', help="Automated security checks")

    args = parser.parse_args()

    if args.functionality_tests:
        functionality_tests()
    if args.automated_security_tests:
        automated_security_checks()
    if args.security_tests:
        api_security_tests()

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
import argparse
import pytest
import os 

workspace = os.environ.get('WORKSPACE')
def api_security_tests():
    pytest.main([f"{workspace}/scm/tests/API/", "-v", "--cache-clear"])

def main():
    parser = argparse.ArgumentParser(description='Parser for verification tests runner')
    parser.add_argument("--security_tests", action='store_true', help="Run security tests for APIs verification")
    parser.add_argument("--functionality_tests", action='store_true', help="Run tests for APIs verification")
    args = parser.parse_args()

    if args.security_tests:
        api_security_tests()

if __name__ == "__main__":
    main()
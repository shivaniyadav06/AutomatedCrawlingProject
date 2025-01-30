import pytest
import sys
import os

def run_tests()
    
    test_args = [
        "-v",
        "--maxfail=1",
        "--disable-warnings",
        "tests"
    ]

    result_code = pytest.main(test_args)
    return result_code

if __name__ == "__main__":
    exit_code = run_tests()

    sys.exit(exit_code)

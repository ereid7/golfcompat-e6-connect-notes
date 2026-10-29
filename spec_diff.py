#!/usr/bin/env python3
"""Compare two requirement tables one spec at a time.

A requirements page answers your machine only when each spec is
compared in its own row: memory, graphics, storage, internet.
"""
import sys, json

def diff(required, yours):
    missing = [k for k in required if k not in yours]
    return {"met": {k: yours[k] for k in required if k in yours},
            "missing": missing}

if __name__ == "__main__":
    required = json.load(open(sys.argv[1]))
    yours = json.load(open(sys.argv[2]))
    print(json.dumps(diff(required, yours), indent=2))

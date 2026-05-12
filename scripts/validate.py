#!/usr/bin/env python3
"""Validate vulnerability YAML entries against the open-cvdb schema."""
import glob, sys, yaml

REQUIRED = ['title', 'slug', 'affectedPlatforms', 'affectedServices', 'severity', 'summary', 'references', 'entryStatus']
PLATFORMS = ['aws', 'azure', 'gcp', 'ibm', 'oracle', 'alibaba']

def validate(path):
    errors = []
    with open(path) as f:
        entry = yaml.safe_load(f)
    if not entry:
        return ["empty file"]
    for field in REQUIRED:
        if field not in entry or (entry[field] is None and field != 'severity'):
            errors.append(f"missing '{field}'")
    if entry.get('severity') and entry['severity'] not in ['critical', 'high', 'medium', 'low']:
        errors.append(f"invalid severity: {entry['severity']}")
    if entry.get('entryStatus') not in ['Stub', 'Finalized']:
        errors.append(f"invalid entryStatus: {entry.get('entryStatus')}")
    for p in (entry.get('affectedPlatforms') or []):
        if p not in PLATFORMS:
            errors.append(f"unknown platform: {p}")
    if not (entry.get('references') or []):
        errors.append("no references")
    return errors

if __name__ == '__main__':
    files = sys.argv[1:] or glob.glob('vulnerabilities/*.yaml')
    failed = sum(1 for f in files if validate(f))
    for f in files:
        errs = validate(f)
        if errs:
            print(f"❌ {f}: {', '.join(errs)}")
    print(f"\n{'✅' if not failed else '❌'} {len(files)-failed}/{len(files)} valid")
    sys.exit(1 if failed else 0)

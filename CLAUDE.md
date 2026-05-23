# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

The Open Cloud Vulnerability & Security Issue Database (cloudvulndb.org) - a community-maintained catalog of cloud provider (CSP) security vulnerabilities and issues. Changes merged to main are automatically reflected on the website.

## Repository Structure

- `vulnerabilities/` - YAML files documenting individual vulnerabilities (282+ entries)
- `pages/` - Static content pages and the `sample.yaml` template
- `images/` - Images referenced by vulnerability entries

## YAML Schema

Each vulnerability file follows this structure (see `pages/sample.yaml` for template):

```yaml
title: Human-readable title
slug: url-friendly-identifier  # Must match filename without .yaml
cves:
  - CVE-YYYY-NNNNN  # Empty array [] if none
affectedPlatforms:
  - aws | azure | gcp | github | gitlab  # Lowercase
affectedServices:
  - Service Name
image: https://...  # Or path to images/[slug].jpg
severity: critical | high | medium | low  # Or null
piercingIndexVector: {version: 1.5, A1: 22, A2: 1, ...}  # Optional
discoveredBy:
  name: Researcher Name
  org: Organization
  domain: https://...
  twitter: @handle or URL
publishedAt: YYYY/mm/dd
disclosedAt: YYYY/mm/dd
exploitabilityPeriod: null  # Or description
knownITWExploitation: true | false | null
summary: |
  Multi-line description of the vulnerability
manualRemediation: |
  Steps customers should take, or "None required"
detectionMethods: |
  How to detect exploitation, or "None" or null
contributor: https://github.com/username
references:
  - https://...  # At least one required
entryStatus: Stub | Stub (AI-Generated) | Finalized
```

## Contribution Guidelines

1. Use `Finalized` for complete entries; `Stub` or `Stub (AI-Generated)` for incomplete
2. The `slug` must match the filename (e.g., `my-vuln.yaml` has `slug: my-vuln`)
3. Include at least one public reference URL
4. Give credit to researchers in the `discoveredBy` block
5. Use respectful language - no disparaging CSPs, vendors, or researchers
6. Severity can be estimated or derived from the [Piercing Index](https://github.com/piercing-index/cloud-vulnerabilities)

## Distilling Sources into YAML

When converting security research blog posts or vendor bulletins into entries:

### Source Types
- **Security researcher blogs** (primary source with technical details)
- **Vendor security bulletins** (AWS Security Bulletins, GCP Support Bulletins, MSRC)
- **CVE records** (for CVE IDs and descriptions)

### Field Extraction Guidelines

**title**: Use the vulnerability's name if it has one (e.g., "Synlapse", "ConfusedFunction"). Otherwise, create a concise descriptive title like "GCP Cloud Functions Privilege Escalation Vulnerability".

**summary**: 3-5 sentences maximum. Include:
- What the vulnerability was (the flaw itself)
- What services/components were affected
- What the potential impact was
- Whether/how it was fixed
- Avoid exploitation steps or technical implementation details

**publishedAt**: Date the blog post or security bulletin was published (not when you're adding it).

**disclosedAt**: When the researcher reported to the vendor. Look for "Timeline" sections, "Responsible Disclosure" notes, or phrases like "reported on X date".

**exploitabilityPeriod**: Extract from timelines. Use formats like "Until YYYY/mm/dd" (when fix deployed) or "YYYY/mm/dd to YYYY/mm/dd" (specific window).

**severity**: Infer from impact if not stated:
- Cross-tenant access, RCE, global admin = `critical`
- Privilege escalation, authorization bypass = `high`
- Information disclosure, logging gaps = `medium`
- Limited scope issues = `low`

**discoveredBy**: Look for:
- Author bylines at top/bottom of blog posts
- "About the Author" sections
- Acknowledgment sections in vendor bulletins
- Use `org` without `name` if only company is credited

**manualRemediation**: Focus on customer actions:
- "None required" if CSP fully remediated server-side
- Specific version upgrades (e.g., "Update to version X.Y.Z or later")
- Configuration changes customers should make
- Workarounds if patches aren't available

**detectionMethods**: Include when available:
- KQL/SQL queries from the research (verbatim)
- CloudTrail event names to monitor
- Version checks to identify vulnerable installations
- Use "None" if no practical detection exists

**references**: Order by importance:
1. Primary technical writeup (researcher's blog)
2. Vendor security bulletin/acknowledgment
3. CVE record link
4. AWS/GCP/Azure documentation if relevant

### Quality Checklist
- Platforms are lowercase: `aws`, `azure`, `gcp`, `github`, `gitlab`
- Domain field is bare domain without `https://` prefix
- Empty fields use `null` not `- null` or empty strings
- Dates use `YYYY/mm/dd` format
- CVEs array is `[]` if none, not `null`

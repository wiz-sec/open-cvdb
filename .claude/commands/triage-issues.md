---
name: triage-issues
description: Triage open GitHub issues labeled "addition" in the open-cvdb repository. Reviews each issue for vulnerability sources, runs the vulnerability skill, and comments with analysis. Idempotent - skips issues already triaged. Use when asked to triage issues, review additions, or process the issue backlog.
---

# Issue Triage Skill

Automatically triage open issues requesting new vulnerability additions.

## Overview

This skill processes open issues with the "addition" label, extracts source URLs, runs the vulnerability skill to evaluate them, and either creates a PR or comments with analysis explaining why not.

## Process

### Step 1: Fetch Open Issues

```bash
gh issue list --repo wiz-sec/open-cvdb --label "addition" --state open --json number,title,body,comments --limit 50
```

### Step 2: Filter Already-Triaged Issues

For each issue, check if already processed:

1. **Check for triage comment marker** in issue comments:
   ```
   <!-- [triage-comment] -->
   ```

2. **Check for linked PR**:
   ```bash
   gh pr list --repo wiz-sec/open-cvdb --search "closes #{issue_number}" --state all
   ```

If either exists, skip the issue - it's already been triaged.

### Step 3: Process Each Untriaged Issue

For each untriaged issue:

#### 3a. Extract Source URLs

Parse the issue body for:
- URLs in the "References" section
- Any URLs pointing to security research (blog posts, bulletins, CVE records)
- Links in markdown format `[text](url)` or bare URLs

If no URLs found, comment asking for sources and skip to next issue.

#### 3b. Run Vulnerability Skill

For each extracted URL, follow the vulnerability skill process:
1. Fetch and analyze sources
2. Check for duplicates
3. Search for additional sources
4. Skeptical impact review
5. Check scope/inclusion criteria

**When creating the PR**, include `Closes #{issue_number}` in the PR body so GitHub auto-links and closes the issue on merge.

#### 3c. Handle Outcome

**If PR is created:**
- The vulnerability skill handles the PR
- Reference the issue in the PR body (e.g., "Closes #{issue_number}") so GitHub auto-links
- Do NOT add a triage comment - the PR linkage is sufficient
- The issue will show the PR reference automatically

**If entry is rejected:**
Add a triage comment explaining why:

```markdown
<!-- [triage-comment] -->
## Triage Analysis

Unable to create an entry for this submission.

**Reason**: {rejection_reason}

**Details**:
{detailed_explanation}

**What would help**:
{suggestions_for_resubmission}

---
*This is an automated triage. If you believe this analysis is incorrect, please reply with additional information.*
```

**Rejection reasons to document:**
- Source unavailable (404, paywall) with no corroborating sources
- Out of scope (customer incident, WAF bypass, non-cloud vulnerability)
- Duplicate of existing entry `{slug}`
- Actively disputed by vendor
- Insufficient public information
- Expected behavior, not a vulnerability

**If more information needed:**
```markdown
<!-- [triage-comment] -->
## Triage: More Information Needed

I attempted to analyze this submission but need clarification:

**Issue**: {what's unclear}

**Questions**:
{specific_questions}

**Found so far**:
{partial_findings}

---
*Please reply with the requested information to continue triage.*
```

### Step 4: Report Summary

After processing all issues, provide a summary:

```
## Triage Summary

Processed: {n} issues
- PRs created: {n}
- Rejected: {n}  
- Need more info: {n}
- Already triaged (skipped): {n}

### Issues Processed:
| Issue | Outcome | Notes |
|-------|---------|-------|
| #123  | PR #456 | Created entry for {slug} |
| #124  | Rejected | Out of scope - customer incident |
| #125  | Skipped | Already triaged |
```

## Idempotency

This skill is idempotent:
- Issues with a `<!-- [triage-comment] -->` marker are skipped (rejected/needs-info)
- Issues already linked to a PR are skipped (check with `gh pr list --search "closes #{issue}"`)
- Safe to run multiple times
- New issues get processed, old ones skipped

## Rate Limiting

- Process maximum 10 issues per run to avoid API limits
- If more than 10 untriaged issues exist, report this and suggest running again

## Example

User: "triage the open issues"

Response flow:
1. Fetch open issues with "addition" label
2. Filter out issues with triage marker
3. For each untriaged issue:
   - Extract URLs
   - Run vulnerability skill
   - Comment with outcome
4. Report summary

## Error Handling

If an error occurs processing an issue:
- Do NOT add triage marker (so it can be retried)
- Log the error
- Continue to next issue
- Include failed issues in summary with error details

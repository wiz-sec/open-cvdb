---
name: hunt
description: Hunt for new cloud vulnerabilities to add to open-cvdb. Checks authoritative security research sources for recent disclosures, or reviews a specific URL provided as argument. Creates PRs for well-documented vulnerabilities or opens GitHub issues when more details are needed. Use when asked to find new vulnerabilities, check for updates, or review a specific security blog/bulletin.
---

# Vulnerability Hunt Skill

Proactively find new cloud vulnerabilities to add to the database.

## Access Requirements

This skill works for both contributors and non-contributors:
- **Source fetching**: No GitHub access required
- **Duplicate checking**: Uses local grep, no special access needed
- **Issue creation**: Any authenticated GitHub user can create issues on public repos
- **PR creation**: Handled by the vulnerability skill, which supports fork-based workflows

## Usage

**Check authoritative sources for new vulnerabilities:**
```
/hunt
```

**Review a specific URL:**
```
/hunt https://example.com/blog/cloud-vuln
```

## Authoritative Sources

### Tier 1: Vendor Security Bulletins (Check First)

These are the most authoritative sources - official vendor acknowledgments.

| Vendor | URL | Check Method |
|--------|-----|--------------|
| AWS | https://aws.amazon.com/security/security-bulletins/feed/ | Fetch RSS feed (works better than web page) |
| GCP | https://cloud.google.com/support/bulletins | Fetch page (redirects to docs.cloud.google.com) |
| Azure/MSRC | https://api.msrc.microsoft.com/cvrf/v3.0/updates | Use MSRC API, then fetch /cvrf/{yyyy-Mon} for details |
| GitHub | https://github.blog/security/ | Check for platform security posts |

**MSRC API Usage:**
1. Fetch `/updates` to get list of monthly security updates
2. For recent months, fetch `/cvrf/{id}` (e.g., `/cvrf/2026-Apr`)
3. Filter for Azure/Entra/M365 products in the CVRF response
4. Cross-reference CVEs with existing entries

### Tier 2: Security Research Firms (High Authority)

Established firms with track records of responsible disclosure.

| Source | Domain | Focus |
|--------|--------|-------|
| Wiz | wiz.io/blog | AWS, Azure, GCP cross-tenant issues |
| Orca Security | orca.security/resources/blog | Multi-cloud vulnerabilities |
| Tenable | tenable.com/blog/search?field_blog_section_tid=453 | Cloud security research |
| Palo Alto Unit42 | unit42.paloaltonetworks.com | Cloud threat research |
| Datadog Security Labs | securitylabs.datadoghq.com | AWS, container security |
| Aqua Security | aquasec.com/blog | Container, Kubernetes, cloud |
| NetSPI | netspi.com/blog | Cloud penetration testing |
| Rhino Security Labs | rhinosecuritylabs.com/blog | AWS, cloud attack research |
| Lightspin | blog.lightspin.io | AWS security |
| TrustOnCloud | trustoncloud.com/blog | AWS IAM, Bedrock |
| Legit Security | legitsecurity.com/blog | CI/CD, supply chain |
| Praetorian | praetorian.com/blog | Azure, cloud security |

### Tier 3: Independent Researchers (Frequently Cited)

Individual researchers with established credibility in cloud security.

| Researcher | Domain | Known For |
|------------|--------|-----------|
| Nick Frichette | frichetten.com | AWS exploitation, Hacking the Cloud |
| Christophe Tafani-Dereeper | blog.christophetd.fr | AWS, GCP research |
| embracethered | embracethered.com | Azure, M365 security |
| binarysecurity.no | binarysecurity.no | Azure security |
| Scott Piper | summitroute.com | AWS security, original CSP mistakes list |
| Dirk-jan Mollema | dirkjanm.io | Azure AD/Entra ID |

## Process

### Mode 1: Check Sources (no argument)

When invoked without a URL:

1. **Select sources to check** - Ask user which tier(s) to check, or check all
2. **Fetch recent posts** from each source's blog/bulletin page
3. **Filter for cloud vulnerabilities** - Look for:
   - AWS, Azure, GCP, GitHub, GitLab mentions
   - CVE assignments for cloud services
   - Terms: vulnerability, security issue, disclosure, cross-tenant, privilege escalation
4. **Cross-reference with existing entries** - Check if already in CVDB
5. **For each new finding**, run the vulnerability skill process

### Mode 2: Review URL (with argument)

When invoked with a URL argument:

1. **Fetch and analyze** the provided URL
2. **Run vulnerability skill** - full analysis including:
   - Scope check (is it a cloud CSP vulnerability?)
   - Duplicate check
   - Source corroboration
   - Skeptical impact review
3. **Create PR or Issue** based on findings

## Output Handling

### Sufficient Information → Create PR

If the vulnerability skill succeeds (passes all checks), create a PR via the vulnerability skill.

**Always set `entryStatus: Stub (AI-Generated)`** - even if information appears complete, human review is required before marking as Finalized.

### Insufficient Information → Create Issue

If we find a potential vulnerability but lack details, create a GitHub issue:

```bash
gh issue create --repo wiz-sec/open-cvdb \
  --label "addition" \
  --title "[Contribution] {vulnerability_title}" \
  --body "## Summary
{brief_description}

## References
{source_urls}

## Notes
This vulnerability was identified during automated hunting but requires additional information:
- {what's_missing}

## Source Authority
{authority_assessment}

---
*Created by automated hunt. Human review needed to complete entry.*"
```

**Create an issue when:**
- Source is behind paywall but title/abstract indicates cloud vuln
- Vulnerability is mentioned but technical details are sparse
- No vendor acknowledgment yet but research looks credible
- Date/timeline information is unclear

### Out of Scope → Skip

If the finding is out of scope for CVDB:
- Customer incidents, WAF bypasses, non-cloud vulns
- Log it in the hunt summary but don't create PR or issue

### Already Exists → Skip

If already in CVDB:
- Note as "already tracked" in summary
- Optionally flag if existing entry needs updates

## Hunt Summary

After checking sources, provide a summary:

```markdown
## Hunt Summary

**Sources checked**: {n}
**New vulnerabilities found**: {n}
**PRs created**: {n}
**Issues created**: {n}
**Already tracked**: {n}
**Out of scope**: {n}

### New Findings
| Source | Vulnerability | Outcome |
|--------|--------------|---------|
| Wiz Blog | CosmosDB cross-tenant | PR #123 |
| AWS Bulletin | ECS agent info disclosure | Already tracked |
| Unit42 | Lambda cold start timing | Out of scope (not CSP vuln) |

### Issues Created (Need More Info)
| Issue | Source | What's Missing |
|-------|--------|----------------|
| #456 | MSRC advisory | Technical details unclear |
```

## Rate Limiting

- Check maximum 5 sources per run to avoid overwhelming
- If more sources need checking, suggest running again
- Add delay between fetches to be respectful to source sites

## Example

**Hunt all sources:**
```
User: /hunt
Assistant: I'll check the authoritative sources for new cloud vulnerabilities.
[Checks Tier 1 vendor bulletins first, then Tier 2 research firms]
[Cross-references findings with existing CVDB entries]
[Creates PRs for well-documented vulns, issues for those needing more info]
```

**Review specific URL:**
```
User: /hunt https://wiz.io/blog/new-azure-vulnerability
Assistant: I'll analyze this Wiz blog post for a potential CVDB entry.
[Runs vulnerability skill on the URL]
[Creates PR if sufficient info, or issue if more details needed]
```

## Integration with Other Skills

This skill uses:
- **vulnerability skill** - For full analysis and PR creation
- **triage-issues skill** - Similar output format for issues created

When creating issues, use the same format as contribution issues so triage-issues can process them later if more information becomes available.
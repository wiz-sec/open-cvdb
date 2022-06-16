# The Open Cloud Vulnerability & Security Issue Database ☁️⚠️
An open project to list all publicly known cloud vulnerabilities and CSP security issues

> Changes and additions to this GitHub repository are automatically reflected at [cloudvulndb.org](https://cloudvulndb.org/).

### Background
Security bugs in Cloud services tend to [fall between the cracks](https://www.wiz.io/blog/security-industry-call-to-action-we-need-a-cloud-vulnerability-database/), as they don’t fit well into the current [shared responsibility model](https://cloudsecurityalliance.org/blog/2020/08/26/shared-responsibility-model-explained/) of cloud security. As a result, remediation often requires a joint effort between both the CSP and their customers.

There is currently no universal standard for cloud vulnerability enumeration – CSPs rarely issue CVEs for security mistakes discovered in their services, there are no industry conventions for assessing severity, no proper notification channels and no unified tracking mechanism – this leads to a great deal of inefficiency and confusion.

Our goal in this project is to pave the way for a centralized cloud vulnerability database, by cataloging CSP security mistakes and listing the exact steps CSP customers can take to detect or prevent these issues in their own environments.

We believe this project can prove the utility of a cloud vulnerability database (VDB), bring more transparency into these issues, and ultimately make the cloud even more secure.

This project was built on the foundations of [Scott Piper](https://twitter.com/0xdabbad00)’s [“Cloud Service Provider security mistakes”](https://github.com/SummitRoute/csp_security_mistakes), and as of June 3rd, 2022, all content included here originally appeared in that repository.

### Contribution guidelines

To contribute a new issue or suggest an edit to an existing one, please add a commit and our maintainers will review it for merging within a few days (but usually sooner). The changes will then automatically be reflected at [cloudvulndb.org](https://cloudvulndb.org/).
<p align="center"><img width="40%" align="center" src="https://github.com/wiz-sec/open-cvdb/blob/main/webscheme.png" alt="cloudvulndb.org is automatically updated according to changes made to this repository" class="center"></p>

Please make sure that your contributions match our [criteria](http://cloudvulndb.org/about) for inclusion, and follow these guidelines:
1.  Use the [CVDB YAML](https://github.com/wiz-sec/open-cvdb/blob/main/pages/sample.yaml) format. 
2.	Include public references (as URLs).
3.	Provide a clear and detailed description of the issue.
4.	Give the issue a descriptive and non-generic title.
5.	Give proper credit to the researchers involved in the discovery.
6.	Use respectful language (avoid disparaging CSPs, vendors or researchers).

### Contact Us
* Join our [Slack group](https://join.slack.com/t/cloud-cve-db/shared_invite/zt-1a0av8bb6-gbR5NE97f0MDP3TCf7kgKQ)
* [Email us](mailto:cloudvulndb@gmail.com)

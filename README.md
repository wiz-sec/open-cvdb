# The Open Cloud Vulnerability & Security Issue Database ☁️⚠️
An open project to list all publicly known cloud vulnerabilities and CSP security issues

> Changes and additions to this GitHub repository are automatically reflected at [cloudvulndb.org](https://cloudvulndb.org/).

### Background
Security bugs in Cloud services tend to [fall between the cracks](https://www.wiz.io/blog/security-industry-call-to-action-we-need-a-cloud-vulnerability-database/), as they don’t fit well into the current [shared responsibility model](https://cloudsecurityalliance.org/blog/2020/08/26/shared-responsibility-model-explained/) of cloud security. As a result, remediation often requires a joint effort between both the CSP and their customers.

There is currently no universal standard for cloud vulnerability enumeration – CSPs [rarely](https://www.cve.org/Media/News/item/blog/2022/09/13/Dispelling-the-Myth-CVE-ID) issue CVEs for security mistakes discovered in their services, there are no industry conventions for assessing severity, no proper notification channels and no unified tracking mechanism – this leads to a great deal of inefficiency and confusion.

Our goal in this project is to pave the way for a centralized cloud vulnerability database, by cataloging CSP security mistakes and listing the exact steps CSP customers can take to detect or prevent these issues in their own environments.

We believe this project can prove the utility of a cloud vulnerability database (VDB), bring more transparency into these issues, and ultimately make the cloud even more secure.

This project was built on the foundations of [Scott Piper](https://twitter.com/0xdabbad00)’s [“Cloud Service Provider security mistakes”](https://github.com/SummitRoute/csp_security_mistakes), and as of June 28th, 2022, all content included here originally appeared in that repository.

### Contribution guidelines

To contribute information about missing cloud vulnerabilities and security issues, you can either use our [contribution form](https://github.com/wiz-sec/open-cvdb/issues/new?assignees=&labels=addition&projects=&template=contribution-template.md&title=%5BContribution%5D+Add+security+issue+or+vulnerability) or create a pull request and our maintainers will review your suggestion within a few days (but usually sooner). The changes will then automatically be reflected at [cloudvulndb.org](https://cloudvulndb.org/). Please make sure that your contributions match our [criteria for inclusion](http://cloudvulndb.org/about).

<p align="center"><img width="40%" align="center" src="https://github.com/wiz-sec/open-cvdb/blob/main/webscheme.png" alt="cloudvulndb.org is automatically updated according to changes made to this repository" class="center"></p>

When creating a pull request, please adhere to the following guidelines:
1.  Use the [CVDB YAML](https://github.com/wiz-sec/open-cvdb/blob/main/pages/sample.yaml) format. 
2.	Include public references (as URLs).
3.	Provide a clear and detailed description of the issue.
4.	Give the issue a descriptive and non-generic title.
5.	Assign the issue an estimated severity and/or rate it using the [Piercing Index](https://github.com/piercing-index/cloud-vulnerabilities).
6.	Give proper credit to the researchers involved in the discovery.
7.	Use respectful language (avoid disparaging CSPs, vendors or researchers).


### Contact Us
* Join our [Slack group](https://bit.ly/cloudVuln)
* Follow us on [Twitter](https://twitter.com/cloudvulndb), [LinkedIn](https://www.linkedin.com/company/cloudvulndb/) and [Mastodon](https://infosec.exchange/@cloudvulndb)
* [Email us](mailto:cloudvulndb@gmail.com)
* Add [requests](https://github.com/wiz-sec/open-cvdb/issues/new/choose) for bugfixes or new features

To learn more about this project and the challenges surrounding cloud vulnerabilities, watch the talk we gave at fwd:cloudsec 2022 ([recording](https://www.youtube.com/watch?v=KwDo6KG76_c&list=PLCPCP1pNWD7N2SPaz4cmuS27xutaf32jy&index=11&ab_channel=fwd%3Acloudsec), [slides](https://pretalx.com/media/fwd-cloudsec-2022/submissions/YJBJPK/resources/cloudvulndb_fwd_jLR2QM9.pdf)).

![CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)

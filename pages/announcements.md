# Announcements 

### September 2023 Updates
*September 03, 2023*

* New website logo 🖼️
* 137 total vulnerabilities and security issues added by 24 contributors (65 added since website launch) ⚠️
* New tag system allows searching for issues with specific severities in each CSP 🏷️
* [RSS feed](https://www.cloudvulndb.org/rss/feed.xml) is now ordered by publication date 🗞
* [New template](https://github.com/wiz-sec/open-cvdb/issues/new?assignees=&labels=addition&projects=&template=contribution-template.md&title=%5BContribution%5D+Add+security+issue+or+vulnerability) for simple contribution of information about a vulnerability or security issue.

### July 2022 Updates
*July 25, 2022*

* [RSS feed](https://www.cloudvulndb.org/rss/feed.xml) is available 🗞
* 10 vulnerabilities added by 5+ contributors ⚠️ 
* CVDB [YAML format](https://github.com/wiz-sec/open-cvdb/blob/main/pages/sample.yaml) now contains publication date field 📆 
* Search engine fixed 🔍
* Laptop stickers available at fwd:cloudsec 2022, AWS re:inforce 2022 & BlackHat 2022

### The Open Cloud Vulnerability & Security Issue Database Launch
*June 28, 2022*

In the past year we witnessed an increasing number of cloud vulnerabilities published by major cloud service providers. Security bugs in cloud services tend to [fall between the cracks](https://www.wiz.io/blog/security-industry-call-to-action-we-need-a-cloud-vulnerability-database/), as they don’t fit well into the current shared responsibility model of cloud security. As a result, remediation often requires a joint effort between both the CSP and their customers.

There is currently no universal standard for cloud vulnerability enumeration – CSPs rarely issue CVEs for security mistakes discovered in their services, there are no industry conventions for assessing severity, no proper notification channels and no unified tracking mechanism. In most cases, CSPs respond quickly to fix the security issue on their side but the lack of standardization leaves many cloud customers vulnerable and unaware of the issues in their environments. 

Today we are launching a community-based website - [cloudvulndb.org](https://cloudvulndb.org/) - to list all cloud vulnerabilities & security issues. Our goal in this project is to pave the way for a centralized cloud vulnerability database, by cataloging CSP security mistakes in a new [format](https://github.com/wiz-sec/open-cvdb/blob/main/pages/sample.yaml) and listing the exact steps CSP customers can take to detect or prevent these issues in their own environments. The website's content is [automatically derived](https://github.com/wiz-sec/open-cvdb/blob/main/webscheme.png) from a [GitHub](https://github.com/wiz-sec/open-cvdb) repository. We invite everyone to join the effort and enrich the database by simply creating a pull request to add a new issue or edit an existing one.

This project was built on the foundations of [Scott Piper](https://twitter.com/0xdabbad00)’s [“Cloud Service Provider security mistakes”](https://github.com/SummitRoute/csp_security_mistakes), who remains as a co-maintainer of this project. As of June 28th, 2022, all content included here originally appeared in that repository. We’d like to thank our [CloudCVE community](https://join.slack.com/t/cloud-cve-db/shared_invite/zt-y38smqmo-V~d4hEr_stQErVCNx1OkMA) for the insightful discussions that helped shape this website. It's important that this conversation continue, as we don't yet claim to have all the answers about the exact form and scope this database should have. What we hope to do here is set a milestone in the ongoing effort to make the cloud even more secure.

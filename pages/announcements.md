# Announcements 

## The Open Cloud Vulnerability & Security Issue Database Launch
*June 28, 2022*

In the past year we witnessed an increasing number of cloud vulnerabilites published by major cloud service providers. Security bugs in cloud services tend to [fall between the cracks](https://www.wiz.io/blog/security-industry-call-to-action-we-need-a-cloud-vulnerability-database/), as they don’t fit well into the current shared responsibility model of cloud security. As a result, remediation often requires a joint effort between both the CSP and their customers.

There is currently no universal standard for cloud vulnerability enumeration – CSPs rarely issue CVEs for security mistakes discovered in their services, there are no industry conventions for assessing severity, no proper notification channels and no unified tracking mechanism. In most cases, CSPs respond quickly to fix the security issue on their side but the lack of standratiztion leaves many cloud customers vulnerable and unaware to the issues and their environemts. 

Today we are lacunhing a community-based website - [cloudvulndb.org](https://cloudvulndb.org/), to list all cloud vulnerabilities & security issues. Our goal in this project is to pave the way for a centralized cloud vulnerability database, by cataloging CSP security mistakes in a new [format](https://github.com/wiz-sec/open-cvdb/blob/main/pages/sample.yaml) and listing the exact steps CSP customers can take to detect or prevent these issues in their own environments. The site content is automatically derived from a [GitHub](https://github.com/wiz-sec/open-cvdb) repository. We invite everyone to join the effort and enrich the database by simply creating a pull request to add a new issue or edit an existing one.

<p align="center"><img width="80%" align="center" src="https://github.com/wiz-sec/open-cvdb/blob/main/webscheme.png" alt="cloudvulndb.org is automatically updated according to changes made to this repository" class="center"></p>

This project was built on the foundations of [Scott Piper](https://twitter.com/0xdabbad00)’s [“Cloud Service Provider security mistakes”](https://github.com/SummitRoute/csp_security_mistakes), who remains as a co-maintainer of this project. As of June 28th, 2022, all content included here originally appeared in that repository. We’d like to thank our [CloudCVE community](https://join.slack.com/t/cloud-cve-db/shared_invite/zt-y38smqmo-V~d4hEr_stQErVCNx1OkMA) for the insightful discussions that helped shape this website. The exact shape and scope of this database is not something we claim to have all the answers to. What we hope to do here is to set a milestone in the effort to secure cloud customers.

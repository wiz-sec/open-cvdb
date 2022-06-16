## Mission Statement

Security bugs in Cloud services tend to [fall between the cracks](https://www.wiz.io/blog/security-industry-call-to-action-we-need-a-cloud-vulnerability-database/), as they don’t fit well into the current [shared responsibility model](https://cloudsecurityalliance.org/blog/2020/08/26/shared-responsibility-model-explained/) of cloud security. As a result, remediation often requires a joint effort between both the CSP and their customers.

There is currently no universal standard for cloud vulnerability enumeration – CSPs rarely issue CVEs for security mistakes discovered in their services, there are no industry conventions for assessing severity, no proper notification channels and no unified tracking mechanism – this leads to a great deal of inefficiency and confusion.

Our goal in this project is to pave the way for a centralized cloud vulnerability database, by cataloging CSP security mistakes and listing the exact steps CSP customers can take to detect or prevent these issues in their own environments.

We believe this project can prove the utility of a cloud vulnerability database (VDB), bring more transparency into these issues, and ultimately make the cloud even more secure.

## Criteria
We define the following criteria for inclusion in this database:
1.	Publicly known security issues in cloud services;
2.	With or without an assigned CVE;
3.	That had a proven actual or potential impact on cloud customers;
4.	And required remediation actions on either side of the shared responsibility model.

Examples include:
-	Security issues in default misconfigurations
-	Vulnerabilities in CSP-provided client software
We consider the following cases to be out of scope of this project:
-	CSP security incidents with no security impact on customers
-	Security issues about which there is no publicly available information
-	CSP customer security incidents

## History
This project was built on the foundations of [Scott Piper](https://twitter.com/0xdabbad00)’s [“Cloud Service Provider security mistakes”](https://github.com/SummitRoute/csp_security_mistakes), and as of June 3rd, 2022, all content included here originally appeared in that repository.

## Next Steps
Besides continuing to document newly discovered cloud vulnerabilities and security issues, we would also like to achieve the following:
1. Reach consensus on definitions for severity (e.g., what makes a cloud vulnerability critical?).
2. Differentiate between closed vs. ongoing security issues, and bring more attention to ongoing issues.
3. Calculate exploitability periods for each issue.
4. List detection methods for every issue, where possible.

## Project Maintainers
* [Scott Piper](https://twitter.com/0xdabbad00)
* [Amitai Cohen](https://twitter.com/amitaico)
* [Alon Schindel](https://twitter.com/41thexplorer)
 
## Related Efforts
-	[CSA Global Security Database](https://globalsecuritydatabase.org/)
-	[Cloud Security Notification Framework](https://onug.net/blog/multi-cloud-security-gets-a-decorator/)

## Contact Us
* Join our [Slack group](https://join.slack.com/t/cloud-cve-db/shared_invite/zt-1a0av8bb6-gbR5NE97f0MDP3TCf7kgKQ)
* [Email us](mailto:cloudvulndb@gmail.com)

## Sponsorship 
This site is kindly sponsored by [Wiz](https://wiz.io). Its content is contributed by the cloud security community and for the cloud security community.

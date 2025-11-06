CTComms sends on average 2 million emails monthly on behalf of over 125 different charities and not for profits.

A software license is a legal agreement between the user and the owner of a program that grants specific permissions that would otherwise be restricted by copyright law. Typical licensing agreements spell out who may use the software, how it may be used, whether it can be copied or modified, and under what conditions it may be redistributed; pricing or licensing fees are sometimes included but frequently are documented separately.

Key licensing categories and terms
- Free vs. proprietary: “Free software” refers to freedoms and permissions (free as in freedom), not necessarily price. Free software licenses usually allow copying, modification, and redistribution without requiring payment or additional permission. Proprietary software imposes restrictions on copying, modification, and redistribution.
- Free, open-source, FOSS: In everyday use these terms are often interchangeable, but their official definitions and underlying philosophies differ. Proponents of each camp largely agree on practical matters, yet there are conceptual distinctions between “free software” (emphasizing user freedoms) and “open source” (emphasizing methodology and development model).
- Copyleft vs. public domain: Copyleft licenses grant the usual free-software freedoms but require that derivative works be released under the same license terms, preventing the code being turned proprietary. Public domain relinquishes copyright entirely and is not copyleft; software in the public domain is free but without the copyleft requirement.
- Freeware and shareware: These are marketing labels rather than formal licensing categories. Freeware is typically proprietary software available at no cost but without source-code access or redistribution rights. Shareware is trial software that can be used temporarily (e.g., 30–60 days) and requires payment for continued use.

End User License Agreement (EULA)
- EULAs are the common click-through agreements presented when acquiring software directly from a vendor or website. For large, negotiated purchases a signed contract typically supersedes a vendor’s standard EULA.

Volume licensing: benefits and practicalities
- Major proprietary vendors commonly offer volume licensing for organisations, with cost and administrative benefits:
  - Lower cost per copy when purchased in volume.
  - Easier installation via organisation-wide activation codes instead of individual product keys.
  - Simplified license tracking, often through online accounts that log activations and coordinate between offices.
- Not-for-profit organisations often qualify for donation or discounted volume-license programs via intermediaries such as TechSoup. Examples include Microsoft donation programs, Microsoft eOpen for locating volume license keys, Adobe donation programs, and vendor-specific nonprofit discount pages.
- Always check donated/discounted stock first (e.g., TechSoup Stock). If stock is insufficient, search for vendor nonprofit programs or reseller volume-licensing offers.

Server software licensing: types and common patterns
- Server applications generally include the license to install and run the server software, but often require additional client licenses for users or devices that access the server.
- Processor licensing: Some server editions (e.g., Windows Server Datacenter or certain SQL Server editions) require a license per processor on the physical host; these are commonly used instead of client licenses for heavily virtualised or high-density servers. Processor-licensed products typically do not require CALs.
- Licensing terminology and options are product-specific, but common structures recur across Microsoft server offerings. Microsoft often provides multiple licensing models for the same server product so organisations can select the most cost-effective scheme for their usage patterns (e.g., per-user vs per-device).

Client Access Licenses (CALs)
- Internal authenticated users (employees, contractors, volunteers) often require CALs for many Microsoft server products (e.g., Windows Server 2003/2008). Some products (e.g., SQL Server in some licensing modes) do not require CALs.
- User CALs: Assigned to a named user, allowing that person to access all instances of the server product from any number of devices. Useful when users need access from multiple devices.
- Device CALs: Assigned to a device, allowing any number of users to access the server from that device. Useful in shift-work environments or shared-terminal scenarios.
- Modes for Windows Server CAL usage: When installing Windows Server you choose a licensing mode—per seat (default) or per server. CALs themselves are not marked by mode and can be used in either. Per server mode treats CALs as simultaneous-connection seats tied to a specific server instance; it can make sense for small setups with limited servers and connection counts.

Practical CAL and server licensing facts
- CALs aren’t “installed” on servers; server software generally cannot enforce licensing by denying access based on license counts, except in per-server mode where the server enforces simultaneous-connection limits.
- Anonymous, unauthenticated external users (e.g., website visitors to an IIS-hosted site) do not require CALs.
- Authenticated external users can be covered either by individual CALs or by an External Connector License (ECL). ECLs cover all authenticated external users but are often much more expensive; they are cost-effective only when many external users need authenticated access. ECLs do not replace CALs for internal staff—employees and contractors still need CALs.
- Terminal Services/Remote Desktop Services (TS/RDS) requires separate TS CALs (in addition to standard Windows Server CALs) for each user or device accessing Terminal Services functionality.
- Microsoft System Center products use management licenses (MLs): desktops/workstations managed by these products require client MLs; servers managed require a server management license (standard or enterprise). There are special licensing considerations for managing virtualized instances.
- Standard vs Enterprise CALs: Some products have both standard and enterprise CALs; enterprise CALs unlock advanced features and may be additive (i.e., a user may require both a Standard CAL and an Enterprise CAL to use advanced functionality, as with some Exchange Server editions).

Virtualisation and instances
- Virtualisation allows multiple operating systems (instances) to run on a single physical server. Each deployed instance of Microsoft software typically counts for licensing purposes. The number of instances allowed per license varies by product and licensing program. Organisations must review product-specific virtualization licensing rules (e.g., Microsoft Volume Licensing briefs, Windows Server virtualization calculators) when designing virtual environments.

Resources, nuances and practical guidance
- Microsoft licensing contains many nuances across versions and products; common threads exist but product documentation and vendor resources should be consulted for precise guidance.
- TechSoup and similar nonprofit-focused intermediaries are valuable resources for donated or discounted licenses, instructions on retrieving volume license keys (e.g., eOpen), and guidance on product-specific licensing scenarios.
- When acquiring server-based software, pay attention to both server licenses and any necessary client/access licenses; determine whether client licenses should be per-user, per-device, or covered by special connectors or external licenses to find the most economical and compliant option.

Author and licensing of this guidance
- The author has a background in technology writing, analysis, consulting and training for libraries and nonprofit organisations, and the guidance is published under a Creative Commons Attribution-NonCommercial-NoDerivs 3.0 License.

Additional note
- The latest version of Microsoft Office Professional Plus is presented as an integrated suite of programs, servers, and services designed to work together to support optimised information work.
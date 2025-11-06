# Understanding Software Licensing: Key Concepts and Practical Guidance

Software licensing determines what you may legally do with a program — what you can install, copy, modify, redistribute, or use in a given context. This guide explains common license types, how to choose licensing for servers and clients, and practical tips for organisations (especially nonprofits and libraries) when acquiring software.

---

## Core definition
- Software license: a legal agreement between you and the software owner that grants certain permissions which would otherwise be restricted by copyright law (e.g., copying, installing, modifying, distributing).

---

## License categories and common terms

### Free vs. Proprietary
- Free software: refers to freedoms (use, copy, modify, redistribute), not necessarily price. Free software licenses grant broader rights.
- Proprietary software: restricts rights (often no source code access, limited copying/redistribution).

### Free, Open Source, FOSS
- Free software, open source, and Free and Open-Source Software (FOSS) are often used interchangeably in conversation. Official definitions and philosophies differ, but all generally allow access to source code and redistribution.

### Copyleft vs Public Domain
- Copyleft: a form of free license that requires derivative works to be distributed under the same license terms. Prevents downstream proprietization.
- Public domain: the author relinquishes copyright; the work can be used without restrictions. Public domain is free but not copyleft.

### Freeware and Shareware (misleading terms)
- Freeware: free to obtain/use but typically proprietary (no source code access, limited redistribution rights).
- Shareware: usually trial or limited-time software that requires payment to continue use; proprietary.

### End User License Agreement (EULA)
- Click-through agreements that users accept when installing or downloading software. For enterprise purchases, a signed contract typically supersedes a EULA.

---

## Volume and Donation Licensing: why it matters for organisations
Buying many copies or using donated/licensed programs for a whole organisation often uses volume licensing. Benefits include:
- Lower cost per copy.
- Easier installation (single organisation-wide activation codes).
- Centralised tracking of licenses (often via online accounts).
- Special donation/discount programs exist for qualified nonprofits and libraries.

Practical steps:
- Check donation programs (e.g., nonprofit-focused distributors) for available products and inventory first.
- If a product is out-of-stock or you need more copies, look for vendor nonprofit discounts or special programs.
- When using donation programs, follow any portal instructions (e.g., locating volume license keys).

---

## Server software licensing basics
Server products often require:
1. A license to install/run the server application itself (usually bundled).
2. Client licenses for users/devices that access the server (Client Access Licenses, or CALs), depending on product and licensing model.
3. In some cases, processor licenses or per-processor licensing for certain server editions.

Examples:
- Some server editions (e.g., certain Windows Server or SQL Server editions) require a license per processor for multi-CPU servers — no CALs required in those scenarios.
- Other server products require CALs for authenticated users/devices.

---

## Client Access Licenses (CALs): User vs Device
- User CAL: assigned to a person; allows that person to access all instances of a server product across the organisation from any device.
  - Best when employees use multiple devices.
- Device CAL: assigned to a device; allows any number of users to use that device to access the server.
  - Best when multiple users share a single device (e.g., shift workstations).

Choosing a CAL mode:
- Two licensing modes are commonly used for Windows Server families:
  - Per seat (default): CALs are assigned per seat (users or devices) across servers.
  - Per server: CALs are tied to a particular server and count simultaneous connections.
- You select the mode at installation/configuration of the server product. CALs themselves are not mode-specific.

Important note:
- CALs are not "installed" in the conventional sense; the server software typically does not enforce CAL counts except in per-server mode (which treats CALs as simultaneous connections).

---

## Special client licensing scenarios and exceptions

- Anonymous (unauthenticated) external users: typically do not need CALs (e.g., website visitors accessing IIS-hosted content anonymously).
- Authenticated external users (clients outside your organisation): options include:
  - Buying individual CALs for those external users (if few).
  - External Connector License (ECL): covers all authenticated external users, but usually much more expensive — cost-effective only with large numbers of external users.
  - Note: ECL covers external users only; internal employees/contractors still require CALs.
- Terminal Services / Remote Desktop Services (RDS): requires separate TS/RDS CALs in addition to Windows Server CALs for each user or device accessing Terminal Services.
- Management software (e.g., enterprise system center products): often uses Management Licenses (MLs) — e.g., desktops/workstations require client MLs; servers require server MLs (standard or enterprise).
- Enterprise CALs: some products have both Standard CALs and Enterprise CALs; advanced features often require both (additive licensing).
- Virtualisation: every installed instance of an application (physical or virtual) is an "instance"; licensing rules for how many instances a single license covers vary by product. Pay attention to virtualization licensing rules and available virtualization rights.

---

## Practical checklist before acquiring software
- Identify who will use the software (employees, volunteers, external clients) and whether users are authenticated.
- Determine whether access is by user or device and choose User CALs or Device CALs accordingly.
- Check whether server editions require per-processor licenses or use CAL-based licensing.
- If external authenticated users exist, estimate their numbers and compare buying CALs vs. acquiring an ECL.
- For virtualised environments, count the number of instances and verify vendor virtualization rights.
- Check nonprofit donation and discount programs and review inventory availability before purchasing retail.
- Confirm activation key & license key retrieval process (single org key vs. per-copy keys).
- Maintain an internal license inventory (product name, license type, quantity, purchase/donation date, activation keys, expiry/renewal info).
- Read product-specific licensing guides or vendor volume-licensing documentation for nuances.

---

## Common pitfalls and how to avoid them
- Underestimating authenticated access: forgetting to license authenticated external users or service accounts can create compliance gaps.
- Miscounting devices vs users: choose the wrong CAL type for your usage pattern and overspend.
- Ignoring server edition differences: some editions include different virtualization or processor licensing requirements.
- Assuming freeware = open source: freeware may be proprietary; verify redistribution and source access rights.
- Relying on assumptions about donation programs: always confirm stock levels and eligibility rules before planning deployment.
- Failing to track licenses centrally: create a simple spreadsheet or use a licence management tool to avoid over- or under-deployment.

---

## Quick glossary
- CAL: Client Access License — grants access rights to server software for a user or device.
- ECL: External Connector License — covers authenticated external users for a server product.
- EULA: End User License Agreement — the click-through agreement you accept to use software.
- ML: Management License — license used by certain enterprise management products.
- Copyleft: licensing approach that requires modified versions to be released under the same license.
- Freeware/Shareware: usually proprietary terms for free-to-obtain or trial software, respectively.

---

## Example: How licensing choices affect cost
- Small organisation with many mobile employees: User CALs are likely most cost-effective (single CAL per person).
- 24-hour call centre with shared workstations: Device CALs can reduce costs since multiple shifts share devices.
- Public-facing website with anonymous visitors: No CALs needed for anonymous access, but authenticated portal users may require CALs or an ECL.

---

## Resources and next steps
- Always read product-specific licensing documentation from the software vendor for exact terms.
- For organisations eligible for donations or discounts, consult nonprofit-focused distributors and donation portals to check available software and instructions for retrieving license keys.
- Maintain records of all licenses and periodically audit installations against entitlements.

---

By understanding license types, how server and client licensing models work, and following a practical acquisition checklist, organisations can make informed choices that meet their needs while staying compliant and optimising cost.
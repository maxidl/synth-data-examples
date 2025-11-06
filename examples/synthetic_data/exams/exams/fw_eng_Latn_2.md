Below are five different exam styles you can choose from. Each exam contains 15 tasks: 5 easy, 5 medium, and 5 hard. Every task includes a model answer/solution for grading. All questions are self-contained and based on the material your students have read.

Exam 1 — Mixed format (multiple-choice + short answers + true/false with justification)
- Easy: 5 multiple-choice questions (one best answer each).
- Medium: 5 short-answer questions (concise explanation).
- Hard: 5 true/false statements; students must mark T/F and give a short justification.

Answers follow each question.

Exam 1
Easy (choose one correct option)
1. Which term describes software that grants the user rights to copy, modify, and redistribute, regardless of price?
   A) Freeware
   B) Free software
   C) Shareware
   D) Proprietary software
   Solution: B) Free software — “free” refers to freedoms and permissions (copy, modify, redistribute); price is not asserted.

2. Which of the following is typically a “click-through” license you accept when installing consumer software?
   A) Volume license
   B) EULA
   C) External Connector License
   D) Public domain declaration
   Solution: B) EULA — click-through End User Licensing Agreement.

3. A copyleft license requires:
   A) Giving up all copyrights
   B) Releasing modifications under the same terms
   C) Charging for every redistribution
   D) Hiding source code
   Solution: B) Releasing modifications under the same terms — copyleft forces derivatives to use same license.

4. Device CALs are most appropriate when:
   A) Each employee has a personal device
   B) Servers are licensed per processor
   C) Multiple employees share the same workstation (e.g., shift work)
   D) External anonymous web users access IIS
   Solution: C) Multiple employees share the same workstation — Device CALs suit shared devices.

5. If you run Windows Server 2008 Datacenter on a two-processor server, you need:
   A) One license for the server regardless of processors
   B) A separate license per processor
   C) Only client access licenses (CALs)
   D) An ECL instead of CALs
   Solution: B) A separate license per processor — processor license required for multi-processor servers.

Medium (short answer — 1–3 sentences)
6. Briefly distinguish “freeware” from “free software.”
   Solution: Freeware is typically proprietary: free of charge but without source code or redistribution rights; free software grants freedom to view, modify, copy, and redistribute (price unrelated).

7. Name two practical benefits of volume licensing listed in the text.
   Solution: Lower cost when buying more; easier installation via single organisation-wide activation code; easier tracking of licenses via online accounts. (Any two of these.)

8. Explain the difference between a User CAL and a Device CAL.
   Solution: User CALs assign a license to a person, letting them access all server instances from any device; Device CALs assign a license to a device, allowing any user of that device to access server instances.

9. When would you consider buying an External Connector License (ECL) instead of User CALs?
   Solution: Only if you have a large number of authenticated external users, because ECL covers all authenticated external users but is much more expensive (admin fee example: ECL £76 vs User CAL £1).

10. Why do Terminal Services (TS) connections require an additional license beyond Windows Server CALs?
    Solution: Because TS requires its own TS CAL for each client (user or device) in addition to the Windows Server CAL—TS is a separate license requirement.

Hard (true/false + justification)
11. T/F: In per server mode Windows ties CALs to a particular server instance, and the 41st authenticated user will be denied if you have 40 CALs.
    Solution: True. Per server mode treats each license as a simultaneous connection to a particular instance; the 41st authenticated user will be denied (document example).

12. T/F: If a server application is licensed by processor, you still always need client CALs for internal users.
    Solution: False. Generally you don’t need client licenses for applications licensed by processor (the document says generally you don't need client licenses for applications licensed this way).

13. T/F: Releasing software into the public domain is an example of copyleft licensing.
    Solution: False. Public domain gives up copyright and is free software but is not copyleft (copyleft imposes the restriction to release modifications under same terms).

14. T/F: Anonymous web visitors to an IIS-hosted site require User CALs.
    Solution: False. You don't need client licenses for anonymous, unauthenticated external users.

15. T/F: With Exchange Server, a user may need both a Standard CAL and an Enterprise CAL to access advanced features.
    Solution: True. For some products (e.g., Exchange), CALs are additive; a user needs both Standard and Enterprise CALs for advanced features.

Exam 2 — Focused tasks (matching + gap-fill + calculation + ordering + short essay)
- Easy: 5 matching/gap-fill items.
- Medium: 5 small calculations/ordering/short procedures.
- Hard: 5 mini-essay or applied reasoning problems.

Answers directly under each task.

Exam 2
Easy (matching / fill-in)
1. Match the term to definition (write letter): Terms: A) ECL B) Copyleft C) Freeware D) Shareware E) Public domain
   Definitions:
   1) Trial software you use for limited time — Solution: D) Shareware
   2) License that forces derivatives to remain under same terms — Solution: B) Copyleft
   3) Software you can download without paying but typically cannot see source — Solution: C) Freeware
   4) Releases all rights; not copyleft — Solution: E) Public domain
   5) License covering all authenticated external users (often costly) — Solution: A) ECL

2. Fill-in: The click-through license commonly accepted during installation is called a __________.
   Solution: EULA.

3. Fill-in: A license that is issued per physical processor rather than per-user is called a __________ license.
   Solution: Processor license.

4. Fill-in: When many copies are bought, organisations often receive a single organisation-wide activation code; this is a benefit of __________ licensing.
   Solution: Volume licensing.

5. Fill-in: If multiple employees share one computer in shifts, the company will likely prefer __________ CALs.
   Solution: Device CALs.

Medium
6. Ordering: Place these actions in the order a small organisation might follow to acquire donated Microsoft licenses through TechSoup according to the text: A) Check TechSoup Stock, B) Go to eOpen to locate Volume keys, C) Search for “volume licensing not-for-profits software”, D) Check TechSoup donation program pages for specific vendor programs.
   Solution: A → D → C → B. (Check Stock first; then vendor-specific donation pages; if not available search broadly; if obtained go to eOpen for keys.)

7. Calculation: Your organisation has 120 employees who each use multiple devices. You run one Windows Server instance (not per-server mode). Which CAL scheme likely minimizes licenses, User CALs or Device CALs? State which and why. (No numeric answer required.)
   Solution: User CALs — because each employee uses multiple devices; a User CAL permits one user to access from many devices, so 120 User CALs < potentially many Device CALs.

8. Short procedure: List three things a nonprofit should check when deciding between User CALs and Device CALs.
   Solution: (1) Whether employees share devices (shift work); (2) how many devices each user uses; (3) cost comparisons and usage patterns (number of users vs number of devices), plus server count if using per-server mode.

9. Calculation/estimate: You have Windows Server in per-server mode with one server and 40 CALs. On a busy day, 60 authenticated users might try to connect simultaneously. What happens, and what are two remedies?
   Solution: The 41st–60th authenticated users will be denied access because only 40 simultaneous connections allowed. Remedies: buy more CALs for that server; switch to per-seat mode and manage CAL allocation differently; set up additional server instances with own CALs.

10. Ordering: Rank these in terms of increasing administrative fee cost based on the example numbers in the text: User CAL admin fee, ECL admin fee.
    Solution: User CAL admin fee (£1) < ECL admin fee (£76).

Hard
11. Mini-essay (3–5 sentences): Explain the licensing wrinkle that occurs with server-based software when distinguishing between “clients” as users vs “clients” as devices. Give one practical implication for procurement.
    Solution: The document explains that “client” can mean either end-users (employees, contractors) or computing devices (PCs, smartphones). Licensing models (User CAL vs Device CAL) depend on that distinction—if clients are users, User CALs fit; if clients are devices (shared devices), Device CALs fit. Practically, procurement must examine actual usage patterns (shift work, BYOD) before buying to avoid overbuying wrong type of CALs.

12. Case calculation: A charity runs SQL Server licensed by processor on a two-processor host. They have 30 internal users and 10 external authenticated users. According to the text, how many processor licenses and CALs are required for SQL Server in this scenario? Explain.
    Solution: For SQL Server licensed by processor, you need a processor license per processor (so 2 processor licenses) and generally you don’t need client licenses for processor-licensed applications. Therefore no CALs required for SQL Server. External users would not need CALs for SQL Server in this licensing mode. (Note: document states SQL Server 2008 works same way regarding processor licenses and generally you don't need client licenses for apps licensed by processor.)

13. Policy question: A nonprofit has many authenticated external users and limited admin budget. Using the example fee numbers, explain under what conditions it makes sense to buy an ECL rather than User CALs, and compute the break-even point in administrative fees if User CAL admin fee £1 and ECL admin fee £76.
    Solution: ECL is worth it only if external authenticated user count is large. Break-even: ECL admin fee (£76) equals admin fees for 76 User CALs at £1 each. So if you’d otherwise need more than ~76 User CALs for external users, ECL admin fee may be comparable; but ECL covers all authenticated external users in one fee while user CALs scale per-user. Consider total license costs beyond admin fee before deciding.

14. Applied reasoning: Why might per-server mode be attractive to a very small organisation with one or two servers and limited access requirements? Give two reasons drawn from text.
    Solution: Per-server mode ties licenses to simultaneous connections per server, which can be simpler if few servers exist (one set per server). If the organisation has a small, well-bounded user base and predictable simultaneous access below purchased CAL count, per-server can be simpler and cheaper because you buy just enough simultaneous connections per server rather than managing wide per-user entitlements.

15. Advanced matching: Identify three special additional licenses mentioned in the text that are required beyond basic Windows Server CALs and briefly state their purpose.
    Solution: (1) TS CAL — for Terminal Services access in addition to Windows Server CALs; (2) Server management licenses (ML) — for System Center products to manage desktops/servers; (3) Enterprise CAL (additive) — grants access to advanced product features and sometimes must be added to Standard CAL.

Exam 3 — Case-study heavy (practical decision-making)
- Easy: 5 quick scenario identifications.
- Medium: 5 mid-length scenarios requiring calculations and recommendations.
- Hard: 5 complex, multi-constraint licensing plans or policy memos.

Each case followed by an instructor solution.

Exam 3
Easy (identify the correct licensing term or immediate action)
1. A volunteer downloads a utility that’s free to use but the distributor doesn’t provide source code and forbids redistribution. What is this most likely called?
   Solution: Freeware (proprietary, free of charge but without source or redistribution rights).

2. You buy many copies of an office product and receive a single activation key for your organisation. What licensing approach is this?
   Solution: Volume licensing (organisation-wide activation code).

3. Your website on IIS is visited by thousands of anonymous readers daily. Do you need CALs for these anonymous users?
   Solution: No—anonymous, unauthenticated external users do not require CALs.

4. A small museum wants to reinstall Windows Server after hardware failure. Where might they find donation volume license keys (per the text)?
   Solution: The eOpen website (if obtained through TechSoup or similar distributors).

5. If a product requires both Standard CAL and Enterprise CAL for advanced features, what term describes this relationship?
   Solution: Additive licensing (both are required).

Medium (scenario + recommendation)
6. Scenario: A library has 50 staff (each with a laptop and a desktop) and 20 public-use terminals shared among patrons. They run multiple instances of Windows Server. Recommend whether to buy User CALs or Device CALs and justify numerically.
   Solution: Device CALs for public terminals (20) make sense because patrons share machines. For staff: User CALs may be better because each staff has two devices; 50 User CALs cover both devices per person. Combined approach: 50 User CALs + 20 Device CALs, or assess whether converting some public terminals to guest/anonymous access avoids CALs. Numerical justification: 50 users × 1 User CAL = 50 licenses vs 50 ×2 if Device CALs per device would be 100, so User CALs are cheaper for staff.

7. Scenario: An organisation runs Exchange Server and needs advanced features for 30 users. How many CALs are required if the product uses additive Standard + Enterprise CAL model?
   Solution: Each of the 30 users needs both a Standard CAL and an Enterprise CAL. So total = 30 Standard CALs + 30 Enterprise CALs.

8. Scenario: A nonprofit considers using SQL Server on a 4-processor machine and plans to license per processor. How many processor licenses are required? Would client CALs still be required for internal users?
   Solution: 4 processor licenses required (one per processor). Generally no client CALs are required when licensing by processor for that application.

9. Scenario: You have Windows Server set up in per-server mode on two servers; you purchased 40 CALs for server A and 40 CALs for server B. If 45 authenticated users try to access server A simultaneously, what happens? What if some users need to access both servers frequently?
   Solution: On server A the 45th authenticated user will be denied because only 40 simultaneous connections are allowed. If users need to access both servers, you'd need CALs appropriate per-server (additional sets) or switch to per-seat mode (User CALs assigned to users) to allow access across multiple servers without tying CALs to particular servers.

10. Calculation: The museum can get up to four Adobe products via TechSoup donation in a year. They need Creative Suite but TechSoup is out of stock. Suggest two alternative options mentioned in the text.
    Solution: Use TechSoup’s special Adobe donation program or check Adobe Solutions for Nonprofits for discounts (also search for other not-for-profit software discount options).

Hard (complex planning / policy memos)
11. Planning: Your organisation runs a physical server with 2 processors, hosts three instances of Windows Server (for different services), and also hosts several virtual machines. The organisation has 150 employees who each use multiple devices. Draft a concise licensing plan (what license types to buy and why), referencing constraints from the text.
    Solution: For the physical server with 2 processors, consider processor licensing for the server applications that allow it (requires two processor licenses). But for Windows Server instances, if using per-user access across multiple servers and multiple devices per user, User CALs are likely most cost-effective: purchase 150 User CALs so each employee can access all instances from any device. If per-server mode is used, you'd need separate CAL pools per server; that's less convenient with multiple instances. Also consider virtualization rules: verify how many instances each license covers (document warns instance rules vary). If Terminal Services will be used, buy TS CALs as well. If managing endpoints with System Center, add MLs for management. Finally, check TechSoup donation programs for discounted volume licensing for nonprofits.

12. Comparative memo: A nonprofit must decide between buying many User CALs or purchasing an ECL for authenticated external users (e.g., partner organisations). Provide the decision criteria and a sample numeric threshold based on admin fees in the text.
    Solution: Decision criteria: number of authenticated external users, total cost of ECL vs aggregated User CAL costs, administrative fee break-even (ECL £76 admin vs User CAL £1 admin), plus per-license purchase price beyond admin fees and whether ECL excludes internal user coverage (it does). Numeric threshold: admin-wise, if you need more than ~76 external User CALs, ECL admin fee equals admin fees of those CALs; but because ECL’s total cost is higher, evaluate total license costs. If external user count is very large and predictable, ECL may be efficient; for few external users, buy individual User CALs.

13. Compliance analysis: An auditor asks whether anonymous external web traffic to your IIS site requires CALs. Provide the canonical answer and a short explanation.
    Solution: No—anonymous, unauthenticated external users do not require CALs. CALs apply to authenticated users/devices accessing Windows-based services; anonymous visitors to a public website are not CAL-covered.

14. Design question: You must recommend a license-tracking approach for a multi-office nonprofit that gets volume licenses and has frequent staff turnover. Based on the text, list four specific measures/tools or practices to implement.
    Solution: (1) Use vendor-provided online account for volume licensing to track activations; (2) keep a centralized inventory of allocated User CALs and devices; (3) use organisation-wide activation keys to simplify reinstallations and store them securely; (4) review TechSoup accounts for donated licenses and eOpen for locating Volume license keys; implement processes for reclaiming CALs on staff exit and for periodic audits.

15. Complex scenario: Your organisation runs System Center Configuration Manager to manage 200 desktops. Which new licenses are required, and what are the distinctions for servers vs desktops according to the text?
    Solution: System Center products use management licenses (ML). Each desktop/workstation managed needs a client management license. Servers managed need a server management license (standard or enterprise); you need either standard or enterprise (not both). Therefore purchase 200 client MLs for desktops and appropriate server ML(s) for servers managed (standard or enterprise depending on features required). Also check special licensing for virtual instances if managing VMs.

Exam 4 — Analytical + synthesis (definitions, comparisons, diagram/flow)
- Easy: 5 concise definitions.
- Medium: 5 comparative analyses or mini-essays.
- Hard: 5 synthesis tasks including drawing or listing process flows (describe expected student diagram in words).

Each task followed by solution.

Exam 4
Easy (concise definitions — one sentence)
1. Define “copyleft.”
   Solution: A license that grants free software freedoms but requires that modifications and derivatives be released under the same terms as the original.

2. Define “EULA.”
   Solution: An End User Licensing Agreement: a click-through license users accept when installing software that sets the terms of use.

3. Define “User CAL.”
   Solution: A Client Access License assigned to a person, allowing that person to access instances of the server product from any device.

4. Define “Device CAL.”
   Solution: A Client Access License assigned to a device, allowing any user of that device to access server instances.

5. Define “volume licensing.”
   Solution: A licensing approach where buying multiple copies provides benefits like lower cost, single activation codes, and easier license tracking.

Medium (comparisons/explanations)
6. Compare “free software” and “open source” briefly and note any nuance mentioned in the text.
   Solution: The terms are used interchangeably in everyday speech; both grant similar practical freedoms, but official definitions and underlying philosophies differ. The text notes proponents largely agree but references reading for nuance.

7. Explain why freeware and shareware are “confusing” relative to free software.
   Solution: Because freeware/shareware concern price or trial terms rather than user freedoms; freeware may be free to obtain but proprietary (no source or redistribution rights), shareware is trialware, typically requiring payment after a period.

8. Explain per-seat mode vs per-server mode in Windows Server CAL usage.
   Solution: Per-seat (default) ties CALs to users or devices across servers (typical User/Device CAL model), while per-server mode ties CALs to simultaneous connections on a specific server instance — each server needs its own CAL pool and denies connections beyond the pool.

9. Describe one licensing complication introduced by virtualization.
   Solution: Virtualization creates multiple instances of operating systems on one physical server; licensing treats each installed instance as an “instance” and the number permitted per license varies by product, complicating license counts and requiring product-specific rules.

10. Explain the difference between a server management license and a client management license for System Center products.
    Solution: Client management licenses are required for each desktop/workstation managed by System Center; server management licenses are required for servers being managed, with two types for servers (standard and enterprise) and you need one or the other but not both.

Hard (synthesis / diagram description)
11. Task: Draw (or describe in words) a flowchart that an IT manager should follow to decide whether to purchase User CALs, Device CALs, per-processor licenses, or an ECL. Describe each decision node succinctly.
    Solution (description): Start: Identify application type (server app licensed per processor? If yes → buy processor licenses; stop). Else ask: Are users internal or external? If external authenticated and many → evaluate ECL cost vs User CALs (branch). Next ask: Are devices shared (shift work)? If yes → prefer Device CALs; if not and users use multiple devices → prefer User CALs. Then ask: Are you using per-server mode? If yes → determine simultaneous connection counts and buy per-server CAL pool for each server. End with check: need for additional TS CALs or management MLs? Add them if necessary.

12. Policy creation: Compose a 6–8 line internal policy paragraph that instructs staff how to handle software obtained via TechSoup donations (activation keys, checking stock, eOpen).
    Solution (model paragraph): Before acquiring donated software, staff must check TechSoup Stock for available products. If the needed product is unavailable, staff should consult TechSoup’s vendor-specific donation pages and search for volume licensing donation options. When a donation is approved, the IT lead must retrieve and securely store organisation-wide activation keys via the eOpen portal and record them in the central license inventory. All installations must be tracked in the online licence account and reassessed annually; do not redistribute activation keys outside authorised IT personnel.

13. Complex comparison: Provide three pros and three cons of per-server mode compared with per-seat (per-user) mode for an organisation with remote workers and multiple servers.
    Solution: Pros of per-server mode: simpler for very small setups; direct control by server instance; may be appropriate if simultaneous connections are predictable. Cons: requires separate license pools per server, denies users when limits hit, not flexible for remote workers who access multiple servers. Per-seat (User CAL) pros: flexible for remote workers and multi-server access; easier to manage per-person entitlements. Cons: may require many user licenses and initial assignment tracking; not optimal when many users share few devices.

14. Design exercise: Describe how you would document Terminal Services licensing for an audit (what to record and why).
    Solution: Record number of TS CALs purchased, whether they are User or Device TS CALs, assignment mapping to users or devices, dates of purchase, license keys, and evidence of installations using TS. Also include Windows Server CAL records because TS CALs are in addition to Windows Server CALs. This shows compliance and explains entitlements to auditors.

15. Advanced synthesis: The organisation runs legacy servers, a mix of virtual instances, and external partners needing occasional authenticated access. Give a prioritized 5-step action plan (brief bullets) to ensure licensing compliance with minimal immediate cost.
    Solution: (1) Audit current server instances (physical and virtual) and processors to identify applications licensed per-processor vs CAL-based. (2) Inventory active users/devices and frequency of external authenticated access. (3) Check TechSoup Stock and vendor donation programs for discounted volume licenses and eOpen for keys. (4) For internal staff who use multiple devices, buy User CALs; for shared machines buy Device CALs; for occasional external authenticated users buy a small number of User CALs rather than a costly ECL. (5) Purchase TS CALs if Terminal Services are used and management MLs if using System Center; document all licenses centrally and set review schedule.

Exam 5 — Applied problems + role-play + math (practical procurement)
- Easy: 5 direct short answers or small calculations.
- Medium: 5 procurement checklists, negotiation points, or short calculations.
- Hard: 5 multi-part problems including math, recommendation, and justification.

Solutions after each task.

Exam 5
Easy
1. True/False: Shareware typically allows indefinite unlimited use without payment.
   Solution: False — shareware is trial software; you usually must pay after a trial period.

2. Short: What website is specifically mentioned as a place to locate Microsoft Volume license keys when you obtained software through TechSoup?
   Solution: eOpen.

3. Short: Which license type covers authenticated external users but is usually more expensive than individual User CALs?
   Solution: External Connector License (ECL).

4. Small calc: If an organisation buys 100 User CALs with an admin fee of £1 each, what is the admin fee total (based on the example)?
   Solution: £100.

5. Small calc: Using the example admin fees, how many User CALs have equivalent admin-fee cost to one ECL at £76?
   Solution: 76 User CALs (76 × £1 = £76).

Medium
6. Procurement checklist (list five items): What five checks should IT perform before acquiring server-based software?
   Solution: (1) Check whether the software requires processor licenses or CALs; (2) Determine number of internal users/devices and external authenticated users; (3) Decide between User vs Device CALs based on usage; (4) Check TechSoup or vendor donation programs for discounts and eOpen for keys; (5) Identify additional license needs (TS CALs, management MLs, Enterprise CAL add-ons) and virtualization instance rules.

7. Negotiation point: You are negotiating a volume licensing deal and the vendor offers per-device CALs at lower unit price than per-user CALs. What operational questions should you ask to decide which to accept?
   Solution: Ask whether devices are shared by multiple users (shift work), how many devices each user uses, mobility/remote access patterns (BYOD), projected turnover, whether devices are centrally managed, and whether lower unit price offsets increased number of devices vs users.

8. Calculation: A nonprofit wants to cover 200 external authenticated users. Which is likely cheaper based solely on admin fees from the text — buying 200 User CALs at £1 admin each, or one ECL at £76 admin? Which is cheaper and by how much (admin fees only)?
   Solution: 200 User CALs admin fees = £200; one ECL admin = £76. ECL is cheaper by £124 in admin fees alone. (But total license cost not provided; must consider full price.)

9. Short: For System Center Configuration Manager, what license type is required for each desktop managed?
   Solution: Client management license (ML).

10. Short: Does the server software enforce CAL counts by refusing connections in per-seat mode?
    Solution: No — the server software generally cannot refuse access on licensing grounds except in per-server mode where simultaneous connections are enforced.

Hard
11. Multi-part licensing math: Your organisation runs:
    - One Windows Server (single instance) in per-server mode with 40 CALs purchased.
    - 120 employees, each using two devices.
    - 10 external authenticated users.
   a) If the organisation remains in per-server mode, what is the maximum number of authenticated internal users who can access the server simultaneously?
   b) If the organisation switches to per-seat (User CAL) mode and buys 120 User CALs, how does that change simultaneous access constraints across multiple devices?
   c) Which mode is likely better for the organisation and why?
   Solutions:
   a) In per-server mode with 40 CALs, only 40 authenticated users can access simultaneously—regardless of total employees.
   b) In per-seat mode with 120 User CALs, up to 120 distinct users can have access (each user can connect from multiple devices). There is no per-server simultaneous connections cap tied to a specific server instance in this mode (aside from normal resource constraints).
   c) Per-seat (User CAL) mode is likely better because each employee uses multiple devices; 120 User CALs allow broader access than the 40 simultaneous limit in per-server mode.

12. Complex scenario with virtualization: Your charity runs two hosts:
    - Host A: 2 physical processors, runs 4 virtual instances of Windows Server for different services.
    - Host B: 1 physical processor, runs 2 virtual instances.
   The vendor’s licensing rule (as in text) is: "Every installation creates an instance; the number of instances permitted per license varies by product." Given only the information in the text (no product-specific instance counts), what questions must you ask the vendor or check in product volume-licensing briefs before deciding on license purchases? Provide at least six specific items.
   Solution: Questions to ask/check: (1) Does the specific Windows Server edition permit multiple virtual instances on a single license and how many? (2) Are processor licenses required per physical processor or per core? (3) If licensing by processor, do processor licenses cover virtual instances on that host? (4) Are CALs still required for users/devices when virtual instances are used? (5) Are there special virtualization licensing terms for the server edition in use (e.g., Datacenter vs Standard)? (6) Are there management ML implications for VMs (System Center rules)? Also check whether measuring instances counts per physical host or per VM and whether any license mobility or virtualization rights apply.

13. Role-play negotiation: You are the IT manager of a small nonprofit with 35 authenticated external partner users and 110 internal users. Using the ECL/admin fee example and other text points, prepare a short argument (3–4 sentences) for acquiring individual User CALs for external partners rather than an ECL.
   Solution (model): Because the ECL has a high administrative fee and is intended mainly for very large external user counts, with only 35 external authenticated partners the ECL is unlikely to be cost-effective (admin-wise a single ECL equals 76 User CAL admin fees). Buying 35 external User CALs keeps costs proportional to actual usage, minimizes upfront expense, and avoids paying for a blanket connector license that still requires CALs for employees. Therefore purchase User CALs for external partners and monitor growth.

14. Combined licensing pitfalls: List five distinct mistakes an organisation might make when interpreting vendor licensing language (based on the nuances in the text), and give one-sentence advice to avoid each.
   Solution:
   - Mistake: Confusing “free” with “freeware” — Advice: Check rights to source, modify, and redistribute, not just price.
   - Mistake: Assuming processor licensing always eliminates CALs — Advice: Confirm product-specific rules; processor licensing often removes need for CALs but verify.
   - Mistake: Buying Device CALs when most staff use multiple devices — Advice: Analyse device-sharing patterns and count devices vs users before buying.
   - Mistake: Assuming anonymous website users require CALs — Advice: Remember anonymous unauthenticated users do not require CALs for IIS.
   - Mistake: Overlooking Terminal Services TS CALs — Advice: Check whether TS is used and plan for TS CALs in addition to Windows Server CALs.

15. Final case (recommendation + justification): A nonprofit wants to host a new internal web application on Windows Server for all staff (200 people, half often remote) and occasional authenticated external clients (~150). They have limited budget and want simplest administration. Provide a recommended licensing approach (concise list of license types and counts or options) and justify in 4–5 lines using principles from the text.
   Solution: Recommended approach: Purchase 200 User CALs for internal staff (one per person) so remote staff can access from multiple devices; purchase 150 User CALs for authenticated external clients if needed (or evaluate an ECL only if external authenticated users will exceed ~76 and full ECL pricing is competitive), ensure any Terminal Services usage has TS CALs for relevant users/devices, and check TechSoup donation programs for possible donated volume licenses and eOpen keys. Justification: User CALs suit many users who use multiple devices; ECL is more expensive and only makes sense at larger scales; TechSoup can reduce costs; TS and System Center MLs are additional requirements to verify.

— End of all 5 exams.

If you want, I can:
- Convert any one exam into a printable PDF format.
- Randomize question order and produce separate answer keys for each student.
- Generate a short rubric for grading long/essay responses.
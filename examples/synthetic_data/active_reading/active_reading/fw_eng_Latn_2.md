# Active-Reading Interleaved Version (English)

Below I simulate an active reader working through the document step by step: a short "Before Reading" prep, then the original text interleaved with annotations, margin thoughts, questions, brief pause-summaries, and finally "After Reading" reflection, review, and application ideas.

---

## BEFORE READING

Preview (skim):  
- Headings / structure spotted: introduction about CTComms, overview of software licenses, Free vs Proprietary, Free/Open Source distinctions, copyleft/public domain, shareware/freeware, EULAs, volume licensing, client/server licensing (CALs, Device vs User), special licensing cases (ECL, TS, System Center, virtualization), author bio, copyright.  
- Repeated vendor focus: Microsoft examples, TechSoup resources.

Set a purpose (why I'm reading):  
- Understand basics of software licensing and practical licensing options for not-for-profits, especially Microsoft server/client licensing and volume licensing tips.

Activate prior knowledge:  
- I know that "free" can mean freedom (FSF) or free of price (freeware). Microsoft uses CALs; virtualization complicates licensing; EULAs often ignored; nonprofits can get donations/discounts via TechSoup.

---

## DURING READING (document text followed by active annotations)

CTComms sends on average 2 million emails monthly on behalf of over 125 different charities and not for profits.

> Annotation — Key data point: CTComms scale = 2M emails/month; serves 125+ charities.  
> Thoughts: This sets context for why licensing and reliable software matter for charities (high volume, many orgs).  
> Question: Is CTComms the article publisher or an example? (Probably context/author source.)

Take the complexity of technology and stir in the complexity of the legal system and what do you get? Software licenses! If you've ever attempted to read one you know how true this is, but you have to know a little about software licensing even if you can't parse all of the fine print.

> Annotation — Main idea: Software licenses are intersection of tech + law and are complex.  
> Thoughts: Yep — I often skip EULAs; but some terms (e.g., server CALs) have major org impacts.  
> Pause & summary: Expect overview of essentials to help non-experts.

By: Chris Peters  
March 10, 2009

A software license is an agreement between you and the owner of a program which lets you perform certain activities which would otherwise constitute an infringement under copyright law. The software license usually answers questions such as:

> Annotation — Definition: license = permission contract to avoid copyright infringement.  
> Question: The sentence ends with "answers questions such as:" — but the list seems missing here; check next lines for examples.

The price of the software and the licensing fees, if any, are sometimes discussed in the licensing agreement, but usually it's described elsewhere.

> Annotation — Note: Price may be in license but often separate.  
> Thought: Administrative details (prices, fees) often in purchase docs not license text.

If you read the definitions below and you're still scratching your head, check out Categories of Free and Non-Free Software which includes a helpful diagram.

> Annotation — Resource suggestion: "Categories of Free and Non-Free Software" for diagram.  
> Action: Flag to check linked resource if I need visual clarification.

Free vs Proprietary:  
When you hear the phrase "free software" or "free software license," "free" is referring to your rights and permissions ("free as in freedom" or "free as in free speech"). In other words, a free software license gives you more rights than a proprietary license. You can usually copy, modify, and redistribute free software without paying a fee or obtaining permission from the developers and distributors. In most cases "free software" won't cost you anything, but that's not always the case – in this instance the word free is making no assertion whatsoever about the price of the software. Proprietary software puts more restrictions and limits on your legal permission to copy, modify, and distribute the program.

> Annotation — Key distinction: "Free" = freedom (rights), not necessarily price. Proprietary = restricted rights.  
> Underline mentally: copy, modify, redistribute = core freedoms of free software.  
> Thought: Important to remember when evaluating license text — price ≠ freedom.

Free, Open-Source or FOSS?  
In everyday conversation, there's not much difference between "free software," "open source software," and "FOSS (Free and Open-Source Software)." In other words, you'll hear these terms used interchangeably, and the proponents of free software and the supporters of open-source software agree with one another on most issues. However, the official definition of free software differs somewhat from the official definition of open-source software, and the philosophies underlying those definitions differ as well. For a short description of the difference, read Live and Let License. For a longer discussion from the "free software" side, read Why Open Source Misses the Point of Free Software. For the "open-source" perspective, read Why Free Software is Too Ambiguous.

> Annotation — Note: Terms often used interchangeably but have philosophical differences. Useful links recommended.  
> Question: Do I need to read those essays now? Probably not unless I care about ideology; practical differences are limited for nonprofit procurement.

Public domain and copyleft.  
These terms refer to different categories of free, unrestricted licensing. A copyleft license allows you all the freedoms of a free software license, but adds one restriction. Under a copyleft license, you have to release any modifications under the same terms as the original software. In effect, this blocks companies and developers who want to alter free software and then make their altered version proprietary. In practice, almost all free and open-source software is also copylefted. However, technically you can release "free software" that isn't copylefted. For example, if you developed software and released it under a "public domain" license, it would qualify as free software, but it isn't copyleft. In effect, when you release something into the public domain, you give up all copyrights and rights of ownership.

> Annotation — Definitions:  
> - Copyleft = must distribute modifications under same license (reciprocity).  
> - Public domain = no copyright, no copyleft.  
> Thought: Copyleft prevents closed forks; public domain allows proprietary forks. Useful when choosing license for projects.

Shareware and freeware.  
These terms don't really refer to licensing, and they're confusing in light of the discussion of free software above. Freeware refers to software (usually small utilities at sites such as Tucows.com) that you can download and install without paying. However, you don't have the right to view the source code, and you may not have the right to copy and redistribute the software. In other words, freeware is proprietary software. Shareware is even more restrictive. In effect, shareware is trial software. You can use it for a limited amount of time (usually 30 or 60 days) and then you're expected to pay to continue using it.

> Annotation — Important practical note: freeware = free to use (often proprietary); shareware = trial.  
> Thought: Distinguish these from "free software" (freedom). Good to clarify to stakeholders who might think "free" equals OSS.

End User Licensing Agreement (EULA).  
When you acquire software yourself, directly from a vendor or retailer, or directly from the vendor's Web site, you usually have to indicate by clicking a box that you accept the licensing terms. This "click-through" agreement that no one ever reads is commonly known as a EULA. If you negotiate a large purchase of software with a company, and you sign a contract to seal the agreement, that contract usually replaces or supersedes the EULA.

> Annotation — EULA = click-through contract; individual retail EULA can be superseded by negotiated contract for large purchases.  
> Question: For nonprofits buying donated licenses, does the donation agreement override EULA? Likely vendor terms still bind.

Most major vendors of proprietary software offer some type of bulk purchasing and volume licensing mechanism. The terms vary widely, but if you order enough software to qualify, the benefits in terms of cost and convenience are significant. Also, not-for-profits sometimes qualify for it with very small initial purchases.

> Annotation — Volume licensing = cost & admin benefits; nonprofits may qualify.  
> Action: Flag volume licensing as a key area for cost savings for charities.

Some of the benefits of volume licensing include:  
- Lower cost. As with most products, software costs less when you buy more of it.  
- Ease of installation. Without volume licenses, you usually have to enter a separate activation code (also known as a product key or license key) for each installed copy of the program. On the other hand, volume licenses provide you with a single, organisation-wide activation code, which makes it much easier to find when you need to reinstall the software.  
- Easier tracking of licenses. Keeping track of how many licenses you own, and how many copies you've actually installed, is a tedious, difficult task. Many volume licensing programs provide an online account which is automatically updated when you obtain or activate a copy of that company's software. These accounts can also coordinate licensing across multiple offices within your organisation.

> Annotation — Bullet summary of benefits: cost, activation simplicity, license tracking.  
> Thought: For an org running many machines, switching to volume licensing could reduce admin time.

To learn more about volume licensing from a particular vendor, check out some of the resources below:  
Qualified not-for-profits and libraries can receive donated volume licenses for Microsoft products through TechSoup. For more information, check out our introduction to the Microsoft Software Donation Program, and the Microsoft Software Donation Program FAQ. For general information about the volume licensing of Microsoft software, see Volume Licensing Overview.

> Annotation — Resource highlight: TechSoup for nonprofits; Microsoft volume licensing docs.  
> Action: If I'm in a nonprofit, visit TechSoup first.

If you get Microsoft software from TechSoup or other software distributors who work with not-for-profits, you may need to go to the eOpen Web site to locate your Volume license keys. For more information, check out the TechSoup Donation Recipient's Guide to the Microsoft eOpen Web Site.

> Annotation — Practical step: Use eOpen site to find volume license keys; TechSoup guide available.  
> Thought: Keep login/credentials for these portals secure and documented.

Always check TechSoup Stock first to see if there's a volume licensing donation program for the software you're interested in. If TechSoup doesn't offer that product or if you need more copies than you can find at TechSoup, search for "volume licensing not-for-profits software" or just "not-for-profits software." For example, when we have an inventory of Adobe products, qualifying and eligible not-for-profits can obtain four individual products or one copy of Creative Suite 4 through TechSoup. If we're out of stock, or you've used up your annual Adobe donation, you can also check TechSoup's special Adobe donation program and also Adobe Solutions for Nonprofits for other discounts available to not-for-profits. For more software-hunting tips, see A Quick Guide to Discounted Software Programs.

> Annotation — Tip: Check TechSoup Stock and alternative vendor nonprofit programs (Adobe, etc.) — stock may be limited.  
> Action: Create a checklist for nonprofit software procurement: 1) TechSoup Stock, 2) vendor nonprofit programs, 3) search web.

Pay close attention to the options and licensing requirements when you acquire server-based software. You might need two different types of license – one for the server software itself, and a set of licenses for all the "clients" accessing the software. Depending on the vendor and the licensing scenario, "client" can refer either to the end users themselves (for example, employees, contractors, clients, and anyone else who uses the software in question) or their computing devices (for example, laptops, desktop computers, smartphones, PDAs, etc.). We'll focus on Microsoft server products, but similar issues can arise with other server applications.

> Annotation — Core warning: server apps often require server license + client licenses (users or devices).  
> Thought: This is where cost surprises often happen; count users/devices carefully.

Over the years, Microsoft has released hundreds of server-based applications, and the licensing terms are slightly different for each one. Fortunately, there are common license types and licensing structures across different products. In other words, while a User CAL (Client Access License) for Windows Server is distinct from a User CAL for SharePoint Server, the underlying terms and rights are very similar. The TechSoup product pages for Microsoft software do a good job of describing the differences between products, so we'll focus on the common threads in this article.

> Annotation — Note: CAL types similar across products; TechSoup pages helpful for product differences.  
> Action: If uncertain, read TechSoup product pages for specifics.

Moreover, Microsoft often lets you license a single server application in more than one way, depending on the needs of your organisation. This allows you the flexibility to choose the licenses that best reflect your organisation's usage patterns and thereby cost you the least amount of money. For example, for Windows Server and other products you can acquire licenses on a per-user basis (for example, User CALs) or per-device basis (for example, Device CALs).

> Annotation — Key choice: User CALs vs Device CALs — choose to match usage patterns to save cost.  
> Pause & summary: Assess whether your org has many users on few devices (Device CALs) or many devices per user (User CALs).

The license required to install and run most server applications usually comes bundled with the software itself. So you can install and run most applications "out of the box," as long as you have the right number of client licenses (see the section below for more on that). However, when you're running certain server products on a computer with multiple processors, you may need to get additional licenses. For example, if you run Windows Server 2008 DataCenter edition on a server with two processors, you need a separate license for each processor. SQL Server 2008 works the same way. This type of license is referred to as a processor license. Generally you don't need client licenses for any application that's licensed this way.

> Annotation — Processor licensing: some editions require licensing per CPU rather than CALs; client licenses often not required in that model.  
> Question: Consider VM/virtual cores — how are processors counted? Author later mentions virtualization — flag for reading.

Client Licenses for Internal Users  
Many Microsoft products, including Windows Server 2003 and Windows Server 2008, require client access licenses for all authenticated internal users (for example, employees, contractors, volunteers, etc.). On the other hand, SQL Server 2008 and other products don't require any client licenses. Read the product description at CTXchange if you're looking for the details about licensing a particular application.

> Annotation — Core rule: Authenticated internal users generally need CALs for some products; others don't. Check CTXchange for details.  
> Action: Generate a user list (employees/contractors/volunteers) to estimate CAL needs.

User CALs: User CALs allow each user access to all the instances of a particular server product in an organisation, no matter which device they use to gain access. In other words, if you run five copies of Windows Server 2008 on five separate servers, you only need one User CAL for each person in your organisation who access those servers (or any software installed on those servers), whether they access a single server, all five servers, or some number in between. Each user with a single CAL assigned to them can access the server software from as many devices as they want (for example, desktop computers, laptops, smartphones, etc.). User CALs are a popular licensing option.

> Annotation — User CALs = license per person; good when users use many devices.  
> Reflection: For modern workplaces with BYOD and mobile access, User CALs often make sense.

Device CALs: Device CALs allow access to all instances of a particular server application from a single device (for example, a desktop computer, a laptop, etc.) in your organisation. Device CALs only make sense when multiple employees use the same computer. For example, in 24-hour call centres different employees on different shifts often use the same machine, so Device CALs make sense in this situation.

> Annotation — Device CALs = license per device; good for shared devices/shift work.  
> Action: For call centers or public kiosks, prefer Device CALs.

Choosing a licensing mode for your Windows Server CALs: With Windows Server 2003 and Windows Server 2008, you use a CAL (either a User CAL or a Device CAL) in one of two licensing modes: per seat or per server. You make this decision when you're installing your Windows Server products, not when you acquire the CALs. The CALs themselves don't have any mode designation, so you can use either a User CAL or a Device CAL in either mode. Per seat mode is the default mode, and the one used most frequently. The description of User CALs and Device CALs above describes the typical per seat mode. In "per server" mode, Windows treats each license as a "simultaneous connection." In other words, if you have 40 CALs, Windows will let 40 authenticated users have access. The 41st user will be denied access. However, in per server mode, each CAL is tied to a particular instance of Windows Server, and you have to acquire a new set of licenses for each new server you build that runs Windows. Therefore, per server mode works for some small organisations with one or two servers and limited access requirements.

> Annotation — Two modes: per seat (default) vs per server (simultaneous connections, server-tied).  
> Thought: Per server mode useful for small orgs with few servers; per seat better for flexibility across multiple servers.

You don't "install" client licenses the way you install software. There are ways to automate the tracking of software licenses indirectly, but the server software can't refuse access to a user or device on licensing grounds. The licenses don't leave any "digital footprint" that the server software can read. An exception to this occurs when you license Windows Server in per server mode. In this case, if you have 50 licenses, the 51st authenticated user will be denied access (though anonymous users can still access services).

> Annotation — Important: CALs are an entitlement/contract, not enforced by software (except per-server mode). Keep accurate records.  
> Action: Implement license inventory and audit trail (spreadsheet or license management tool).

Some key points to remember about client licensing:

> Annotation — Looks like summary bullets follow — I'll pay attention for exceptions.

The licensing scenarios described in this section arise less frequently, and are too complex to cover completely in this article, so they're described briefly below along with more comprehensive resources.

> Annotation — Author indicates complexity and points to external deeper resources. Good to consult vendor docs for special cases.

You don't need client licenses for anonymous, unauthenticated external users. In other words, if someone accesses your Web site, and that site runs on Internet Information Server (IIS), Microsoft's Web serving software, you don't need a client license for any of those anonymous users.

> Annotation — Rule: Anonymous web visitors do NOT require CALs.  
> Thought: That prevents paying per website visitor — good to know.

If you have any authenticated external users who access services on your Windows-based servers, you can obtain CALs to cover their licensing requirements. However, the External Connector License (ECL) is a second option in this scenario. The ECL covers all use by authenticated external users, but it's a lot more expensive than a CAL, so only get one if you'll have a lot of external users. For example, even if you get your licenses through the CTXchange donation program, an ECL for Windows Server 2008 has an £76 administrative fee, while a User CAL for Windows Server 2008 carries a £1 admin fee. If only a handful of external users access your Windows servers, you're better off acquiring User CALs. Also, an ECL only applies to external users and devices. In other words, if you have an ECL, you still have to get a CAL for all employees and contractors.

> Annotation — ECL = covers all authenticated external users (expensive); compare cost vs buying User CALs individually.  
> Action: Estimate number of authenticated external users before choosing ECL.

Even though Terminal Services (TS) is built into Windows Server 2003 and 2008, you need to get a separate TS CAL for each client (i.e. each user or each device) that will access Terminal Services in your organisation. This TS license is in addition to your Windows Server CALs.

> Annotation — TS CALs are extra on top of Windows CALs — dual licensing required.  
> Action: If using Remote Desktop/Terminal Services, add TS CALs to budget.

Microsoft's System Centre products (a line of enterprise-level administrative software packages) use a special type of license known as a management license (ML). Applications that use this type of licensing include System Center Configuration Manager 2007 and System Center Operations Manager 2007. Any desktop or workstation managed by one of these applications needs a client management license. Any server managed by one of these applications requires a server management license, and there are two types of server management licenses – standard and enterprise. You need one or the other but not both. There are also special licensing requirements if you're managing virtual instances of Windows operating systems. For more information, see TechSoup's Guide to System Center Products and Licensing and Microsoft's white paper on Systems Center licensing.

> Annotation — System Center uses MLs (client & server); standard vs enterprise server MLs (choose one). Virtualization imposes special rules.  
> Action: If deploying System Center, consult vendor licensing whitepaper and TechSoup guide.

Some Microsoft server products have two client licensing modes, standard and enterprise. As you might imagine, an Enterprise CAL grants access to more advanced features of a product. Furthermore, with some products, such as Microsoft Exchange, the licenses are additive. In other words, a user needs both a Standard CAL AND an Enterprise CAL in order to access the advanced features. See Exchange Server 2007 Editions and Client Access Licenses for more information.

> Annotation — Note: Some CALs are additive (Standard + Enterprise). Check product-specific rules (Exchange example).  
> Thought: Additive licensing increases cost — verify needed features before buying.

With virtualisation technologies, multiple operating systems can run simultaneously on a single physical server. Every time you install a Microsoft application, whether on a physical hardware system or a virtual hardware system, you create an "instance" of that application. The number of "instances" of particular application that you can run using a single license varies from product to product. For more information see the Volume Licensing Briefs, Microsoft Licensing for Virtualization and the Windows Server Virtualization Calculator. For TechSoup Stock products, see the product description for more information.

> Annotation — Virtualization: count instances per license rules; varies by product. Use Microsoft calculators/docs.  
> Action: Use Windows Server Virtualization Calculator to model costs for VMs.

There are a lot of nuances to Microsoft licensing, and also a lot of excellent resources to help you understand different scenarios.

> Annotation — Final note of caution: consult detailed resources for complex scenarios.

About the Author:  
Chris is a former technology writer and technology analyst for TechSoup for Libraries, which aims to provide IT management guidance to libraries. His previous experience includes working at Washington State Library as a technology consultant and technology trainer, and at the Bill and Melinda Gates Foundation as a technology trainer and tech support analyst. He received his M.L.S. from the University of Michigan in 1997.

> Annotation — Author credibility: experience in tech guidance for libraries/nonprofits — relevant to audience.

Originally posted here.  
Copyright © 2009 CompuMentor. This work is published under a Creative Commons Attribution-NonCommercial-NoDerivs 3.0 License.

> Annotation — Licensing of the article: CC BY-NC-ND 3.0 — can share with attribution, noncommercial, no derivatives.

The latest version of Microsoft Office Professional Plus is an integrated collection of programs, servers, and services designed to work together to enable optimised information work.

> Annotation — Closing sentence: highlights Office Professional Plus as integrated suite. Might be promotional/transition.

---

## AFTER READING

Summarize main ideas (brief, from memory):  
- Software licenses define legal permissions; "free" refers to rights, not price.  
- Distinctions: free software vs open source vs proprietary; copyleft vs public domain; freeware/shareware are often proprietary.  
- EULAs are common; enterprise purchases use negotiated contracts.  
- Volume licensing (esp. Microsoft) offers cost/admin benefits for nonprofits; TechSoup is a key resource.  
- Server software often requires both server license and client access licenses (CALs); choose User vs Device CALs to match usage.  
- Special cases: processor licenses, External Connector Licenses (ECL), Terminal Services CALs, System Center management licenses, virtualization instance rules, additive CALs (Standard + Enterprise).  
- Always consult vendor-specific documentation; licensing is nuanced.

Review your annotations (quick checklist extracted):  
- Check TechSoup Stock and vendor nonprofit programs first.  
- Count authenticated internal users and shared devices to choose User vs Device CALs.  
- Consider virtualization instance counts and processor-based licensing.  
- Beware additive CALs and extra TS CALs for Terminal Services.  
- Use vendor calculators/guides for complex scenarios.

Make connections to other knowledge / experience:  
- This matches my prior understanding that "free" is ambiguous and that Microsoft licensing is complex and can cause budget surprises. Volume licensing and donation programs are crucial for nonprofits. Virtualization adds licensing complexity I've seen in server consolidation projects.

Generate remaining questions (things I'm still wondering / would ask the author or vendor):  
- How does Microsoft now count cores/processors for licensing in modern (post-2009) editions? (Licensing has changed over time.)  
- For small nonprofits with hybrid cloud/on-prem setups, what is the most cost-effective mix of licenses?  
- How are subscription models (Office 365 / Microsoft 365) compared with on-prem CALs/donations? (Not covered — article predates cloud shifts.)  
- For donated licenses via TechSoup, what are ongoing support/upgrade limitations?

Reflect on application — How I might use this:  
- If advising a nonprofit, create a licensing checklist: inventory users/devices, identify server apps that need CALs, evaluate TechSoup options, model costs for User vs Device vs processor-based licensing, and check for additive CALs/TS/ML needs.  
- Keep documentation of donated volume license keys and TechSoup/eOpen credentials.  
- Schedule a license audit before major purchases or virtualization projects.

Final quick action items (practical next steps):  
- Inventory: list all authenticated users and shared devices.  
- Visit TechSoup and CTXchange product pages relevant to current software needs.  
- If planning virtualization, run vendor virtualization license calculator and consult vendor whitepapers.  
- If Terminal Services or System Center are in play, budget for additional CALs/MLs.

---

If you'd like, I can:
- Produce a one-page nonprofit licensing checklist based on this article.  
- Convert the key licensing choices (User vs Device, per-seat vs per-server, processor vs CAL) into a decision flowchart you can use when buying/licensing software.
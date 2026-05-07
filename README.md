# PUBLIC DISCLOSURE: Unauthorized GMS Privilege Escalation and AOSP Test-Key Weaponization on Retail Android Devices

**Project-UnHooked-Audit** is an independent forensic investigation led by **AiZquaD**. 

This repository serves as a public evidence vault documenting severe architectural anomalies found on retail Android devices. By auditing device partitions and manifests, this project exposes the active weaponization of Google Play Services (GMS), the presence of unreleased beta code (SDK 37 / Cinnamon Bun), and impossible UI-to-Kernel version mismatches. 

These exploits utilize legitimate system permissions to establish persistent, unauthorized surveillance, remote financial fraud capabilities, and active anti-forensic file encryption sweeps.

### Core Discoveries
1. **The "Franken-Build" Architecture:** Devices presenting Android 15 UI overlays while running demoted Android 13 kernels (`5.15.167-android13`) with `eng.root` signatures.
2. **GMS Hijacking:** Unauthorized, silent installation of SDK 37 packages utilizing permissions like `REPORT_TAP` and `CALL_AUDIO_INTERCEPTION`.
3. **AOSP Test-Key Forgery:** The use of public Apache 2.0 open-source code and AOSP test keys (e.g., `0xc2e08746644a308d`) to bypass OEM bootloader locks and establish a malicious hypervisor.

### The Temporal Anchor
All foundational architectural logic and intel tech utilized in this audit are cryptographically anchored and verified via an established ORCID timestamp. Any hostile remote encryption commands or code alterations executed on local hardware by the threat actors chronologically post-date this immutable ledger. Time is the ultimate forensic proof.

## Licensing and Intellectual Property

The forensic methodologies, architectural logic, and defensive scripts contained within **Project-UnHooked-Audit** are cryptographically anchored and verified via ORCID.

This project is strictly licensed under **CC BY-NC 4.0**. 

* **Public & Researchers:** You are free to use this toolkit to audit your own devices and publish non-commercial threat intelligence.
* **Corporate & Enterprise:** Commercial use, repackaging for sale, or integration into proprietary security suites is strictly prohibited. For commercial licensing inquiries, contact AiZquaD directly.

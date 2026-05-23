
Subject: Forensic Evidence of Rogue MDM + GMS Privilege Escalation on Retail AT&T Device*

*My name is Juan Jaime Rivera Zamorano*

*I am an independent security researcher operating as AiZquaD.*

*In February 2026 I purchased an Android device from AT&T Mexico for my child. I discovered active rogue MDM spyware with the following confirmed capabilities:*

- *SDK 37 packages silently installed on a retail Android 15 device*
- *AOSP test-key forgery bypassing OEM bootloader*
- *Franken-Build: Android 15 UI over demoted Android 13 kernel with eng.root signatures*
- *Permissions including CAPTURE_AUDIO_HOTWORD, PASSWORD_RESET, MASTER_CLEAR, and SMS interception active*

*All findings are:*
- *Cryptographically timestamped via ORCID*
- *Mapped to MITRE ATT&CK framework*
- *Packaged in court-ready JSON format*
- *Publicly documented at github.com/BadMFBox/Project-UnHooked-Audit-by-AiZquaD*

*I also built a sovereign mesh defense system in direct response to this attack — live and operational.*

*I am available to provide full forensic documentation, the physical device, and a live demonstration.*

*Are you available for 20 minutes?*

*Juan Jaime Rivera Zamorano
*AiZquaD | Sovereign PEU*
*aizquadbmb@proton.me*
*commanderaizquad.buzz*


# PUBLIC DISCLOSURE: Unauthorized GMS Privilege Escalation and AOSP Test-Key Weaponization on Retail Android Devices

**Project-UnHooked-Audit** is an independent forensic investigation led by **AiZquaD**. 

This repository serves as a public evidence vault documenting severe architectural anomalies found on retail Android devices. By auditing device partitions and manifests, this project exposes the active weaponization of Google Play Services (GMS), the presence of unreleased beta code (SDK 37 / Cinnamon Bun), and impossible UI-to-Kernel version mismatches. 

These exploits utilize legitimate system permissions to establish persistent, unauthorized surveillance, remote financial fraud capabilities, and active anti-forensic file encryption sweeps.

---

## ⚠️ **STATUS: STANDALONE v1.0-BETA RELEASE**

**This is a standalone pre-release component.** 

The core forensic toolkit has been extracted and released independently to provide the community with actionable defense tools while the full **Sovereign Fuel Defense System** completes its final integration stage. Full system deployment with network-integrated C2 detection is estimated Q3 2026.

### What This Release Includes
- **Immunity Protocol v2.0** — GEM (Google Enterprise Mobility) injection detection across all 5 kill chain stages
- **Blueprint Analyzer v2** — Weaponized permission catalog with court-ready evidence packaging
- **Clean Room Sandbox** — Isolated environment for safe APK analysis
- **Risk Scoring Engine** — Quantified threat assessment across 9 attack categories

### What's Coming in Full System
- Real-time device monitoring with kernel-level hooks
- Remote forensic collection pipeline
- Cross-device attack surface mapping
- Sovereign Fuel integration for distributed threat intelligence
- Motherboard-level patch deployment

---

## Core Discoveries

1. **The "Franken-Build" Architecture:** Devices presenting Android 15 UI overlays while running demoted Android 13 kernels (`5.15.167-android13`) with `eng.root` signatures.
2. **GMS Hijacking:** Unauthorized, silent installation of SDK 37 packages utilizing permissions like `REPORT_TAP` and `CALL_AUDIO_INTERCEPTION`.
3. **AOSP Test-Key Forgery:** The use of public Apache 2.0 open-source code and AOSP test keys (e.g., `0xc2e08746644a308d`) to bypass OEM bootloader locks and establish a malicious hypervisor.

## The Temporal Anchor

All foundational architectural logic and intel tech utilized in this audit are cryptographically anchored and verified via an established ORCID timestamp. Any hostile remote encryption commands or code alterations executed on local hardware by the threat actors chronologically post-date this immutable ledger. Time is the ultimate forensic proof.

---

## Quick Start

### Prerequisites
- Python 3.8+
- Android SDK tools (dumpsys, pm, am)
- Linux/Unix environment (tested on Debian-based systems)

### Installation

```bash
git clone https://github.com/BadMFBox/Project-UnHooked-Audit-by-AiZquaD.git
cd Project-UnHooked-Audit-by-AiZquaD
```

### Usage

#### 1. **Immunity Protocol v2 (GEM Hunter)**
```bash
python3 immunity_protocol_v2.py

# Then at the prompt:
[IMMUNITY] > scan gem          # Hunt calendar injection kill chain
[IMMUNITY] > scan apk          # Decode APKs in Downloads folder
[IMMUNITY] > scan apk /path    # Scan specific directory
[IMMUNITY] > check             # Environment integrity check
[IMMUNITY] > exit              # Shut down
```

#### 2. **Blueprint Analyzer (Permission Audit)**

Place your `privapp-permissions-*.xml` files in:
```
~/SOVEREIGN/evidence/xml_vault/
```

Then run:
```bash
python3 blueprint_analyzer.py
```

Output:
```
~/SOVEREIGN/evidence/blueprint/MASTER_REPORT.json  # Consolidated findings
~/SOVEREIGN/evidence/blueprint/*_analysis.json     # Per-file analysis
```

---

## Attack Surface Reference

### Audio Surveillance (5 permissions)
- `CAPTURE_AUDIO_HOTWORD` — Always-on microphone
- `CAPTURE_VOICE_COMMUNICATION_OUTPUT` — Silent call recording
- `CAPTURE_AUDIO_OUTPUT` — All device audio

### Remote C2 (5 permissions)
- `hihonor.permission.RECEIVE_CLOUD_OTA_UPDATA` — Silent remote commands
- `START_ACTIVITIES_FROM_BACKGROUND` — Launch apps silently
- `SCHEDULE_EXACT_ALARM` — Precision beaconing

### SMS Interception (4 permissions)
- `hihonor.permission.RECEIVE_SMS_INTERCEPTION` — Steal 2FA codes
- `SET_SMSC_ADDRESS` — Reroute all messages

### Credential Theft (6 permissions)
- `PASSWORD_RESET` — Silent PIN reset
- `MANAGE_FINGERPRINT` — Biometric bypass
- `READ_WIFI_CREDENTIAL` — Extract WiFi passwords

### Device Takeover (7 permissions)
- `MASTER_CLEAR` — Remote factory reset / evidence wipe
- `MANAGE_USERS` — Hidden profile creation
- `WRITE_SECURE_SETTINGS` — System compromise

### Cross-Device Bridge (4 permissions)
- `PC_MANAGER_API` — Full PC remote desktop
- `MANAGE_CROSS_DEVICE` — Data pipeline hijacking

---

## Evidence Quality

All findings are:
- **Timestamped** — ISO 8601 format with cryptographic anchoring
- **Hashed** — SHA256/MD5 fingerprints for APK verification
- **Categorized** — Mapped to MITRE ATT&CK and Android framework
- **Risk-Scored** — Quantified severity from 0-300+ scale
- **Court-Ready** — JSON structure suitable for legal proceedings

---

## Known Limitations (v1.0-beta)

⚠️ **Before deploying in production, review:**
1. No XXE protection on XML parsing — validate XMLs before analysis
2. File I/O error handling is basic — ensure directories are writable
3. APK analysis uses static signatures only — no dynamic hooking detection (coming in v2)
4. Sandbox is process-level only, not hardware-isolated
5. No automated remote reporting (manual JSON export required)

**Security advisories:** See [SECURITY.md](./SECURITY.md) for responsible disclosure procedures.

---

## Licensing and Intellectual Property

The forensic methodologies, architectural logic, and defensive scripts contained within **Project-UnHooked-Audit** are cryptographically anchored and verified via ORCID.

This project is strictly licensed under **CC BY-NC 4.0**. 

* **Public & Researchers:** You are free to use this toolkit to audit your own devices and publish non-commercial threat intelligence.
* **Corporate & Enterprise:** Commercial use, repackaging for sale, or integration into proprietary security suites is strictly prohibited. For commercial licensing inquiries, contact AiZquaD directly.

---

## Timeline

| Phase | Status | ETA |
|-------|--------|-----|
| **Standalone Audit Toolkit** (Current) | ✅ Released v1.0-beta | May 2026 |
| **Kernel Patching Framework** | 🔄 In Progress | Q2 2026 |
| **Sovereign Fuel Integration** | 🔄 In Progress | Q3 2026 |
| **Motherboard-Level Defense** | ⏳ Planned | Q3 2026 |
| **Full System Deployment** | ⏳ Planned | Q4 2026 |

---

## Contributing

This is a public evidence vault, not a traditional open-source project. Contributions are limited:

- **Forensic Findings:** Submit new permission IOCs or attack signatures via GitHub Issues
- **Bug Reports:** Report code issues (not exploit techniques) via Issues
- **Documentation:** Help clarify threat models and detection methods

**Do NOT submit:**
- Exploit code or weaponized payloads
- Personal device forensic data
- Methodology improvements for attack execution

---

## Citation

If you use this toolkit for security research or threat intelligence publication, cite as:

```
AiZquaD (2026). Project-UnHooked-Audit: Android Device Forensic Framework.
GitHub: https://github.com/BadMFBox/Project-UnHooked-Audit-by-AiZquaD
ORCID: [Temporal Anchor]
```

---

## Support

This is a **standalone beta release** with limited support:
- GitHub Issues for bugs only
- No active Discord/Slack community yet
- Full system support coming with v2.0 release

For urgent security disclosures: Contact AiZquaD directly.

---

## Disclaimer

This toolkit is for **authorized security research and device auditing only**. Unauthorized access to devices, data theft, or circumventing security controls is illegal. Use responsibly and only on devices you own or have explicit permission to audit.

**The developer assumes no liability for misuse.**

---

*Last Updated: May 7, 2026*  
*Standalone Release v1.0-beta*  
*Full System Integration Timeline: Q3 2026*

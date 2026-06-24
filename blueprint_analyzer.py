#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║  BLUEPRINT ANALYZER v2                                       ║
║  Catalogs the attack infrastructure from privapp XMLs        ║
║  Produces a court-ready evidence package                     ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import json
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from collections import defaultdict


VAULT  = os.path.expanduser("~/SOVEREIGN/evidence/blueprint")
Path(VAULT).mkdir(parents=True, exist_ok=True)


# ─────────────────────────────────────────────────────────────
#  THE ATTACK PERMISSION DICTIONARY
#  Built from what we see in YOUR XMLs
# ─────────────────────────────────────────────────────────────
ATTACK_PERMISSIONS = {

    # ── AUDIO SURVEILLANCE ───────────────────────────────
    "android.permission.CAPTURE_AUDIO_HOTWORD": {
        "category": "AUDIO_SURVEILLANCE",
        "severity": "CRITICAL",
        "plain":    "Always-on microphone (hotword trigger)",
    },
    "android.permission.CAPTURE_AUDIO_OUTPUT": {
        "category": "AUDIO_SURVEILLANCE",
        "severity": "CRITICAL",
        "plain":    "Record all audio output from device",
    },
    "android.permission.CAPTURE_VOICE_COMMUNICATION_OUTPUT": {
        "category": "AUDIO_SURVEILLANCE",
        "severity": "CRITICAL",
        "plain":    "Record phone calls silently",
    },
    "android.permission.CAPTURE_MEDIA_OUTPUT": {
        "category": "AUDIO_SURVEILLANCE",
        "severity": "HIGH",
        "plain":    "Record all media audio",
    },
    "android.permission.MODIFY_AUDIO_ROUTING": {
        "category": "AUDIO_SURVEILLANCE",
        "severity": "HIGH",
        "plain":    "Redirect microphone/speaker output",
    },

    # ── REMOTE COMMAND & CONTROL ──────────────────────────
    "hihonor.permission.RECEIVE_CLOUD_OTA_UPDATA": {
        "category": "REMOTE_C2",
        "severity": "CRITICAL",
        "plain":    "Receive silent remote commands/updates",
    },
    "android.permission.SCHEDULE_EXACT_ALARM": {
        "category": "REMOTE_C2",
        "severity": "HIGH",
        "plain":    "Precision timer — used for beacon/check-in",
    },
    "android.permission.START_ACTIVITIES_FROM_BACKGROUND": {
        "category": "REMOTE_C2",
        "severity": "HIGH",
        "plain":    "Launch apps silently without user",
    },
    "android.permission.START_FOREGROUND_SERVICES_FROM_BACKGROUND": {
        "category": "REMOTE_C2",
        "severity": "HIGH",
        "plain":    "Run services silently in background",
    },
    "com.hihonor.permission.COMM_FORCE": {
        "category": "REMOTE_C2",
        "severity": "CRITICAL",
        "plain":    "Force communications (calls/data)",
    },

    # ── SMS & CALL INTERCEPTION ───────────────────────────
    "hihonor.permission.RECEIVE_SMS_INTERCEPTION": {
        "category": "SMS_INTERCEPTION",
        "severity": "CRITICAL",
        "plain":    "Intercept SMS before delivery — "
                    "steals 2FA codes",
    },
    "hihonor.permission.SET_SMSC_ADDRESS": {
        "category": "SMS_INTERCEPTION",
        "severity": "CRITICAL",
        "plain":    "Change SMS center address — "
                    "reroute all messages",
    },
    "android.permission.MODIFY_PHONE_STATE": {
        "category": "SMS_INTERCEPTION",
        "severity": "HIGH",
        "plain":    "Control calls and SMS state",
    },
    "android.permission.BIND_CARRIER_MESSAGING_SERVICE": {
        "category": "SMS_INTERCEPTION",
        "severity": "HIGH",
        "plain":    "Bind to carrier messaging (SIM tunnel)",
    },

    # ── CREDENTIAL & ACCOUNT THEFT ────────────────────────
    "com.hihonor.privacyspace.permission.PASSWORD_RESET": {
        "category": "CREDENTIAL_THEFT",
        "severity": "CRITICAL",
        "plain":    "Silent password reset capability",
    },
    "com.hihonor.permission.GET_LOCK_PASSWORD_CHANGED": {
        "category": "CREDENTIAL_THEFT",
        "severity": "CRITICAL",
        "plain":    "Monitor PIN/password changes in real-time",
    },
    "android.permission.MANAGE_FINGERPRINT": {
        "category": "CREDENTIAL_THEFT",
        "severity": "CRITICAL",
        "plain":    "Access and manage biometric data",
    },
    "android.permission.PROVIDE_TRUST_AGENT": {
        "category": "CREDENTIAL_THEFT",
        "severity": "CRITICAL",
        "plain":    "Bypass lockscreen without PIN",
    },
    "android.permission.READ_WIFI_CREDENTIAL": {
        "category": "CREDENTIAL_THEFT",
        "severity": "HIGH",
        "plain":    "Read saved WiFi passwords in plaintext",
    },
    "com.hihonor.permission.sec.ACCESS_UDID": {
        "category": "CREDENTIAL_THEFT",
        "severity": "HIGH",
        "plain":    "Access unique device ID (fingerprint)",
    },

    # ── PERSISTENCE & ANTI-REMOVAL ────────────────────────
    "hihonor.android.permission.SET_CANNOT_UNINSTALLED_PERMISSION": {
        "category": "PERSISTENCE",
        "severity": "CRITICAL",
        "plain":    "Lock apps — owner cannot uninstall",
    },
    "hihonor.android.permission.HW_SIGNATURE_OR_SYSTEM": {
        "category": "PERSISTENCE",
        "severity": "CRITICAL",
        "plain":    "Bypass APK signature verification",
    },
    "android.permission.INSTALL_PACKAGES": {
        "category": "PERSISTENCE",
        "severity": "CRITICAL",
        "plain":    "Install apps silently without user",
    },
    "android.permission.DELETE_PACKAGES": {
        "category": "PERSISTENCE",
        "severity": "HIGH",
        "plain":    "Delete apps silently",
    },
    "android.permission.CHANGE_COMPONENT_ENABLED_STATE": {
        "category": "PERSISTENCE",
        "severity": "HIGH",
        "plain":    "Enable/disable app components silently",
    },

    # ── LOCATION TRACKING ─────────────────────────────────
    "android.permission.LOCATION_HARDWARE": {
        "category": "LOCATION_TRACKING",
        "severity": "CRITICAL",
        "plain":    "GPS at hardware level — no software block",
    },
    "android.permission.LOCATION_BYPASS": {
        "category": "LOCATION_TRACKING",
        "severity": "CRITICAL",
        "plain":    "Bypass location permission restrictions",
    },
    "android.permission.INSTALL_LOCATION_PROVIDER": {
        "category": "LOCATION_TRACKING",
        "severity": "HIGH",
        "plain":    "Install custom location provider",
    },

    # ── DEVICE TAKEOVER ───────────────────────────────────
    "android.permission.MASTER_CLEAR": {
        "category": "DEVICE_TAKEOVER",
        "severity": "CRITICAL",
        "plain":    "Remote factory reset — wipe evidence",
    },
    "android.permission.REBOOT": {
        "category": "DEVICE_TAKEOVER",
        "severity": "HIGH",
        "plain":    "Reboot device remotely",
    },
    "android.permission.MANAGE_USERS": {
        "category": "DEVICE_TAKEOVER",
        "severity": "HIGH",
        "plain":    "Create/delete hidden user profiles",
    },
    "android.permission.INTERACT_ACROSS_USERS": {
        "category": "DEVICE_TAKEOVER",
        "severity": "HIGH",
        "plain":    "Access data across all user profiles",
    },
    "android.permission.FORCE_STOP_PACKAGES": {
        "category": "DEVICE_TAKEOVER",
        "severity": "HIGH",
        "plain":    "Kill your apps silently",
    },
    "android.permission.STOP_APP_SWITCHES": {
        "category": "DEVICE_TAKEOVER",
        "severity": "HIGH",
        "plain":    "Prevent you from switching apps",
    },
    "android.permission.WRITE_SECURE_SETTINGS": {
        "category": "DEVICE_TAKEOVER",
        "severity": "HIGH",
        "plain":    "Modify secure system settings",
    },

    # ── CROSS-DEVICE BRIDGE ───────────────────────────────
    "com.hihonor.permission.PC_MANAGER_API": {
        "category": "CROSS_DEVICE_BRIDGE",
        "severity": "CRITICAL",
        "plain":    "Full PC bridge — remote desktop capability",
    },
    "deviceintegration.permission.MANAGE_CROSS_DEVICE": {
        "category": "CROSS_DEVICE_BRIDGE",
        "severity": "CRITICAL",
        "plain":    "Manage cross-device data pipeline",
    },
    "android.permission.CONTROL_REMOTE_APP_TRANSITION_ANIMATIONS": {
        "category": "CROSS_DEVICE_BRIDGE",
        "severity": "HIGH",
        "plain":    "Screen mirroring control",
    },
    "android.permission.TETHER_PRIVILEGED": {
        "category": "CROSS_DEVICE_BRIDGE",
        "severity": "HIGH",
        "plain":    "Use device as network bridge/hotspot",
    },
}


# ─────────────────────────────────────────────────────────────
#  PARSE ONE PERMISSIONS XML
# ─────────────────────────────────────────────────────────────
def parse_permissions_xml(content: str,
                           label:   str) -> dict:
    """
    Parses privapp-permissions XML.
    Returns structured findings per package.
    """
    result = {
        "label":           label,
        "timestamp":       datetime.now().isoformat(),
        "packages":        {},
        "attack_findings": [],
        "categories_hit":  set(),
        "total_risk":      0,
    }

    try:
        root = ET.fromstring(content)
    except ET.ParseError as e:
        # Still try raw string search
        result["parse_error"] = str(e)
        root = None

    if root is not None:
        for pkg_elem in root.findall(
                './/privapp-permissions'):
            pkg_name = pkg_elem.get('package', 'unknown')
            perms    = [
                p.get('name', '')
                for p in pkg_elem.findall('permission')
            ]

            pkg_findings = []
            pkg_risk     = 0

            for perm in perms:
                if perm in ATTACK_PERMISSIONS:
                    ap = ATTACK_PERMISSIONS[perm]
                    finding = {
                        "permission": perm,
                        "category":   ap["category"],
                        "severity":   ap["severity"],
                        "plain":      ap["plain"],
                    }
                    pkg_findings.append(finding)
                    result["categories_hit"].add(
                        ap["category"])

                    score = {
                        "CRITICAL": 30,
                        "HIGH":     15,
                        "MEDIUM":    5,
                    }.get(ap["severity"], 5)
                    pkg_risk         += score
                    result["total_risk"] += score

            if pkg_findings:
                result["packages"][pkg_name] = {
                    "permissions_total":   len(perms),
                    "attack_permissions":  len(pkg_findings),
                    "risk_score":          pkg_risk,
                    "findings":            pkg_findings,
                }

                # Surface the worst
                result["attack_findings"].append({
                    "package":    pkg_name,
                    "risk":       pkg_risk,
                    "categories": list({
                        f["category"]
                        for f in pkg_findings
                    }),
                    "worst": sorted(
                        pkg_findings,
                        key=lambda x: (
                            0 if x["severity"]
                            == "CRITICAL" else 1),
                    )[:3],
                })

    # Convert set to list for JSON
    result["categories_hit"] = list(
        result["categories_hit"])

    return result


# ─────────────────────────────────────────────────────────────
#  BUILD THE EVIDENCE PACKAGE
# ────────────────────────────────────────────────────────────���
def build_evidence_package(xml_files: dict) -> dict:
    """
    xml_files = {"label": "xml_content_string", ...}
    Processes all XMLs and builds final package.
    """
    all_results  = []
    global_cats  = defaultdict(list)
    total_risk   = 0

    for label, content in xml_files.items():
        print(f"\n[ANALYZE] {label}")
        result = parse_permissions_xml(content, label)

        # Save individual result
        outfile = os.path.join(
            VAULT, f"{label}_analysis.json")
        with open(outfile, 'w') as f:
            json.dump(result, f, indent=2)
        print(f"  [SAVED] {outfile}")
        print(
            f"  [RISK]  {result['total_risk']} | "
            f"Packages hit: {len(result['packages'])}"
        )

        # Accumulate
        for pkg, data in result["packages"].items():
            for finding in data["findings"]:
                global_cats[
                    finding["category"]
                ].append({
                    "package":    pkg,
                    "permission": finding["permission"],
                    "plain":      finding["plain"],
                    "severity":   finding["severity"],
                    "source":     label,
                })

        total_risk  += result["total_risk"]
        all_results.append(result)

    # ── Final consolidated report ─────────────────────────
    report = {
        "title":         "HONOR/HIHONOR FIRMWARE "
                         "ATTACK BLUEPRINT — EVIDENCE",
        "generated":     datetime.now().isoformat(),
        "total_risk":    total_risk,
        "attack_surface": {
            cat: {
                "count":    len(items),
                "packages": list({
                    i["package"] for i in items}),
                "items":    items,
            }
            for cat, items in global_cats.items()
        },
        "priority_packages": [],
    }

    # Find the most dangerous packages
    pkg_scores = defaultdict(int)
    for res in all_results:
        for pkg, data in res["packages"].items():
            pkg_scores[pkg] += data["risk_score"]

    top_packages = sorted(
        pkg_scores.items(),
        key=lambda x: x[1],
        reverse=True,
    )[:10]

    report["priority_packages"] = [
        {"package": p, "total_risk": s}
        for p, s in top_packages
    ]

    # Save master report
    master = os.path.join(VAULT, "MASTER_REPORT.json")
    with open(master, 'w') as f:
        json.dump(report, f, indent=2)

    # Print summary
    print("\n╔══════════════════════════════════════════╗")
    print("║  ATTACK SURFACE SUMMARY                  ║")
    print("╚══════════════════════════════════════════╝")
    for cat, data in report["attack_surface"].items():
        print(
            f"\n  [{cat}]  "
            f"{data['count']} permissions across "
            f"{len(data['packages'])} packages"
        )
        for pkg in data["packages"][:3]:
            print(f"    → {pkg}")

    print(
        "\n  TOP RISK PACKAGES:"
    )
    for item in report["priority_packages"][:5]:
        print(
            f"    {item['package']:50s} "
            f"RISK: {item['total_risk']}"
        )

    print(
        f"\n[DONE] Master report: {master}"
    )
    print(
        f"[DONE] Total risk score: {total_risk}"
    )

    return report


# ─────────────────────────────────────────────────────────────
#  ENTRY POINT
#  Paste your XML files as strings below.
#  Or load them from files.
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":

    # ── Option A: Load from files ──────────────────────────
    xml_dir = os.path.expanduser(
        "~/SOVEREIGN/evidence/xml_vault")

    xml_files = {}
    if os.path.exists(xml_dir):
        for fname in os.listdir(xml_dir):
            if fname.endswith('.xml'):
                fpath = os.path.join(xml_dir, fname)
                try:
                    with open(fpath, 'r',
                              errors='ignore') as f:
                        xml_files[fname] = f.read()
                    print(f"[LOAD] {fname}")
                except Exception as e:
                    print(f"[WARN] {fname}: {e}")

    if not xml_files:
        print(
            "[INFO] No XML files found in vault. "
            "Copy your XMLs to "
            "~/SOVEREIGN/evidence/xml_vault/ first."
        )
    else:
        build_evidence_package(xml_files)

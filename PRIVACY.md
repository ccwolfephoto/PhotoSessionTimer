# PhotoSessionTimer Privacy Policy

**Last updated:** 2026-11-25

## Summary

**PhotoSessionTimer collects no data.** It runs entirely on your Mac. Nothing is sent to any server. No analytics, no telemetry, no third parties.

## What PhotoSessionTimer does

PhotoSessionTimer is a menu bar timer app that displays a floating overlay with a countdown and a stopwatch. Your settings (countdown target time, panel position and size, lock state, transparency, text colors, precision, sound choice, delay-start duration, per-timer visibility) are stored locally on your Mac in your user account's preferences (`UserDefaults`). They never leave your device.

## Data PhotoSessionTimer does NOT collect

- Personal information (name, email, address, phone)
- Device identifiers (IDFA, UUID, hardware serial)
- Location
- Health, financial, browsing, or search data
- Crash reports or diagnostics
- Anything sent over the network — PhotoSessionTimer makes no network calls

## Third parties

PhotoSessionTimer uses no third-party SDKs, no analytics services, no advertising networks, no crash reporters. The source repository is https://github.com/ccwolfephoto/TimeStack. The original upstream source is published at https://github.com/planBe/TimeStack so you can verify its history yourself.

## App Sandbox

PhotoSessionTimer runs inside Apple's App Sandbox with **no network entitlements**. It cannot make network calls.

The only file-system entitlement PhotoSessionTimer uses is `com.apple.security.files.user-selected.read-only`, which is required to support the "Custom…" option in the Sound menu (described below). With this entitlement, PhotoSessionTimer can read a file ONLY when you explicitly pick that file via the standard macOS Open File dialog — there is no broader file-system access, no scanning, no enumeration.

## Sound playback

When you choose a notification sound, PhotoSessionTimer plays one of:

- **Alarm** — a short two-tone sound bundled inside the app (no network access required).
- **Siren** — a Taiwan EAS-style alert tone bundled inside the app (Pixabay-licensed; see the [Credits section of the README](README.md#credits) for attribution).
- **One of the 14 macOS-bundled system sounds** (`/System/Library/Sounds/`) via the standard `NSSound` API.
- **A custom audio file you pick yourself** via the "Custom…" menu option. PhotoSessionTimer stores a sandbox-permitted Security-Scoped Bookmark to that file so the same picked file can play across launches. The file is read only at countdown-end (when you trigger the sound) — never scanned, never sent anywhere, never modified.

If you pick a custom sound and later move or delete the file, PhotoSessionTimer silently falls back to no sound and you can pick another file via the menu.

## Children's privacy

PhotoSessionTimer is not directed at children under 13. Because PhotoSessionTimer collects no data at all, no child-specific protections beyond those above are necessary.

## Changes to this policy

If PhotoSessionTimer ever changes its data practices, this file will be updated and the "Last updated" date above will change. Past versions of the upstream TimeStack policy are available in the git history at https://github.com/planBe/TimeStack/commits/main/PRIVACY.md.

## Contact

Questions about this policy or about PhotoSessionTimer itself: open an issue at https://github.com/ccwolfephoto/TimeStack/issues. For the original TimeStack project, open an issue at https://github.com/planBe/TimeStack/issues or email **michael@planbecreative.com**.

---

Made by Michael Wild – plan Be creative.

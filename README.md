# PhotoSessionTimer

An always-on-top timer for MacOS specialized for photographer use during minisessions when the laptop screen is being shown to the subject.

Based on the TimeStack app from PlanBeCreative, of which this is a divergent fork.  Thank you to the original authors.

My use case: I shoot tethered to my laptop with my screen mirrored to a monitor facing the subject.  My out-of-camera shots are displayed nearly full-screen.  each client gets a small, fixed amount of time in front of the camera - often 3 minutes.

I need to:
 * show the subject the time remaining
 * not distract the subject with a constantly changing timer (which would draw their eyes to the screen)
 * control the timer using a hardware remote away from the laptop
 * play a sound at a custom time prior to the end of the countdown (so I can stop and do review at the 2:00 mark, for example)
 * display tighter formatting than TimeStack

By modifying TimeStack, PhotoSessionTimer does all these things.

## Features beyond TimeStack

* Countdown timer main focus, stopwatch to be removed in future version
* Media controls control countdown timer - Play-Pause starts/stops; prev-track adds 10 sec; next-track resets
* Media control compatibility allows use of bluetooth media remotes (such as steering wheel media controllers) to control timer
* Optional visual indicator when running; optionally blinks
* Countdown by increment to prevent subject distraction - I like 5 seconds (use with running indicator)
* Optionally play sound at time remaining
* Assume less than 10 minutes for tighter formatting
* Assume seconds precision (will remove precision option in future)

## Requirements

- macOS 13 Ventura or later
- Xcode 16 or later + [XcodeGen](https://github.com/yonaskolb/XcodeGen) (`brew install xcodegen`) to build from source

## Building from source

The Xcode project is generated from `project.yml` via XcodeGen. From the repo root:

```bash
xcodegen generate
open PhotoSessionTimer.xcodeproj
```

Then ⌘R to build and run.

## How it works

The overlay is a borderless `NSPanel` at `.statusBar` level (always on top) hosting a SwiftUI view via `NSHostingView`. When locked, `ignoresMouseEvents = true` makes the window click-through. A separate small companion `NSPanel` at the top-left stays clickable regardless, so you can lock or unlock without leaving the overlay — no global hotkey needed (PhotoSessionTimer stays sandbox-clean by avoiding the Accessibility-permission flow that global hotkeys require on Mac).

Font sizes scale with the window via a SwiftUI `GeometryReader` + custom `Environment` value (`timerFontSize`) — at small windows the timer text floors at 28pt for legibility; at large windows it grows to fill the available space. The card aspect ratio locks dynamically to 8:5 (both timers visible), 8:3 (one timer), or 8:3 (neither — empty state).

Sound playback uses `NSSound` with a delegate-replay model: when you pick "Play 3×", the engine sets `NSSound.delegate` to a `SoundReplayDelegate` that re-calls `play()` after each `sound:didFinishPlaying:` callback until the count is exhausted. Custom user-picked audio files are persisted via Security-Scoped Bookmarks (the sandbox-permitted mechanism for re-accessing user-chosen files across launches).

Settings persist in `UserDefaults` under `PhotoSessionTimer.settings.v2`. Multi-monitor robust — if a saved window frame is off-screen at launch (monitor unplugged), PhotoSessionTimer falls back to centering on the main screen.

PhotoSessionTimer uses the bundle identifier `com.ccwolfephoto.PhotoSessionTimer` and a separate sandbox container. It starts with fresh settings and custom sound selections; existing TimeStack preferences and files are left untouched.

## Roadmap

- [x] **TimeStack v1.0** — initial TimeStack release. Full feature set above: overlay countdown + stopwatch, click-through lock with always-clickable lock corner, NSColorPanel per-timer colors, GeometryReader-driven font scaling, precision picker, click-to-edit countdown numbers, optional 3-2-1 delay-start with audio tick, both-at-once controls with Pause/Resume Both consolidation, bundled Alarm + Siren sounds plus 14 system sounds plus user-picked custom audio file, play-N-times count semantic, multi-monitor robust persistence
- [*] **PhotoSessionTimer v1.1** - Initial PhotoSessionTimer source release.

## Privacy

PhotoSessionTimer collects no data. Everything runs on your Mac; nothing is sent anywhere. See [PRIVACY.md](PRIVACY.md) for the full policy.

## License

MIT. See [LICENSE](LICENSE).

## Credits

- Based on [TimeStack](https://github.com/planBe/TimeStack) from PlanBeCreative, by Michael Wild, under the MIT License.
- **Alarm** (bundled default sound) — generated programmatically; see [`gen_alarm.py`](gen_alarm.py).
- **Siren** (bundled alternate sound, Taiwan EAS-style wail) — by [jeremayjimenez](https://pixabay.com/users/jeremayjimenez-28887262/) on Pixabay, used under the [Pixabay Content License](https://pixabay.com/service/license-summary/).

## Contributing

Issues and PRs welcome.

## About

Maintained by [ccwolfephoto](https://www.ccwolfephoto.com)
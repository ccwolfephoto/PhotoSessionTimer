#!/usr/bin/env python3
"""
Regenerates every PNG in PhotoSessionTimer/Assets.xcassets/AppIcon.appiconset/
from the single master image at assets/AppIcon-master-1024.png.

No vector/SVG editor needed — edit the master as a flat 1024x1024 PNG in
Photoshop (or any raster editor) and re-run this script to fan it out into
every size/scale macOS's app icon slot requires. Uses the macOS-bundled
`sips` tool (no Python imaging dependency) to do the resizing.

Master image guidelines (Photoshop):
    - Canvas: exactly 1024x1024 px.
    - Don't pre-round the corners or add a drop shadow/bevel — macOS Sonoma+
      applies its own continuous-corner mask and system shadow on top of
      whatever you provide, so a pre-rounded master double-masks oddly.
    - Leave a little breathing room near the edges (Apple's own icons keep
      roughly 8-10% padding) — content flush to the edge gets visually
      clipped once the system mask is applied.
    - Flatten before exporting (File > Export > PNG, or Save a Copy): no
      unflattened transparency *inside* the square is required, but the PNG
      itself should still have an alpha channel if you want a non-opaque
      background; opaque square-corner PNGs also work fine.

Usage:
    python3 gen_icon.py

Edit SOURCE/SIZES below if the master path or required sizes ever change.
"""

import os
import subprocess
import sys

SOURCE = "assets/AppIcon-master-1024.png"
OUT_DIR = "PhotoSessionTimer/Assets.xcassets/AppIcon.appiconset"

# (output filename, pixel size) — mirrors Contents.json in OUT_DIR exactly.
SIZES = [
    ("icon_16x16.png", 16),
    ("icon_16x16-2x.png", 32),
    ("icon_32x32.png", 32),
    ("icon_32x32-2x.png", 64),
    ("icon_128x128.png", 128),
    ("icon_128x128-2x.png", 256),
    ("icon_256x256.png", 256),
    ("icon_256x256-2x.png", 512),
    ("icon_512x512.png", 512),
    ("icon_512x512-2x.png", 1024),
]


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(script_dir, SOURCE)
    out_dir = os.path.join(script_dir, OUT_DIR)

    if not os.path.isfile(source_path):
        sys.exit(f"Master image not found: {source_path}")
    if not os.path.isdir(out_dir):
        sys.exit(f"Output dir not found: {out_dir}")

    for filename, size in SIZES:
        out_path = os.path.join(out_dir, filename)
        # 1024->1024 is a no-op resize; sips handles that fine, just copies
        # pixel-for-pixel, so no special-casing needed for the largest size.
        result = subprocess.run(
            ["sips", "-z", str(size), str(size), source_path, "--out", out_path],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            sys.exit(f"sips failed on {filename}:\n{result.stderr}")
        print(f"Wrote {filename} ({size}x{size})")

    print(f"\nDone — regenerated {len(SIZES)} icons from {SOURCE}.")
    print("Clean build (Shift+Cmd+K then Cmd+B) if Xcode caches the old icon.")


if __name__ == "__main__":
    main()

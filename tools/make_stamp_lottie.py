#!/usr/bin/env python3
"""Transparent pomegranate stamp — Lottie accent for power points."""
from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "media" / "lottie" / "stamp.json"


def color(r, g, b, a=1):
    return {"a": 0, "k": [r, g, b, a]}


def stamp():
    # 240x240, 90 frames @ 30fps, transparent, one-shot draw of a ring
    return {
        "v": "5.7.4",
        "fr": 30,
        "ip": 0,
        "op": 90,
        "w": 240,
        "h": 240,
        "nm": "power-stamp",
        "ddd": 0,
        "assets": [],
        "layers": [
            {
                "ddd": 0,
                "ind": 1,
                "ty": 4,
                "nm": "ring",
                "sr": 1,
                "ks": {
                    "o": {"a": 0, "k": 100},
                    "r": {"a": 0, "k": 0},
                    "p": {"a": 0, "k": [120, 120, 0]},
                    "a": {"a": 0, "k": [0, 0, 0]},
                    "s": {"a": 0, "k": [100, 100, 100]},
                },
                "ao": 0,
                "shapes": [
                    {
                        "ty": "el",
                        "p": {"a": 0, "k": [0, 0]},
                        "s": {"a": 0, "k": [168, 168]},
                    },
                    {
                        "ty": "st",
                        "c": color(0.72, 0.22, 0.18),
                        "o": {"a": 0, "k": 100},
                        "w": {"a": 0, "k": 3},
                        "lc": 2,
                        "lj": 1,
                    },
                    {
                        "ty": "tm",
                        "s": {"a": 1, "k": [
                            {"t": 0, "s": [0], "i": {"x": [0.5], "y": [1]}, "o": {"x": [0.5], "y": [0]}},
                            {"t": 48, "s": [0]},
                        ]},
                        "e": {"a": 1, "k": [
                            {"t": 0, "s": [0], "i": {"x": [0.5], "y": [1]}, "o": {"x": [0.5], "y": [0]}},
                            {"t": 48, "s": [100]},
                        ]},
                        "o": {"a": 0, "k": 0},
                    },
                ],
                "ip": 0,
                "op": 90,
                "st": 0,
                "bm": 0,
            },
            {
                "ddd": 0,
                "ind": 2,
                "ty": 4,
                "nm": "core",
                "sr": 1,
                "ks": {
                    "o": {"a": 1, "k": [
                        {"t": 24, "s": [0], "i": {"x": [0.5], "y": [1]}, "o": {"x": [0.5], "y": [0]}},
                        {"t": 60, "s": [100]},
                    ]},
                    "r": {"a": 0, "k": 0},
                    "p": {"a": 0, "k": [120, 120, 0]},
                    "a": {"a": 0, "k": [0, 0, 0]},
                    "s": {"a": 1, "k": [
                        {"t": 24, "s": [72, 72, 100], "i": {"x": [0.5, 0.5, 0.5], "y": [1, 1, 1]}, "o": {"x": [0.5, 0.5, 0.5], "y": [0, 0, 0]}},
                        {"t": 60, "s": [100, 100, 100]},
                    ]},
                },
                "ao": 0,
                "shapes": [
                    {
                        "ty": "el",
                        "p": {"a": 0, "k": [0, 0]},
                        "s": {"a": 0, "k": [18, 18]},
                    },
                    {
                        "ty": "fl",
                        "c": color(0.72, 0.22, 0.18),
                        "o": {"a": 0, "k": 100},
                        "r": 1,
                    },
                ],
                "ip": 0,
                "op": 90,
                "st": 0,
                "bm": 0,
            },
        ],
        "markers": [],
    }


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(stamp(), separators=(",", ":")))
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()

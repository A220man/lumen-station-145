# Changelog

## 1.3.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

## 1.2.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

## 1.1.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

## 1.0.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.


## 1.2.0 — work-in-progress checkpoint (UI repair)

Fixed `ui/index.html`: file contained literal `\n` escapes and a `getElement2Element`
typo, so the page rendered raw text and never queried the API. Rewrote with real
newlines, corrected the DOM lookup, and switched to safe DOM construction.

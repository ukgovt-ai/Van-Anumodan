# Van Anumodan — Installable PWA

Intelligent scrutiny & decision-support for PARIVESH forest-diversion proposals.
Government of Uttarakhand · Forest, Environment & Climate Change.

## Files (keep them all in the same folder / repo root)

| File | Purpose |
|---|---|
| `index.html` | The application (all 163 Master Checklist controls, gate logic, reports) |
| `manifest.webmanifest` | Makes it installable (name, icons, standalone display) |
| `sw.js` | Service worker — offline cache + rules auto-update |
| `rules.json` | **The Rules & Guidelines Library** (versioned, editable) |
| `icon-192.png`, `icon-512.png`, `icon-any-512.png`, `icon-180.png` | App icons |

All paths are **relative**, so it works at either a user site
(`https://you.github.io/`) or a project site (`https://you.github.io/van-anumodan/`).

## Deploy (your iPad workflow)

1. In **Working Copy**, put all files above in the repo root (or a subfolder).
2. Commit and push to GitHub.
3. In the repo on GitHub: **Settings → Pages → Deploy from branch → main / root**.
4. Open the published `https://…github.io/…/` URL in **Safari**.

GitHub Pages serves over HTTPS, which the service worker requires — so install and
offline both work.

## Install on iPad / iPhone

Safari → **Share** → **Add to Home Screen** → **Add**.
It then opens full-screen and works fully offline. (On Android/desktop Chrome an
**Install app** button appears in the header.)

## Where the Rules Library lives

The library is **`rules.json`, published next to the app**. On launch the app fetches
it (network-first), so the newest published version is used when online and the last
cached copy is used offline. Inside the app, **Rules Library** shows the current
version, e.g. `v2026.07.1 · updated 2026-07-15`, and marks each row *Published* or *Local*.

## Updating the library when an amendment is issued

Pick whichever is easier — both end with a commit + push:

**A. Edit the file directly**
1. Open `rules.json` in Working Copy.
2. Add the new instrument (or set `super` on the one it supersedes, so old findings stay reproducible).
3. **Bump `libraryVersion` and `updated`** (e.g. `2026.07.1` → `2026.09.1`).
4. Commit → push. GitHub Pages redeploys.

**B. Edit inside the app, then export**
1. Rules Library → **Add rule** / edit rows.
2. **Export rules.json** (downloads the file).
3. Put that file in the repo (replacing the old one) in Working Copy → commit → push.

**On every installed device:** the next time it's opened online, the app sees the higher
`libraryVersion`, refreshes the library, and shows *"Rules library updated to vX"*.
Published rows update in place; any purely local rows you added are preserved.
There's also a **Check for updates** button to pull immediately, and **Import rules file**
to load a `rules.json` shared by a colleague without editing the repo.

## Pushing an app update (not rules)

If you change `index.html` or any other shell file, **bump `CACHE_VERSION`** at the top of
`sw.js` (e.g. `v1.0.0` → `v1.0.1`) and push. Installed devices get a *"new version
available — reload?"* prompt on their next online launch.

## Notes

- Scrutiny data is stored per device (`localStorage`). Use **Reports → Export case (JSON)**
  to move a case between devices or to archive it.
- The starter `rules.json` is instrument-level only. Verify every clause reference and add
  exact provisions, dates and official source URLs before the library gates any decision;
  approval by the designated competent authority is the governance step the FRS requires.

# Base888 Quantum Geometry v1.0 — executed checks

## Environment

- Run in isolated Linux container, Python 3.13, standard-library `unittest`, Chromium through Playwright.
- Browser loaded exact standalone `index.html` text using `page.set_content` (local `file://` and loopback HTTP browsing are blocked by this environment).
- No external network, dependencies or data services were needed by the simulator.

## Independent reference tests

Command: `python3 -m unittest -v test_model.py`

**Result: 8 tests run, 8 passed.** Covered graph combinatorics, pair entanglement bounds, exact link normalization, uniform flat-mesh curvature, triangle inequality on randomized test samples, null / altered coupling equations, dimension embeddings, and disjoint unitary circuit gates.

## Browser interaction tests

All of the following were actually exercised:

| Check | Observed result |
|---|---|
| Page script exceptions | None |
| Graph construction | 49 registers, 120 links |
| Single-qudit norm | displayed `1.0000000000` |
| Null candidate `kappa=0` | geometric shift `0.00000`; Zoo null check `PASS` |
| Uniform network interior curvature | maximum `|K| = 0` in smoke check |
| Two-node graph path | `(0,0) → (6,6)`, reference `7.5950`, candidate `7.8440` in one dynamic test |
| JSON experiment download | `base888-experiment.json` produced |
| CSV timeseries download | `base888-history.csv` produced |
| 3-panel PNG download | `base888-geometry.png` produced |
| Browser script errors after interactions | None |
| Dimension sweep control | 887 / 888 / 889 declared feasible with fixed local support 64 |

Detailed machine-readable snapshots of the smoke check appear in `browser_checks.json`. The path results depend on the test moment and parameters, and **are not scientific measurements**.

## Interpretation

These tests establish basic software operation and several narrow mathematical invariants of the toy model. They do **not** validate a physical EFMW coupling, emergence of Lorentzian spacetime, or quantum gravity.

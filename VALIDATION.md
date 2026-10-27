# Verification protocol

## Levels of claim

1. **Mathematical identity:** known facts about the explicitly defined independent-link quantum ansatz (state normalization, pair entropy, local embedding).
2. **Numerical check:** finite precision implementation respects relevant mathematical identities within tolerance.
3. **Model assumption:** the correlation-to-length mapping and `kappa` Hamiltonian deformation are stipulated for research, not derived.
4. **Physical claim:** quantum gravity, EFMW novelty, or Einstein-limit recovery remains **UNRESOLVED**.

The Zoo indicator `PASS` applies **only to the adjacent narrow check**. `N/A` means a control condition does not hold (e.g. a null test requires `kappa=0`), not that an open proof was satisfied.

## Executable checks

Run `python3 -m unittest -v test_model.py`; expected tests:

- Graph size and max local degree (`49`, `120`, `72`, `6`).
- Exact bipartite entropy extrema (`0, 2, 0` bits).
- Pair state normalization.
- Unmodified equal-length triangulation produces zero *interior* angle-defect curvature.
- All supported edge-length mappings satisfy triangle inequalities for tested random link correlations.
- Null coupling yields the identical pair-phase trajectories.
- 887/888/889 each contain enough states for the chosen max local support 64.
- Alternating pair unitary gates conserve norm for `d=887,888,889` to tolerance.

Browser interaction smoke test: check load without JS exceptions; inspect live running norm, null reduction, dimension sweep log, chart, node path selection, JSON/CSV/PNG exports.

## Strict non-claims

- The finite model has no tensor-network entangling dynamics beyond independent virtual bonds; it is not a generic many-body 888-state simulation.
- The graph topology and background are fixed; geometry is assigned from correlators. Neither spacetime nor topology emerges from unconstrained quantum dynamics.
- `kappa` is a *manually imposed* Hamiltonian change. Nonzero differences are expected by construction, not evidence of EFMW.
- `C` is an error-monitor metric and cannot serve as a measure of von Neumann coherence or prove a collapse law.
- The internal unitary circuit and pair network are distinct demonstrations, not a coupled quantum-gravity dynamics.
- No Einstein equations, field constraints, relativistic propagation, stress energy or Newtonian potential are evaluated.
- No lab measurement or external physical observational data has been fitted.

## Criteria for future scientific progress

A candidate path toward gravity would require a microscopic physical Hamiltonian fixed independently of target spacetime, controlled continuum / low-energy limit with identifiable metric and causal structure, equations of motion for the metric, and empirical predictions recovering established tests. Compare dimension 888 against nearby dimensions and physically matched control models without changing nuisance parameters. Freeze tests before looking at outcomes.

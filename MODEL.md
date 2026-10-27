# Base888 Quantum Geometry — frozen v1.0 model specification

**Status:** finite quantum-information and graph-geometry toy model, **not a derivation of quantum gravity** and not a validated Einstein–Feynman–Maxwell–Wright physical theory.

## A. Mathematical substrate and relation to Codex-888

The published [`enuminous/Codex-888`](https://github.com/enuminous/Codex-888) supplies a symbolic finite base `888`, phase rotations and formal register-count identities. Its own `Foundation.lean` says no quantum amplitudes are assumed. **This application adds new quantum semantics**: at each graph vertex, a local Hilbert space `C^d`, initially `d = 888`. The independent dimension-control values 887 and 889 are included to test whether a calculation actually depends on the value 888.

A 7 × 7 square lattice with one diagonal in each square contains 49 vertices, 120 undirected links, 72 triangular faces, and maximum vertex degree 6. This is a finite fixed adjacency structure, not an emergent topology or causal manifold.

## B. Exact entangled-link network

For each edge `e = (u,v)` define two virtual qubit factors, one at each end, in a normalized pure state

```
|psi_e(t)> = cos(theta_e(t)) |0_u 0_v> + sin(theta_e(t)) |1_u 1_v>.
```

The full state is exactly `|Psi> = tensor_product_e |psi_e>`; each vertex contains one virtual qubit per incident edge, mapped by an injective isometry into `C^d`. Thus, the active local subspace has at most `2^degree = 64` levels, which fits inside 887, 888, and 889. There are **no interacting multipartite entanglement tensors**: entanglement consists only of independent edge pairs.

For an edge with `p = cos^2(theta)`, a one-endpoint reduced density matrix has eigenvalues `(p, 1-p)`, and so

```
S(edge end) = H_2(p) = -p log2(p) - (1-p) log2(1-p)
I(u:v) = 2 H_2(p)   bits.
```

Because the full state is a product of edge states, the mutual information between adjacent whole-node subsystems is exactly the corresponding expression, and between non-neighbors is zero. These are derived from the stipulated quantum state, **not measured hardware entanglement**.

The pair Hamiltonian can be chosen as `H_e(t) = -hbar Omega_e(t) sigma_y` on `span{|00>,|11>}`. In a consistent sigma-y sign convention, this gives `theta_e(t) = theta_e(0) + integral Omega_e dt`; every link state evolves by a unitary rotation. In v1, the explicit example is

```
reference: theta_e(t) = theta0_e + f * omega_e * t
candidate: theta_e(t) = theta0_e + f * omega_e * t + kappa * 0.018 * w_e * t
w_e = exp[-((x_e - 3)^2 + (y_e - 3)^2)/(2 sigma^2)]
      * [1 + 0.15 sin(1.1*x_e + 0.7*y_e)]
```

`f` = base-frequency multiplier; `sigma` = localization width; `kappa` = user-controlled toy-model perturbation. Frequencies, time and lattice lengths are **dimensionless simulator conventions**; `.018` is an arbitrary illustrative coefficient. This candidate perturbation is **not derived from EFMW** or its C1 action. The seed determines deterministic initial inhomogeneity.

## C. Inferred candidate geometry

A link's assigned length is defined as

```
L_e = L0_e * [1 + a * tanh(2*(1 - I_e))]
L0_e = 1 for horizontal/vertical links; sqrt(2) for diagonals.
```

`a` is adjustable with maximum `0.14`. The monotone map makes highly correlated links shorter and weakly correlated links longer. **This map is posited, not entailed by entanglement theory or EFMW.** It is designed so all chosen triplets satisfy strict Euclidean triangle inequalities across the supported correlation range. Triangular face areas are determined by Heron's formula; interior vertex Gaussian-curvature proxies are

```
K_v = [2*pi - sum_{T incident on v} angle_T(v)]
      / [sum_{T incident on v} Area(T)/3]
```

Boundary vertices are deliberately `N/A`: boundary curvature would require additional boundary terms and is not plotted as an intrinsic interior value. This is a metric on a triangulated fixed graph, **not a Lorentzian spacetime**, and there is no Einstein dynamics, stress-energy source or graviton. Paths are shortest paths through weighted graph edges (Dijkstra), not spacetime geodesics.

## D. Separate 888-level circuit demonstration

A single `d`-level qudit has `d` complex amplitudes and evolves by unitary alternating two-position gates `exp(i gamma sigma_x)` for disjoint even/odd pairs, followed by a position-dependent diagonal phase gate. The circuit preserves `sum |amplitude_j|^2` within numerical precision. It is **separate from the link network**: it demonstrates that the application has an actual dimension-888 complex quantum state representation rather than merely rendering the number 888. The wavepacket display is a measurement-basis probability distribution, not a gravitational observable.

## E. EFMW-inspired operational monitor

A state-dependent comparison residual is computed from `Delta I_e = I_e(candidate) - I_e(reference)`. The displayed root-mean-square residual is `r = sqrt(mean_e (Delta I_e)^2)`. An operational memory estimate is updated with bounded numerical time increment:

```
q_t = (r_t / 0.2)^2
M_new = lambda^(0.8*Delta t)*M_old + [1 - lambda^(0.8*Delta t)]*q_t
C_new = exp(-beta * M_new)
```

The constants `0.2` and `0.8` are chosen scaling conventions. `C` is a **monitor score**, not physical quantum coherence and not an emergent law. This is inspired by the recurrence in [`EFMW-F001`](https://github.com/enuminous/papers/blob/main/EFMW-F001-Recursive-Coherence-Dynamics.md), which explicitly describes itself as a not-yet-validated estimator.

## F. Why the study does not derive quantum gravity

No Lorentzian metric, causal cone, Hamiltonian/momentum gravitational constraints, diffeomorphism algebra, Einstein–Hilbert effective action, stress tensor, gravitational waves, Einstein/Newtonian low-energy limit or independently discriminating measurement are derived. The 888 count is not shown physically preferred. An observed nonzero `Delta I` reflects a **known inserted perturbation**; it cannot be presented as evidence of EFMW physics.

## G. Numerics

- Exact trigonometric link evolution means there is no approximate link-time-step integrator to validate; independent register circuit gates are unitary up to floating point.
- Entropy and triangle angles use IEEE-754 double precision.
- The history sampling cadence depends on presentation speed and is **not an equal-time ensemble**.
- No randomness after initial seed, so user controls + seed + model commit specify the run.
- Cross-version reproduction should pin this source file or commit hash; published file changes are not silently equivalent.

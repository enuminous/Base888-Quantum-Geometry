"""Independent standard-library reference calculations for Base888 Quantum Geometry.

This implements a finite entangled-edge toy model, NOT quantum gravity.
The physical EFMW coupling is not derived: kappa is an arbitrary control term.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import acos, cos, exp, hypot, log2, pi, sin, sqrt, tanh
from typing import Sequence

SIZE = 7

@dataclass(frozen=True)
class Edge:
    a: int
    b: int
    diagonal: bool
    midpoint: tuple[float, float]


def triangulation(size: int = SIZE) -> tuple[list[Edge], list[tuple[int, int, int]], list[list[int]]]:
    """Triangulate square cells along their NW/SE diagonals."""
    index = lambda x, y: y * size + x
    edges: list[Edge] = []
    lookup: dict[tuple[int, int], int] = {}
    links: list[list[int]] = [[] for _ in range(size * size)]
    tris: list[tuple[int, int, int]] = []
    def insert(a: int, b: int) -> None:
        a, b = sorted((a, b))
        if (a, b) in lookup:
            return
        ia, ib = (a % size, a // size), (b % size, b // size)
        diagonal = abs(ia[0] - ib[0]) + abs(ia[1] - ib[1]) == 2
        idx = len(edges)
        edges.append(Edge(a, b, diagonal, ((ia[0]+ib[0])/2, (ia[1]+ib[1])/2)))
        lookup[(a,b)] = idx
        links[a].append(idx)
        links[b].append(idx)
    for y in range(size - 1):
        for x in range(size - 1):
            a, b, c, d = index(x,y), index(x+1,y), index(x+1,y+1), index(x,y+1)
            for tri in ((a,b,c),(a,c,d)):
                tris.append(tri)
                insert(tri[0],tri[1]); insert(tri[1],tri[2]); insert(tri[2],tri[0])
    return edges, tris, links


def binary_entropy(p: float) -> float:
    p = max(0.0, min(1.0, p))
    if p <= 1e-12 or p >= 1-1e-12:
        return 0.0
    return -p*log2(p)-(1-p)*log2(1-p)


def link_mutual_information(theta: float) -> float:
    """For cos(theta)|00>+sin(theta)|11>, I(A:B)=2 H_2(cos^2 theta)."""
    return 2*binary_entropy(cos(theta)**2)


def inferred_length(mi: float, diagonal: bool, sensitivity: float=0.11) -> float:
    """Chosen phenomenological metric mapping; NOT a physical derivation."""
    return (sqrt(2) if diagonal else 1)*(1+sensitivity*tanh((1-mi)*2))


def triangle_area(a: float, b: float, c: float) -> float:
    if min(a+b-c, b+c-a, c+a-b) <= 0:
        raise ValueError('triangle inequality violated')
    s=(a+b+c)/2
    return sqrt(max(0, s*(s-a)*(s-b)*(s-c)))


def curvature_from_links(size: int, edges: Sequence[Edge], tris: Sequence[tuple[int,int,int]], lengths: Sequence[float]) -> list[float | None]:
    lookup = {(e.a,e.b):i for i,e in enumerate(edges)}
    def L(a,b):return lengths[lookup[tuple(sorted((a,b)))]]
    angles=[0.0]*(size**2); areas=[0.0]*(size**2)
    for i,j,k in tris:
        # side opposite i is jk etc.
        ai,aj,ak=L(j,k),L(i,k),L(i,j)
        area=triangle_area(ai,aj,ak)
        angles[i]+=acos(max(-1,min(1,(aj*aj+ak*ak-ai*ai)/(2*aj*ak))))
        angles[j]+=acos(max(-1,min(1,(ai*ai+ak*ak-aj*aj)/(2*ai*ak))))
        angles[k]+=acos(max(-1,min(1,(ai*ai+aj*aj-ak*ak)/(2*ai*aj))))
        for v in (i,j,k):areas[v]+=area/3
    out=[]
    for i in range(size**2):
        x,y=i%size,i//size
        if x==0 or y==0 or x==size-1 or y==size-1:
            out.append(None)
        else:
            out.append((2*pi-angles[i])/areas[i])
    return out


def link_theta(theta0: float, omega: float, t: float, kappa: float, influence: float, candidate: bool) -> float:
    """Exact evolution under commuting 2x2 sigma-y link Hamiltonians."""
    return theta0 + omega*t + (kappa*.018*influence*t if candidate else 0.0)


def dimension_sweep(dimensions=(887,888,889), degree: int=6) -> dict[int, bool]:
    """Whether a fixed 2-level per incident bond can be encoded locally."""
    return {d:d>=2**degree for d in dimensions}


def unitary_circuit_gate(a: complex, b: complex, theta: float) -> tuple[complex,complex]:
    """exp(i theta sigma_x) on two basis amplitudes."""
    return cos(theta)*a+1j*sin(theta)*b, cos(theta)*b+1j*sin(theta)*a


def circuit_layer(amps: list[complex], theta: float, odd: bool=False) -> list[complex]:
    """Disjoint pair gates, with a wraparound gate for even-sized cyclic odd layers."""
    n=len(amps)
    out=amps[:]
    start=int(odd)
    for i in range(start,n-1,2):
        out[i],out[i+1]=unitary_circuit_gate(out[i],out[i+1],theta)
    if odd and n%2==0:
        out[-1],out[0]=unitary_circuit_gate(out[-1],out[0],theta)
    return out


def norm2(amps: Sequence[complex])->float:
    return sum(abs(a)**2 for a in amps)

"""Supplementary exact counts for three-direction arrangements on R^2/Z^2.

Prepared 2026-11-06. Statically reviewed; NOT executed in this preparation.
All grids have a common origin. N, R, Y and K must be positive integers.
Counts concern geometric faces, not labelled tuples or sampled trajectories.

Only Python's standard library is used. There is no file or network access,
data deserialization, dynamic execution, or import-time example calculation.
"""

from fractions import Fraction
from math import gcd


def _validate_parameters(N, R, Y, K):
    for name, value in (("N", N), ("R", R), ("Y", Y), ("K", K)):
        if type(value) is not int:
            raise TypeError(f"{name} must be a positive integer (not bool)")
        if value <= 0:
            raise ValueError(f"{name} must be positive")


def closed_form_counts(N, *, R=12, Y=27, K=60):
    """Return exact counts using the general gcd formula in the manuscript."""
    _validate_parameters(N, R, Y, K)
    common_vertical = gcd(N, R)
    nv = N + R - common_vertical
    d = gcd(Y, K)
    L = (Y // d) * K
    triple = d * (
        gcd(N, 2 * L) + gcd(R, 2 * L) - gcd(common_vertical, 2 * L)
    )
    pair_count = nv * (Y + K) + 2 * Y * K
    return {
        "nv": nv,
        "T": triple,
        "V": pair_count - 2 * triple,
        "E": 2 * pair_count - 3 * triple,
        "F": pair_count - triple,
    }


def _grid(n):
    return {Fraction(j, n) for j in range(n)}


def exact_arrangement_counts(N, *, R=12, Y=27, K=60):
    """Enumerate rational vertices and count their curve incidences.

    This routine does not call closed_form_counts or use its triple formula.
    Agreement is an implementation consistency check, not a substitute for
    the mathematical proof. Work and memory grow with the pair count.
    """
    _validate_parameters(N, R, Y, K)
    verticals = _grid(N) | _grid(R)
    sum_lines = _grid(Y)
    difference_lines = _grid(K)
    vertices = set()

    # x = u and x+y = a (mod 1).
    for u in verticals:
        for a in sum_lines:
            vertices.add((u, (a - u) % 1))

    # x = u and x-y = b (mod 1).
    for u in verticals:
        for b in difference_lines:
            vertices.add((u, (u - b) % 1))

    # x+y = a and x-y = b have two solutions on the torus.
    for a in sum_lines:
        for b in difference_lines:
            base = (a + b) / 2
            for x in (base % 1, (base + Fraction(1, 2)) % 1):
                vertices.add((x, (a - x) % 1))

    edges = 0
    triples = 0
    for x, y in vertices:
        incidence = (
            int(x in verticals)
            + int((x + y) % 1 in sum_lines)
            + int((x - y) % 1 in difference_lines)
        )
        if incidence not in (2, 3):
            raise ArithmeticError("Unexpected vertex incidence")
        edges += incidence
        if incidence == 3:
            triples += 1

    vertex_count = len(vertices)
    return {
        "nv": len(verticals),
        "T": triples,
        "V": vertex_count,
        "E": edges,
        "F": edges - vertex_count,
    }


def main():
    """Optional small example comparison; runs only on explicit invocation.

    This function has not been run during preparation. The all-one case
    checks nondefault Y,K, which were mishandled by an older source version.
    """
    examples = (
        (1, 1, 1, 1, {"nv": 1, "T": 1, "V": 2, "E": 5, "F": 3}),
        (27, 12, 27, 60,
         {"nv": 36, "T": 108, "V": 6156, "E": 12420, "F": 6264}),
    )
    for N, R, Y, K, expected in examples:
        formula = closed_form_counts(N, R=R, Y=Y, K=K)
        enumerated = exact_arrangement_counts(N, R=R, Y=Y, K=K)
        if formula != enumerated or formula != expected:
            raise ArithmeticError(
                f"Mismatch at {(N, R, Y, K)}: {formula}, {enumerated}"
            )
        print(f"N={N}, R={R}, Y={Y}, K={K}: {formula}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Independent verifier for the counterexample N = 57297303441525855
to Zhi-Wei Sun's Conjecture (OEIS A303540 / MathOverflow #301581):
  Every integer n > 1 can be written as a^2 + b^2 + C(2c, c) + C(2d, d)
  with nonnegative integers a <= b and c <= d.

Requirements: Python 3.8+ and sympy (for deterministic primality/factorization
of 64-bit integers).
"""
import math
import sympy

N = 57297303441525855

def verify_counterexample(n: int) -> None:
    assert n > 1, "n must be > 1"
    c_max = 0
    while math.comb(2 * (c_max + 1), c_max + 1) <= n:
        c_max += 1
    assert math.comb(2 * (c_max + 1), c_max + 1) > n

    total_pairs = 0
    for c in range(c_max + 1):
        bc = math.comb(2 * c, c)
        for d in range(c, c_max + 1):
            bd = math.comb(2 * d, d)
            if bc + bd > n:
                continue
            total_pairs += 1
            m = n - bc - bd
            assert m > 0, f"Representation found with a=b=0 at (c,d)=({c},{d})"
            fac = sympy.factorint(m)
            # Reconstruct product & verify primality
            prod = 1
            for p, e in fac.items():
                assert sympy.isprime(p), f"Factor {p} is not prime"
                prod *= p ** e
            assert prod == m, f"Factorization product mismatch for m={m}"
            # By Fermat's sum-of-two-squares theorem, m is NOT a^2+b^2 iff
            # some prime p == 3 (mod 4) has odd exponent v_p(m).
            witnesses = [(p, e) for p, e in sorted(fac.items()) if p % 4 == 3 and e % 2 == 1]
            assert witnesses, f"Valid representation exists at (c,d)=({c},{d}), m={m}, fac={fac}"

    print(f"VERIFIED: A303540({n}) = 0 across all {total_pairs} pairs (c, d) with 0 <= c <= d <= {c_max}.")

if __name__ == "__main__":
    verify_counterexample(N)

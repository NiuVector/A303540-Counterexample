# Counterexample to Zhi-Wei Sun's A303540 conjecture

**Counterexample:** `N = 57297303441525855`.

The 2018 conjecture asks whether every integer n > 1 is a sum of two squares and two central binomial coefficients:

```math
n=a^2+b^2+\binom{2c}{c}+\binom{2d}{d},
\qquad 0\le a\le b,\quad 0\le c\le d.
```

This repository provides an exact computational certificate that A303540(N) = 0, disproving that universal assertion. No claim is made that N is the smallest counterexample.

## Proof

Write B(k) = binomial(2k,k). The sequence B(k) is strictly increasing for k >= 0, and

- B(29) = 30067266499541040;
- B(30) = 118264581564861424 > N.

Consequently only 0 <= c <= d <= 29 need be considered. Of the 465 unordered pairs in this range, (29,29) is the only pair with B(c)+B(d)>N. For each of the remaining 464 pairs, the positive integer m = N-B(c)-B(d) has a prime divisor p congruent to 3 modulo 4 whose valuation v_p(m) is odd. By Fermat's two-square theorem, none of these remainders is a sum of two integer squares.

Thus no representation of N exists.

## Reproduce

Requires Python 3.8+ and SymPy. Run without Python's `-O` flag so assertions remain enabled.

```sh
python -m pip install -r requirements.txt
python verify_a303540.py
```

Expected output:

```text
VERIFIED: A303540(57297303441525855) = 0 across all 464 pairs (c, d) with 0 <= c <= d <= 29.
```

## Files

- `verify_a303540.py`: original independent verifier; enumerates all eligible pairs, factors each remainder, verifies the prime factors and reconstructs each factorization.
- `a303540_counterexample_certificate.csv`: 464-row certificate, including the exact remainder, a witness prime and its odd valuation. Read integer fields as arbitrary-precision integers, not floating-point numbers. The first column is a zero-based row index.
- `requirements.txt`: verification dependency.

To check the certificate, recompute the binomial coefficients and remainder for each row, check that the witness p is prime and p mod 4 = 3, and verify that its exact valuation in m is odd. Check that every eligible pair appears exactly once. The verifier independently proves the same result without relying on the CSV.

## Original conjecture

- [OEIS A303540](https://oeis.org/A303540)
- [Zhi-Wei Sun's MathOverflow question, May 30, 2018](https://mathoverflow.net/questions/301581/is-every-integer-n1-the-sum-of-two-squares-and-two-central-binomial-coefficie)

The counterexample and code are provided for independent mathematical verification.

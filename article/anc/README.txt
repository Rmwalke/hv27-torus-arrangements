Supplement to An Explicit GCD Evaluation for Three-Direction Torus Arrangements
Rushikesh Murlidhar Walke
Licensed author-review preparation v08, 6 November 2026

FILES
hv27_torus_counts.py       Parameterized gcd formula and exact rational
                          vertex/incidence enumeration.
run_hv27_checks.py         Finite validation suite and report writer.
RUN_HV27_WINDOWS.bat       Optional Windows launcher.
validation/RESULTS.json    Author-supplied structured runtime report.
validation/RESULTS.txt     Author-supplied readable runtime report.
SHA256SUMS.txt             File-integrity manifest for this supplement.
LICENSE                   MIT license for the three software files.
START_HERE_MR.txt          Marathi pointer retained for the Windows launcher.
validation/README_LICENSE.txt  License scope for unchanged report files.

REPORTED VALIDATION
The included author-supplied reports record 284 completed checks, all PASS,
from a Windows CPython 3.14.7 run dated 6 November 2026. The core and runner
source hashes match the versions accompanying those reports. This is a
record of the author's run, not independent execution by the preparation
assistant. The reports do not record a terminal process exit code.

Coverage: 2 reference cases, 26 default cases N=15..40, 8 nondefault cases,
200 pure-grid triple-count comparisons, and 48 invalid-input cases.
For N=27,R=12,Y=27,K=60 the reported counts are
nv=36, T=108, V=6156, E=12420, F=6264.
The adjacent default counts are F(26)=6336 and F(28)=6336.

OPTIONAL REPRODUCTION BY A READER
Use an already installed Python 3.8 or later; the files use its standard
library. Extract the files into a new writable folder. From that folder:

    python3 -I -S -B run_hv27_checks.py

On Windows, RUN_HV27_WINDOWS.bat is an optional launcher. Neither route
installs Python. Each run writes a newly named results folder; it does not
replace the reports distributed in validation/. These commands were not
executed during this release preparation.

SOURCE IDENTIFICATION
Core SHA-256:
4ddf34683d88d24c0720b831b30cc5319245485783678efb08f09198503296e2
Runner SHA-256:
b10a54c9015dbdce05df0924b8c3e6717dc291914257eee9c461658a801a8ddf
The research source files and supplied reports are unchanged from preparation v05.
Documentation and its manifest have been updated for this review package.

INTERPRETATION
Finite agreement supports implementation consistency. It is not an
all-input proof, an originality certificate, or peer review. The vertex
enumerator obtains F=E-V; it does not independently enumerate geometric
faces. Cellularity and the all-parameter result are established by the
mathematical argument in the article. Faces, distinct labels, and sampled
trajectory states must not be equated without a separate argument.

LICENSES
The author selected CC BY 4.0 for the article and separate documentation,
and MIT for the original supplementary software. The three software files
listed above are covered by LICENSE, including their inline documentation.
This README is separate CC BY 4.0 documentation.
Copyright (c) 2026 Rushikesh Murlidhar Walke
https://creativecommons.org/licenses/by/4.0/
For precise file scopes and third-party exclusions, see ../LICENSING_SCOPE.txt.
Licensing is now applied; author-review status does not postpone the grants.
No public repository submission is claimed by this review package.

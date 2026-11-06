# HV27 — Three-Direction Torus Arrangements

Supplementary code and manuscript for **An Explicit GCD Evaluation for Three-Direction Torus Arrangements**, by **Rushikesh Murlidhar Walke**, Independent Researcher, Maharashtra, India.

- **Published preprint:** [Zenodo, version v08, 6 November 2026](https://doi.org/10.5281/zenodo.24014501)
- **Author ORCID:** [0009-0006-6749-5660](https://orcid.org/0009-0006-6749-5660)
- **Read the PDF:** [HV27_Preprint_Review_v08.pdf](HV27_Preprint_Review_v08.pdf)
- **All-versions DOI:** [10.5281/zenodo.24014500](https://doi.org/10.5281/zenodo.24014500)

## Scope

The note gives an explicit gcd evaluation for three families of closed curves on a two-dimensional torus. It includes a finite-grid triple-intersection calculation, a cellularity argument and the passage from incidences to geometric faces. It is an explicit specialization of established toric-arrangement and arithmetic-Tutte theory, with a self-contained proof and parameterized example. It does not claim a new general chamber-counting theory.

Its relationship to the author's earlier cyclic-grid note is explained in the paper. That earlier work has DOI [10.5281/zenodo.23184983](https://doi.org/10.5281/zenodo.23184983); it is a separate publication.

## Files

| Path | Purpose |
|---|---|
| `HV27_Preprint_Review_v08.pdf` | Six-page published preprint |
| `article/main.tex` | Manuscript source |
| `article/anc/hv27_torus_counts.py` | Parameterized formula and exact rational vertex/incidence enumeration |
| `article/anc/run_hv27_checks.py` | Finite validation suite and report writer |
| `article/anc/RUN_HV27_WINDOWS.bat` | Optional Windows launcher |
| `article/anc/validation/RESULTS.json` and `RESULTS.txt` | Author-supplied runtime reports |
| `article/anc/README.txt` | Reproduction instructions and limitations |
| `article/LICENSING_SCOPE.txt` | Original file-level license scopes |
| `CITATION.cff` | Preferred citation to the preprint |
| `LICENSE` | Repository licensing index |

For optional reproduction, follow [the supplementary README](article/anc/README.txt) from the **`article/anc/` directory**, where the runner and core files are located. The software uses Python's standard library. No research code, tests, simulation or proof checker was executed to prepare this repository.

## Validation evidence

The supplied reports record **284 completed checks, all PASS**, from the author's Windows CPython 3.14.7 run on 6 November 2026. The core and runner hashes match the versions accompanying those reports. The reports do not include a terminal process exit code.

Finite checks support implementation consistency; they are not an all-input proof or independent peer review. The vertex enumerator obtains the face count from the Euler relation, rather than independently enumerating geometric faces. The mathematical argument is in the preprint.

## Publication and file provenance

The PDF and all files under `article/` preserve the v08 preparation files byte-for-byte. New repository-level documentation is provided separately in this README, `CITATION.cff` and `LICENSE`.

Some preserved notices describe the earlier preparation stage: `article/LICENSE-CC-BY-4.0.txt` says that no HV27 public DOI had yet been assigned, and `article/anc/README.txt` does not claim a public submission. Those statements record the preparation stage and are superseded by the published preprint DOI **10.5281/zenodo.24014501**. The PDF retains its original “author-review copy v08” label. It remains a preprint; independent human peer review is not claimed.

## Author contribution and AI assistance

The author supplied the motivating mathematical idea, initial hypotheses and starting basis, and pursued the investigation with AI assistance. **ChatGPT (OpenAI)** and **Claude (Anthropic)** assisted across calculations, proof arguments, exposition, literature comparison and supplementary code. The paper gives the full disclosure. Completed personal verification of every proof step is not asserted; AI tools are not authors.

## Licenses

| Material | License |
|---|---|
| Article PDF, manuscript source and identified separate documentation; new root README, citation metadata and licensing index | **CC BY 4.0**, to the extent of rights held by the author |
| `article/anc/hv27_torus_counts.py`, `article/anc/run_hv27_checks.py`, `article/anc/RUN_HV27_WINDOWS.bat` | **MIT** |
| Supplied validation reports | CC BY 4.0 only to the extent of applicable rights held by the author; factual results remain facts |

See [the licensing index](LICENSE), [CC BY notice](article/LICENSE-CC-BY-4.0.txt), [MIT notice](article/anc/LICENSE) and [original scope notice](article/LICENSING_SCOPE.txt). These are separate file scopes, not a choice of either license for every file. No new exclusive rights are asserted in mathematical facts or file hashes. Third-party publications and external dependencies retain their own rights and licenses.

## Cite the preprint

Walke, Rushikesh Murlidhar. (2026). *An Explicit GCD Evaluation for Three-Direction Torus Arrangements* (Version v08). Zenodo. https://doi.org/10.5281/zenodo.24014501

Use the version DOI above when citing this particular release. [CITATION.cff](CITATION.cff) supplies the preferred article citation for GitHub's citation feature.

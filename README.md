# HV27 — Three-Direction Torus Arrangements

Supplementary code and manuscript for **An Explicit GCD Evaluation for Three-Direction Torus Arrangements**, by **Rushikesh Murlidhar Walke**, Independent Researcher, Maharashtra, India.

- [Read the v09 appendix on GitHub (author’s PDF)](v09/HV27_Appendix_Author_Copy.pdf) or [cite the Zenodo v09 deposit](https://doi.org/10.5281/zenodo.24061769) (9 November 2026).
- [Browse the v09 numerical tables](#v09-numerical-tables) for the two boundary sets, the four partition results and the one-step edit counts.
- [Reproduce the v08 software checks](article/anc/README.txt) or [read the original v08 paper](HV27_Preprint_Review_v08.pdf).
- [Independent reading guide · मराठी / English (one-page PDF)](HV27_v09_Review_Guide_MR_EN.pdf). Start with the boundary example on page 6 of the appendix. Sections 2 and 3 explain how faces correspond to five-label records and how to count valid one-step changes.
- [Report a discrepancy or counterexample](https://github.com/Rmwalke/hv27-torus-arrangements/issues). Please include the version, page or section, the case you checked and the result you obtained.

[Author ORCID](https://orcid.org/0009-0006-6749-5660) · [All Zenodo versions](https://doi.org/10.5281/zenodo.24014500)

## Interactive companion

Explore the v08 paper and v09 appendix with the H-v27 Torus Lab, an educational demonstration.

- [English edition](https://hv27-torus-lab.rushikeshwalkehtc.chatgpt.site/english/)
- [Trilingual edition (English, हिन्दी, मराठी)](https://hv27-torus-lab.rushikeshwalkehtc.chatgpt.site)

## Scope

The v08 paper gives an explicit gcd evaluation for three families of closed curves on a two-dimensional torus. It includes a finite-grid triple-intersection calculation, a cellularity argument and the passage from incidences to geometric faces. It is an explicit specialization of established toric-arrangement and arithmetic-Tutte theory, with a self-contained proof and parameterized example. It does not claim a new general chamber-counting theory.

Its relationship to the author's earlier cyclic-grid note is explained in the paper. That earlier work has DOI [10.5281/zenodo.23184983](https://doi.org/10.5281/zenodo.23184983); it is a separate publication.

The v09 appendix studies realizable combinations of five labels and counts which single-label edits are detectable under its stated sampling rule. The code and 284 recorded checks in this repository cover the v08 implementation. Independent human review of the appendix is pending.

## v09 numerical tables

These CSV files transcribe values reported by Rushikesh Murlidhar Walke in *Counting five-label records and detecting one-step errors on the Sun–Moon torus*. Page numbers refer to the six-page appendix. Independent computational reproduction of these tables remains open.

| CSV | Appendix | How to read it |
|---|---|---|
| [J2000 mansion boundaries](v09/j2000_mansion_boundaries.csv) | p. 6 | The 27 numbered rows give right endpoints in sidereal degrees for H20 and H21, to eight decimal places. Row 1 is Ashvini and row 27 is Revati. Each arc includes the preceding endpoint and excludes its own right endpoint, wrapping through zero. |
| [Reported results for four partitions](v09/published_model_results.csv) | p. 2 | For each partition, `v` counts distinct mansion and rashi boundaries together, `q` counts those on the one-third-degree lattice, and `C` counts distinct realizable five-label records. The last two columns give the exact numerator and denominator of the detection probability. |
| [One-step edit counts](v09/one_step_edit_counts.csv) | p. 4 | The first five counts are unordered pairs differing in one label. The last two count detected and total directed edits. The second row applies separately to H20, H21 and the shifted equal grid. |

The probability gives equal weight to each distinct realizable record, each label and each of the two edit directions. The files contain summary counts and boundary inputs. The complete lists of individual records and a v09 verification program are outside this release.

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

The original v08 PDF and all files under `article/` preserve the v08 preparation files byte-for-byte. The bilingual reading guide is a companion to the v09 appendix. The v09 PDF in this repository is the author’s manuscript copy. Its six pages of text match the Zenodo download previously checked. The deposited PDF additionally contains embedded Content Credentials and has a different file checksum. Cite the [deposited version](https://doi.org/10.5281/zenodo.24061769) for v09.

Some preserved notices describe the earlier preparation stage: `article/LICENSE-CC-BY-4.0.txt` says that no HV27 public DOI had yet been assigned, and `article/anc/README.txt` does not claim a public submission. Those statements record the preparation stage and are superseded by the published preprint DOI **10.5281/zenodo.24014501**. The v08 PDF retains its original “author-review copy v08” label. It remains a preprint; independent human peer review is not claimed.

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

Walke, Rushikesh Murlidhar. (2026). *An Explicit GCD Evaluation for Three-Direction Torus Arrangements* (Version v09). Zenodo. https://doi.org/10.5281/zenodo.24061769

[CITATION.cff](CITATION.cff) gives v09 as the preferred article citation. For a run of the original software, identify the software as v08 and cite the [v08 deposit](https://doi.org/10.5281/zenodo.24014501).

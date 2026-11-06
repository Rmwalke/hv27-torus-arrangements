"""HV27 offline finite consistency checks, v01 (2026-11-06).

Prepared by source inspection only: not executed during preparation.
Run with an installed Python 3.8+ using: python -I -S -B run_hv27_checks.py
No third-party packages, network, shell commands, or data deserialization.
Writes only new report files in a new directory beside this script.
"""

import sys
from datetime import datetime, timezone
from fractions import Fraction  # Preload the core's dependency before local import.
from hashlib import sha256
import json
from math import gcd
from pathlib import Path
from time import perf_counter


CORE_SHA256 = "4ddf34683d88d24c0720b831b30cc5319245485783678efb08f09198503296e2"
PLANNED_CHECKS = 284
EXPECTED_F = (
    5256, 5280, 5640, 5256, 5814, 5592, 5814, 5988, 6162,
    5256, 6324, 6336, 6264, 6336, 6684, 6264, 6858, 6672,
    6858, 7032, 7194, 6264, 7380, 7380, 7380, 7272,
)
GENERIC_CASES = (
    (2, 2, 1, 1), (1, 1, 2, 2), (3, 2, 4, 5), (5, 3, 6, 4),
    (4, 6, 5, 7), (6, 4, 8, 10), (7, 5, 9, 6), (1, 2, 1, 3),
)


def new_result_directory(base):
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
    for suffix in range(1000):
        path = base / ("HV27_RESULTS_" + stamp + "_" + str(suffix))
        try:
            path.mkdir()
            return path
        except FileExistsError:
            continue
    raise OSError("Could not create a fresh report directory")


def add_check(report, name, passed, details, show=True):
    status = "PASS" if passed else "FAIL"
    report["checks"].append({"name": name, "status": status, "details": details})
    if show or not passed:
        print(status + "  " + name, flush=True)


def compare_counts(report, core, name, parameters, expected=None, expected_f=None):
    N, R, Y, K = parameters
    formula = core.closed_form_counts(N, R=R, Y=Y, K=K)
    enumerated = core.exact_arrangement_counts(N, R=R, Y=Y, K=K)
    passed = formula == enumerated
    if expected is not None:
        passed = passed and formula == expected
    if expected_f is not None:
        passed = passed and formula["F"] == expected_f
    add_check(report, name, passed, {
        "parameters": {"N": N, "R": R, "Y": Y, "K": K},
        "formula": formula, "enumerated": enumerated,
        "expected_counts": expected, "expected_F": expected_f,
    })


def run_checks(report, core):
    print("Checking two hand-derived examples...", flush=True)
    compare_counts(report, core, "known_all_one", (1, 1, 1, 1),
                   expected={"nv": 1, "T": 1, "V": 2, "E": 5, "F": 3})
    compare_counts(report, core, "known_HV27", (27, 12, 27, 60),
                   expected={"nv": 36, "T": 108, "V": 6156, "E": 12420, "F": 6264})

    print("Comparing all default cases N=15..40...", flush=True)
    for N, expected_f in enumerate(EXPECTED_F, start=15):
        compare_counts(report, core, "default_N=" + str(N), (N, 12, 27, 60),
                       expected_f=expected_f)

    print("Checking eight nondefault parameter cases...", flush=True)
    for index, parameters in enumerate(GENERIC_CASES, start=1):
        compare_counts(report, core, "generic_" + str(index), parameters)

    print("Checking pure-grid TT(n) by integer congruences, n=1..200...", flush=True)
    Y, K = 27, 60
    for n in range(1, 201):
        # For u=i/n and x+y=j/Y, x-y is in G_K exactly when
        # K*(2*i*Y-j*n) is divisible by n*Y. No Fraction enumeration here.
        counted = sum(
            1 for i in range(n) for j in range(Y)
            if (K * (2 * i * Y - j * n)) % (n * Y) == 0
        )
        expected = 3 * gcd(n, 1080)
        add_check(report, "pure_TT_n=" + str(n), counted == expected,
                  {"n": n, "Y": Y, "K": K,
                   "integer_enumeration": counted, "expected": expected}, show=False)
        if n % 50 == 0:
            print("Completed TT through n=" + str(n), flush=True)

    print("Checking input validation (48 cases)...", flush=True)
    bad_values = ((0, ValueError), (-1, ValueError), (True, TypeError),
                  (1.5, TypeError), ("2", TypeError), (None, TypeError))
    for function in (core.closed_form_counts, core.exact_arrangement_counts):
        for parameter in ("N", "R", "Y", "K"):
            for value, expected_error in bad_values:
                arguments = {"N": 27, "R": 12, "Y": 27, "K": 60}
                arguments[parameter] = value
                actual_error = "NO_EXCEPTION"
                try:
                    function(**arguments)
                except Exception as error:
                    actual_error = type(error).__name__
                add_check(report, "input_" + function.__name__ + "_" + parameter
                          + "_" + repr(value), actual_error == expected_error.__name__,
                          {"parameter": parameter, "value_repr": repr(value),
                           "expected_exception": expected_error.__name__,
                           "actual_exception": actual_error}, show=False)


def save_reports(directory, report):
    # Exclusive creation prevents overwriting any existing result file.
    with (directory / "RESULTS.json").open("x", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2, ensure_ascii=True)
        handle.write("\n")
    with (directory / "RESULTS.txt").open("x", encoding="utf-8") as handle:
        handle.write("HV27 OFFLINE CHECKS v01\n")
        handle.write("Overall status: " + report["status"] + "\n")
        for key, value in report.items():
            if key not in ("checks", "status"):
                handle.write(key + ": " + json.dumps(value, ensure_ascii=True) + "\n")
        handle.write("\nALL COMPLETED CHECKS\n")
        for check in report["checks"]:
            handle.write(check["status"] + "  " + check["name"] + "  "
                         + json.dumps(check["details"], sort_keys=True) + "\n")


def main():
    base = Path(__file__).resolve().parent
    try:
        directory = new_result_directory(base)
    except OSError:
        print("ERROR: Cannot create reports. Extract into a writable local folder.")
        return 2

    start = perf_counter()
    report = {
        "runner_version": "HV27 offline checks v01, 2026-11-06",
        "preparation": "Source reviewed only; not executed during preparation.",
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "python_version": list(sys.version_info[:3]),
        "python_implementation": sys.implementation.name,
        "platform": sys.platform,
        "expected_core_sha256": CORE_SHA256,
        "planned_checks": PLANNED_CHECKS,
        "checks": [], "status": "ERROR",
        "scope": "Finite consistency evidence only; not proof, novelty or peer review.",
        "face_count_limit": "The enumerator derives F=E-V; it does not independently enumerate faces.",
        "pure_TT_limit": "Pure TT(n) concerns G_n alone, not the union G_n plus G_12.",
    }
    exit_code = 2
    try:
        if sys.version_info < (3, 8):
            raise RuntimeError("Python 3.8 or newer is required")
        if not (sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode):
            raise RuntimeError("Use the supplied launcher, or python3 -I -S -B run_hv27_checks.py")

        report["runner_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
        source = base / "hv27_torus_counts.py"
        if source.is_symlink():
            raise RuntimeError("Use the supplied regular source file, not a symbolic link")
        report["core_sha256"] = sha256(source.read_bytes()).hexdigest()
        if report["core_sha256"] != CORE_SHA256:
            raise RuntimeError("Core source hash mismatch: stopped BEFORE import")
        # A source hash alone cannot authenticate an existing bytecode cache.
        for name in ("__pycache__", "hv27_torus_counts.pyc", "hv27_torus_counts"):
            if (base / name).exists():
                raise RuntimeError("Use a fresh extraction: unexpected cache or package found")
        for entry in base.iterdir():
            if entry.name.lower().startswith("hv27_torus_counts.") and entry.name != source.name:
                raise RuntimeError("Use a fresh extraction: an alternate core module was found")

        sys.path.insert(0, str(base))
        try:
            import hv27_torus_counts as core
        finally:
            sys.path.pop(0)
        if Path(core.__file__).resolve() != source.resolve():
            raise RuntimeError("Unexpected imported source location")
        report["core_integrity"] = "MATCHED_BEFORE_IMPORT"
        run_checks(report, core)
        if len(report["checks"]) != PLANNED_CHECKS:
            raise RuntimeError("Incomplete planned check count")
        report["status"] = ("PASS" if all(c["status"] == "PASS" for c in report["checks"])
                            else "FAIL")
        exit_code = 0 if report["status"] == "PASS" else 1
    except KeyboardInterrupt:
        report["status"] = "INTERRUPTED"
        report["error"] = "Interrupted by user; checks are incomplete."
        exit_code = 130
    except Exception as error:
        report["status"] = "ERROR"
        # OS error messages can contain private paths; omit their message from portable logs.
        report["error"] = type(error).__name__
        if not isinstance(error, OSError):
            report["error"] += ": " + str(error)

    report["finished_utc"] = datetime.now(timezone.utc).isoformat()
    report["elapsed_seconds"] = round(perf_counter() - start, 3)
    report["completed_checks"] = len(report["checks"])
    report["passed_checks"] = sum(c["status"] == "PASS" for c in report["checks"])
    report["failed_checks"] = sum(c["status"] == "FAIL" for c in report["checks"])
    try:
        save_reports(directory, report)
    except OSError:
        print("ERROR: Reports could not be fully saved. Do not treat this run as confirmed.")
        return 2
    print("\nOverall: " + report["status"], flush=True)
    print("Completed: " + str(report["completed_checks"]) + "/" + str(PLANNED_CHECKS))
    if "error" in report:
        print(report["error"])
    print("Reports folder: " + directory.name)
    print("Share RESULTS.txt and RESULTS.json for review.")
    return exit_code


if __name__ == "__main__":
    sys.exit(main())

@echo off
setlocal EnableExtensions DisableDelayedExpansion
title HV27 Offline Checks
cd /d "%~dp0"
if errorlevel 1 goto location_error
rem Use an already installed Python only. Do not request automatic installation.
set "PYTHON_MANAGER_AUTOMATIC_INSTALL=false"
set "PYTHON_MANAGER_SHEBANG_CAN_RUN_ANYTHING=false"
set "PYLAUNCHER_ALLOW_INSTALL="
set "PYLAUNCHER_ALWAYS_INSTALL="
set "PYLAUNCHER_DRYRUN="
echo HV27 offline checks. Keep internet disconnected during the run.
echo No pip, installer or download commands are included.
echo.
py -3 -I -S -B --version >nul 2>&1
if not errorlevel 1 goto run_py
python -I -S -B --version >nul 2>&1
if not errorlevel 1 goto run_python
echo ERROR: An installed Python 3 could not be found.
echo See START_HERE_MR.txt. No results have been confirmed.
set "HV27_EXIT=2"
goto finish
:run_py
py -3 -I -S -B "%~dp0run_hv27_checks.py"
set "HV27_EXIT=%errorlevel%"
goto finish
:run_python
python -I -S -B "%~dp0run_hv27_checks.py"
set "HV27_EXIT=%errorlevel%"
goto finish
:location_error
echo ERROR: Extract the complete ZIP into a writable local folder first.
set "HV27_EXIT=2"
:finish
echo.
echo Exit code: %HV27_EXIT%
echo 0 = all checks passed and reports saved; any other code needs review.
echo.
pause
exit /b %HV27_EXIT%

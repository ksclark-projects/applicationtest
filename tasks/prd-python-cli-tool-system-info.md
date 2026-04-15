[PRD]
# PRD: Python CLI Tool — System Info

## Overview

A lightweight CLI tool for developers that displays Python version information directly in the terminal. Invoked as `python main.py` with optional flags, it targets technical users and outputs plain, human-readable text. No packaging or installation required — runs in-place.

## Goals

- Display Python version information clearly in the terminal
- Support flag-based invocation (e.g. `--version`, `--all`)
- Output plain human-readable text using `colorama` for color accents
- Maintain a passing `pytest` test suite

## Quality Gates

These commands must pass for every user story:

- `python -m pytest` — runs all unit tests

## User Stories

### US-001: Display Python version via default command

**Description:** As a developer, I want to run `python main.py` and see the current Python version so that I can quickly confirm my environment.

**Acceptance Criteria:**

- [ ] Running `python main.py` prints the Python version (e.g. `Python 3.14.2`)
- [ ] Output is plain text, human-readable
- [ ] Uses `sys.version_info` for structured version access
- [ ] Output includes major, minor, and micro version numbers

### US-002: Add `--version` flag

**Description:** As a developer, I want to run `python main.py --version` and see just the version string so that I can use it in scripts or verify quickly.

**Acceptance Criteria:**

- [ ] `python main.py --version` prints only the version string (e.g. `3.14.2`)
- [ ] No extra labels or formatting — just the version number
- [ ] Uses `argparse` to handle the flag
- [ ] Exits with code 0 on success

### US-003: Add `--all` flag for full info display

**Description:** As a developer, I want to run `python main.py --all` to see a full summary of my Python environment so that I can debug environment issues quickly.

**Acceptance Criteria:**

- [ ] `python main.py --all` displays: Python version, version info tuple, and platform string
- [ ] Output uses `colorama` to colorize labels (e.g. label in cyan, value in white)
- [ ] Falls back to plain text if `colorama` is not installed
- [ ] Each piece of info is on its own labeled line

### US-004: Add `--help` flag with usage documentation

**Description:** As a developer, I want `python main.py --help` to show available flags so that I can discover what the tool can do.

**Acceptance Criteria:**

- [ ] `--help` prints a usage summary listing `--version` and `--all`
- [ ] Each flag has a short description
- [ ] Handled automatically by `argparse`

### US-005: Write unit tests for CLI behavior

**Description:** As a developer, I want a `pytest` test suite that validates the CLI output so that regressions are caught automatically.

**Acceptance Criteria:**

- [ ] Test file exists at `tests/test_main.py`
- [ ] Tests verify `--version` returns a valid semver string (e.g. matches `\d+\.\d+\.\d+`)
- [ ] Tests verify default run includes "Python" in output
- [ ] Tests verify `--all` output contains platform info
- [ ] All tests pass with `python -m pytest`

## Functional Requirements

- FR-1: The tool must accept `--version`, `--all`, and `--help` flags via `argparse`
- FR-2: Default invocation (`python main.py`) must print the Python version
- FR-3: `--version` must output only the version number string, nothing else
- FR-4: `--all` must print Python version, version info tuple, and platform string
- FR-5: Color output must use `colorama` and gracefully degrade if unavailable
- FR-6: All exit codes must be `0` on success, non-zero on error
- FR-7: A `tests/` directory with `pytest`-compatible tests must exist

## Non-Goals

- No OS/platform info beyond `--all` flag
- No installed packages listing
- No JSON or machine-readable output format
- No `pip install` packaging or standalone executable
- No interactive menus or prompts
- No network calls or remote version checks

## Technical Considerations

- Use `argparse` (stdlib) — no extra CLI framework needed
- Use `colorama` for color output; add to `requirements.txt`
- Use `sys.version_info` for structured version data
- Use `platform.platform()` for platform string in `--all`
- Keep all logic in `main.py` for simplicity; tests in `tests/test_main.py`
- Use `subprocess` or `importlib` in tests to invoke CLI and capture stdout

## Success Metrics

- `python -m pytest` passes with 0 failures
- All three flags (`--version`, `--all`, `--help`) work as documented
- Color output renders correctly on macOS terminal

## Open Questions

- Should `colorama` be auto-installed if missing, or just silently skip colors?
- Should `--all` output be extensible in the future (e.g. add `--packages` later)?
[/PRD]

# CI/CD Pipeline - GitHub Actions

Automated testing, quality checks, benchmarking, and deployment workflows.

## Workflows Overview

### 1. **Tests** (`tests.yml`)
Runs on every push and pull request to `main` and `develop` branches.

**What it does:**
- ✅ Tests across Python 3.9, 3.10, 3.11
- ✅ Lints with flake8
- ✅ Type checks with mypy
- ✅ Format checks with black
- ✅ Runs pytest with coverage
- ✅ Uploads coverage to Codecov
- ✅ Archives coverage reports as artifacts

**Trigger:**
```yaml
- Push to main or develop
- Pull request to main or develop
```

**Artifacts:**
- `coverage-reports-py*.zip` - HTML coverage reports

**Output:**
- Test results in GitHub Actions UI
- Coverage badge (if configured in Codecov)

---

### 2. **Code Quality** (`code-quality.yml`)
Analyzes code quality and reports issues.

**What it does:**
- ✅ Checks code formatting (black)
- ✅ Lints code (flake8)
- ✅ Type checks (mypy)
- ✅ Static analysis (pylint)
- ✅ Counts TODOs and FIXMEs
- ✅ Posts summary in GitHub step summary

**Trigger:**
```yaml
- Push to main or develop
- Pull request to main or develop
```

**Output:**
- Code quality report in GitHub Actions UI
- TODO/FIXME count and locations
- Lint issues and recommendations

---

### 3. **Documentation** (`docs.yml`)
Builds and deploys documentation.

**What it does:**
- ✅ Builds Sphinx documentation
- ✅ Archives documentation as artifact
- ✅ Deploys to GitHub Pages (on main push)

**Trigger:**
```yaml
- Push to main
- Pull request to main
```

**Artifacts:**
- `documentation` - HTML documentation

**Deploy:**
- Automatically deployed to GitHub Pages when pushed to main
- URL: `https://<owner>.github.io/<repo>/`

---

### 4. **Performance Benchmarks** (`benchmarks.yml`)
Runs algorithm benchmarks and generates comparisons.

**What it does:**
- ✅ Runs all 4 algorithm benchmarks
- ✅ Generates visualization charts
- ✅ Archives results and visualizations
- ✅ Comments results on PRs

**Trigger:**
```yaml
- Push to main
- Pull request to main
- Weekly schedule (Mondays at 00:00 UTC)
```

**Artifacts:**
- `benchmark-results-<run-number>` - Results and charts

**Schedule:**
Edit cron to change frequency:
```yaml
schedule:
  - cron: '0 0 * * 1'  # Weekly Monday
  # - cron: '0 0 * * *'  # Daily
  # - cron: '0 */6 * * *'  # Every 6 hours
```

---

### 5. **Release** (`release.yml`)
Automates version releases and PyPI publishing.

**What it does:**
- ✅ Builds distribution packages
- ✅ Creates GitHub Release
- ✅ Publishes to PyPI

**Trigger:**
```yaml
- Push tag matching v*.*.* (e.g., v1.0.0)
```

**Example Usage:**
```bash
# Create and push a release
git tag v1.0.0
git push origin v1.0.0
```

**Note:** Requires `PYPI_API_TOKEN` secret in repository settings.

---

## Setup Instructions

### 1. **Initial Setup**
All workflows are ready to use - no additional setup needed! They activate automatically when pushed to the repository.

### 2. **Configure Secrets** (for Release)
For PyPI publishing, add a secret to your GitHub repository:

1. Go to: `Settings → Secrets and variables → Actions`
2. Create new secret: `PYPI_API_TOKEN`
3. Get token from: https://pypi.org/account/ (API Tokens section)
4. Paste token value

### 3. **Enable GitHub Pages** (for Documentation)
1. Go to: `Settings → Pages`
2. Set Source: `Deploy from a branch`
3. Select Branch: `gh-pages` (created automatically by workflow)
4. Directory: `/ (root)`
5. Click Save

### 4. **Configure Codecov** (Optional, for Coverage Badges)
1. Go to: https://codecov.io
2. Sign in with GitHub
3. Select repository
4. Copy coverage badge code

---

## Status Badges

Add these badges to your `README.md` to show CI/CD status:

```markdown
[![Tests](https://github.com/MagePro310/Quantum_Simulation_Scheduling_ver1/actions/workflows/tests.yml/badge.svg)](https://github.com/MagePro310/Quantum_Simulation_Scheduling_ver1/actions/workflows/tests.yml)
[![Code Quality](https://github.com/MagePro310/Quantum_Simulation_Scheduling_ver1/actions/workflows/code-quality.yml/badge.svg)](https://github.com/MagePro310/Quantum_Simulation_Scheduling_ver1/actions/workflows/code-quality.yml)
[![Documentation](https://github.com/MagePro310/Quantum_Simulation_Scheduling_ver1/actions/workflows/docs.yml/badge.svg)](https://github.com/MagePro310/Quantum_Simulation_Scheduling_ver1/actions/workflows/docs.yml)
[![Benchmarks](https://github.com/MagePro310/Quantum_Simulation_Scheduling_ver1/actions/workflows/benchmarks.yml/badge.svg)](https://github.com/MagePro310/Quantum_Simulation_Scheduling_ver1/actions/workflows/benchmarks.yml)
```

---

## Workflow Files Structure

```
.github/workflows/
├── tests.yml              # Unit tests + coverage
├── code-quality.yml       # Linting & code quality
├── docs.yml               # Documentation build & deploy
├── benchmarks.yml         # Algorithm benchmarks
├── release.yml            # Version releases & PyPI
└── README.md              # This file
```

---

## Performance Considerations

### Tests Workflow
- **Duration:** ~5-10 minutes (3 Python versions)
- **Cost:** Low (shared runners)
- **Parallelization:** Runs on 3 Python versions in parallel

### Code Quality Workflow
- **Duration:** ~2-3 minutes
- **Cost:** Low
- **Parallelization:** All checks run sequentially

### Benchmarks Workflow
- **Duration:** ~15-20 minutes (all 4 algorithms)
- **Cost:** Medium (long-running)
- **Schedule:** Weekly to avoid frequent runs

### Documentation Workflow
- **Duration:** ~3-5 minutes
- **Cost:** Low
- **Deploy:** Only on main branch

### Release Workflow
- **Duration:** ~3-5 minutes
- **Cost:** Low
- **Trigger:** Manual (tag push)

---

## Customization

### Modify Python Versions
Edit `tests.yml`:
```yaml
strategy:
  matrix:
    python-version: ['3.9', '3.10', '3.11', '3.12']  # Add 3.12
```

### Change Test Arguments
Edit `tests.yml`:
```yaml
- name: Run tests with pytest
  run: |
    pytest tests/ -v --tb=short -k "not slow"  # Skip slow tests
```

### Adjust Benchmark Frequency
Edit `benchmarks.yml` cron schedule:
```yaml
schedule:
  - cron: '0 0 * * 1'  # Monday
  # - cron: '0 0 * * *'  # Every day
  # - cron: '0 */12 * * *'  # Every 12 hours
```

### Modify Lint Rules
Edit `code-quality.yml` flake8 options:
```yaml
flake8 component/ flow/ benchmarks/ tests/ \
  --max-line-length=120 \
  --extend-ignore=E203,W503 \
  --count --statistics
```

---

## Troubleshooting

### Tests Fail Locally but Pass in CI
- Check Python version matches CI (usually 3.10)
- Clear pip cache: `pip cache purge`
- Recreate venv: `rm -rf venv && python -m venv venv`
- Install deps: `pip install -e ".[dev]"`

### Coverage Not Uploading
- Verify `codecov/codecov-action` version (currently v3)
- Check if repository is public or configured for Codecov
- Run locally: `pytest --cov=component --cov-report=xml`

### Benchmarks Timeout
- Reduce job count in `runLoopTestFFD.py` args (currently 3)
- Run only one algorithm instead of all 4
- Increase GitHub Actions timeout (default 360 minutes)

### Documentation Build Fails
- Check Sphinx configuration in `docs/conf.py`
- Verify all imports work
- Test locally: `cd docs && make html`

### Release Not Publishing to PyPI
- Verify `PYPI_API_TOKEN` is set in GitHub Settings
- Check token is not expired
- Verify tag format matches `v*.*.*`
- Check `twine check dist/*` passes locally

---

## Best Practices

### ✅ Do
- Run tests locally before pushing
- Create descriptive commit messages
- Keep branches up-to-date with main
- Review CI output before merging
- Use semantic versioning for releases

### ❌ Don't
- Ignore CI failures
- Force-push to main
- Skip test coverage
- Commit broken code
- Deploy without testing

---

## Useful Commands

### View Workflow Status
```bash
# GitHub CLI (if installed)
gh run list
gh run view <run-id>

# Or visit:
# https://github.com/MagePro310/Quantum_Simulation_Scheduling_ver1/actions
```

### Re-run Failed Workflow
```bash
# GitHub CLI
gh run rerun <run-id>

# Or click "Re-run jobs" in GitHub UI
```

### Create Release
```bash
git tag v1.0.0
git push origin v1.0.0
# Workflow will automatically:
# 1. Build packages
# 2. Create GitHub Release
# 3. Publish to PyPI
```

---

## Monitoring

### Check GitHub Actions Usage
- Go to: `Settings → Billing and plans`
- View: "Actions usage this month"

### Set Notifications
- Go to: `Settings → Notifications`
- Choose: Email/Web notifications for workflow status

### Status Page
- Open: https://www.githubstatus.com for GitHub service status

---

## Support

For workflow issues:
1. Check GitHub Actions documentation: https://docs.github.com/actions
2. Review workflow logs in GitHub UI
3. Test locally with `act`: https://github.com/nektos/act
4. File issue in repository

---

## See Also

- [GitHub Actions Documentation](https://docs.github.com/actions)
- [Action Marketplace](https://github.com/marketplace?type=actions)
- [Workflow Syntax](https://docs.github.com/actions/using-workflows/workflow-syntax-for-github-actions)
- [PyPI Publishing](https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions/)

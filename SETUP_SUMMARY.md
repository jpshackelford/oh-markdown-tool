# PyPI Publishing Setup Summary

## ✅ What's Been Configured

Your repository is now fully configured for automated PyPI publishing with Release Please!

### New Files Created

1. **`.github/workflows/release-please.yml`** - Automates release PR creation
2. **`.release-please-manifest.json`** - Tracks current version
3. **`release-please-config.json`** - Configures Release Please behavior
4. **`CHANGELOG.md`** - Initial changelog (will be auto-updated)
5. **`PUBLISHING.md`** - Complete publishing guide

### Modified Files

1. **`.github/workflows/release.yml`** - Updated to trigger on GitHub releases
2. **`Makefile`** - Added build/publish commands
3. **`README.md`** - Added conventional commit guidelines

### Existing Configuration (Already Good!)

✅ `pyproject.toml` - Perfect metadata and dependencies  
✅ CI workflow - Tests and linting in place  
✅ Trusted Publishing setup - Secure PyPI authentication configured  
✅ Package structure - Proper `src/` layout  

## 🚀 Next Steps

### 1. One-Time PyPI Setup (Required)

Before your first release, configure Trusted Publishing on PyPI:

1. **Create a PyPI account**: https://pypi.org/account/register/
2. **Set up Trusted Publishing**:
   - Go to: https://pypi.org/manage/account/publishing/
   - Click "Add a new pending publisher"
   - Fill in:
     - **PyPI Project Name**: `oh-markdown-tool`
     - **Owner**: `jpshackelford`
     - **Repository name**: `oh-markdown-tool`
     - **Workflow name**: `release.yml`
     - **Environment name**: `pypi`
   - Click "Add"

This reserves the package name and allows GitHub Actions to publish without API tokens!

### 2. Push Your Changes

```bash
# Review changes
git status
git diff

# Commit with conventional commit format
git add .
git commit -m "chore: configure Release Please for automated PyPI publishing"

# Push to GitHub
git push origin main
```

### 3. Verify Release Please is Working

After pushing:
- Go to: https://github.com/jpshackelford/oh-markdown-tool/actions
- Check that "Release Please" workflow ran successfully
- It may not create a PR yet (since you started at 0.1.0 with a `chore:` commit)

### 4. Make a Change to Trigger a Release

```bash
# Make any change (example: update README)
echo "\nUpdated!" >> README.md

# Commit with a conventional commit that triggers a release
git add README.md
git commit -m "feat: add publishing documentation"
git push origin main
```

After this push:
- Release Please will create a PR titled "chore(main): release 0.2.0"
- Review the PR to see auto-generated version bump and changelog
- Merge the PR when ready → **automatic PyPI publish!**

## 📖 How to Use Release Please

### Daily Workflow

1. **Make changes** and commit with conventional commit messages:
   ```bash
   git commit -m "feat: add new operation"
   git commit -m "fix: correct TOC generation bug"
   ```

2. **Push to main**:
   ```bash
   git push origin main
   ```

3. **Release Please creates/updates a Release PR** automatically
   - Reviews the changelog and version bump
   - Merges when ready

4. **Automatic publish to PyPI** when PR is merged!

### Commit Message Format

```bash
feat:     # New feature → minor version bump (0.1.0 → 0.2.0)
fix:      # Bug fix → patch version bump (0.1.0 → 0.1.1)
feat!:    # Breaking change → major version bump (0.1.0 → 1.0.0)

docs:     # Documentation (in changelog, no version bump alone)
refactor: # Code refactoring (in changelog, no version bump alone)
test:     # Tests (in changelog, no version bump alone)
chore:    # Maintenance (hidden from changelog)
```

### Version Bumping Rules

- `fix:` commits → **Patch** bump (0.1.0 → 0.1.1)
- `feat:` commits → **Minor** bump (0.1.0 → 0.2.0)
- `feat!:` or commits with `BREAKING CHANGE:` → **Major** bump (0.1.0 → 1.0.0)
- Multiple commits are batched into a single release

## 🛠️ Manual Publishing (Alternative)

If you need to test locally or bypass automation:

```bash
# Build the package
make build

# Test on TestPyPI first
make publish-test

# Publish to production PyPI
make publish
```

See [PUBLISHING.md](PUBLISHING.md) for details on manual publishing with API tokens.

## 📚 Resources

- **Publishing Guide**: [PUBLISHING.md](PUBLISHING.md)
- **Release Please Docs**: https://github.com/googleapis/release-please
- **Conventional Commits**: https://www.conventionalcommits.org/
- **PyPI Trusted Publishing**: https://docs.pypi.org/trusted-publishers/

## ❓ Questions?

- Check the **Troubleshooting** section in [PUBLISHING.md](PUBLISHING.md)
- Review Release Please GitHub Actions logs
- Test locally with `make build` before pushing

---

**You're all set!** 🎉 Just complete the PyPI Trusted Publishing setup and make your first conventional commit!

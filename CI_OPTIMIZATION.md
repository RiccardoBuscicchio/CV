# CI Workflow Optimization

## Baseline Profiling (before consolidation)

Recent successful runs measured from GitHub Actions metadata:

| Workflow | Run ID | Total runtime |
|---|---:|---:|
| `main.yml` (English) | 31632475160 | ~6.2 min |
| `main_ita.yml` (Italian) | 31632475048 | ~5.0 min |

Per-step timing from those runs (build job):

| Step | English | Italian |
|---|---:|---:|
| Checkout | ~1s | ~1s |
| Cache Conda environment | ~2s | ~2s |
| Set up conda | ~80s | ~42s |
| Python generation (connected) | ~71s | ~87s |
| Python short CV | ~3s | ~2s |
| LaTeX CV | ~1s | ~1s |
| LaTeX publist | ~1s | ~1s |
| LaTeX talklist | ~1s | ~1s |
| LaTeX CVshort | ~2s | ~1s |
| Upload artifacts | ~1s | ~1s |

Cache signal from latest sampled build jobs:
- `~/conda_pkgs_dir` + `/usr/share/miniconda3/envs/buildcv`: **2/2 cache hits (100% in sample)**

## Implemented Optimizations

### 1) Unified workflow for EN/IT builds

Replaced two near-duplicate workflows with one language-aware workflow:
- `.github/workflows/main.yml`

The unified workflow builds both languages through a matrix and keeps separate deploy targets:
- English deploy branch: `build`
- Italian deploy branch: `build_ita`

### 2) Change-aware execution

Added a `detect-changes` job to selectively run language builds:
- Shared source changes (`makeCV.py`, templates, shared tex/database/environment/workflow) → run **both** EN and IT
- Only `locales/en.json` changed → run **EN only**
- Only `locales/it.json` changed → run **IT only**
- Irrelevant-only changes → skip both builds

### 3) Deterministic conda cache reload with fallback

Conda setup now follows this sequence:
1. Restore cache for package dir + full env
2. Validate restored env quickly (`python --version`, imports)
3. If cache miss or validation fails, rebuild env from `environment.yml`
4. Re-validate env before execution

This prevents stale/broken cache restores from failing the pipeline.

### 4) Environment portability fix

Removed local machine-specific `prefix` from:
- `environment.yml`

This improves cross-runner cache stability and avoids path-coupled environment behavior.

### 5) Reduced LaTeX action overhead

Collapsed four separate LaTeX action invocations into one multi-root invocation per language build to reduce repeated container startup overhead.

## Cache Behavior and Invalidation

Conda cache key:
- `${{ runner.os }}-conda-env-${{ hashFiles('environment.yml') }}`

Cache is effectively invalidated when:
- `environment.yml` changes
- cache expires/evicts on GitHub side

## Troubleshooting

If CI time regresses:
1. Check `Cache Conda environment` for cache-hit/miss state
2. Check `Validate restored conda environment` outcome
3. If validation fails repeatedly, inspect environment rebuild logs and dependency resolution output
4. Confirm no unnecessary shared-file changes are forcing both language builds

## Optional Second-Stage Acceleration (not yet enabled)

- Prebuilt conda environment refresh workflow (scheduled/manual) for heavy dependency updates
- TeX auxiliary caching only if profiling shows repeated compile cost is significant

# RunThis

Run code from GitHub in one command.

## What It Does

```bash
runthis <github-url>
```

That's it. Clones the repo, reads the README, figures out how to run it, installs deps, runs it.

## Install

```bash
pip install runthis
```

## Setup

Run `runthis` once - it will prompt you to create `~/.config/runthis`:

```ini
openai_base_url=https://api.openai.com/v1  # or your OpenAI-compatible API (e.g., https://openrouter.ai/api/v1)
model=gpt-4o
key=sk-your-api-key-here
cache_dir=$HOME/runthis  # defaults to $HOME/runthis
```

## Directory Structure

RunThis creates the following directories in `~/.runthis` (or your configured `cache_dir`):

- `~/.runthis/pkgs/` - Where repositories are cloned
- `~/.runthis/bin/` - Executables from builds
- `~/.runthis/lib/` - Libraries
- `~/.runthis/include/` - Header files

## Use

```bash
# Run any GitHub project
runthis https://github.com/user/repo

# Want details?
runthis --verbose https://github.com/user/repo

# Skip installing deps (if you're feeling lucky)
runthis --no-install https://github.com/user/repo
```

## How It Works

1. Clones the repo to `~/.runthis/pkgs/`
2. Sends README to AI: "How do I run this?"
3. Installs whatever it needs (pip, npm, make, etc.)
4. Runs what the AI says
5. If running fails, asks AI how to fix (up to 3 tries) and installs needed tools/libs

## Warning

This is 1.0. YOLO mode. No sandbox. No safety. It runs whatever the AI says to run. It will install system packages via apt-get. Don't run random shit you don't trust.

## License

MIT

---

**One command to run them all.**

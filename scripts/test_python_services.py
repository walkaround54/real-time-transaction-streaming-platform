from pathlib import Path
import subprocess
import sys

ROOT_DIR = Path(__file__).resolve().parents[1]

PYTHON_APPS = [
    ROOT_DIR / "producer",
]

def run_command(command: list[str], cwd: Path) -> None:
    result = subprocess.run(
        command,
        cwd=cwd,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
        raise RuntimeError(f"Command failed in {cwd.name}: {' '.join(command)}")

def run_tests() -> None:
    for app_dir in PYTHON_APPS:
        print(f"Installing Python app for {app_dir.name}...")
        run_command([sys.executable, "-m", "pip", "install", "-e", ".[test]"], cwd=app_dir)

        print(f"Running Python tests for {app_dir.name}...")
        run_command([sys.executable, "-m", "pytest"], cwd=app_dir)
        print(f"Python tests passed for {app_dir.name}.")


if __name__ == "__main__":
    run_tests()
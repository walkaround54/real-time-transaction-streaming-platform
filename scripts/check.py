from scripts.update_project_tree import update_status_project_tree
import subprocess
import sys

def run_tests() -> None:
    print("Running Unit Tests...")
    result = subprocess.run(
        [sys.executable,"-m","pytest"],
        capture_output = True,
        text= True,
    )
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
        raise RuntimeError("Unit Tests Failed.")
    
    print("All Tests Passed.")

def main():
    print("Updating STATUS.md project tree section")
    update_status_project_tree()
    run_tests()

    print("Project checks completed successfully, STATUS.md updated.")

if __name__ == "__main__":
    main()

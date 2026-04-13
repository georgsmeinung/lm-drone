import subprocess
import sys
import os
import argparse
from datetime import datetime

# Default number of iterations
NUM_ITERATIONS = 3

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Run airsim_commander.py multiple times for flight simulation recreation."
    )
    parser.add_argument(
        "iterations",
        nargs="?",
        type=int,
        default=NUM_ITERATIONS,
        help=f"Number of times to run airsim_commander.py (default: {NUM_ITERATIONS})"
    )
    args = parser.parse_args()
    
    # Validate input
    if args.iterations <= 0:
        print(f"Error: Number of iterations must be positive. Got: {args.iterations}")
        sys.exit(1)
    
    return args.iterations

def run_iteration(iteration_num, script_path):
    """
    Run a single iteration of airsim_commander.py.
    
    Args:
        iteration_num: Current iteration number (1-indexed)
        script_path: Path to airsim_commander.py
    
    Returns:
        Tuple (success: bool, error_msg: str or None)
    """
    try:
        print(f"\n{'='*60}")
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting iteration {iteration_num}")
        print(f"{'='*60}")
        
        # Run the commander script
        result = subprocess.run(
            [sys.executable, script_path],
            cwd=os.path.dirname(script_path),
            capture_output=False,
            timeout=None
        )
        
        if result.returncode == 0:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Iteration {iteration_num} completed successfully.")
            return True, None
        else:
            error_msg = f"Iteration {iteration_num} exited with return code {result.returncode}"
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {error_msg}")
            return False, error_msg
    
    except subprocess.TimeoutExpired:
        error_msg = f"Iteration {iteration_num} timed out"
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error: {error_msg}")
        return False, error_msg
    
    except Exception as e:
        error_msg = f"Iteration {iteration_num} failed with exception: {str(e)}"
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error: {error_msg}")
        return False, error_msg

def main():
    """Main function to run multiple iterations of airsim_commander.py."""
    # Parse arguments
    num_iterations = parse_arguments()
    
    print(f"Starting airsim_iterator with {num_iterations} iteration(s)")
    print(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Get path to airsim_commander.py
    script_dir = os.path.dirname(os.path.abspath(__file__))
    commander_path = os.path.join(script_dir, "airsim_commander.py")
    
    if not os.path.exists(commander_path):
        print(f"Error: {commander_path} not found.")
        sys.exit(1)
    
    # Run iterations
    results = []
    for i in range(1, num_iterations + 1):
        success, error_msg = run_iteration(i, commander_path)
        results.append((i, success, error_msg))
    
    # Summary report
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"Total iterations: {num_iterations}")
    
    successful = sum(1 for _, success, _ in results if success)
    failed = sum(1 for _, success, _ in results if not success)
    
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    
    if failed > 0:
        print("\nFailed iterations:")
        for iter_num, success, error_msg in results:
            if not success:
                print(f"  - Iteration {iter_num}: {error_msg}")
    
    print(f"\nEnd time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")
    
    # Exit with appropriate code
    sys.exit(0 if failed == 0 else 1)

if __name__ == "__main__":
    main()

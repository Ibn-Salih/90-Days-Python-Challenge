# - Topics:
# - Basic concepts of reverse engineering and decompiling binaries.
# - Using tools like pyinstxtractor to extract Python bytecode from executables.
# - Project:
# - Extract the contents of a .exe file made with Python 
# - using pyinstxtractor and analyze its contents.


import os
import subprocess
import shutil
from pathlib import Path

# Path to pyinstxtractor.py (download from GitHub) you change this to specific path
PYINSTEXTRACTOR_PATH = "pyinstxtractor.py"

def extract_exe(exe_path):
    """Extract the contents of a .exe file using pyinstxtractor."""
    try:
        print(f"[+] Extracting {exe_path}...")
        result = subprocess.run(
            ["python", PYINSTEXTRACTOR_PATH, exe_path],
            capture_output=True,
            text=True,
        )
        if "Successfully extracted" in result.stdout:
            extracted_dir = exe_path + "_extracted"
            print(f"[+] Extraction successful. Files saved to {extracted_dir}")
            return extracted_dir
        else:
            print("[-] Extraction failed. Check the output below:")
            print(result.stdout)
            return None
    except Exception as e:
        print(f"[-] Error during extraction: {e}")
        return None

def find_pyc_files(directory):
    """Find all .pyc files in the extracted directory."""
    pyc_files = list(Path(directory).rglob("*.pyc"))
    if not pyc_files:
        print("[-] No .pyc files found in the extracted directory.")
    return pyc_files

def decompile_pyc(pyc_file, output_dir):
    """Decompile a .pyc file using uncompyle6."""
    try:
        output_file = os.path.join(output_dir, f"{pyc_file.stem}.py")
        print(f"[+] Decompiling {pyc_file} to {output_file}...")
        subprocess.run(
            ["uncompyle6", "-o", output_file, str(pyc_file)],
            check=True,
        )
        print(f"[+] Decompilation successful: {output_file}")
    except Exception as e:
        print(f"[-] Error decompiling {pyc_file}: {e}")

def main():
    # Input: Path to the .exe file
    exe_path = input("Enter the path to the .exe file: ").strip()
    if not os.path.isfile(exe_path):
        print("[-] Invalid file path.")
        return

    # Step 1: Extract the .exe file
    extracted_dir = extract_exe(exe_path)
    if not extracted_dir:
        return

    # Step 2: Find .pyc files in the extracted directory
    pyc_files = find_pyc_files(extracted_dir)
    if not pyc_files:
        return

    # Step 3: Decompile all .pyc files
    output_dir = os.path.join(extracted_dir, "decompiled")
    os.makedirs(output_dir, exist_ok=True)
    for pyc_file in pyc_files:
        decompile_pyc(pyc_file, output_dir)

    print(f"[+] Decompilation complete. Files saved to {output_dir}")

if __name__ == "__main__":
    main()
import subprocess
import sys
import os

def run_sqlmap(url):
    try:
        # Run SQLmap on the provided URL
        subprocess.run(['sqlmap', '-u', url, '--batch', '--output-dir=./sqlmap_output'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running SQLmap on {url}: {e}")

def main(input_path):
    # Check if the input is a file or a single URL
    if os.path.isfile(input_path):
        # Read URLs from the file
        with open(input_path, 'r') as file:
            urls = file.readlines()
            for url in urls:
                url = url.strip()
                if url:
                    run_sqlmap(url)
    else:
        # Treat the input as a single URL
        run_sqlmap(input_path)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python sqlmap_auto.py <url_or_file>")
    else:
        input_path = sys.argv[1]
        main(input_path)

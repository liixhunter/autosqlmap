# AutoSQLmap

## Overview
AutoSQLmap is a script designed to automate SQLmap scans for a list of URLs or a single URL. It aims to streamline your security testing workflow by running SQLmap scans with minimal effort.



## How to Use

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/liixhunter/sqlmap-auto-scanner.git
    cd sqlmap-auto-scanner
    ```

2. **Ensure SQLmap is Installed and Available in Your PATH:**
    - **Debian-based Systems:**
      ```
      sudo apt-get install sqlmap
      ```
    - **Fedora / RHEL / CentOS:**
      ```
      sudo yum install sqlmap
      ```
    - **Fedora / RHEL / CentOS (DNF):**
      ```
      sudo dnf install sqlmap
      ```
    - **Arch Linux:**
      ```
      sudo pacman -S sqlmap
      ```

3. **Provide a URL or a Text File Containing a List of URLs as an Argument When Running the Script:**

    - **Single URL:**
      ```
      python sqlmap_auto.py "http://example.com/vulnerable_page.php?id=1"
      ```

    - **List of URLs (in a file called `urls.txt`):**
      ```
      python sqlmap_auto.py urls.txt
      ```

## Important Notes:
- **Use Responsibly**: Only run SQLmap scans on systems you have explicit permission to test.
- **Output Directory**: The script saves the SQLmap output to a directory called `sqlmap_output`.

# autosqlmap

How to Use:
Clone the repository:

git clone https://github.com/liixhunter/sqlmap-auto-scanner.git
cd sqlmap-auto-scanner
Ensure SQLmap is installed and available in your PATH. :

sudo apt-get install sqlmap (Debian )
sudo yum install sqlmap (Fedora / RHEL / CentOS )
sudo dnf install sqlmap (Fedora / RHEL / CentOS )
sudo pacman -S sqlmap ( Arch linux)




Provide a URL or a text file containing a list of URLs as an argument when running the script.

Single URL:

python sqlmap_auto.py "http://example.com/vulnerable_page.php?id=1"
List of URLs (in a file called urls.txt):

python sqlmap_auto.py urls.txt

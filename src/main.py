from copystatic import ensure_clean_directory, copy_directory_to_another
from generatepage import generate_pages_recursive
import sys

def main():
    if len(sys.argv) == 2:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    ensure_clean_directory("docs")
    copy_directory_to_another("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()
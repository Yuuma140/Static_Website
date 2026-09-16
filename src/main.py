from copystatic import ensure_clean_directory, copy_directory_to_another
from generatepage import generate_pages_recursive

def main():
    ensure_clean_directory("public")
    copy_directory_to_another("static", "public")
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()
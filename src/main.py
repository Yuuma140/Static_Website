from copystatic import ensure_clean_directory, copy_directory_to_another
from generatepage import generate_page

def main():
    ensure_clean_directory("public")
    copy_directory_to_another("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()
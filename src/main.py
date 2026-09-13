from copystatic import ensure_clean_directory, copy_directory_to_another

def main():
    ensure_clean_directory("public")
    copy_directory_to_another("static", "public")


if __name__ == "__main__":
    main()
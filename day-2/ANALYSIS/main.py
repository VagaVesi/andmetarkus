from file_functions import FileFunctions


def main():

    file_path = r"/Users/vaga_vesi/Projects/andmetarkus2025/andmetarkus/day-2/ANALYSIS/request-log.txt"

    # filecontent = ""

    # with open(file_path, encoding='utf-8') as f:
    #     filecontent = f.read()

    # request_log_entries = filecontent.split("\n")

    request_log_entries = FileFunctions().read_file(file_path)

    for line in request_log_entries:
        print(line + "\n")

    row_count = len(request_log_entries)
    print(f"Logifailis on {row_count} rida.")

    FileFunctions().add_line_to_file(
        file_path, f"Logifailis on {row_count} rida.")


if __name__ == "__main__":
    main()

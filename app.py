import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()
    # Will continue printing lines until there are no more
    if line:
        # If line exits, call print line function
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    # Strip line of leading/ending whitespace
    next_lang = line.strip()
    # Why errors = errors?
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("sample.txt", encoding="utf-8")
main(languages, input_encoding, error)

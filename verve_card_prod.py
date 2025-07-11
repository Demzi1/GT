def card_format(input_file, outputfile):
    with open(input_file, 'r') as infile, open(outputfile, 'w') as outfile:
        lines = infile.readlines()
        first_line = lines[0]
        last_line = lines[-1]
        outfile.write(first_line)
        for line in lines[1:-1]:
            line_parts = line.split('=')
            modified_part = line_parts[1][:7] + "01" + line_parts[1][7:]
            result = line_parts[0] + "=" + modified_part
            outfile.write(result)
        outfile.write(last_line)
    print(f'The file {outputfile} has been generated')


card_format("transformed__file.txt", "format_verve.txt")

import os
import re
import glob


# Function that finds all files ending with .d in the current directory
def find_d_files():
    current_directory = os.getcwd()
    d_files = glob.glob(os.path.join(current_directory, '*.d'))
    return d_files


# Function that prints list of files
def print_file_names(files):
    if not files:
        print('No files found')
    else:
        for file in files:
            print(file)


# A funtion that parses .tra files and makes a dictionary of the tokens and their translations
def parse_tra_file(tra_file):
    with open(tra_file, 'r') as file:
        translations = {}
        key = None
        value = None
        for line in file:
            if line.startswith('@'):
                key, value = line.split(' = ', 1)
                key = key.strip()
                translations[key] = value
            else:
                translations[key] += line

    # Iterate over translations and right strip the endlines
    for key, value in translations.items():
        translations[key] = translations[key].strip()

    return translations


# A function that prints the translations
def print_translations(translations):
    for key, value in translations.items():
        print(f'{key}: {value}')


# Function that returns the .tra file for a .d file if one exists, else returns None
def get_tra_file(d_file):
    tra_file = d_file[:-2] + '.tra'
    if os.path.exists(tra_file):
        return tra_file
    else:
        print(f'{tra_file} does not exist')
        return None


# Main function, that untraifies the .d files
if __name__ == '__main__':
    d_files = find_d_files()
    for d_file in d_files:
        tra_file = get_tra_file(d_file)
        if tra_file:
            text = parse_tra_file(tra_file)
            with open(d_file, 'r+') as d:
                untraified_lines_num = 0
                # Read the entire content of the file
                content = d.readlines()
                
                # Replace the tokens in the .d file with the translations from the .tra file
                for i, line in enumerate(content):
                    # If there is @number in the line (a token), replace it with the translation from the .tra file
                    if '@' in line:
                        match = re.search(r'@\d+', line)
                        if match:
                            token = match.group(0)

                        # Replace the token with the translation from the .tra file
                        line = line.replace(token, text[token])
                        content[i] = line
                        untraified_lines_num += 1
                
                # Overwrite the file with the modified content
                d.seek(0)
                d.writelines(content)
                d.truncate()
            print(f'{d_file} has been untraified, {untraified_lines_num} replacements.')

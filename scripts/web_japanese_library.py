
import glob
import os.path

file_contents = '''<!DOCTYPE html>
<html lang="ja">
<head>
 <meta charset="utf-8">
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>{}</title>
</head>
<body>
{}
</body>
<html>
'''

for file_name in glob.glob('../_japlib_input_files/*.txt'):
    title = os.path.splitext(os.path.basename(file_name))[0]
    out_name = os.path.join('..', '_to_japlib', title + '.html')
    body = ''
    with open(file_name, encoding='shift-jis', errors='ignore') as in_file, \
         open(out_name, mode='w', encoding='utf-8') as out_file:
        for line in in_file.readlines():
            body += '<div>{}</div>\n'.format(line.strip())
        out_file.write(file_contents.format(title, body))
        print(file_name, 'processed')
    #break
    #print()

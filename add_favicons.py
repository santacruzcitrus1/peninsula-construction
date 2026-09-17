
import glob

favicon_tags = '  <link rel="icon" type="image/x-icon" href="/favicon.ico">\n  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">\n  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">'

files = glob.glob('**/*.html', recursive=True)
updated = 0
skipped = 0
for f in files:
    with open(f, 'r') as fh:
        content = fh.read()
    if 'favicon' in content:
        skipped += 1
        continue
    new_content = content.replace('</head>', favicon_tags + '\n</head>', 1)
    if new_content != content:
        with open(f, 'w') as fh:
            fh.write(new_content)
        updated += 1

print(f'Updated: {updated}, Skipped (already had favicon): {skipped}')

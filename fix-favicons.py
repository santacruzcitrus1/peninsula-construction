
import os, glob

favicon_sub = '    <link rel="icon" type="image/png" sizes="32x32" href="../favicon-32x32.png">\n    <link rel="icon" type="image/png" sizes="16x16" href="../favicon-16x16.png">\n    <link rel="apple-touch-icon" sizes="180x180" href="../apple-touch-icon.png">'

favicon_root = '    <link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">\n    <link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">\n    <link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">'

all_files = glob.glob('/root/pc3-speedfix/*.html') + glob.glob('/root/pc3-speedfix/city-pages/*.html') + glob.glob('/root/pc3-speedfix/blog-posts/*.html')

fixed = 0
for f in all_files:
    with open(f, 'r') as fh:
        content = fh.read()
    if 'favicon' not in content:
        is_subdir = 'city-pages' in f or 'blog-posts' in f
        tags = favicon_sub if is_subdir else favicon_root
        content = content.replace('</head>', tags + '\n</head>', 1)
        with open(f, 'w') as fh:
            fh.write(content)
        fixed += 1
        print(f"Fixed: {os.path.basename(f)}")

print(f"\nTotal fixed: {fixed}")

import os

# Load keywords
with open("keywords.txt", "r") as f:
    keywords = [line.strip() for line in f if line.strip()]

# Split into 10 chunks
chunks = [keywords[i:i+10] for i in range(0, len(keywords), 10)]

os.makedirs("pages", exist_ok=True)

for idx, chunk in enumerate(chunks, 1):
    html = f"""
    <html>
    <body>
      <ul>
    """
    for kw in chunk:
        html += f"<li>{kw}</li>\n"
    html += """
      </ul>
    </body>
    </html>
    """
    
    with open(f"pages/page{idx}.html", "w") as f:
        f.write(html)

import re
from pathlib import Path

# Input and output file names
src_file = Path("4_5_metrics_std.tex")
dst_file = Path("4_5_metrics_std_reduced.tex")

# Read input
text = src_file.read_text()

# --- Step 1: compress number + parentheses spacing ---
# Replace "num (num)" → "num(num)"
text = re.sub(r'(\d)\s+\(([-+]?\d)', r'\1(\2', text)

# --- Step 2: round all numeric values to 2 decimals ---
def round_num(match):
    num = float(match.group())
    return f"{num:.2f}"

# This pattern matches floats (e.g., 0.12345, .5, 10.0, etc.)
float_pattern = re.compile(r"(?<![A-Za-z])[-+]?\d*\.\d+(?![A-Za-z])")

text = float_pattern.sub(round_num, text)

# --- Step 3: write output ---
dst_file.write_text(text)

print(f"✅ Saved compacted table to {dst_file}")


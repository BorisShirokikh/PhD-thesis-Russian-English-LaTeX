import re
from pathlib import Path

input_file = Path("4_6_ablation.tex")
output_file = Path("4_6_ablation_reduced.tex")

text = input_file.read_text(encoding="utf-8")

# 1️⃣ Remove the leading numeric value before \textcolor
# e.g. "0.364 \textcolor{lightGreen}{...}" -> "\textcolor{lightGreen}{...}"
text = re.sub(r"\d+\.\d+\s+\\textcolor", r"\\textcolor", text)

# 2️⃣ Remove all \textcolor{color}{...}, keeping only the inner {...} content
# e.g. "\textcolor{lightGreen}{$\uparrow$0.031}" -> "$\uparrow$0.031"
text = re.sub(r"\\textcolor\{[^}]+\}\{([^}]*)\}", r"\1", text)

# 3️⃣ Optional: clean multiple spaces (can appear after replacements)
# text = re.sub(r"\s{2,}", " ", text)

# Save cleaned version
output_file.write_text(text, encoding="utf-8")

print(f"✅ Cleaned table written to {output_file}")


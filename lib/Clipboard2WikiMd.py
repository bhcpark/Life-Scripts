# Convert Text to Wiki-friendly Markdown
# work in progress as I find more needs
# Work off clipboard for now
import pyperclip as pc
import re
text = pc.paste()

# change A. or 1. etc to heading level 3
text = re.sub("\n([A-Z0-9]\.)(.*)\r\n", r"===\g<2> ===", text, re.MULTILINE)
# simplify line breaks
new_text = text.replace("\r\n\r\n", "<br/>")

pc.copy(new_text)

from datetime import datetime

now = datetime.now()

with open("text.txt", "r", encoding="utf-8") as f:
    content = f.read()

new_text = f"{content}\n\nLast updated: {now}\n"

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_text)

print("README updated")

import re

import markdown
from django.core.files.storage import default_storage


def list_entries():
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                       for filename in filenames if filename.endswith(".md")))


def get_entry(title):
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None


def get_html_content(title):
    all_pages = [item.lower() for item in list_entries()]
    if title.lower() in all_pages:
        text = get_entry(title)
        return markdown.markdown(text)
    else:
        return False

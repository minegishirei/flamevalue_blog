from datetime import datetime
import requests as req

HATENA_ID = "minegishirei"
BLOG_DOMAIN = "flamevalue.hatenablog.com"
API_KEY = "u6v0f3440e"

def hatena_entry(title, contents, entry_id, categorys=[], updated="", draft=False):
    BASE_URL = f"https://blog.hatena.ne.jp/minegishirei/psy.hatenadiary.com/atom/entry/{entry_id}"
    updated = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    category = lambda x: "\n".join([f"<category term='{e}' />" for e in x])
    categorys = category(categorys) if category else ""

    xml = f"""<?xml version="1.0" encoding="utf-8"?>
    <entry xmlns="http://www.w3.org/2005/Atom"
          xmlns:app="http://www.w3.org/2007/app">
      <title>{title}</title>
      <author><name>name</name></author>
      <content type="text/plain">
        {contents}
      </content>
    </entry>""".encode(
        "UTF-8"
    )
    r = req.put(BASE_URL, auth=(HATENA_ID, API_KEY), data=xml)
    return r.text


if __name__ == "__main__":
    import sys
    _, arg = sys.argv
    with open(arg, "r") as f:
        title, categorys, entry_id, *content = f.readlines()
    categorys = categorys.split(",")
    content = "\n".join(content)
    r = hatena_entry(title, content, entry_id, categorys,True, False)
    print(r)
from datetime import datetime
import requests as req
import json

HATENA_ID = "minegishirei"
BLOG_DOMAIN = "flamevalue.hatenablog.com"
API_KEY = "u6v0f3440e"

def hatena_entry(title, contents, entry_id, categorys=[], updated="", draft=False):
    BASE_URL = f"https://blog.hatena.ne.jp/minegishirei/{BLOG_DOMAIN}/atom/entry/{entry_id}"
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


def main():
    FLAMEWORKDICT = GEN_FLAMEWORKDICT("/static/flamevalue/")
    with open( f'/static/flamevaluedict/flamevaluedict.json', 'w+') as f:
        json.dump(FLAMEWORKDICT, f, indent=4, ensure_ascii=False)

    lang_names = ["Python", "Java"] #"Scala", "Ruby", "PHP", "Javascript", "Typescript", "Rust", "Swift", "Kotlin", "Vue", "React", "MySQL", "PostgreSQL"]
    for lang_name in lang_names:
        with open( f'/static/flamevalue/{lang_name}.json', 'w') as f:
            json.dump(build_param(lang_name, FLAMEWORKDICT), f, indent=4, ensure_ascii=False)



if __name__ == "__main__":
    from flamevalue.main import build_param , GEN_FLAMEWORKDICT
    import sys
    _, arg = sys.argv
    with open(arg, "r") as f:
        title, categorys, entry_id, *content = f.readlines()
    categorys = categorys.split(",")
    content = "\n".join(content)
    #r = hatena_entry(title, content, entry_id, categorys,True, False)

    FLAMEWORKDICT = GEN_FLAMEWORKDICT("/static/flamevalue/")
    with open( f'/static/flamevaluedict/flamevaluedict.json', 'w+') as f:
        json.dump(FLAMEWORKDICT, f, indent=4, ensure_ascii=False)

    lang_names = ["Python", "Java", "Ruby"] #"Scala", "Ruby", "PHP", "Javascript", "Typescript", "Rust", "Swift", "Kotlin", "Vue", "React", "MySQL", "PostgreSQL"]
    for lang_name in lang_names:
        with open( f'/static/flamevalue/{lang_name}.json', 'w') as f:
            json.dump(build_param(lang_name, FLAMEWORKDICT), f, indent=4, ensure_ascii=False)



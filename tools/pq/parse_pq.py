import re,html,json,os
L=json.load(open("list.json"))
def syntax(path,name):
    s=open(path,errors="ignore").read()
    i=s.find('id="syntax"'); i = i if i>=0 else s.find("Syntax</h2>")
    if i<0: return None
    m=re.search(r"<pre[^>]*>(.*?)</pre>",s[i:],re.S)
    if not m: return None
    t=re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]+>","",m.group(1)))).strip()
    m2=re.match(re.escape(name)+r"\s*\((.*)\)\s*as\s+[^()]+$",t) or re.match(re.escape(name)+r"\s*\((.*)\)",t)
    return m2.group(1).strip() if m2 else None
def args_of(sx):
    parts,depth,cur=[],0,""
    for ch in sx:
        if ch in "([{": depth+=1
        if ch in ")]}": depth-=1
        if ch=="," and depth==0: parts.append(cur); cur=""; continue
        cur+=ch
    if cur.strip(): parts.append(cur)
    out=[]
    for p in parts:
        p=p.strip()
        if p in ("...","…"): out.append({"n":"...","opt":True}); continue
        opt=p.startswith("optional ")
        p=re.sub(r"^optional\s+","",p)
        n=p.split(" as ")[0].strip()
        out.append({"n":n,"opt":opt})
    return out
out=[];bad=[]
for o in L:
    p="fn/"+(o["href"] or "")+".html"
    sx=syntax(p,o["name"]) if o["href"] and os.path.exists(p) else None
    if sx is None: bad.append(o["name"]); continue
    out.append({**o,"syntax":sx,"args":args_of(sx)})
json.dump(out,open("parsed.json","w"),indent=1)
print(len(out),"bad",len(bad),bad)
for n in ["Table.SelectRows","Text.Combine","List.Sum","Table.Group","Table.AddColumn","Date.AddDays","Table.Join","Table.NestedJoin","Text.Split"]:
    for x in out:
        if x["name"]==n: print(n, ", ".join(("["+a["n"]+"]") if a["opt"] else a["n"] for a in x["args"]))
odd=[x["name"] for x in out if any(not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*|\.\.\.",a["n"]) for a in x["args"])]
print("odd",len(odd),odd[:20])

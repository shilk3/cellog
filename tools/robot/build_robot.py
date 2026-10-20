# robot_raw.json (from extract.py) -> robot_clean.json: people's names removed,
# duplicates merged, each LAMBDA's arguments read from its own formula
# ([x] = optional), and commands tagged hard (Robot-only) or easy in Excel.
# Usage: python3 -I build_robot.py <folder with the workbooks>
import sys,json,re
sys.path.insert(0,".")
from xl import book
SP = sys.argv[1].rstrip("/") + "/"
raw=json.load(open("robot_raw.json"))
PEOPLE=["Jaq Kennedy","Erik Oehm","Hadyn Wiseman","Bo Rydobon","Diarmuid Early","Emilie Williams","Lianna Gerrish","Ben de Leon","Ha Dang","Harry Gross","Fabian Sjöblom","Gabe Sotero","Laza Ranoelison"]
def strip_names(s):
    s=re.sub(r"_by[A-Z][A-Za-z]+","",s or "")
    for p in PEOPLE: s=re.sub(r"\s*(,\s*)?(using |by |requested by |extended by )?"+re.escape(p)+r"('s)?","",s)
    s=re.sub(r"\bJJ\b","",s)
    return re.sub(r"\s{2,}"," ",s).strip(" ,;")
def lambda_params(formula):
    f=formula.strip()
    m=re.match(r"_xlfn\.LAMBDA\(",f)
    if not m: return None
    i=m.end(); depth=1; parts=[]; cur=""
    while i<len(f) and depth:
        ch=f[i]
        if ch in "({[": depth+=1
        elif ch in ")}]": depth-=1
        if depth==1 and ch==",": parts.append(cur); cur=""
        elif depth>0: cur+=ch
        i+=1
    parts.append(cur)
    params=[]
    for p in parts[:-1]:
        p=p.strip()
        mm=re.fullmatch(r"_xl(pm|op)\.(\w+)",p)
        if not mm: return None
        params.append(("["+mm.group(2)+"]") if mm.group(1)=="op" else mm.group(2))
    return params
def meta(formula,key):
    m=re.search(r"_xlpm\.\\\\"+key+r',\s*"([^"]*)"',formula or "")
    return m.group(1) if m else ""
# --- LAMBDAs
lams={}
_,lr=book(SP+"lambda_robot.xlam")
raw["lams"].append({"src":"Lambda Robot","name":"LETStack","desc":"","params":"","formula":lr["LETStack"]["formula"]})
for l in raw["lams"]:
    name=strip_names(l["name"])
    params=lambda_params(l["formula"])
    if params is None and l.get("params") and ":" not in l["params"]:
        params=[p.strip() for p in l["params"].split(",") if p.strip()]
    desc=strip_names(l["desc"] or meta(l["formula"],"Description"))
    key=name.lower()
    rec={"name":name,"params":params,"desc":desc,"src":l["src"]}
    if key in lams:
        old=lams[key]
        if (not old["desc"] and desc) or (old["params"] is None and params is not None): lams[key]={**old,**{k:v for k,v in rec.items() if v}}
        lams[key]["src"]+=" + "+l["src"]
    else: lams[key]=rec
# --- commands
cmdDesc={}
for l in raw["lams"]:
    cn=meta(l["formula"],"CommandName"); d=meta(l["formula"],"Description")
    if cn and d: cmdDesc[cn.lower()]=d
HARD=r"colou?r|background|exact formula|translat|volatile|search workbook|format formula|compact formula|formula bar|backup|name used ranges|iterative|goto similar|spill parent|outer function|time formula|timer|generate|filter by copied|as references|clipboard|copied|paste.*(formula|value)s? over|save (from|game)|import|unused lambda|launch|palette|sheet|workbook|macro|vba|similar"
cmds={}
for c in raw["cmds"]:
    name=strip_names(c["name"])
    if not name or "DEV ONLY" in (c["desc"] or ""): continue  # developer-only commands
    desc=strip_names(c["desc"] or cmdDesc.get(c["name"].lower(),""))
    group=strip_names(c["group"]).replace(" Related Commands","").replace(" Related Command","")
    key=name.lower()
    if key in cmds:
        if not cmds[key]["desc"] and desc: cmds[key]["desc"]=desc
        if c["src"] not in cmds[key]["src"]: cmds[key]["src"]+=" + "+c["src"]
        continue
    text=(name+" "+desc).lower()
    cmds[key]={"name":name,"group":group,"desc":desc,"code":c.get("code",""),"src":c["src"],"hard":bool(re.search(HARD,text))}
L=sorted(lams.values(),key=lambda x:x["name"].lower()); C=sorted(cmds.values(),key=lambda x:x["name"].lower())
json.dump({"lams":L,"cmds":C},open("robot_clean.json","w"),indent=1)
print("lambdas",len(L),"no params",[x["name"] for x in L if x["params"] is None],"no desc",len([x for x in L if not x["desc"]]))
print("commands",len(C),"hard",sum(c["hard"] for c in C),"no desc",len([c for c in C if not c["desc"]]))
# Any name still in there (first or last, whole words only).
words=sorted({w for p in PEOPLE for w in p.split() if len(w)>2}|{"Bo","JJ","Haydn"})
left=[x for x in L+C if any(re.search(r"\b"+re.escape(w)+r"\b",x["name"]+" "+x["desc"]) for w in words)]
print("names left:",[(x["name"],x["desc"][:60]) for x in left][:10])

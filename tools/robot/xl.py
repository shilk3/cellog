import zipfile, re, html
def book(path):
    z=zipfile.ZipFile(path)
    wb=z.read("xl/workbook.xml").decode()
    sheets=re.findall(r'<sheet [^>]*name="([^"]+)"[^>]*r:id="([^"]+)"',wb)
    rels=dict(re.findall(r'Id="([^"]+)"[^>]*Target="([^"]+)"',z.read("xl/_rels/workbook.xml.rels").decode()))
    ss=[]
    if "xl/sharedStrings.xml" in z.namelist():
        x=z.read("xl/sharedStrings.xml").decode()
        ss=[html.unescape("".join(re.findall(r"<t[^>]*>(.*?)</t>",si,re.S))) for si in re.findall(r"<si>(.*?)</si>",x,re.S)]
    out={}
    for n,rid in sheets:
        t=rels[rid].lstrip("/"); t=t if t.startswith("xl/") else "xl/"+t
        x=z.read(t).decode()
        rows={}
        for attrs,body in re.findall(r'<c ([^>]*?)(?:/>|>(.*?)</c>)',x,re.S):
            ref=re.search(r'r="([A-Z]+)(\d+)"',attrs); v=re.search(r"<v>(.*?)</v>",body or "",re.S); tt=re.search(r't="([^"]+)"',attrs)
            isv=re.search(r"<is>.*?<t[^>]*>(.*?)</t>",body or "",re.S)
            if v: val=ss[int(v.group(1))] if tt and tt.group(1)=="s" else html.unescape(v.group(1))
            elif isv: val=html.unescape(isv.group(1))
            else: continue
            rows.setdefault(int(ref.group(2)),{})[ref.group(1)]=val
        out[n]=rows
    names={}
    for a,v in re.findall(r'<definedName ([^>]*)>(.*?)</definedName>',wb,re.S):
        nm=re.search(r'name="([^"]+)"',a).group(1)
        cm=re.search(r'comment="([^"]*)"',a)
        if not nm.startswith("_xl"): names[nm]={"formula":html.unescape(v),"comment":html.unescape(cm.group(1)) if cm else ""}
    return out,names

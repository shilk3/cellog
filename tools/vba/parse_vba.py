import re,html,json,os
L=[o for o in json.load(open("list.json")) if o["cat"]!="See also"]
def text(s): return re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]+>"," ",s))).strip()
out=[];bad=[]
for o in L:
    s=open("fn/"+os.path.basename(o["href"])+".html",errors="ignore").read()
    body=s[s.find("<main"):] if "<main" in s else s
    names=[n.strip() for n in re.split(r",|\band\b",o["label"]) if n.strip()]
    # description: first <p> after the h1
    h1=body.find("</h1>")
    desc=text(re.search(r"<p>(.*?)</p>",body[h1:],re.S).group(1)) if h1>=0 else ""
    si=body.find('id="syntax"')
    seg=text(body[si:si+3000]) if si>=0 else ""
    for name in names:
        m=re.search(r"(?<![A-Za-z])"+re.escape(name)+r"\s*(\$)?\s*\((.*?)\)(?=\s|$)",seg)
        sx=None
        if m:
            # balance parens from the match start
            i=seg.find("(",m.start()); depth=0; j=i
            while j<len(seg):
                if seg[j]=="(": depth+=1
                elif seg[j]==")":
                    depth-=1
                    if depth==0: break
                j+=1
            sx=seg[i+1:j].strip()
        elif re.search(r"(?<![A-Za-z])"+re.escape(name)+r"\b",seg) and name in ("Now","Date","Time","Timer","Err","Error","Rnd","Erl","Space"):
            sx=""
        if sx is None: bad.append(name); continue
        out.append({"name":name,"cat":o["cat"],"desc":desc,"syntax":sx,"href":o["href"]})
json.dump(out,open("parsed.json","w"),indent=1)
print(len(out),"bad",len(bad),bad)
for n in ["MsgBox","InputBox","Left","Mid","DateAdd","Format","Now","IIf","Replace","Split","Dir","InStr","CreateObject"]:
    print([ (x["name"],x["syntax"]) for x in out if x["name"]==n][:1])

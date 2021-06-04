a = open("users", "r", encoding="utf-8")
b = open("hobby", "r", encoding="utf-8")
sl_ = {}
f_read1 = len(a.read().split("\n"))
f_read2 = len(b.read().split("\n"))
a.seek(0)
b.seek(0)
dop = 0
sch1 = f_read1
if f_read1 < f_read2:
    sch1 = f_read1
    sch2 = f_read2-f_read1
    dop = 1
if f_read1 > f_read2:
    sch1 = f_read2
    sch2 = f_read1-f_read2
    dop = 2
gn_ = {a.readline().replace(",", " ").replace("\n", ""): b.readline().replace(",", " ").replace("\n", "") for i in range(sch1)}
sl_.update(gn_)
if dop == 1:
    for i in range(sch2):
        a2 = b.readline().replace(",", ", ").replace("\n", "")
        sl_new = {None: a2}
        sl_.update(sl_new)
if dop == 2:
    for i in range(sch2):
        a1 = a.readline().replace(",", " ").replace("\n", "")
        sl_new = {a1: "1"}
        sl_.update(sl_new)
a.close()
b.close()
print(sl_)
gff-relationships
=================

GFF3 Parser which maps parent/children relationships between features

Example Session
```python
import gffR
a = gffR.ReadFile('Cpapaya_113_gene.gff3')
mrna = a.by_type['mRNA'].values()[0]
print mrna
# ID:PAC:16407288	Type:mRNA	Start:921888	Stop:927188	Parent:evm.TU.supercontig_125.56	8 Children
print mrna.parent
# ID:evm.TU.supercontig_125.56	Type:gene	Start:921888	Stop:927188	Parent:None	1 Children
[(x.stop-x.start+1) for x in mrna.children]
#[Out]# [184, 114, 69, 20, 53, 31, 82, 179]
sum([(x.stop-x.start+1) for x in mrna.children])
#[Out]# 732
mrna.stop - mrna.start + 1
#[Out]# 5301
```

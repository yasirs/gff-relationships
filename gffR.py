import re

class Feature:
	id_re = re.compile('ID=([^;]+)')
	parent_re = re.compile('Parent=([^;]+)')
	def __init__(self,line):
		self.line = line
		words = line.rstrip().split('\t')
		self.type = words[2]
		m = Feature.id_re.search(words[8])
                if m:
                        self.id = m.groups()[0]
		else:
			self.id = None
		self.attribs = words[8]
		self.start = int(words[3])
		self.stop = int(words[4])
		m = Feature.parent_re.search(words[8])
		if m:
			self.parent_id = m.groups()[0]
		else:
			self.parent_id = None
		self.children = []
	def __str__(self):
		return "ID:%s\tType:%s\tStart:%i\tStop:%i\tParent:%s\t%i Children" %(self.id, self.type, self.start, self.stop, self.parent_id, len(self.children))

class GFF:
	def __init__(self,byt,byid):
		self.by_type = byt
		self.by_id = byid



def ReadFile(path):
	# prelims
	features_by_type = {}
	features_by_id = {}

	fi = open(path,'r')
	for line in fi:
		if line[0]=='#':
			continue
		feat = Feature(line)
		type = feat.type
		if (type not in features_by_type):
			features_by_type[type] = {}
		if feat.id:
			id = feat.id
		else:
			id = feat.line
		features_by_type[type][id] = feat
		features_by_id[id] = feat
		if feat.parent_id:
			feat.parent = features_by_id[feat.parent_id]
			feat.parent.children.append(feat)
	return GFF(features_by_type, features_by_id)

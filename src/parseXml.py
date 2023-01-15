
import xmltodict
import json

class Parser:


	def __init__(self, filename='kb.xml', filepath='../xml/'):
		with open(filepath + filename) as xmlFile:
			doc = xmltodict.parse(xmlFile.read())
		self.data = json.loads(json.dumps(doc))
		self.data = self.data['kb']
		# print(self.data)				

	def get_puncte_vamale(self):
		return self.data['fapte']['puncte_vamale']

	def get_punct_vamal(self, punct_vamal_cautat):
		print('test here')
		puncte_vamale = self.get_puncte_vamale()['punct_vama']
		print(punct_vamal_cautat)
		for punct_vamal in puncte_vamale:
			if punct_vamal['nume'].lower() == punct_vamal_cautat.lower():
				return punct_vamal
		return "not found"

	def get_persoana(self, persoana_cautata):
		persoane = self.data['fapte']['persoane']['persoana']
		for persoana in persoane:
			print(persoana)
			if persoana['buletin']['CNP'].lower() == persoana_cautata.lower():
				return persoana
		return "not found"


	def check_punct_vamal_in_control_sporit(self, nume_punct_vamal):

		found_condition = self.get_predicat('punct_vama_in_control_sporit',nume_punct_vamal)
		if found_condition['condition'] == 'false':
			return 'false'

		punct_vama = self.get_punct_vamal(nume_punct_vamal)	
		print("Punct vama in fapte: " + str(punct_vama))
		print("Punct vama din reguli: " + found_condition['condition'])
		if str(punct_vama) in found_condition['condition']:
			return found_condition['then']
		else:
			return found_condition['else']
		

	def get_supermarket(self, s):
		return s in self.data['supermarket']


	def get_persoanaLaSupermarket(self, p):
		return p in self.data['persoanaLaSupermarket']


	def get_predicat(self,searched_answer,query):
		rules = self.data['reguli']['regula']
		for rule in rules:
			then_rule = rule['then']
			if then_rule == None:
				continue
			if then_rule[searched_answer] != None:
				conditions = [rule['if']]
				conditions = self.flatten_list(conditions)
				for condition in conditions:
					print(condition)
					try:
						rule_condition_change = self.rules_conditions_dex('punct_vama_in_control_sporit')
						print('Replacing condition...' + query)
						condition = str(condition)
						condition = condition.replace(rule_condition_change, query)
						print('Here ' + condition)
						return {
							"condition":json.dumps(condition),
							"then":then_rule,
							"else":rule['else']
						}
					except Exception as exception:
						print('Error ' + str(exception))
						return {
							"condition":'false'
						}

	def flatten_list(self,_2d_list):
		flat_list = []
		# Iterate through the outer list
		for element in _2d_list:
			if type(element) is list:
				# If the element is of type list, iterate through the sublist
				for item in element:
					flat_list.append(item)
			else:
				flat_list.append(element)
		return flat_list

	def rules_conditions_dex(self, rule_name):
		if rule_name == 'punct_vama_in_control_sporit':
			return 'nume_punct_vama'
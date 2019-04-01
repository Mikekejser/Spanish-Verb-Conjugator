verb = input('')

if verb.endswith('se'):
	verb = verb[:-2]

verb_root = verb[:-2]

if verb.endswith('ar'):
	with open(verb + '_conjugations.txt', 'w') as fo:
		fo.write(
			f"""
			***INDICATIVE***
			\nPresent:\n{verb_root+'o'}, {verb_root+'as'}, {verb_root+'a'}, {verb_root+'amos'}, {verb_root+'áis'}, {verb_root+'an'}
			\nPreterite:\n{verb_root+'é'}, {verb_root+'aste'}, {verb_root+'ó'}, {verb_root+'amos'}, {verb_root+'asteis'}, {verb_root+'aron'}
			\nImperfect:\n{verb_root+'aba'}, {verb_root+'abas'}, {verb_root+'aba'}, {verb_root+'ábamos'}, {verb_root+'abais'}, {verb_root+'aban'}
			\nPresent Perfect:\n{'he '+verb_root+'ado'}, {'has '+verb_root+'ado'}, {'ha '+verb_root+'ado'}, {'hemos '+verb_root+'ado'}, {'habéis ' +verb_root+'ado'}, {'han '+verb_root+'ado'}
			\nPast Perfect:\n{'había '+verb_root+'ado'}, {'habías '+verb_root+'ado'}, {'había '+verb_root+'ado'}, {'habíamos '+verb_root+'ado'}, {'habíais '+verb_root+'ado'}, {'habían '+verb_root+'ado'}
			\nFuture:\n{verb+'é'}, {verb+'ás'}, {verb+'á'}, {verb+'emos'}, {verb+'éis'}, {verb+'án'}
			\n
			\n
			***SUBJUNCTIVE***
			\nPresent:\n{verb_root+'e'}, {verb_root+'es'}, {verb_root+'e'}, {verb_root+'emos'}, {verb_root+'éis'}, {verb_root+'en'}
			\nImperfect:\n{verb+'a'}, {verb+'as'}, {verb+'a'}, {verb_root+'áramos'}, {verb+'ais'}, {verb+'an'}
			\nPresent Perfect:\n{'haya '+verb_root+'ado'}, {'hayas '+verb_root+'ado'}, {'haya '+verb_root+'ado'}, {'hayamos '+verb_root+'ado'}, {'hayáis '+verb_root+'ado'}, {'hayan '+verb_root+'ado'}
			\nPast Perfect:\n{'hubiera '+verb_root+'ado'}, {'hubieras '+verb_root+'ado'}, {'hubiera '+verb_root+'ado'}, {'hubiéramos '+verb_root+'ado'}, {'hubierais '+verb_root+'ado'}, {'hubieran '+verb_root+'ado'}
			\nFuture:\n{verb+'e'}, {verb+'es'}, {verb+'e'}, {verb_root+'áremos'}, {verb+'eis'}, {verb+'en'}
			\n
			\n
			***CONDITIONAL***
			\n{verb+'ía'}, {verb+'ías'}, {verb+'ía'}, {verb+'íamos'}, {verb+'íais'}, {verb+'ían'}
			\n
			\n
			***IMPERATIVE***
			\n{'tú: '+verb_root+'a'}, {'vosotros: '+verb_root+'ad'}
			\n
			"""
			)

elif verb.endswith('er'):
	with open(verb + '_conjugations.txt', 'w') as fo:
		fo.write(
			f"""
			***INDICATIVE***
			\nPresent:\n{verb_root+'o'}, {verb_root+'es'}, {verb_root+'e'}, {verb_root+'emos'}, {verb_root+'éis'}, {verb_root+'en'}
			\nPreterite:\n{verb_root+'í'}, {verb_root+'iste'}, {verb_root+'ió'}, {verb_root+'imos'}, {verb_root+'isteis'}, {verb_root+'ieron'}
			\nImperfect:\n{verb_root+'ía'}, {verb_root+'ías'}, {verb_root+'ía'}, {verb_root+'íamos'}, {verb_root+'íais'}, {verb_root+'ían'}
			\nPresent Perfect:\n{'he '+verb_root+'ido'}, {'has '+verb_root+'ido'}, {'ha '+verb_root+'ido'}, {'hemos '+verb_root+'ido'}, {'habéis ' +verb_root+'ido'}, {'han '+verb_root+'ido'}
			\nPast Perfect:\n{'había '+verb_root+'ido'}, {'habías '+verb_root+'ido'}, {'había '+verb_root+'ido'}, {'habíamos '+verb_root+'ido'}, {'habíais '+verb_root+'ido'}, {'habían '+verb_root+'ido'}
			\nFuture:\n{verb+'é'}, {verb+'ás'}, {verb+'á'}, {verb+'emos'}, {verb+'éis'}, {verb+'án'}
			\n
			\n
			***SUBJUNCTIVE***
			\nPresent:\n{verb_root+'a'}, {verb_root+'as'}, {verb_root+'a'}, {verb_root+'amos'}, {verb_root+'áis'}, {verb_root+'an'}
			\nImperfect:\n{verb_root+'iera'}, {verb_root+'ieras'}, {verb_root+'iera'}, {verb_root+'iéramos'}, {verb_root+'ierais'}, {verb_root+'ieran'}
			\nPresent Perfect:\n{'haya '+verb_root+'ido'}, {'hayas '+verb_root+'ido'}, {'haya '+verb_root+'ido'}, {'hayamos '+verb_root+'ido'}, {'hayáis '+verb_root+'ido'}, {'hayan '+verb_root+'ido'}
			\nPast Perfect:\n{'hubiera '+verb_root+'ido'}, {'hubieras '+verb_root+'ido'}, {'hubiera '+verb_root+'ido'}, {'hubiéramos '+verb_root+'ido'}, {'hubierais '+verb_root+'ido'}, {'hubieran '+verb_root+'ido'}
			\nFuture:\n{verb_root+'iere'}, {verb_root+'ieres'}, {verb_root+'iere'}, {verb_root+'iéremos'}, {verb_root+'iereis'}, {verb_root+'ieren'}
			\n
			\n
			***CONDITIONAL***
			\n{verb+'ía'}, {verb+'ías'}, {verb+'ía'}, {verb+'íamos'}, {verb+'íais'}, {verb+'ían'}
			\n
			\n
			***IMPERATIVE***
			\n{'tú: '+verb_root+'e'}, {'vosotros: '+verb_root+'ed'}
			\n
			"""
			)

else:
	with open(verb + '_conjugations.txt', 'w') as fo:
		fo.write(
			f"""
			***INDICATIVE***
			\nPresent:\n{verb_root+'o'}, {verb_root+'es'}, {verb_root+'e'}, {verb_root+'imos'}, {verb_root+'ís'}, {verb_root+'en'}
			\nPreterite:\n{verb_root+'í'}, {verb_root+'iste'}, {verb_root+'ió'}, {verb_root+'imos'}, {verb_root+'isteis'}, {verb_root+'ieron'}
			\nImperfect:\n{verb_root+'ía'}, {verb_root+'ías'}, {verb_root+'ía'}, {verb_root+'íamos'}, {verb_root+'íais'}, {verb_root+'ían'}
			\nPresent Perfect:\n{'he '+verb_root+'ido'}, {'has '+verb_root+'ido'}, {'ha '+verb_root+'ido'}, {'hemos '+verb_root+'ido'}, {'habéis ' +verb_root+'ido'}, {'han '+verb_root+'ido'}
			\nPast Perfect:\n{'había '+verb_root+'ido'}, {'habías '+verb_root+'ido'}, {'había '+verb_root+'ido'}, {'habíamos '+verb_root+'ido'}, {'habíais '+verb_root+'ido'}, {'habían '+verb_root+'ido'}
			\nFuture:\n{verb+'é'}, {verb+'ás'}, {verb+'á'}, {verb+'emos'}, {verb+'éis'}, {verb+'án'}
			\n
			\n
			***SUBJUNCTIVE***
			\nPresent:\n{verb_root+'a'}, {verb_root+'as'}, {verb_root+'a'}, {verb_root+'amos'}, {verb_root+'áis'}, {verb_root+'an'}
			\nImperfect:\n{verb_root+'iera'}, {verb_root+'ieras'}, {verb_root+'iera'}, {verb_root+'iéramos'}, {verb_root+'ierais'}, {verb_root+'ieran'}
			\nPresent Perfect:\n{'haya '+verb_root+'ido'}, {'hayas '+verb_root+'ido'}, {'haya '+verb_root+'ido'}, {'hayamos '+verb_root+'ido'}, {'hayáis '+verb_root+'ido'}, {'hayan '+verb_root+'ido'}
			\nPast Perfect:\n{'hubiera '+verb_root+'ido'}, {'hubieras '+verb_root+'ido'}, {'hubiera '+verb_root+'ido'}, {'hubiéramos '+verb_root+'ido'}, {'hubierais '+verb_root+'ido'}, {'hubieran '+verb_root+'ido'}
			\nFuture:\n{verb_root+'iere'}, {verb_root+'ieres'}, {verb_root+'iere'}, {verb_root+'iéremos'}, {verb_root+'iereis'}, {verb_root+'ieren'}
			\n
			\n
			***CONDITIONAL***
			\n{verb+'ía'}, {verb+'ías'}, {verb+'ía'}, {verb+'íamos'}, {verb+'íais'}, {verb+'ían'}
			\n
			\n
			***IMPERATIVE***
			\n{'tú: '+verb_root+'a'}, {'vosotros: '+verb_root+'id'}
			\n
			"""
			)



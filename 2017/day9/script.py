import re


def clean(raw):
	text = re.sub('!.', '', raw)

	for char in text:
		if char=='<'


	
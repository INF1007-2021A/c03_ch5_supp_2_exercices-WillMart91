#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from typing import List

def get_num_letters(text):
	cpt=0
	for letter in text :

		if letter.isalnum() :
			cpt+=1
	return cpt

def get_word_length_histogram(text):
	word_list=text.split()
	
	
	max_char=0
	for word in word_list :
		nb_current_char=get_num_letters(word)
		if nb_current_char>max_char:
			max_char=nb_current_char
	
	list_nb_char = []
	for i in range(0,max_char+1):
   		#list_nb_char[i] = 0
		list_nb_char.append(0)

	
	for word in word_list :
		list_nb_char[get_num_letters(word)]+=1

	#list_nb_char.
	return list_nb_char

def format_histogram(histogram: List):
	ROW_CHAR = "*"

	string=''
	for number in range(0,len(histogram)):
		char=''
		for j in range (0,histogram[number]):
			char+=ROW_CHAR
		string+=(f"{number}: {char}\n")

	return string

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"

	return ""


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))

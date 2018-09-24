# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 16:21:03 2018

@author: yamini

"""
def compress(string):
  if len(string) == 0:
    return string
  parts = []
  current_letter = string[0]
  current_count = 1
  for letter in string[1:]:
    if current_letter == letter:
      current_count += 1
    else:
      parts.append(current_letter + str(current_count))
      current_letter = letter
      current_count = 1
  parts.append(current_letter + str(current_count))
  compressed = "".join(parts)
  if len(compressed) < len(string):
    return compressed
  else:
    return string
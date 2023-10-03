from datetime import datetime
import pytest


########################################################################
########################################################################
############ Try to get Datetime from String
def getDateFromString2(text):
  for fmt in ('%Y-%m-%d', '%d.%m.%Y', '%d/%m/%Y'):
    try:
      return datetime.strptime(text, fmt)
    except ValueError:
      pass
  raise ValueError(f"Impossible de transcrire le texte [{text}] en une date")


########################################################################
########################################################################
############ Try to get Datetime from String (manuel)
def getDateFromString(text):

  lisStr = getListStrings(text)  #Séparation
  for str in lisStr:
    print(str)


########################################################################
############ Split input text by spaces
def getListStrings(text):
  if isinstance(text, str): return text.split()  #Split by all spaces
  raise Exception(f"Input [{text}] must be a String !")  #Split by all spaces
  #raise ValueError(f"Input [{text}] must be a String !")  #Split by all spaces

###### TESTS
#def test_getListStrings_ERROR_With_None():
#  with pytest.raises(ValueError, match='Input [None] must be a String !'):
#    getListStrings(None)
def test_getListStrings_ERROR_With_None2():
  #with pytest.raises(Exception, match='Input [None] must be a String !') as e_info:
  with pytest.raises(Exception) as e_info:
    getListStrings(None)
#def test_getListStrings_ERROR_With_Int():
#  assert getListStrings(1) == ValueError('Input [1] must be a String !')
def test_getListStrings3():
  assert getListStrings("  1 2  3   ") == ["1", "2", "3"]


###### FIN TESTS
########################################################################

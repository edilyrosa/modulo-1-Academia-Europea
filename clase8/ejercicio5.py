# Del siguiente str = “1,2,3,4,5” debes: Elevar cada numero al cubo y 
# retornar una list de elementos TDD int que son los cubo resultantes.
#  ⭐Usa Métodos: split() castea de str a list  int()+pow()+append() dentro de  for ⭐


str_nums = "1,2,3,4,5"
#? para manejar cada num debo pasarlos a ele de list
str_nums_list = str_nums.split(',')
print(str_nums_list)

str_nums_result = []
for num in str_nums_list:
    str_nums_result.append(pow(int(num), 3))
    
print(f'original {str_nums_list} resulatdo{str_nums_result}')
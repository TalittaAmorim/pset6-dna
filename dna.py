from csv import reader, DictReader
from sys import argv, exit 

def main():
    
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)
    
    #abrir arquivos
    csv_file = open("./" + argv[1])
    dna_file = open("./" + argv[2])
   
   # obtem STRs database do cabeçalho 
   # leitor de banco de dados
    database_reader = DictReader(csv_file) # DictReader é uma funçao q ler esse tipo de dado em python em formato de Dict 
    strs = database_reader.fieldnames[1:] # ignorando name e focando no campo de quantidade de STRs
    
   #copiar o conteudo do dna_file em string e fechar os arquivos
    dna = dna_file.read() #returna
    dna_file.close()
    
  # examinar o dna e contar quantas vezes uma sequencia se repete 
    dna_exame = {} #Dict para armazenar organizadamente o STR e como chave e suas repetições como valores
   
    for str in strs:
        dna_exame[str] = repetic_consec(str,dna)
        
    # Encontrar o nome correspondente ao número de STRs "e
    for linha in database_reader:
        
        if reconhecimento(strs,dna_exame, linha):       
            print(f"{linha['name']}")
            csv_file.close()
            return
    print("Não encontrado")
    csv_file.close()

       #calcula quantas vezes o str se repete 
def repetic_consec(str, dna):
    r=0 
    while str*( r+1) in dna:
        r +=1
    return r
    
    # Comparação 
def reconhecimento(strs, dna_exame, linha):
    for str in strs:
        if dna_exame[str] != int(linha[str]):
            return False
    return True 
   
   
main()       

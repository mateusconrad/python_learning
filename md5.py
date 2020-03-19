import hashlib
import json #usar deois pra gravar json

print ('mensagem para cifrar: ')
hashirama = hashlib.md5()
mensagem = input().encode('utf-8') #ou predefinir uma string
hashirama.update(mensagem)
print (hashirama.hexdigest())


#script  python
#	proteger senhas
#	entrada de string
#	md5 
#	gerar hash
#	saida em hexadecimal 
#	gerar json
#	gravar arquivo
#	ler json
	
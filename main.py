# 1. Função de Hash da aula (exemplo baseado na soma do código ASCII dos caracteres)
def calcula_hash(palavra):
    hash_valor = 0
    for letra in palavra:
        hash_valor += ord(letra)
    return hash_valor

# 2. Palavras escolhidas para o desafio (anagramas)
palavra1 = "AMOR"
palavra2 = "ROMA"

# 3. Calculando o hash de cada palavra
hash1 = calcula_hash(palavra1)
hash2 = calcula_hash(palavra2)

# 4. Exibindo os resultados
print(f"Palavra: '{palavra1}' -> Hash: {hash1}")
print(f"Palavra: '{palavra2}' -> Hash: {hash2}")

# 5. Verificação da colisão
if hash1 == hash2:
    print("\nEncontrada uma colisão de hash! Duas palavras diferentes geraram o mesmo resultado.")
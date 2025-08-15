#dados = [line for line in open("post.txt")if ":"in line]  #list comprehension

#dados = {line.split(":")[0]:line.split(":")[1].strip() #dict comprehension
#          for line in open("post.txt")
#          if ":" in line}


dados = {}
for line in open("post.txt"):
    if ":" in line:
        key,value = line.split(":")
        dados[key] = value.strip()

print(dados)
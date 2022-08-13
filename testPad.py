bitmap = """
=================================================
asdasdasd
asdasdasdasd
asdasdasdasd
adas    dadas
adadasdasd
asdasdadasd
"""

message = 'hello'
for line in bitmap.splitlines():
    for i,bit in enumerate(line):
        print(message[i % len(message)])

nota1 = float(input('primeira nota: '))
nota2 = float(input('segunda nota: '))
nota3 = float(input('terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
print('tiarndo {} e {}, a media do aluno é {:.1f}'. format(nota1, nota2, nota3, media))
if media >= 7:
    print('aprovado.')
elif media == 5 and media < 7:
    print('recuperação')
elif media < 5:
    print('reprovado')
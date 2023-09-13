from ultilidades.moeda import (
    double,
    half,
    PlusPorcent,
    ReducePorcent,
    verificar_numero,
    resume,
    obter_numero_valido,
    obter_porcentagem_valido,
)

numero = obter_numero_valido()
porcent = obter_porcentagem_valido()

dobro = double(numero)
metade = half(numero)
PlusPorcente = PlusPorcent(numero, porcent)
ReducePorcente = ReducePorcent(numero, porcent)

resume(numero, porcent, dobro, metade, PlusPorcente, ReducePorcente)

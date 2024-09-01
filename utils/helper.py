def formata_float_str_moeda(valor: float) -> str:
    # A função recebe um valor do tipo float e retorna uma string formatada como valor monetário brasileiro.
    
    return f'R$ {valor:,.2f}'
    # ex: Se você passar o valor 1234.5 para essa função, ela retornará a string "R$ 1.234,50".

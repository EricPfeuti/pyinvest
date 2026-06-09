# Projeto - PyInvest
import math
import locale
import random
import statistics
import datetime

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# VERIFICAR VALORES
def verificar_valores(valor, nome):
    if valor <= 0:
        print(f"Erro: O {nome} deve ser positivo!!")
        exit()
       
# FORMATAR VALOR (R$ 1.000,00)
def formatar_valor(valor):
    return locale.currency(valor, grouping=True)

# CONVERTER TAXA ANUAL para MENSAL
def converter_taxa_anual_mensal(taxa_anual):
    return (1 + taxa_anual) ** (1/12) - 1

# CALCULAR TOTAL INVESTIDO
def calcular_total_investido(capital, aporte, meses):
    return capital + (aporte * meses)

# CALCULAR JUROS COMPOSTOS
def calcular_juros_compostos(capital, aporte, taxa, meses):
    return capital * (1 + taxa) ** meses + aporte * (((1 + taxa) ** meses - 1) / taxa)

# CALCULAR CDB
def calcular_cdb(capital, aporte, meses, cdi_mensal, perc_cdi):
    taxa = cdi_mensal * perc_cdi
    montante = calcular_juros_compostos(capital, aporte, taxa, meses)
    
    total_investido = calcular_total_investido(capital, aporte, meses)
    lucro = montante - total_investido
    
    dias = meses * 30
    if dias <= 180:
        ir = 0.225
    elif dias <= 360:
        ir = 0.20
    elif dias <= 720:
        ir = 0.175
    else:
        ir = 0.15
    
    imposto = lucro * ir
    return montante - imposto

# CALCULAR LCI
def calcular_lci(capital, aporte, meses, cdi_mensal, perc_cdi):
    taxa = cdi_mensal * perc_cdi
    return calcular_juros_compostos(capital, aporte, taxa, meses)

# CALCULAR POUPANÇA
def calcular_poupanca(capital, aporte, meses):
    taxa = 0.005
    return calcular_juros_compostos(capital, aporte, taxa, meses)

# CALCULAR FII
def calcular_fII(capital, aporte, meses, taxa_mensal):
    juros_compostos = calcular_juros_compostos(capital, aporte, taxa_mensal, meses)
    
    simulacaoI = juros_compostos * (1 + random.uniform(-0.03, 0.03))
    simulacaoII = juros_compostos * (1 + random.uniform(-0.03, 0.03))
    simulacaoIII = juros_compostos * (1 + random.uniform(-0.03, 0.03))
    simulacaoIV = juros_compostos * (1 + random.uniform(-0.03, 0.03))
    simulacaoV = juros_compostos * (1 + random.uniform(-0.03, 0.03))
    
    simulacao = [simulacaoI, simulacaoII, simulacaoIII, simulacaoIV, simulacaoV]
    
    media = statistics.mean(simulacao)
    mediana = statistics.median(simulacao)
    desvio = statistics.stdev(simulacao)
    
    return media, mediana, desvio

# REALIZAR O GRÁFICO DE NO MÁXIMO 50 BLOCOS
def fazer_grafico(valor, valor_max):
    if valor_max == 0:
        return ""

    proporcao = valor / valor_max
    grafico = math.floor(proporcao * 50)

    if valor > 0 and grafico == 0:
        grafico = 1

    return "█" * grafico

# RELATÓRIO
def gerar_relatorio(capital, aporte, meses, meta, cdb, lci, poupanca, fII_media, fII_mediana, fII_desvio):
    dia_de_hoje = datetime.datetime.now()
    data_de_resgata = dia_de_hoje + datetime.timedelta(days = meses * 30)
    
    total_investido = calcular_total_investido(capital, aporte, meses)
    
    max_valor = max(cdb, lci, poupanca, fII_media)
    
    print("===================================================")
    print(f"RELATÓRIO PYINVEST - {dia_de_hoje.strftime('%d/%m/%Y')}")
    print(f"Data estimada de resgate: {data_de_resgata.strftime('%d/%m/%Y')}")
    print(f"Total investido: {formatar_valor(total_investido)}")
    print("---------------------------------------------------")
    print(f"CDB: {formatar_valor(cdb)}")
    print(f"Gráfico: {fazer_grafico(cdb, max_valor)}")
    print(f"LCI/LCA: {formatar_valor(lci)}")
    print(f"Gráfico: {fazer_grafico(lci, max_valor)}")
    print(f"Poupança: {formatar_valor(poupanca)}")
    print(f"Gráfico: {fazer_grafico(poupanca, max_valor)}")
    print(f"FII (Média): {formatar_valor(fII_media)}")
    print(f"Gráfico: {fazer_grafico(fII_media, max_valor)}")
    print("---------------------------------------------------")
    print(f"Estatísticas FII (Mediana): {formatar_valor(fII_mediana)}")
    print(f"Desvio Padrão FII: {formatar_valor(fII_desvio)}")
    
    melhor = max(cdb, lci, poupanca, fII_media)
    if melhor >= meta:
        print("Meta atingida? Sim\n")
    else:
        print("Meta atingida? Não\n")

    if melhor == cdb:
        print(f"Melhor opção: CDB com {formatar_valor(cdb)}")
    elif melhor == lci:
        print(f"Melhor opção: LCI/LCA com {formatar_valor(lci)}")
    elif melhor == poupanca:
        print(f"Melhor opção: Poupança com {formatar_valor(poupanca)}")
    else:
        print(f"Melhor opção: FII (Média) com {formatar_valor(fII_media)}")
    
def main():
    print("==================== PYINVEST ====================")
    
    capital = float(input("Capital Inicial (R$): "))
    aporte = float(input("Aporte Mensal (R$): "))
    meses = int(input("Prazo (meses): "))
    cdi_anual = float(input("CDI Anual (%): ")) / 100
    perc_cdb = float(input("Percentual CDI no CDB (%): ")) / 100
    perc_lci = float(input("Percentual CDI na LCI (%): ")) / 100
    fII_mensal = float(input("Rentabilidade FII (%): ")) / 100
    meta = float(input("Meta Financeira (R$): "))
    
    verificar_valores(capital, "Capital Inicial")
    verificar_valores(aporte, "Aporte Mensal")
    verificar_valores(meses, "Meses")
    
    cdi_mensal = converter_taxa_anual_mensal(cdi_anual)
    
    cdb = calcular_cdb(capital, aporte, meses, cdi_mensal, perc_cdb)
    lci = calcular_lci(capital, aporte, meses, cdi_mensal, perc_lci)
    poupanca = calcular_poupanca(capital, aporte, meses)
    fII_media, fII_mediana, fII_desvio = calcular_fII(capital, aporte, meses, fII_mensal)
    gerar_relatorio(capital, aporte, meses, meta, cdb, lci, poupanca, fII_media, fII_mediana, fII_desvio)
    
main()
                        

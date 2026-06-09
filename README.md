# PyInvest

## Descrição do Projeto

O **PyInvest** é uma aplicação desenvolvida em Python para simular investimentos e auxiliar na tomada de decisão financeira. O sistema compara diferentes modalidades de investimento com base em parâmetros fornecidos pelo usuário, gerando um relatório detalhado com projeções de rendimento.

As modalidades analisadas são:

- 💰 CDB
- 🏦 LCI/LCA
- 📈 Fundos Imobiliários (FII)
- 💵 Poupança

Além das simulações, o programa apresenta estatísticas, gráficos em texto e verifica se uma meta financeira será atingida dentro do prazo informado.

---

## Tecnologias Utilizadas

- Python
- Bibliotecas padrão:
  - math
  - locale
  - random
  - statistics
  - datetime

---

## Estrutura do Projeto

```text
pyinvest.py
```

---

## Funcionalidades

### Simulação de Investimentos

O sistema calcula projeções para:

- CDB com tributação de Imposto de Renda.
- LCI/LCA isentas de IR.
- Poupança com taxa fixa.
- FII com simulações de mercado.

### Conversão de Taxas

- Conversão automática da taxa CDI anual para mensal.

### Estatísticas para FIIs

São realizadas cinco simulações aleatórias de rentabilidade para estimar:

- Média
- Mediana
- Desvio padrão

### Relatório Financeiro

O relatório apresenta:

- Data atual.
- Data estimada de resgate.
- Valor total investido.
- Valor final projetado.
- Gráfico comparativo em texto.
- Melhor investimento encontrado.
- Verificação da meta financeira.

---

## Funções Implementadas

### verificar_valores()

Valida se os valores informados são positivos.

### formatar_valor()

Formata valores monetários para o padrão brasileiro.

### converter_taxa_anual_mensal()

Converte uma taxa anual para taxa equivalente mensal.

### calcular_total_investido()

Calcula o total aplicado durante todo o período.

### calcular_juros_compostos()

Realiza o cálculo de juros compostos com aportes mensais.

### calcular_cdb()

Calcula o rendimento líquido de um CDB considerando a tabela regressiva do Imposto de Renda.

### calcular_lci()

Calcula o rendimento de uma aplicação em LCI/LCA.

### calcular_poupanca()

Simula o rendimento da poupança.

### calcular_fII()

Realiza múltiplas simulações para estimar o comportamento de um Fundo Imobiliário.

### fazer_grafico()

Gera gráficos textuais utilizando blocos proporcionais ao rendimento.

### gerar_relatorio()

Exibe todas as informações finais da simulação.

### main()

Controla a execução principal do sistema.

---

## Como Executar

### Pré-requisitos

- Python instalado.

### Execução

```bash
python pyinvest.py
```

---

## Exemplo de Utilização

```text
==================== PYINVEST ====================

Capital Inicial (R$): 10000
Aporte Mensal (R$): 500
Prazo (meses): 24
CDI Anual (%): 12
Percentual CDI no CDB (%): 110
Percentual CDI na LCI (%): 95
Rentabilidade FII (%): 1
Meta Financeira (R$): 30000
```

---

## Autor

Eric Pfeuti, projeto desenvolvido para fins acadêmicos.

**Disciplina:** Algoritmos e Programação
**Linguagem:** Python
**Tipo de Projeto:** Simulador de Investimentos Financeiros.

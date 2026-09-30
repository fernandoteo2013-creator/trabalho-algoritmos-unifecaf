# Desafio de Automação Digital: Gestão de Peças, Qualidade e Armazenamento

Sistema desenvolvido em Python para a disciplina de **Algoritmos e Lógica de Programação** (UniFECAF), com o objetivo de prototipar uma solução de automação digital para controle de produção, inspeção de qualidade e empacotamento em uma linha de montagem industrial.

---

## 🚀 Funcionalidades do Sistema
O programa conta com um menu interativo totalmente funcional contendo as seguintes opções:
1. **Cadastrar nova peça:** Recebe ID, peso, cor e comprimento, avaliando automaticamente os critérios de qualidade.
2. **Listar peças aprovadas/reprovadas:** Exibe os registros filtrados ou gerais com seus respectivos detalhes e motivos de falha.
3. **Remover peça cadastrada:** Permite excluir uma peça do sistema através do seu ID (atualizando automaticamente as caixas e estoques).
4. **Listar caixas fechadas:** Mostra o status das caixas já fechadas (limite de 10 peças por caixa) e o progresso da caixa atual.
5. **Gerar relatório final:** Apresenta o consolidado total de peças processadas, taxas de aprovação, contagem de motivos de reprovação e total de caixas utilizadas.
6. **Sair:** Encerra a execução do programa com segurança.

---

## 📋 Critérios de Qualidade Validados
Para que uma peça seja **aprovada**, ela deve atender simultaneamente a três regras de negócio:
- **Peso:** Entre 95g e 105g.
- **Cor:** Apenas *azul* ou *verde*.
- **Comprimento:** Entre 10cm e 20cm.

Caso contrário, a peça é **reprovada** e o sistema registra especificamente o motivo da falha.

---

## 🛠️ Como Rodar o Programa (Passo a Passo)

Certifique-se de ter o **Python 3** instalado em sua máquina.

1. Clone este repositório ou baixe o arquivo `sistema.py`.
2. Abra o seu terminal de preferência (ou o **Visual Studio Code**).
3. Navegue até a pasta onde o arquivo foi salvo.
4. Execute o comando abaixo no terminal:
   ```bash
   python sistema.py
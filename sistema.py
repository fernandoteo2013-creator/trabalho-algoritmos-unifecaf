def main():
    pecas_aprovadas = []
    pecas_reprovadas = []
    caixas_fechadas = []
    caixa_atual = []
    
    # Contador de motivos de reprobación
    motivos_reprovacao = {
        "Peso": 0,
        "Cor": 0,
        "Comprimento": 0
    }

    while True:
        print("\n========================================")
        print("    SISTEMA DE GESTÃO DE PRODUÇÃO TIC   ")
        print("========================================")
        print("1. Cadastrar nova peça")
        print("2. Listar peças aprovadas/reprovadas")
        print("3. Remover peça cadastrada")
        print("4. Listar caixas fechadas")
        print("5. Gerar relatório final")
        print("6. Sair")
        
        opcao = input("Escolha uma opção (1-6): ").strip()
        
        if opcao == '1':
            print("\n--- CADASTRO DE NOVA PEÇA ---")
            id_peca = input("Digite o ID da peça: ").strip()
            
            try:
                peso = float(input("Digite o peso da peça (g): "))
                comprimento = float(input("Digite o comprimento da peça (cm): "))
            except ValueError:
                print("Erro: Peso e comprimento devem ser valores numéricos!")
                continue
                
            cor = input("Digite a cor da peça (ex: azul, verde, vermelho): ").strip().lower()
            
            # Evaluación de calidad
            reprovada = False
            motivos = []
            
            if not (95 <= peso <= 105):
                reprovada = True
                motivos.append("Peso fora do padrão (95g - 105g)")
                motivos_reprovacao["Peso"] += 1
                
            if cor not in ["azul", "verde"]:
                reprovada = True
                motivos.append("Cor inválida (deve ser azul ou verde)")
                motivos_reprovacao["Cor"] += 1
                
            if not (10 <= comprimento <= 20):
                reprovada = True
                motivos.append("Comprimento fora do padrão (10cm - 20cm)")
                motivos_reprovacao["Comprimento"] += 1
                
            peca = {
                "id": id_peca,
                "peso": peso,
                "cor": cor,
                "comprimento": comprimento
            }
            
            if reprovada:
                peca["motivos"] = motivos
                pecas_reprovadas.append(peca)
                print(f"\n[X] Peça ID {id_peca} REPROVADA!")
                for m in motivos:
                    print(f"    - {m}")
            else:
                pecas_aprovadas.append(peca)
                caixa_atual.append(peca)
                print(f"\n[V] Peça ID {id_peca} APROVADA e adicionada à caixa atual!")
                
                # Control de capacidad de cajas (10 piezas por caja)
                if len(caixa_atual) == 10:
                    caixas_fechadas.append(list(caixa_atual))
                    print(f">> Caixa fechada com sucesso! Total de caixas fechadas: {len(caixas_fechadas)}")
                    caixa_atual = []

        elif opcao == '2':
            print("\n--- LISTAGEM DE PEÇAS ---")
            print(f"Total de peças aprovadas: {len(pecas_aprovadas)}")
            print(f"Total de peças reprovadas: {len(pecas_reprovadas)}")
            
            sub = input("\nDeseja listar:\n1. Aprovadas\n2. Reprovadas\n3. Ambas\nEscolha (1-3): ").strip()
            
            if sub in ['1', '3']:
                print("\n--- PEÇAS APROVADAS ---")
                if not pecas_aprovadas:
                    print("Nenhuma peça aprovada cadastrada.")
                for p in pecas_aprovadas:
                    print(f"ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comprimento: {p['comprimento']}cm")
                    
            if sub in ['2', '3']:
                print("\n--- PEÇAS REPROVADAS ---")
                if not pecas_reprovadas:
                    print("Nenhuma peça reprovada cadastrada.")
                for p in pecas_reprovadas:
                    print(f"ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comprimento: {p['comprimento']}cm")
                    print(f"    Motivos: {', '.join(p['motivos'])}")

        elif opcao == '3':
            print("\n--- REMOVER PEÇA CADASTRADA ---")
            id_remover = input("Digite o ID da peça que deseja remover: ").strip()
            removida = False
            
            # Buscar en aprobadas
            for p in pecas_aprovadas:
                if p['id'] == id_remover:
                    pecas_aprovadas.remove(p)
                    removida = True
                    if p in caixa_atual:
                        caixa_atual.remove(p)
                    else:
                        for caixa in caixas_fechadas:
                            if p in caixa:
                                caixa.remove(p)
                    break
                    
            # Buscar en reprobadas
            if not removida:
                for p in pecas_reprovadas:
                    if p['id'] == id_remover:
                        pecas_reprovadas.remove(p)
                        removida = True
                        break
                        
            if removida:
                print(f"[Sucesso] Peça com ID '{id_remover}' foi removida do sistema.")
            else:
                print(f"[Aviso] Nenhuma peça encontrada com o ID '{id_remover}'.")

        elif opcao == '4':
            print("\n--- LISTAGEM DE CAIXAS FECHADAS ---")
            print(f"Total de caixas fechadas: {len(caixas_fechadas)}")
            print(f"Peças na caixa atual (em andamento): {len(caixa_atual)}/10")
            
            if not caixas_fechadas:
                print("Nenhuma caixa foi fechada ainda.")
            else:
                for idx, caixa in enumerate(caixas_fechadas, 1):
                    print(f"\nCaixa #{idx} (Contém {len(caixa)} peças):")
                    for p in caixa:
                        print(f"  - ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']}")

        elif opcao == '5':
            print("\n========================================")
            print("         RELATÓRIO FINAL DE PRODUÇÃO    ")
            print("========================================")
            total_aprovadas = len(pecas_aprovadas)
            total_reprovadas = len(pecas_reprovadas)
            total_geral = total_aprovadas + total_reprovadas
            
            print(f"Total de peças processadas: {total_geral}")
            print(f"Total de peças APROVADAS: {total_aprovadas}")
            print(f"Total de peças REPROVADAS: {total_reprovadas}")
            
            print("\nDetalhamento dos motivos de reprovação:")
            for motivo, qtd in motivos_reprovacao.items():
                print(f"  - {motivo}: {qtd} ocorrências")
                
            total_caixas = len(caixas_fechadas) + (1 if len(caixa_atual) > 0 else 0)
            print(f"\nQuantidade de caixas fechadas: {len(caixas_fechadas)}")
            print(f"Caixa atual em andamento: {len(caixa_atual)} peças")
            print(f"Total de caixas utilizadas (fechadas + em aberto): {total_caixas}")
            print("========================================")

        elif opcao == '6':
            print("\nEncerrando o sistema. Obrigado!")
            break
        else:
            print("\nOpção inválida! Escolha um número entre 1 e 6.")

if __name__ == "__main__":
    main()
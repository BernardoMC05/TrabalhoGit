# info_disciplina.py

def exibir_cabecalho():
    print("=" * 60)
    print("       📚 SISTEMA DE INFORMAÇÕES DA DISCIPLINA 📚       ")
    print("=" * 60)

def informacoes_disciplina():
    # Altere os valores abaixo com o nome real da sua matéria!
    nome_disciplina = "Desenvolvimento Web Avançado e Sistemas Integrados"
    professor = "Nome do Professor"
    
    descricao = (
        "Esta disciplina aborda a criação de aplicações modernas utilizando "
        "múltiplas tecnologias. O projeto final integra a estruturação em HTML, "
        "estilização com CSS, dinamismo via JavaScript, regras de negócio em Java "
        "e automação/scripts auxiliares com Python."
    )
    
    print(f"📖 Disciplina: {nome_disciplina}")
    print(f"👨‍🏫 Professor(a): {professor}")
    print("\n📝 Descrição da Matéria:")
    print(descricao)
    print("=" * 60)

def mini_quiz():
    print("\n🧠 MINI-DESAFIO DE CONHECIMENTO (GIT & LINGUAGENS)")
    print("-" * 60)
    
    pontos = 0
    
    # Pergunta 1
    print("1. Qual comando Git cria e muda para uma nova branch ao mesmo tempo?")
    print("   [A] git merge")
    print("   [B] git checkout -b")
    print("   [C] git commit")
    resp1 = input("Sua resposta (A/B/C): ").strip().upper()
    if resp1 == "B":
        print("✅ Correto!")
        pontos += 1
    else:
        print("❌ Incorreto. A resposta certa era B (git checkout -b).")
        
    print("-" * 30)

    # Pergunta 2
    print("2. Qual dessas linguagens é famosa por usar indentação obrigatória?")
    print("   [A] Java")
    print("   [B] JavaScript")
    print("   [C] Python")
    resp2 = input("Sua resposta (A/B/C): ").strip().upper()
    if resp2 == "C":
        print("✅ Correto! Python usa blocos baseados em espaços.")
        pontos += 1
    else:
        print("❌ Incorreto. A resposta certa era C (Python).")

    print("=" * 60)
    print(f"🎉 Fim do Quiz! Você acertou {pontos}/2 perguntas.")
    print("=" * 60)

def main():
    exibir_cabecalho()
    informacoes_disciplina()
    
    quer_jogar = input("Deseja testar seus conhecimentos no Mini-Quiz? (S/N): ").strip().upper()
    if quer_jogar == "S":
        mini_quiz()
    else:
        print("\n👋 Obrigado por usar o sistema! Bons estudos!")

if __name__ == "__main__":
    main()

# Cat Platformer - Jogo de Plataforma

Um jogo de plataforma 2D desenvolvido em Python usando Pygame Zero, onde você controla um herói que deve coletar moedas, pular sobre gatos e chegar ao final do nível.
![Image](https://github.com/user-attachments/assets/b13fc93a-d392-4fbe-9e0c-77b24228f295)

## 📚 Bibliotecas Externas Utilizadas

Este projeto utiliza as seguintes bibliotecas Python:

| Biblioteca | Versão | Função no Projeto |
|------------|---------|-------------------|
| **pgzero** | 1.2.1 | Framework principal para desenvolvimento de jogos 2D com zero boilerplate |
| **pygame** | 2.6.1 | Biblioteca de baixo nível para gráficos, áudio e entrada do usuário |
| **numpy** | 2.3.2 | Biblioteca para operações numéricas e matemáticas |

### Descrição das Bibliotecas

- **pgzero (1.2.1)**: É o framework principal que simplifica o desenvolvimento de jogos. Fornece funções como `Actor`, `screen`, `keyboard`, `sounds` e `music` que tornam a criação de jogos muito mais simples.

- **pygame (2.6.1)**: Biblioteca fundamental que pgzero utiliza internamente. Responsável por renderizar gráficos, reproduzir sons, detectar entrada do teclado/mouse e gerenciar o loop principal do jogo.

- **numpy (2.3.2)**: Biblioteca matemática que pgzero usa para cálculos internos, como posicionamento de sprites, detecção de colisões e operações vetoriais.

## 🚀 Instalação e Configuração

### Pré-requisitos

- Python 3.6 ou superior
- pip (gerenciador de pacotes Python)

### Passo 1: Clonar ou Baixar o Projeto

```bash
git clone [URL_DO_REPOSITORIO]
cd Game
```

### Passo 2: Criar e Ativar Ambiente Virtual

#### Windows (PowerShell/CMD)

```powershell
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
venv\Scripts\Activate.ps1
# OU para CMD:
venv\Scripts\activate.bat
```

#### Linux/Mac (Terminal)

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate
```

### Passo 3: Instalar Dependências

Com o ambiente virtual ativado, execute:

```bash
pip install -r requirements.txt
```

### Passo 4: Executar o Jogo

```bash
pgzrun game.py
```

## 🎮 Como Jogar

- **Setas Esquerda/Direita**: Mover o herói
- **Barra de Espaço**: Pular
- **Objetivo**: Coletar moedas e chegar ao final do nível
- **Cuidado**: Evite tocar nos gatos, a menos que esteja pulando sobre eles!

## 📁 Estrutura do Projeto

```
Game/
├── game.py              # Arquivo principal do jogo
├── requirements.txt     # Dependências do projeto
├── README.md           # Este arquivo
├── images/             # Sprites e imagens do jogo
├── sounds/             # Efeitos sonoros
├── music/              # Música de fundo
└── venv/               # Ambiente virtual (não incluir no controle de versão)
```

## 🔧 Solução de Problemas

### Erro: "pgzrun não encontrado"
- Certifique-se de que o ambiente virtual está ativado
- Verifique se todas as dependências foram instaladas: `pip list`

### Erro: "pygame não encontrado"
- Reinstale pygame: `pip install pygame==2.6.1`

### Problemas de Áudio
- Verifique se o sistema de áudio está funcionando
- Teste com `pygame.mixer.init()`

## 📝 Desenvolvimento

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Faça commit das mudanças
4. Abra um Pull Request

## 👥 Autores

[Juliana Pereira] - Desenvolvedor principal

---

**Divirta-se jogando!**

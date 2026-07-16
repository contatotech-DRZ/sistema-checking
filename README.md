# Dashboard de Monitoramento de Hardware

Um dashboard leve e moderno, desenvolvido para monitorar o uso de recursos do sistema (CPU e Memória RAM) em tempo real. Este projeto foi criado como um exercício prático de integração entre Backend (Python/FastAPI) e Frontend (HTML/JS).

Funcionalidades
- **Monitoramento em tempo real:** Atualização automática dos dados a cada 2 segundos.
- **Interface Limpa:** Design estilo "Dark Mode" para melhor visualização.
- **Leve:** Utiliza o mínimo de recursos do sistema.

Tecnologias Utilizadas
- **Linguagem:** Python
- **Backend:** FastAPI
- **Coleta de Dados:** psutil
- **Frontend:** HTML5, CSS3, JavaScript (Fetch API)

Como Rodar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/NOME-DO-REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME-DO-REPOSITORIO.git)
   cd NOME-DO-REPOSITORIO


Crie e ative um ambiente virtual (recomendado):

Bash
python -m venv venv
 No Windows:
.\venv\Scripts\Activate.ps1
Instale as dependências:

Bash
pip install fastapi uvicorn psutil
Inicie o servidor:

Bash
uvicorn main:app --reload
Acesse no navegador:
Abra http://127.0.0.1:8000

Desenvolvido por Adriano Aquino.

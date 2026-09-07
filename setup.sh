#!/usr/bin/env bash
# Setup do ambiente de prática de Python + VS Code (somente Linux)
# Rode este script UMA VEZ: bash setup.sh
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$PROJECT_DIR/.venv"

echo "==> Pasta do projeto: $PROJECT_DIR"

# 1) Garante python3, pip e venv instalados
if ! command -v python3 >/dev/null 2>&1; then
    echo "python3 não encontrado. Instalando..."
    sudo apt update && sudo apt install -y python3
fi

if ! python3 -m venv --help >/dev/null 2>&1; then
    echo "Módulo venv não encontrado. Instalando python3-venv..."
    sudo apt update && sudo apt install -y python3-venv
fi

if ! python3 -m pip --version >/dev/null 2>&1; then
    echo "pip não encontrado. Instalando python3-pip..."
    sudo apt update && sudo apt install -y python3-pip
fi

# 2) Cria a config do VS Code (workspace-only: não sincroniza com o Windows)
mkdir -p "$PROJECT_DIR/.vscode"

cat > "$PROJECT_DIR/.vscode/settings.json" <<'EOF'
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
    "python.terminal.activateEnvironment": true,
    "python.testing.pytestEnabled": true,
    "python.testing.unittestEnabled": false,
    "editor.formatOnSave": true,
    "editor.rulers": [88],
    "files.exclude": {
        "**/__pycache__": true,
        "**/*.pyc": true
    },
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter"
    }
}
EOF

cat > "$PROJECT_DIR/.vscode/extensions.json" <<'EOF'
{
    "recommendations": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-python.debugpy",
        "ms-python.black-formatter"
    ]
}
EOF

# 3) Cria o ambiente virtual (venv) se ainda não existir
if [ ! -d "$VENV_DIR" ]; then
    echo "==> Criando ambiente virtual em $VENV_DIR"
    python3 -m venv "$VENV_DIR"
else
    echo "==> Ambiente virtual já existe, reaproveitando."
fi

# 4) Instala as bibliotecas do requirements.txt dentro do venv
echo "==> Instalando bibliotecas (isso pode levar um minuto)..."
"$VENV_DIR/bin/pip" install --upgrade pip
"$VENV_DIR/bin/pip" install -r "$PROJECT_DIR/requirements.txt"

# 5) Instala as extensões do VS Code (só afeta o perfil atual da sua conta)
if command -v code >/dev/null 2>&1; then
    echo "==> Instalando/atualizando extensões do VS Code..."
    code --install-extension ms-python.python --force
    code --install-extension ms-python.vscode-pylance --force
    code --install-extension ms-python.debugpy --force
    code --install-extension ms-python.black-formatter --force
else
    echo "AVISO: comando 'code' não encontrado no PATH."
    echo "Abra o VS Code, aperte Ctrl+Shift+P, digite e rode:"
    echo "  Shell Command: Install 'code' command in PATH"
    echo "Depois rode este script de novo, ou instale manualmente as extensões:"
    echo "  ms-python.python, ms-python.vscode-pylance, ms-python.debugpy"
fi

echo ""
echo "=================================================="
echo " Tudo pronto!"
echo " Abra esta pasta no VS Code:"
echo "   code \"$PROJECT_DIR\""
echo " O interpretador Python já vem configurado (.venv)."
echo " Teste rodando o arquivo exemplo.py (Run > Run Without Debugging)."
echo "=================================================="

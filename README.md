# Agenda Físio

Sistema de Agendamentos e Anamnese da Fisioterapia

## Como desenvolver?

1. Clone o repositório;
1. Crie um virtualenv com Python 3.9;
1. Ative o virtualenv;
1. Instale as dependências.
1. Configure a instância com o .env

```
git clone git@github
cd agenda_fisio
python -m venv .agenda_fisio
# Linux/MacOs
source .agenda_fisio/bin/activate
cp contrib/env-sample .env
# Windows
.agenda_fisio\Script\activate
copy contrib\env-sample .env

pip install -r requirements-dev.txt
```

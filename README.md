# 🏎️ F1 Database & Championship Management System

Sistema em Python com SQLite desenvolvido para gerenciamento de dados históricos da Fórmula 1 (2020 a 2026), acompanhamento de pódios, resultados por circuito e simulação de campeonatos.

> 🚀 **Status do Projeto:** Versão 1.0 (Terminal/CLI) — *Pronto para evolução Web em HTML/CSS/JS*.

---

## 📌 Sobre o Projeto

Este projeto consiste em um sistema de banco de dados relacional para registrar e consultar dados da Fórmula 1. Ele automatiza o preenchimento de informações dos pilotos (equipes e números) por temporada e calcula automaticamente a pontuação oficial da FIA para gerar a classificação final do Mundial de Pilotos e Construtores.

### 🌟 Principais Funcionalidades
- **Automação de Ingestão de Dados:** Importação dinâmica de temporadas históricas (arquivos de dados por ano via `importlib`).
- **Cadastro Inteligente de Corridas:** Busca automatizada por iniciais/sobrenomes dos pilotos (`VER`, `HAM`, `BOR`, etc.) integrando equipe e número do carro automaticamente.
- **Tabela Oficial de Pontuação:** Cálculo automático do 1º ao 10º lugar no padrão FIA (25-18-15-12-10-8-6-4-2-1).
- **Consultas Rápidas:** Busca de pódios por circuito/ano e verificação imediata dos Campeões Mundiais (*World Champions*).
- **Encerramento Automático:** Detecção do limite de 24 corridas por temporada.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Banco de Dados:** SQLite3
- **Controle de Versão:** Git / GitHub

---

![Sistema em visualização](tabela.png)

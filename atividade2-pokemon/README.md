# Pokédex - Aplicação Flask

Uma aplicação web desenvolvida em Flask que consome a PokeAPI para exibir informações sobre Pokémons.

## Funcionalidades

- **Página Inicial**: Apresentação da aplicação com navegação intuitiva
- **Lista de Pokémons**: Exibe cards com informações básicas dos primeiros 20 Pokémons
- **Detalhes do Pokémon**: Página detalhada com estatísticas, habilidades e informações completas
- **Design Responsivo**: Interface moderna e adaptável a diferentes dispositivos

## Estrutura do Projeto

```
atividade2-pokemon/
├── app.py                 # Arquivo principal da aplicação Flask
├── controllers/
│   └── routes.py         # Definição das rotas e lógica da aplicação
├── views/
│   ├── base.html         # Template base com navegação
│   ├── index.html        # Página inicial
│   ├── pokemon.html      # Lista de Pokémons
│   ├── pokemoninfo.html  # Detalhes do Pokémon
│   └── error.html        # Página de erro
├── static/
│   └── css/
│       └── style.css     # Estilos personalizados
└── README.md             # Este arquivo
```

## Como Executar

1. **Instalar dependências**:
   ```bash
   pip install flask
   ```

2. **Executar a aplicação**:
   ```bash
   python app.py
   ```

3. **Acessar no navegador**:
   ```
   http://localhost:5000
   ```

## Rotas Disponíveis

- `/` - Página inicial
- `/pokemon` - Lista de Pokémons
- `/pokemon/<id>` - Detalhes do Pokémon específico

## Tecnologias Utilizadas

- **Flask**: Framework web Python
- **Bootstrap 5**: Framework CSS para design responsivo
- **PokeAPI**: API pública para dados dos Pokémons
- **HTML/CSS/JavaScript**: Frontend da aplicação

## Características da Aplicação

- ✅ Interface moderna e intuitiva
- ✅ Cards responsivos com efeitos hover
- ✅ Navegação clara entre páginas
- ✅ Exibição de estatísticas com barras de progresso
- ✅ Tratamento de erros para Pokémons não encontrados
- ✅ Design adaptável para mobile e desktop

## API Utilizada

A aplicação consome a [PokeAPI](https://pokeapi.co/), uma API pública que fornece dados completos sobre Pokémons, incluindo:
- Informações básicas (nome, ID, tipos)
- Imagens dos Pokémons
- Estatísticas base
- Habilidades
- Altura e peso

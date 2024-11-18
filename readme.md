# Sistema de Estoque

Este é um sistema de gerenciamento de estoque desenvolvido em Python com uma interface gráfica criada usando a biblioteca `tkinter`. O sistema permite cadastrar, consultar e gerar relatórios dos produtos em estoque.

## Funcionalidades

- **Cadastro de Produtos**: Adicione produtos ao estoque com ID, nome, preço e quantidade.
- **Consulta de Produtos**: Busque produtos no estoque pelo ID.
- **Geração de Relatórios**: Crie relatórios em formato Excel com todos os produtos cadastrados.
- **Interface Gráfica (GUI)**: Desenvolvida com `tkinter` e `ttk` para estilos e widgets.
- **Tela de Login**: Diferencia entre administradores e usuários padrão, carregando a interface principal correspondente.

## Requisitos

- Python 3.x
- Bibliotecas:
  - `tkinter`
  - `Pillow`
  - `pandas`

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu_usuario/sistema-de-estoque.git
    cd sistema-de-estoque
    ```

2. Instale as dependências:
    ```bash
    pip install pandas pillow
    ```

3. Execute o script:
    ```bash
    python sistemaestoque.py
    ```

## Como Usar

1. Inicie o aplicativo e faça login com as credenciais apropriadas:
   - **Administrador**: Usuário: `adm`, Senha: `11042003`
   - **Usuário Padrão**: Usuário: `padrao`, Senha: `1234`
   
2. Use as opções disponíveis na interface gráfica para cadastrar, consultar produtos e gerar relatórios.

## Criar Executável

Para criar um executável do projeto, você pode usar a biblioteca `pyinstaller`. Siga os passos abaixo:

1. Instale o `pyinstaller`:
    ```bash
    pip install pyinstaller
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd caminho/para/o/diretorio/do/projeto
    ```

3. Gere o executável:
    ```bash
    pyinstaller --onefile sistemaestoque.py
    ```

4. O executável será criado na pasta `dist`. Você pode encontrá-lo em `dist/sistemaestoque.exe`.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

## Contato

Para mais informações, entre em contato com [seu_email@exemplo.com](mailto:seu_email@exemplo.com).

# # Boas-vindas ao repositório do Job Insights!
  
Neste projeto foi implementado análises a partir de um conjunto de dados sobre empregos.  
  
Minhas implementações foram incorporadas a um aplicativo Web desenvolvido com Flask (um framework web muito popular na comunidade Python). Também foi desenvolvido testes para a implementação de uma análise de dados.  
  
Os dados foram extraídos do site Glassdoor e obtidos através do Kaggle, uma plataforma disponiblizando conjuntos de dados para cientistas de dados.  
  
Habilidades a que foram trabalhadas:  
Utilizar o terminal interativo do Python.  
Utilizar estruturas condicionais e de repetição.  
Utilizar funções built-in do Python.  
Utilizar tratamento de exceções.  
Realizar a manipulação de arquivos.  
Escrever funções.  
Escrever testes com Pytest.  
Escrever seus próprios módulos e importá-los em outros códigos.


#  Orientações

<details>
<summary><strong>Dependencias</strong></summary><br />
1.  Clone o repositório

-   Use o comando:  `git clone git@github.com:F-Herbert/job-insights.git`.
-   Entre na pasta do repositório que você acabou de clonar:
    -   `cd sd-023-a-project-job-insights`

2.  Crie o ambiente virtual para o projeto

-   `python3 -m venv .venv && source .venv/bin/activate`

3.  Instale as dependências

-   `python3 -m pip install -r dev-requirements.txt`
</details>

<details>
  <summary><strong>Testes</strong></summary><br />

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

  ```bash
  $ python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Se desejar que os testes parem de ser executados quando acontecer o primeiro erro, use o parâmetro `-x`

  ```bash
  python3 -m pytest -x tests/test_jobs.py
  ```
  
  Para executar um teste específico de um arquivo, basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py::test_nome_do_teste
  ```

  Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse [artigo](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).

  Além dos testes com o Pytest, você pode (e vai ser bem bacana) rodar a aplicação flask para visualizar no navegador o resultado do desenvolvimento das funções.
  Para isso, digite o comando `flask run`, e acesse o site gerado pelo Flask em `http://localhost:5000`. No começo do desenvolvimento, você verá que muitas coisas não funcionam, mas conforme você for implementando os requisitos, perceberá que a aplicação web começa a utilizar suas implementações e passa a ganhar vida.

</details>
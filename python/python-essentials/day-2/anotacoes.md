# Tipos de dados no Python
- Video 1

    Tipos de dados e protocolo: são duas coisas que sempre andam juntas.

    Classe / Categoria / Tipo: são as mesmas coisas.

    Classe: é o objeto em si.
    Categoria: é toda a teoria.
    Tipo: é o tipo de dado.
    No Python, todo dado que começa com 0b é um número binário.

    Se um dia você quiser saber em que posição o Python guarda cada endereço de
    memória que você reservou (variável), você pode passar a variável.
    Por exemplo:


    ```python

    numero = 64

    ```


    ```python

    id(numero)  # Retorna o endereço da memória que está reservado para aquela variável

    ```


    Outro exemplo é verificar o tipo da variável:

    ```python

    type(numero)  # Retorna o tipo da variável

    ```


    Os tipos de dados no Python são separados em duas categorias:

    Primários e Compostos.
    Primários ou Scalar types: são tipos de dados definidos para representar apenas um valor.

    Por exemplo:


    ```python

    numero = 65

    ```


    Aqui está um exemplo de código forçando o tipo:

    ```python

    numero = int(65)

    ```

    Apesar de o Python aceitar isso, esse código é redundante e não é aconselhável usar.


    Para a gente saber quantos metodos tem um obj do tipo int
    podemos passar o seguinte comando:
    ```python

    dir(int) # lista todos os metodos do int

    ``
    obs: No int temos 72 metodos disponivel para usar

- Video 2
    - Tipos de dados Float

        Aqui usamos para dados fracionado

    ex:

    ```python
    valor = 5/2

    ```
    um bom exemplo de float sao numero de latitute e longitude


    - bool
        o bool sempre que comparamos no python um valor diferente de 0 ele sempre retorna
        True pq ele entende que somente 0 é False e qualquer coisa diferente de 0 é True
        ```python

        if 4940950:
            print("É true")

        ```
    - NoneType
        nulo, ausencia de valor
        ex:
        ```python

            nome = None

        ```

        Uma curiosidade: no python se declarar 5 variavel com valor None se vc obj
        ou dar o comando id(a) / id(b) / id(c) pode perceber que o python guarda as variavel no mesmo
        espaco de memoria isso é chamado de Singleton, pois todas variavel tem o mesmo valor.

        Toda funcao no python retorna um obj


- Video 3

    String em python
    no python usamos um padrao ASCII para juntar todo caracteri das string

    temos uma tabela com toda info no ASCII chamada ASCII TABLE
    string = corrente de byte.


#OBS: No python nao existe vc nao declarar uma variavel ou obj, tudo tem que ser iniciado

    uma str em python ela é interabe ou seja ela é percorrivel ex:

    ```python

        for letra in nome:
            print(letra)
    ```

    outuput:
    C
    a
    r
    l
    o
    s

    para vc ordernar e desordenar um str vc pode usar o sorted para deixar em orderm alfabetica
    e usar o reversed para deixar ao contrario a str

- Video 4
    segunda parte de str

    OBS: O python é de tipagem dinamica e forte

    tipos de formatacao de str
        # Interpolação
            exemplo:

            ```python
                templade = "o sadlo é %s é o total de %d"
            ```

    temos tbm a centralizacao de string, que podemos fazer assim:

    ex:

    ```python

        "{:^11}".format("Carlos")
    ```
    assim ele centraliza com 11 espaço a string Carlos

    tipos de formatacao:
    ```python
    "{:<11}".format("Carlos") # esquerda
    "{:>11}".format("Carlos") # direita
    "{:^11}".format("Carlos") # centralizado
    "{:*^11}".format("Carlos") # neste exemplo ele preenche o espaco vazio por *
    "{:*^11.3}".format("Carlos") # neste, ele corta a string nas 3 primeiras letras
    "{:.4f}".format(456.89) # formata com 4 digitos dps do ponto ou virgula
    "{:^20.4f}".format(456.89) # formata centralizado e 4 digitos dps da virgula
    "{:-^20.4f}".format(456.89) # formata centralizado e 4 digitos dps da virgula e preenche os espacos vazios com -
    ```


    quando vc usa cada modo de formatacao?

    concatenacao %s --> para logging
    string.format{} --> msg longas, email
    f-string --> para todo o resto

    DICA: para vc procurar um emoji no ipython vc pode fazer assim:

    ```python
    print("\N{GREEN APPLE}") # dentro do {} vc coloca o emoji que vc quer
    ```

    toda vez que temos 3 pontos: ... --> chamamos no python de elipices

    é aconsavel nao fazer operacoes dentro do {} do fstring, nao é uma boa pratica

- Video 5
    Tipos de dados compostos
    1 - Tuplas
    Tuplas sao com ()
    unpacking --> é quando vc desempacota uma tupla para uma variavel ex:

    ```python

    pontos = 2, 1, 99
    x, y, z = pontos # aqui vc esta referindo 3 variavel com os valores da tupla

    ```

    temos tbm assim:

    ```python
    pontos = 2, 1, 99
    x, *_ = pontos # neste exemplo ele pega apenas o primeiro, elemento e dps junta todos os valores da tupla na variavel _

    ```

    obs: neste exemplo a cima usamos o _ pq na convensao do python significa que vc nao esta se importando com o resto dos dados
    por isso usamos _, so estamos importando com o dado do x neste caso

    na convesao do python usamos a seguinte estrutura para desenpacotamento

    head --> inicio ou primeiro elemento de uma sequencia
    body --> corpo ou meio de uma estrutura
    tail --> ultimo elemento de uma sequencia


- Video 6
    Tipos de dados compostos
    1 - Lista

    temos dois jeito de criar uma lista no python
    ```python
     user = [] # essa é uma boa maneira de usar lista
     user = list() # essa nao é uma boa pratica
    ```



- Video 7
    Tipos de dados compostos
    1 - Sets ou conjunto no portugues
    Sets sao definido assim no python:
    ```python
    c1 = {1, 2, 3} # este metodo nao é muito recomendavel
    c2 = set((1, 2, 3)) # assim é mais recomendavel
    ```

    c2 = set((1, 2, 3)) neste exemplo, criamos um set a partir de uma tupla ou
    podemos criar a partir de umalista tbm ex:
    c3 = set([1, 2, 3])
    a grande questao do set é que ao passar um set e ao acessar ele, ele retorna
    o obj item por item sem duplicatas ex:
    c5 = set("banana")
    se vc acessar ele ele ira retornar algo assim:
    {'a', 'b', 'n'}
    mesmo banana tendo 3 a e 2 n ele retorna apenas um
    o set tbm serve para implementar a terioria de conjunto representada na imagem
    dentro da pasta day-2 com o nome de diagrama-venn-conjuntos.jpg

    representando uma teoria de conjunto com sets no python:

    ```python
    conjunto_a = [1, 2, 3, 4 ,5]
    conjunto_b = [4, 5, 6, 7, 8]
    # esses dois conjuntos sao declarado como listas
    ```
    agora podemos realizar o que chamamos de uniao ao tranformar essas duas listas em set

    ```python
    uniao_com_set = set(conjunto_a) | set(conjunto_b)
    ```

    obs: nunca podemos confiar na ordenacao do set, caso precisamos de ordenacao
        devemos ordenar apos juntar os sets

    podemos tbm realizar a uniao de dois metodos | igual fizemos acima e com a
        palvra union ex:

    ```python
    uniao_com_set = set(conjunto_a).(set(conjunto_b))
    ```

    temos tbm o metodo de intersecao dos conjuntos que mostra qual valores se
        repete nos dois conjuntos

    ```python
    conjunto_a = set([1, 2, 3, 4 ,5])
    conjunto_b = set([4, 5, 6, 7, 8])
    # esses dois conjuntos sao declarado como listas
    ```
    usamos o intersection para retornar os valores repetidos ex:

    ```python
    conjunto_a.intersection(conjunto_b)
    ```
    output:
    {4, 5}

    ou podemos usar o & para o intersection ex:
    ```python
    conjunto_a & conjunto_b
    ```
    output:
    {4, 5}

    temos tbm a diferenca de conjuntos ex:
    qual os valores que tem no conjunto que nao existe no conjunto b ?
    ```python
    conjunto_a - conjunto_b
    ```
    ou podemos usar o difference ex:
    ```python
    conjunto_a.difference(conjunto_b)
    ```
    obs: no sets a ordem sempre vai importar

    temos tbm a diferenca simetrica que pega todos os conjuntos que esta so no
        conjunto_a + todos que estao so no conjunto_b ex:
    ```python
    conjunto_a.symmetric_difference(conjunto_b)
    ```
    ou podemos usar o operador ^ para a diferenca simetrica
    ```python
    conjunto_a ^ conjunto_b
    ```

    Quando temos um lista muito grande e temos que procurar um elemento nela
    falamos que essa operacao é chamada de # O(n) ou seja um big O para n

    se tentamos fazer essa mesma operacao para um set chamamos ele de:
    O(1) - Constante
    isso ocorre pq no set ele tem o # Hash Table, a grosso modo seria um mapa dos elementos que temos no set
        por isso a operacao dele sempre vai ser mais rapida que uma lista.

- Video 8
    Tipos de dados compostos
    Dicionarios
    Dicionarios no python sao representados por chave e valor e uma {} ex:
    ```python
    exemplo_dicionario = {idade: "37", sexo: "F"}
    ```
    obs: o dicionario ele aceita apenas 3 tipos de dados representado nessa seguencia

    ex:
    ```python
    exemplo_dict_01 = {"key": "valor"} # duas strings

    exemplo_dict_02 = {"key": 0123} # chave string e um valor numerico

    exemplo_dict_03 = {0: "exemplo"} # chave inteira e valor string
    ```
    adicionando novos valores em um dict:

    ```python
    clientes = {"nome": "Carlos", "cod": 123}
    clientes["cidade"] = "Viena" # add um novo valor
    clientes{"nome": "Carlos", "cod": 123, "cidade": "Viena"} # output do dicionario dps de add um novo valor

    del cliente["nome"] # vc apaga o nome e valor do cliente
    ```

    Como o dicionario as busca sao muito mais rapidas dos que outras estruturas composta
        por ele ja sabe o index dos valores e por isso aqui vamos dar exemplo de como buscamos
        objs dentro de um dict:

    ```python
    "cod" in cliente:
    True #output
    ```

    OBS: uma obs bem importante sempre que a busca foi baseada na chave a
    busca vai ser bem rapida agora se a busca for baseada no valor a busca nao
    vai ser tao rapida. e tambem que dic nao permites adicionar valores duplicados

    No dict podemos acessar todos os nomes das chaves atraves do comando:

    ```python
    clientes.keys()

    dict_keys(['nome', 'cod', 'cidade']) #output

    # ou podemos tbm so pegar os valores assim:
    clientes.values()

    dict_values(['Carlos', 123, 'Viena']) #output

    # ou podemos tbm ter os dois valores no formato de tuplas assim:

    clientes.items()

    dict_items([('nome', 'Carlos'), ('cod', 123), ('cidade', 'Viena')]) #output

    ```

    - Merge ou juncao de dicts

    Podemos fazer assim:

    ```python
    novo_dict = {'pais': 'Portugal'}

    clientes.update(novo_dict) # junta os dois dicts
    {'nome': 'Carlos', 'cod': 123, 'cidade': 'Viena', 'pais': 'Portugal'} # output

    ```

    ou podemos fazer assim tbm para desempacotar dois dicionarios

    ```python
    cliente = {"nome": "Carlos", "cod": 123, "cidade": "Viena"}

    extra = {"pais": "Brazillian"}

    final = {**cliente, **extra}

    ```

    OBS: no python usamos os * para desempactor os pacotes ou ** duplos
        para desempacotar elementos com dois obs

    Podemos fazer assim para percorrer uma chave e valor no python:

    ```python
    for chave, valor in cliente.items():
        print(chave, "-->", valor)
    ```

    No dicionario tbm podemos pegar os valores com get ex:

    ```python

    cliente = {"nome": "Carlos", "cod": 123, "cidade": "Viena"}

    # pegando valores com get

    cliente.get("telefone")

    ```
    Nota: neste exemplo vc percebe que tentamos pegar um chave do valor
        telefone que nao existe dentro de cliente, ai neste caso ele vai
        retornar None pq nao temos a chave de valor telefone, por isso sempre
        recomendamos usar get para pegar um valor no dicionario pq ele nao da
        erro caso nao encontre o valor.
        Tbm podemos usar um valor default, caso nao encontre a chave e valor
        que estamos pesquisando, podemos fazer assim quando quiser passar um
        valor default.

    ```python

    cliente.get("telefone", "191")

    ```


    sets --> (hash table) - O(1) - constante
    dicts --> (Hash Table)
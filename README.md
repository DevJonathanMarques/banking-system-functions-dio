
# Projeto de Sistema Bancário em Python da Dio

Esse é o meu primeiro projeto em python desenvolvido nas aulas da Dio.
## Sobre o Projeto
O projeto foi desenvolvido utilizando o VS Code e a linguagem de programação Python. Criei um sistema onde é possível realizar o depósito, saque e visualização de extrato de uma conta bancária de um usuário.

Para rodar o sistema, basta abrir o seguinte arquivo no terminal:

```http
banking-system-dio.py
```
Agora, para você conseguir realizar operaçoes, você deve realizar o seguinte passo a passo:

## Passo 1 - Criar Usuário

O menu abaixo será exibido assim que o arquivo for aberto:

```http
[0] Criar usuário
[1] Acessar usuário
[2] Sair do sistema

=>
```

Somente após criar um usuário, você poderá acessá-lo. Para acessar, você deve utilizar o mesmo cpf que foi inserido ao criar o usuário.

Caso você selecione a opção 2, sair do sistema, o sistema será encerrado e, para iniciá-lo, deverá abrir o arquivo novamente.

## Passo 2 - Criar Conta

Para realizar as operações, deve ser criada uma conta dentro de um usuário. Um usuário pode ter várias contas e cada uma delas é independente da outra. Ao selecionar a opção 0, criar conta, a conta será automaticamente criada e será informado o número dela. Então, para acessá-la, selecione a opção 1 e informe o número da conta.

```http
[0] Criar conta
[1] Acessar conta
[2] Sair do usuário

=>
```

A opção 2, sair do usuário, sairá do cpf do usuário acessado e retornará para o menu anterior.

## Passo 3 - Realizar Operações

Agora, com o usuário e conta acessados, você pode realizar as operações de depositar um valor, sacar um valor e exibir o extrato.

```http
[0] Depositar
[1] Sacar
[2] Exibir extrato
[3] Sair da conta

=>
```

Caso seja selecionada a opção 3, sair da conta, você sairá da conta atual e retornará ao menu anterior, podendo selecionar outra conta.
#language:pt

@login
Funcionalidade: realizar login no sistema da Globo Play
Para validar a autenticação no sistema da Globo Play
Como usuário do sistema
Eu quero logar e validar se de fato estou logado

Cenário: realizar login no sistema com usuários válidos
            Dado que usuário possa acessar a tela de login do sistema
            Quando inserir um email valido
            E inserir uma senha válida e clicar em Entrar
            Então o nome do usuario logado deve ser exibido.


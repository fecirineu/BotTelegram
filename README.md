🤖 Bot de Lembretes e Cotação
Este é um bot simples usado para fins educacionais, mas funcional, para Telegram. Ele foi projetado para ajudá-lo a criar lembretes e consultar a cotação atual de Dólar e Bitcoin diretamente no chat.

🚀 Funcionalidades Atuais
Lembretes: Crie lembretes rápidos para não esquecer de tarefas, eventos ou qualquer coisa que precise ser lembrada.

Cotação de Moedas: Obtenha a cotação em tempo real de Dólar e Bitcoin, utilizando uma API pública para dados atualizados.

Interação Básica: O bot responde a qualquer mensagem de texto com a mesma mensagem, confirmando o que você disse.

Envio para Site (Opcional): Possui uma função para enviar mensagens e IDs de chat para uma URL específica, permitindo integração com um site ou painel externo (requer configuração da URL_SITE no código).

📦 Como Instalar e Executar
Siga os passos abaixo para configurar e rodar o bot no seu ambiente local.

Pré-requisitos
Python 3.10 ou superior instalado na sua máquina.

Uma conta no Telegram.

Um token de bot do Telegram, que você pode obter facilmente conversando com o @BotFather no próprio Telegram.

Configure seu token do Telegram:
Abra o arquivo main.py no seu editor de código. Localize a linha que define o TOKEN e insira o token que você obteve do @BotFather:

TOKEN = "SEU_TOKEN_AQUI" # Substitua SEU_TOKEN_AQUI pelo seu token real

☁️ Como Publicar na Discloud (24/7 Online)
Para que seu bot fique online 24 horas por dia, você pode hospedá-lo gratuitamente na Discloud. Siga estes passos:

Pré-requisitos
Uma conta na Discloud.

Ter o CLI da Discloud (Command Line Interface) instalado e configurado no seu computador.

Os arquivos main.py, requirements.txt e discloud.config devem estar no diretório raiz do seu projeto.

1. Verifique o arquivo discloud.config
Este arquivo é essencial para a Discloud saber como rodar seu bot. Ele já está incluído neste repositório. Certifique-se de que os valores correspondem ao que você deseja para seu deploy:

ID=telegrambotdiscloud
NAME=MeuBotTelegram
TYPE=python
MAIN=main.py
RAM=100
AUTORESTART=true
VERSION=3.10

ID: Um ID único para seu bot na Discloud (pode ser o que está ou você pode mudar).

NAME: O nome que aparecerá no painel da Discloud.

TYPE: Tipo da aplicação (Python neste caso).

MAIN: O arquivo principal a ser executado quando o bot iniciar.

RAM: Quantidade de RAM que seu bot usará (100MB é geralmente suficiente para bots simples).

AUTORESTART: Define se o bot deve reiniciar automaticamente em caso de falha.

VERSION: A versão do Python a ser usada.

2. Faça o login no CLI da Discloud
Abra o terminal ou prompt de comando e execute o comando de login da Discloud:

discloud login

Você será instruído a colar seu token de acesso da Discloud. Você pode encontrar este token no painel da Discloud, na seção de API.

3. Faça o deploy do seu bot
Com o discloud.config no diretório do projeto e o login feito no CLI, basta executar o comando de deploy:

discloud push

O CLI da Discloud irá compactar e enviar todos os arquivos do seu projeto para a plataforma. A Discloud cuidará da instalação das dependências e da inicialização do bot. Em poucos minutos, seu bot estará online e acessível 24/7! Você pode acompanhar o status e os logs através do painel da Discloud.

💡 Comandos e Uso
Uma vez que o bot esteja online, você pode interagir com ele no Telegram usando os seguintes comandos:

/start - Inicia uma conversa com o bot e exibe uma mensagem de boas-vindas.

/lembra <mensagem> em <tempo> segundos - Cria um lembrete que será enviado após o tempo especificado.

Exemplo: /lembra beber agua em 60 segundos

/cotacao - Exibe a cotação atual do Dólar (USD) e do Bitcoin (BTC) em Reais (BRL).

Qualquer outra mensagem de texto que você enviar ao bot será repetida de volta para você.

🛠️ Tecnologias Utilizadas
Python: A linguagem de programação principal para o desenvolvimento do bot.

python-telegram-bot: Uma biblioteca robusta e fácil de usar para interagir com a API do Telegram.

requests: Usada para fazer requisições HTTP para a API de cotação de moedas.

json: Para salvar e carregar os lembretes em um arquivo local.

threading: Utilizado para agendar lembretes sem bloquear o fluxo principal do bot.

API economia.awesomeapi.com.br: Fonte dos dados de cotação de moedas.

Discloud: Plataforma de hospedagem para manter o bot online 24/7.

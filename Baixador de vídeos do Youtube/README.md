# Youtube Videos Downloader
<p>Esse projeto consiste em um aplicativo de usabilidade simples que tem como função baixar um vídeo do YouTube, suportando os formatos mp3 e mp4.</p> 

<p align="center">
 <a href="#pré-requisitos">Pré Requisitos</a> •
 <a href="#tecnologias">Tecnologias</a> •
 <a href="#autor">Autor</a>

 ---
</p>

## Pré-requisitos

Para você poder testar a aplicação ou olhar e entender o código fonte, precisará ter na sua máquina instalado as seguintes ferramentas:
[Git](https://git-scm.com/), [Python](https://www.python.org/), e um bom editor de código, como o [Visual Studio Code](https://code.visualstudio.com/).

### 🎲 Rodando o aplicativo
```bash
# Clone este repositório
$ git clone <https://github.com/AlefPontes/youtube-videos-downloader>

# Acesse a pasta
$ cd youtubevideosdownloaderpython

# Instale as bibliotecas necessárias
$ pip install pytube
$ pip install moviepy

# Execute o arquivo .py
$ python .\main.py
```

### 💾 Transformando o projeto em um arquivo executável
```bash
# Primeiramente vamos baixar a biblioteca pyinstaller
# Para isso acesse o seu terminal e digite o seguinte comando
$ pip install pyinstaller

# Agora vamos transformar o arquivo .py em um .exe
$ pyinstaller --onefile --noconsole --windowed .\main.py
```

Após fazer isso, arraste o arquivo executável que está localizado na pasta dist para a pasta mãe do projeto onde estão localizadas todas as outras pastas

## Tecnologias
💻 As seguintes ferramentas foram utilizadas no projeto:
- [Python](https://www.python.org/)
- [PyTube](https://pytube.io/en/latest/)
- [MoviePy](https://pypi.org/project/moviepy/)

## Autor
Feito por [Alef Pontes](https://www.github.com/AlefPontes) 👋 Veja meu [LinkTree](https://linkr.bio/AlefPontes) 🎄

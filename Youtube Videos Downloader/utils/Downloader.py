from pytube import YouTube
from pytube.exceptions import VideoUnavailable, RegexMatchError
from moviepy.audio.io.AudioFileClip import AudioFileClip
import os

filesize = 0

class YoutubeDownloadLib:
    def __init__(self):
        pass
        
        
    def Mp4Download(self, source, path):
        try:        
            # Downloading the video in a mp4 format / Baixando o vídeo em formato mp4
            video = source.streams.get_highest_resolution()
            global filesize
            filesize = video.filesize
            video.download(output_path=path)
        except:
            return 'dcerror'


    def Mp3Download(self, source, path):
        try:
            # Downloading only the audio, but in a mp4 format / Baixando apenas o áudio, mas em formato mp4
            video = source.streams.get_audio_only()
            global filesize
            filesize = video.filesize
            video.download(output_path=path)

            # Converting the mp4 file in a mp3 file
            title = str(source.title)
            clip = AudioFileClip(rf"{path}\{title}.mp4")
            clip.write_audiofile(rf"{path}\{title}.mp3")
            os.remove(rf"{path}\{title}.mp4")

            clip.close()
        except:
            return 'dcerror'


    def MainDownload(self, link, format, path):
        try:
            # Picking up the video basic informations / Pegando as informações básicas do vídeo
            yt = YouTube(link)

            # These informations are not used on application, but if you want, you can use otherwise / Essas informações não são usadas no aplicativo, mas se você quiser, pode usar de outra forma
            result = {
                'author': yt.author,
                'title': yt.title,
                'description': yt.description,
                'views': yt.views,
                'lenght': yt.length,
                'publish_date': yt.publish_date,
                'thumbnail': yt.thumbnail_url
            }

            # Downloading the video / Baixando o vídeo
            if format == 'mp3':
                video = self.Mp3Download(yt, path)

                if video == 'dcerror':
                    return False

            elif format == 'mp4':
                video = self.Mp4Download(yt, path)

                if video == 'dcerror':
                    return False

            return result

        # Exceptions
        except VideoUnavailable:
            return False

        # if the link is invalid, it will trigger this error / Se o link for inválido, irá acionar este erro
        except RegexMatchError:
            return False

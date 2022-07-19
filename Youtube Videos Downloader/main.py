from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import messagebox

from utils.Downloader import YoutubeDownloadLib

def Browse():
    global path
    path = askdirectory(initialdir="C:")
    path_label['text'] = rf"{path}"


def After_Download():
    # Validating superficially the URL / Validando superficialmente a URL
    url = urlEntry.get()

    if url == '':
        messagebox.showerror(title='ERROR!', message='Invalid URL, please try again.')
        return
    
    if url.startswith('https://www.youtu.be') or url.startswith('https://www.youtube'):
        pass
    
    else:
        messagebox.showerror(title='ERROR!', message='The specified URL was not found, please verify that it is correct and try again.')
        return

    # Validating the destiny path / Validando o caminho de destino
    try:
        if path == '':
            messagebox.showerror(title='ERROR!', message='No path selected')
            return

    except:
        messagebox.showerror(title='ERROR!', message='No path selected')
        return

    format = formatValue.get()

    Download_Video(url=url, format=format, path=path)


def Download_Video(url, format, path):
    d = YoutubeDownloadLib()
    video = d.MainDownload(link=url, format=format, path=path)

    if video == False:
        messagebox.showerror(title='ERROR!', message='Somenthing went wrong with the video downloading, try again.')
        return
    
    else:
        messagebox.showinfo(title='SUCESS!', message='The download has finished!')


# Creating the window / Criando a janela
window = Tk()
window.title("YouTube Videos Downloader")
window.geometry("490x560+610+153")
window.resizable(width=False, height=False)
window.iconbitmap("images\\icon.ico")

# Preparing the images / Preparando as imagens
yt_background_image = PhotoImage(file="images\\background.png")
download_button_image = PhotoImage(file="images\\download_button.png")
browse_button_image = PhotoImage(file="images\\browse_button.png")

# Background Label / Label do fundo
youtube_background_label = Label(window)
youtube_background_label['image'] = yt_background_image
youtube_background_label.pack()

# The URL entry box / A caixa de entrada da URL
urlEntry = Entry(window, bd=1, font="Calibri 15 bold", justify=LEFT, bg="#545454", fg="#feffff")
urlEntry.place(width=392, height=40, x=49, y=239)

# The destiny path box / A caixa do texto do caminho de destino
path_label = Label(window, font="Calibri 13 bold", justify=LEFT, anchor=W, bd=1, bg="#545454", fg="#feffff")
path_label.place(width=292, height=40, x=49, y=315)

# Creating the buttons / Criando os botões
download_button = Button(window, bd=0, image=download_button_image, relief=RAISED, overrelief=RIDGE, command=(After_Download))
download_button.place(width=175, height=62, x=159, y=451)

browse_button = Button(window, bd=0, image=browse_button_image, relief=RAISED, overrelief=RIDGE, command=(Browse))
browse_button.place(width=86, height=40, x=355, y=315)

# Video format buttons / Botões do formato do vídeo
formatValue = StringVar()
mp3_button = Radiobutton(window, text='MP3', font="Calibri 15 bold", value='mp3', variable=formatValue, indicator = 0, bg="#545454")
mp3_button.place(width=65, height=40, x=165, y=380)
mp4_button = Radiobutton(window, text='MP4', font="Calibri 15 bold", value='mp4', variable=formatValue, indicator = 0, bg="#545454")
mp4_button.place(width=65, height=40, x=263, y=380)
mp4_button.select()

window.mainloop()

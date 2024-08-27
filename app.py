import yt_dlp as youtube_dl
from flask import Flask, render_template, request, send_file, redirect, url_for, flash
import os
import shutil

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form.get('url')

    if not url:
        flash('Por favor, proporciona una URL de YouTube válida.')
        return redirect(url_for('index'))

    # Ruta de la carpeta de descargas de Windows
    download_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_title = ydl.prepare_filename(info_dict)
            # Si el archivo se ha guardado en la carpeta de descargas, se devuelve directamente
            return send_file(video_title, as_attachment=True)
    except Exception as e:
        flash(f'Error durante la descarga: {e}')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

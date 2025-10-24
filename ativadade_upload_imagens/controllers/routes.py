from flask import FLask, render_template, flash, redirect, request, url_for, session
from models.database import db, Imagem
import os
import uuid

def init_app(app):
    FILE_TYPES = set(['png', 'jpg', 'jpeg', 'gif'])    
    def arquivos_permitidos(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in FILE_TYPES
    
    @app.route('/galeria', methods=['GET', 'POST'])
    def galeria():
        if request.method == "POST":
            file = request.files('file')
            if not arquivos_permitidos(file.filename):
                flash("O arquivo enviado não é suportado por nosso sistema, tente usar um tipo de arquivo válido." , "danger")
                return redirect(request.url)
            filename = str(uuid.uuid4())
            file.save(as.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash("Imagem enviada com sucesso", "success")
            return redirect(url_for('galeria'))
        return render_template('galeria.html')

    
    

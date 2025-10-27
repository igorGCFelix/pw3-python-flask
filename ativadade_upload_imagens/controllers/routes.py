from flask import Flask, render_template, flash, redirect, request, url_for, session
from models.database import db, Imagem
import os
import uuid

def init_app(app):
    FILE_TYPES = set(['png', 'jpg', 'jpeg', 'gif'])    
    def arquivos_permitidos(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in FILE_TYPES
    
    @app.route('/')
    def index():
        return redirect(url_for('galeria'))
    
    @app.route('/galeria', methods=['GET', 'POST'])
    def galeria():
        imagens = Imagem.query.all()
        if request.method == "POST":
            
            file = request.files['file']
            
            if not arquivos_permitidos(file.filename):
                flash("O arquivo enviado não é suportado por nosso sistema, tente usar um tipo de arquivo válido." , "danger")
                return redirect(request.url)
            
            filename = str(uuid.uuid4())
            extensao = file.filename.rsplit('.', 1)[1].lower()
            filename_completo = f"{filename}.{extensao}"
            
            # Garantir que o diretório de upload existe
            upload_dir = app.config['UPLOAD_FOLDER']
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)
            
            img = Imagem(filename_completo)
            db.session.add(img)
            db.session.commit()
            
            file.save(os.path.join(upload_dir, filename_completo))
            flash("Imagem enviada com sucesso", "success")
            return redirect(url_for('galeria'))
        return render_template('galeria.html', imagens=imagens)

    
    

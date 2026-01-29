# 📌 FakePinterest

🔗 **Aplicação online:** https://fakepinterest-goqd.onrender.com  

> ⚠️ A aplicação utiliza o plano gratuito do Render.  
> No primeiro acesso após um período de inatividade, o site pode levar alguns segundos para iniciar.

Projeto inspirado no Pinterest, desenvolvido em Python com Flask, utilizando PostgreSQL em ambiente de produção e Cloudinary para armazenamento de imagens.  
A aplicação está hospedada no Render e tem como objetivo o aprendizado e a prática de desenvolvimento web backend.

---

## 🚀 Funcionalidades

- Cadastro e login de usuários
- Autenticação de usuários
- Upload de imagens
- Armazenamento de imagens via Cloudinary
- Salvamento da URL da imagem no banco PostgreSQL
- Feed com exibição das imagens
- Perfil do usuário com suas postagens

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Flask
- Flask-Login
- Flask-WTF
- Flask-Bcrypt
- SQLAlchemy
- PostgreSQL
- Cloudinary API
- HTML / CSS
- Render (deploy)

---

## 🌐 Arquitetura de Upload de Imagens

1. O usuário faz upload da imagem pelo site  
2. A imagem é enviada para a API do Cloudinary  
3. O Cloudinary retorna a URL pública da imagem  
4. Apenas essa URL é salva no banco PostgreSQL  
5. A imagem é exibida no site diretamente via Cloudinary  

> Nenhuma imagem é armazenada localmente no servidor.

---

---
title: 069 - Cómo generar una clave SSH
date: '2021-03-03T08:30:00+00:00'
url: /2021/03/03/069-como-generar-una-clave-ssh/
image: /img/blog-images/old-post/2021/02/foto66.png
categories:
- automation
- best-practices
- code-quality
- git
- qa
tags:
- github
- gitlab
- mac
- ssh
author: estefafdez
---
¡Hola a todos!

En esta entrada vamos a hablar de qué es una clave SSH, para qué sirve y cómo generarla.

¡Empezamos!

## ¿Qué es una conexión SSH y para qué sirve?

SSH o Secure Shell, es un protocolo de administración remota que le permite a los usuarios controlar y modificar sus servidores remotos a través de Internet a través de un mecanismo de autenticación.

Proporciona un mecanismo para autenticar un usuario remoto, transferir entradas desde el cliente al host y retransmitir la salida de vuelta al cliente. El servicio se creó como un reemplazo seguro para el Telnet sin cifrar y utiliza técnicas criptográficas para garantizar que todas las comunicaciones hacia y desde el servidor remoto sucedan de manera encriptada.

Una clave SSH es uno de los dos archivos utilizados en un método de autenticación conocido como autenticación de clave pública SSH. En este método de autenticación, un archivo (conocido como la clave privada) generalmente se mantiene en el lado del cliente y el otro archivo (conocido como la clave pública) se almacena en el lado del servidor.

Las claves SSH se pueden usar para dos tipos de autenticación:

- **Autenticación para usuarios** donde el servidor SSH verifica la identidad del usuario que se está conectando. Puede autenticarse tanto con clave pública como privada.
- **Autenticación para servidores** donde el cliente SSH es el que verifica la identidad del servidor SSH.Permite a los usuarios que se conectan a un servidor verificar que este sea, de hecho, el mismo servidor SSH al que me conecté la última vez o que este sea el servidor que dice ser (básicamente para evitar un ataque Man-in-the-middle). Las claves utilizadas para este propósito se denominan claves de host SSH.

## ¿Cómo generar una clave SSH?

Nosotros en este ejemplo la vamos a generar mediante consola. Estos pasos podrían seguirse en cualquier sistema operativo.

Lo primero que debemos hacer es asegurarnos de que no tengamos ya una clave generada. Por defecto, las claves de cualquier usuario SSH se guardan en la carpeta **~/.ssh** de dicho usuario. Puedes verificar si tienes ya unas claves, simplemente situándote sobre dicha carpeta y viendo su contenido:

```
$ cd ~/.ssh
$ ls
authorized_keys2  id_dsa       known_hosts
config            id_dsa.pub
```

Tienes que buscar un par de archivos con nombres tales como 'algo' y 'algo.pub'; siendo ese "algo" normalmente 'iddsa' o 'idrsa'.

El archivo terminado en '.pub' es tu clave pública, y el otro archivo es tu clave privada. Si no tienes esos archivos (o no tienes ni siquiera la carpeta '.ssh'), debes de crearlos; utilizando un programa llamado **'ssh-keygen',** que viene incluido en el paquete SSH de los sistemas Linux/Mac o en el paquete MSysGit en los sistemas Windows:

```
$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/estefafdez/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /Users/schacon/.ssh/id_rsa.
Your public key has been saved in /Users/schacon/.ssh/id_rsa.pub.
The key fingerprint is:
43:c5:5b:5f:b1:f1:50:43:ad:20:a6:92:6a:1f:9a:3a estefafdez.local
```

Como se vé, este comando primero solicita confirmación de dónde van a a guardarse las claves ('.ssh/id\_rsa'), y luego solicita, dos veces, una contraseña (passphrase), contraseña que puedes dejar en blanco si no deseas tener que teclearla cada vez que uses la clave.

Tras generarla, cada usuario ha de encargarse de enviar su clave pública a quien quiera que administre el servidor Git (en el caso de que este esté configurado con SSH y así lo requiera). Esto se puede realizar simplemente copiando los contenidos del archivo terminado en '.pub' y añadiéndola al proveedor que queramos utilizar (Github, Gitlab...)

```
$ cat ~/.ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAklOUpkDHrfHY17SbrmTIpNLTGK9Tjom/BWDSU
GPl+nafzlHDTYW7hdI4yZ5ew52JH4JW9jbhUFrviQzM7xlELEVf4h9lFX5QVkbPppSwg0cda3
Pbv7kOdJ/MTyBlWXFCR+HAo3FXRitBqxiX1nKhXpHAZsMciLq8V6RjsNAQwdsdMFvSlVK/7XA
t3FaoJoAsncM1Q9x5+3V0Ww68/eIFmb1zuUFljQJKprrX88XypNDvjYNby6vw/Pb0rwert/En
mZ+AW4OZPnTPI89ZPmVMLuayrD2cE86Z/il8b+gw3r3+1nKatmIkjn2so1d01QraTlMqVSsbx
NrRFi9wrf+M7Q== estefanialocal
```

Si vemos que las claves nos están dando problemas y no se reconocen, lo mejor es borrar las claves utilizadas previamente y volver a generarlas. Actualizaremos la información en nuestra cuenta de git y todo debería funcionar.

Espero que os haya parecido fácil y que me digáis si vosotros utilizáis SSH o no para conectaros a vuestros servidores Git y hacer commits seguros.

¡Nos leemos en la siguiente entrada!

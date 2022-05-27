# Dasa_Pointer

## App

Projeto criado para marcar o ponto de segunda a quinta das 09:00 as 19:00 e de sexta das 09:00 as 18:00.

### Configurar o Python

Realizar o download do Python: https://www.python.org/downloads/<br/>
<b>Lembre de selecionar a opção para adicionar o Python a váriavel se sistema Path</b><br/>
De resto é só dar next e concluir a instalação.

### Configurar o Anaconda3

Realizar o donwload do Anaconda3: https://www.anaconda.com/products/distribution<br/>
É só dar next e concluir a instalação (caso queria alterar o path padrão de instalação lembre de salvar).

### Configurar o Selenium

Abra o prompt e execute:

```
pip install selenium
```

### Instalação

```
git clone https://github.com/MatheusGPrada/Dasa_Pointer.git
```

### Variáveis de ambiente do Windows

Adicione as duas linhas na variável Path

```
C:\Users\SEU_USUARIO\Anaconda3\
C:\Users\SEU_USUARIO\Anaconda3\Scripts
```

### Configuração da rotina no Windows

É necessário realizar a configuração da rotina agendada pelo agendador de tarefas do windows: 

 -> Agendador de Tarefas<br/>
 -> Criar tarefa básica<br/>
 -> Inserir um nome (descrição opicional)<br/>
 -> Selecionar a opção <b>Diariamente</b><br/>
 -> Selecionar o dia atual e o horário que deseja que o script seja executado (sugerido após as 19:00)<br/>
 -> Inciar um programa<br/>
 -> Programa/script: Adicionar o caminho do Anaconda3 (geralmente C:\Users\SEU_USUARIO\anaconda3)<br/>
 -> Adicione argumentos: pointer.py<br/>
 -> Iniciar em: Caminho do clone do repositório: C:\Users\SEU_USUARIO\Dasa_Pointer\<br/>
 -> Concluir
 
 ### Pronto
 
 Agora seu script está configurado para rodar todos os dias, ele consegue identificar se o dia atual é sábado ou domingo e ele cancela a execução nesses dias específicos.

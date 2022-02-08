'''
Clean code: Code that is readable, simple, and concise
Modular code: Code that is logically broken up into functions and modules.
Refactoring: Restructuring your code to improve its internal structure without changing its external functionality.
Writing: Be descriptive and imply type, Avoid abbreviations and single letters, Long names aren't the same as descriptive names
Writing Modular code: DRY (Don't Repeat Yourself)
Efficient Code: Execute faster, Take up less space in memory/storage

'''

'''
Inline comments - line level
Docstrings - module and function level
    -Docstring, or documentation strings, are valuable pieces of documentation that explain the functionality of any function or module in your code
    -Docstrings are surrounded by triple quotes. The first line of the docstring is a brief explanation of the function's purpose.
    -The next element of a docstring is an explanation of the function's arguments. Here, you list the arguments, state their purpose, and state what types the arguments should be. Finally, it is common to provide some description of the output of the function. Every piece of the docstring is optional; however, doc strings are a part of good coding practice.
    
Project documentation - project level
'''

'Git control'

'''
Switch to the develop branch
    git checkout develop

Pull the latest changes in the develop branch
    git pull

Create and switch to a new branch called demographic from the develop branch
    git checkout -b demographic

Work on this new feature and commit as you go
    git commit -m 'added gender recommendations'
    git commit -m 'added location specific recommendations'

Commit your changes before switching
    git commit -m 'refactored demographic gender and location recommendations'

Switch to the develop branch
    git checkout develop

Create and switch to a new branch called friend_groups from the develop branch
    git checkout -b friend_groups

Commit your changes before switching
    git commit -m 'finalized friend_groups recommendations '

Switch to the develop branch
    git checkout develop

Merge the friend_groups branch into the develop branch
    git merge --no-ff friends_groups

Push to the remote repository
    git push origin develop

Switch to the demographic branch
    git checkout demographic

View the log history
    git log

Check out a commit
    git checkout bc90f2cbc9dc4e802b46e7a153aa106dc9a88560

switch to the develop branch
    git checkout develop

Merge the friend_groups branch into the develop branch
    git merge --no-ff friend_groups

Push your changes to the remote repository
    git push origin develop

Commit the changes on the documentation branch
    git commit -m "standardized all docstrings in process.py"

Switch to the develop branch
    git checkout develop

Pull the latest changes on the develop branch down
    git pull

Merge the documentation branch into the develop branch
    git merge --no-ff documentation

Push the changes up to the remote repository
    git push origin develop

Merge the develop branch into the master branch
    git merge --no-ff develop

Push the changes up to the remote repository
    git push origin master

For example, in this situation, let’s say you deleted a line that Andrew modified on his branch. Git wouldn’t know whether to delete the line or modify it. You need to tell Git which change to take, and some tools even allow you to edit the change manually. If it isn’t straightforward, you may have to consult with the developer of the other branch to handle a merge conflict.

'''

'''
git init
git clone --recurse-submodules <url> (clona um projeto já existente, e seus submódulos caso exista)

git add . (adiciona todos os arquivos a serem comitados)
git commit -m “comentários” (comita as modificações do projeto)
git push origin master (envia as alterações ao repositório remoto na branch master)
git pull origin master (caso queira pegar as alterações do repositório remoto na branch master)
git sumodule add <url> (caso queira importar um outro projeto existente ao seu  projeto. Ex.: Postgres, Slack, ...)


Caso você tenha um projeto local e queira associar a um repositório remoto, basta seguir os comandos:
git init (dentro da pasta do projeto)
git add .
git commit -m “Initial commit”
git remote add origin <url>



'''

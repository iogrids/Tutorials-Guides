## Step 1: 

 Download git - git-scm.com for windows and install the .exe file


To find what version of git you have installed

```
git --version
```

Returns

git version 1.9.5.msysgit.1

---

## Step 2: Git configuration

```
git config --global user.email "you@example.com"
git config --gloal user.name "Your Name"
```

---

## Step 3: Initialize

Initialize a folder as a git repository

* Create a folder and an html file inside the folder
* Open Git Bash and go to that folder
   
 ```
  cd Desktop/project
  git init
 ```

Once you do "get init" the folder "project" will be initialized as a git repository

---

## Step 4: Staging

Adding file to staging environment. 

Every time a file is changed you will have to add it to the staging enviroment

Before committing you will have to add the file to the staging environment

   To add a specific file to the staging environment

```
 git add index.html

```

  To add all files to the staging enviroment

```
  git add .
``` 
  To find which all files are inside staging enviroment

```
 git status
```
---

## Step 5: Committing 

  To commit a file from the staging enviroment

```
 git commit -m "revision one" 
```

  To find whether everyfile is committed use

```
git status
```

Returns:

nothing to commit, working directory clean

---

## Step 6: List Commits

To find the list of commits done

```
git log
```

Returns all the revisions that we have done

commit bbd70e1e6eee2f282c821ada84300e0f9b0d6488  
Author: Ray Villalobos <ray@lynda.com>  
Date: Tue May 26 23:05:46 2015 - 0400  

revision one


## To reverse the changes from staging environment

You are working on index.html(working environment) inside the editor. The staging enviroment might have an older version of index.html. To replace index.html inside the editor(working enviroment) with the index.html from the staging enviroment use

```
git checkout index.html

```

## To delete the file from staging enviroment. The below code works as if we are never meant to add index.html to the staging enviroment.

```
git reset HEAD index.html
```

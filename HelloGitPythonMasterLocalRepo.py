'''
1- Go To Desktop 
C:\Users\HosnyRamadan>cd desktop
2-  Go To GitLocalRepo file Desktop 
C:\Users\HosnyRamadan\Desktop>cd  GitLocalRepo
3- Make  GitLocalRepo file as git file 
git init
5- open GitLocalRepo file by VS code Program 
File  -- Add Folder to Workspace
6- Create python file 
GitLocalRepo newfile  HelloGitPythonMasterLocalRepo.py 
7- U means HelloGitPythonMasterLocalRepo.py is Untracked (needed to be added to Staging Area ) 
8- Added  HelloGitPythonMasterLocalRepo.py to Staging Area 
git add HelloGitPythonMasterLocalRepo.py   
if You want to add  all file into your stage you  can write     git add .
now   elloGitPythonMasterLocalRepo.py          A  (Added to Staging Area) 
I write on python file it  becomes             M (modified)
9- Show status 
   git status
   it will give us status 
Enter
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   HelloGitPythonMasterLocalRepo.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   HelloGitPythonMasterLocalRepo.py

It means
 A- On branch master ---- > We are in branch master 
 B- No commits yet   ---- > We need to commit the HelloGitPythonMasterLocalRepo.py stagged python file 

 10- Commit the file with last update message like we print Hello 
 git commit -m "printing Hello world master branch "
 #print("Hello python world master branch ")
 Enter
 [master 6639282] printing Hello world master branch
 1 file changed, 42 insertions(+)
 11- Make new branch to edit and add and test code before  to macter branch 
 git checkout -b testbranch
 output 
 Switched to a new branch 'testbranch'
  C:\Users\HosnyRamadan\Desktop\GitLocalRepo>git status
  On branch testbranch
12 - commit 
git commit -m "printing Hello world test branch "
print("Hello python world test branch ")
output 
[testbranch fa953f8] printing Hello world test branch
 2 files changed, 73 insertions(+), 2 deletions(-)
 create mode 100644 exe.txt
13- Update master branch by test branch edit 
A-  git checkout -b master
 output 
 Switched to a new branch 'master'
B- git merge  testbranch 
'''
print("Hello python world master branch ")
print("Hello python world test branch ")

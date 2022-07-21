 ### GIT
 # What is git?
 Git is a clear source drew up to virsionalise the control system made up to handle everything from
 small to big projects with speed and efficiency; whenever the added codes are becoming
  more, git changes the codes stored. Git has a remote repository which is stored in a server and a local
   repository stored in a computer. Drew up virsion control system helps in handling this by maintaining a history of what changes have been made, it also provides features like branches and merges which will be covered thereafter.
  
   # GitHub
   #What is github?

   Github is a git repository hosting service. It also clear the way with many of its features, such as access control and  teamwork. It provides a web-based praphical interface.
   Github also offers both distributed version control code management (SCM) functionality of git. It also spead up with some collabolation features such as bug tracking , feature requests, task management for every project. Its feares;
         .   code hosting
         .   team management
         .   project management
         .   praphical representation of branches
         .   collabolation
         .   git repository hosting

 # benefits of using github

         .   it is easy to contribute to open source projects through github. 
         .   it helps to einnivet an excellent document.
         .   you can trace changes across versions.        

  # Git commands

 - In git we have command drew up to be followed when using git. we have commants like;
 . git init which is used to open a new enpty reporsitory. This is the first step in creating a repository. It can be that you're working on an existing reporsitory and then you think of switching to new reporsitory, git init is the only command that has power to command the opening of a new reporsitory.
 When git init runs the adding and commiting of files will simply be possible.  
 . git add command add new or charneled files in your workimg directory to the straging area. withouth 
 this command nothing can be done because it can allow the user to access histry of the written 
 data without charnging your working environment. Before a file is available to commit to a repository, the file should fistly be added to the git index.  When workimg with git before you commit
 you firstly type git add to give you access of choice to a selected a file or files if you want many because git add can be used in other ways when adding, you can addthe intire directories, you can specify the file you want, or all unstaged files.
 . git commit plays a role of recoding the changes made to the files to a local repository. For easy reference, each commit has a unique ID. It's best practice to include a new message with each commit explaining the changes made in a mommit made. Adding a commit message helps to find a particula change or infer the changes.
 . git status returns the current state of the repository. It also turns back the current working base if a file is in the base area, but not commited, it shows with git status. Or if there are no changes it will return nothing to commit.  
 . we also have ```git checkout``` this is the command that can dirrect the user on the branches available
 and giving the name of a current branch, and you can switch these branches using checkout commant
 and access that git branch, its role is switching the branches.
 . git pull is also another very inportant command. This commant is used to pick and push the commits
 from a local repository and quickly give an update to a remote reporsitory in order to resemble the 
 content. It is therefore a combination of two other git commands which are git fetch and git merge 
 it does the two commands in itself a one time, git fetch takes the first part by downloading the content
 fron a given file then merging pick it up to function into the remote content to allow merge commit to 
 take place.
 . git rm it is used to delete the file in a reporsitory and from the filesystem.
 git has its main function which is removing marcked files from the both the index and the working 
 directory, it also walk with specification of what the user want to delete from the file before 
 giving a command. 
 . git clone, this command is used to make a reporsitory in an already existing repository. If i want a local copy of my repository from github, this command allows creating a local copy of that repository on your local directory from the repository.   
 . git branch it lists all the branches from the working environment and add a branch aguement to creat 
 another branch name branch.
 . git status it plays a role of listing all the starged, unstarged aslo the untrached files. The status command is used to display the state of the working directory and the staging area. It will show you which changes have been starged, which haven't, and which files aren't being tracked by git. It does not show you any information about the committed project history. For this, you need to use the git log. It also lists the files that you've changed and those you still need to add or commit.
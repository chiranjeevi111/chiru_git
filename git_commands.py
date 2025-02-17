- **`git init`**: Initializes a new Git repository.
- **`git status`**: Shows the status of the working directory and staging area.
- **`git add .`**: Stages all changes in the current directory.
- **`git commit -m`**: Commits staged changes to the local repository with a message.
- **`git push -u origin <branch-name>`**: Pushes local commits to the remote repository and sets the upstream reference.
- **`git --version`**: Displays the installed Git version.
- **`code .`**: Opens the current directory in VSCode.
- **`git checkout -b`**: Creates and switches to a new branch.
- **`git branch -M`**: Renames the current branch.
- **`.gitignore`**: Specifies files and directories to be ignored by Git.

### **1. Basic Workflow Commands**
- **`git clone <repository-url>`**:  
  Clones a remote repository to your local machine.
  
- **`git pull`**:  
  Fetches changes from the remote repository and merges them into the current branch.  
  (Equivalent to `git fetch` + `git merge`).

- **`git fetch`**:  
  Downloads changes from the remote repository but does not merge them into your working directory.

- **`git diff`**:  
  Shows the differences between the working directory and the staging area (unstaged changes).  
  - `git diff --staged`: Shows differences between the staging area and the last commit (staged changes).

---

### **2. Branching and Merging**
- **`git branch`**:  
  Lists all local branches.  
  - `git branch -a`: Lists all branches (local and remote).  
  - `git branch -d <branch-name>`: Deletes a branch.  
  - `git branch -D <branch-name>`: Force deletes a branch (even if it has unmerged changes).

- **`git checkout <branch-name>`**:  
  Switches to an existing branch.  
  - `git checkout -b <new-branch>`: Creates and switches to a new branch.

- **`git merge <branch-name>`**:  
  Merges the specified branch into the current branch.

- **`git rebase <branch-name>`**:  
  Reapplies commits from the current branch on top of another branch (used for a cleaner commit history).

---

### **3. Undoing Changes**
- **`git restore <file>`**:  
  Discards changes in the working directory for a specific file (unstages and reverts changes).  
  - `git restore --staged <file>`: Unstages a file but keeps the changes in the working directory.

- **`git reset`**:  
  - `git reset --soft <commit>`: Moves the branch pointer to a previous commit but keeps changes staged.  
  - `git reset --mixed <commit>`: Moves the branch pointer and unstages changes (default).  
  - `git reset --hard <commit>`: Moves the branch pointer and discards all changes (use with caution).

- **`git revert <commit>`**:  
  Creates a new commit that undoes the changes of a specific commit (safer than `reset` for shared history).

---

### **4. Remote Repository Commands**
- **`git remote -v`**:  
  Lists all remote repositories associated with the local repository.

- **`git remote add origin <repository-url>`**:  
  Adds a remote repository (e.g., GitHub) to your local repository.

- **`git push origin <branch-name>`**:  
  Pushes local commits to the remote repository.  
  - `git push --force`: Force pushes changes (use with caution).

- **`git remote remove origin`**:  
  Removes a remote repository.

---

### **5. Log and History**
- **`git log`**:  
  Displays the commit history.  
  - `git log --oneline`: Shows a compact commit history.  
  - `git log --graph`: Displays a visual representation of branches and merges.

- **`git show <commit>`**:  
  Shows details about a specific commit.

- **`git blame <file>`**:  
  Shows who last modified each line in a file.

---

### **6. Stashing**
- **`git stash`**:  
  Temporarily saves uncommitted changes in a stash.  
  - `git stash pop`: Applies the most recent stash and removes it from the stash list.  
  - `git stash list`: Lists all stashes.  
  - `git stash apply`: Applies a stash without removing it from the stash list.

---

### **7. Tagging**
- **`git tag <tag-name>`**:  
  Creates a lightweight tag for the current commit.  
  - `git tag -a <tag-name> -m "message"`: Creates an annotated tag with a message.  
  - `git push origin <tag-name>`: Pushes a tag to the remote repository.  
  - `git push --tags`: Pushes all tags to the remote repository.

---

### **8. Configuration**
- **`git config --global user.name "Your Name"`**:  
  Sets your name for Git commits.  
- **`git config --global user.email "your-email@example.com"`**:  
  Sets your email for Git commits.  
- **`git config --list`**:  
  Lists all Git configuration settings.

---

### **9. Advanced Commands**
- **`git cherry-pick <commit>`**:  
  Applies a specific commit from one branch to another.

- **`git bisect`**:  
  Helps find the commit that introduced a bug using binary search.

- **`git reflog`**:  
  Shows a log of all Git operations (useful for recovering lost commits or branches).

---

### **10. Cleanup**
- **`git clean -n`**:  
  Shows which untracked files will be removed (dry run).  
- **`git clean -f`**:  
  Deletes untracked files from the working directory.

---

These commands cover the majority of daily Git usage. Mastering these will make you highly efficient in managing Git repositories!
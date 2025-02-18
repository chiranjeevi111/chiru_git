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


Git Lense:
-----------

**GitLens** is a popular **Visual Studio Code (VS Code) extension** that supercharges Git capabilities within the editor. It provides powerful features to help you visualize, navigate, and understand your Git repository, making it easier to work with version control directly in VS Code.

---

### Key Features of GitLens:

1. **Enhanced Git Blame**:
   - Displays detailed blame annotations inline in your code, showing:
     - Who last modified each line.
     - When the change was made.
     - The commit message associated with the change.
   - You can hover over the blame annotations to see even more details.

2. **Code Lens**:
   - Adds actionable information directly in your code, such as:
     - The number of authors who have worked on a piece of code.
     - The latest commit message for a function or block of code.
   - Clicking on the Code Lens can show you the commit history or open a comparison view.

3. **Commit History**:
   - Provides a detailed view of the commit history for:
     - The entire repository.
     - A specific file.
     - A specific line or block of code.
   - You can easily browse, search, and filter commits.

4. **File History**:
   - Shows the history of changes for a specific file, including:
     - Who changed the file.
     - When the changes were made.
     - What changes were made.

5. **Compare Changes**:
   - Allows you to compare:
     - Branches.
     - Commits.
     - Files or specific lines of code.
   - Helps you understand the differences between versions.

6. **Repository Navigation**:
   - Provides a **GitLens Explorer** in the VS Code sidebar, where you can:
     - View branches, tags, and remotes.
     - Navigate through stashes and commit history.
     - Access quick actions for common Git operations.

7. **Interactive Rebasing**:
   - Simplifies the process of interactive rebasing by providing a visual interface to reorder, edit, squash, or drop commits.

8. **Worktrees Support**:
   - Helps you manage multiple worktrees (parallel working directories) for the same repository.

9. **Search and Compare**:
   - Allows you to search and compare changes across commits, branches, and files.

10. **Customizable**:
    - GitLens is highly customizable, allowing you to configure:
      - Which features to enable or disable.
      - How blame annotations and Code Lens are displayed.
      - Keyboard shortcuts for quick access to GitLens features.

---

### Why Use GitLens?
- **Improved Productivity**: GitLens integrates Git functionality directly into your editor, reducing the need to switch to a terminal or external Git tool.
- **Better Code Understanding**: By visualizing who changed what and when, you can better understand the evolution of your codebase.
- **Enhanced Collaboration**: GitLens makes it easier to track changes made by team members and understand the context behind those changes.

---

### How to Install GitLens:
1. Open **VS Code**.
2. Go to the **Extensions Marketplace** (Ctrl+Shift+X or Cmd+Shift+X on macOS).
3. Search for **GitLens**.
4. Click **Install**.

---

### Example Use Cases:
1. **Viewing Blame Information**:
   - Hover over a line of code to see who last modified it and the associated commit message.

2. **Exploring Commit History**:
   - Right-click a file and select **GitLens: Open File History** to see all changes made to that file.

3. **Comparing Branches**:
   - Use the **GitLens Explorer** to compare the differences between two branches.

4. **Interactive Rebasing**:
   - Use the **GitLens Rebasing** feature to clean up your commit history before merging.

---

### Summary:
- **GitLens** is a powerful VS Code extension that enhances Git functionality.
- It provides features like **blame annotations**, **Code Lens**, **commit history**, **file history**, and **branch comparisons**.
- It helps you work more efficiently with Git directly within VS Code.

Let me know if you'd like a deeper dive into any specific feature! 😊

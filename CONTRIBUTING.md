# How To Contribute
Follow this page for proper GitHub etiquette.
## Got A New Feature or Bug
Create a new branch off of `main`, commit all of your changes to that branch.
#### Example: add a blur filter
Create local branch on your machine:
```
$ git checkout main
$ git checkout -b blur-filter
```
Add the branch to our remote repo with the same name :
`$ git push -u origin blur-filter`

##  Commit and Push Your Changes
To commit means you are saving your changes into your local branch with a message.  
To push means you are pushing all of your changes (your commits) into our remote GitHub repo.  
Before pushing, if others are working on your branch as well, then remember to use `git fetch` to fetch any new updates from the remote branch. Then use `git pull` to pull those new updates into your local branch.   
**THIS IS VERY IMPORTANT AS IT AVOIDS ANY POTENTIAL MERGE OR PUSH CONFLICTS.**
#### Example: add a blur filter
Committing your changes:
```
$ git status //check what changes you have
// follow the instructions displayed to add(stage) or revert your changed files from this commit
$ git status //do it again to confirm your staged files for this commit
$ git commit //this will open up your default commandline text editor
// follow the instruction to write your commit message, then save and exit the file
```
*Alternative quick commit*: 
```
$ git commit -a -m "feat: added blur function"
// -a means stage all changed files
//note that it does not stage any untracked files (i.e. new files you created)
// -m means add a commit message
```
Pushing your changes:
```
$ git fetch
$ git pull
// potential conflicts with local commits, resolve them, then continue
$ git push
// or if pushing for the first time without a cooresponding remote branch
$ git push -u origin blur-filter
```
## Getting New Changes from `Main`
Sometimes as we are working on a feature or bug, we need the new changes that someone just merged into main. To do so, we'll rebase our branch.  
You cannot rebase while there are currently unsaved changes, so either commit them, or stash them using `git stash`.
#### Example: adding a blur filter
```
$ git fetch
$ git checkout blur-filter //make sure you are on the right branch
$ git rebase origin/main --committer-date-is-author-date
// the --committer... is important as it avoids duplicate commits from rebasing
```
Here's how rebase works( as far as I understands it):
 * Git temporarily removes all of the commits unique to `blur-filter`.
 * Git then applies all the commits from `main` into `blur-filter` starting from the commit that diverged the two branches.
 * Git then attempts to apply all the removed commits back onto `blur-filter`.
 * The branch now has the new changes for `main` with commits unique to `blur-filter` on top.  

**Notices that merge conflicts can occur when git attempts to apply the removed commits back**  
The incoming change would be the commits from `blur-filter`, while the current commit is from the rebase.  
If this occurs, resolve the conflict either through your code editor or through your command line text editor.  
Google your respective editor to see how to resolve conflicts.  
After resolving the conflicts, use `git rebase --continue`
```
$ git push --force-with-lease
\\ --force-with... is important as it forces github to take your local branch over the remote
\\ this is needed as your local branch now conflicts with the remote one after rebasing
```
## Merging Your Change Back into `Main`
After you are done with the feature or bug. Please use GitHub's Pull Request function to merge your branch into `main`. Do not directly merge them.  
This allows us to track our history.
#### Example: adding a blur filter
Open up a new pull request in the website, select `main` as the base branch, `blur-filter` as the compare branch.  
Make sure the compare page states that the two branches can be merged without conflict, then click create new pull request.  
The Pull Request should show you all the commits to be merged into `main` and all the changed files.  
Title the PR "adding a blur filter", and add whatever comment necessary.   
If you feel necessary for others to check your work, add a reviewer to the pull request.  
When you are ready, merge the pull request. At this point, you can feel free to delete branch `blur-filter` .  
## (Optional) Commit Message Etiquette
This is optional, but can be good practice and make the commits easier to read.  
* Prefix your commits with `feat: `, `chore: `, or `fix: ` so your intent is clear.
* When the commit gets too long (more than 80 characters), break the commit onto a new line, preferably with a prefix as well. GitHub cannot display more than 80 characters per line for commit messages.

# Launch instructions for Linux

### The easiest:

1. Download zip archive and extract it (or clone this repository) to your system

2. Add a Directory with your executable (file `git-checker` is stored in `'YOUR PATH'/github-checker/dist/git-checker`) to $PATH: permanently by running the following in Terminal: `nano ~/.bashrc`

3. Add in the end of the file `PATH=$PATH:~/YOUR NEW PATH TO SCRIPT`, mark it with ##PATH## for further needs

4. Save & exit wtih: `ctrl+O` `ctrl+X`

5. Run: `source ~/.bashrc`

6. Confirm changes with: `echo $PATH`. You'll see the path to your new directory in the end of the line.

7. Launch it from terminal with `git-checker` command. That's all.

## You may also use source script instead of app, in this case just use `git-checker.py`.
 

### If you want to have it in your App List and on the App Dock:

1. Choose the directory which is in your `$PATH` or create your own directory and just add it in your `$PATH`

2. Open `git-checker.desktop` file and replace `'PATH TO THE FILE'` in `Exec=`, `Path=` and `Icon=` with your real path to these files.

3. Move `git-checker.desktop` to `~/.local/share/applications/`

4. If you setup the `git-checker.desktop` file correctly, you will now be able to see it in your App List and will be able to move an app to your App Dock. 

# #----------------------OTHER OPTIONS-----------------------#

### [WIN APP](https://github.com/Cacodemon503/github-checker/tree/windows)  

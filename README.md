# spaceback
command line tool for managing spacemacs backups


### Why?

I am a huge fan of spacemacs. It's my primary text editor.
And yet, every so often I break everything when I'm upgrading
to a newer version or installing a new package. A couple times, I've managed 
to break things so badly that a fresh install of spacemacs doesn't even help and I need to spend
hours mucking around on online forums for similar problems.

This tool lets me revert to an old spacemacs configuration of my choice without requireing any internet connection.

### What does spaceback do?

*spaceback* offers a quick way to save and retrive multiple versions of the config file (.spacemacs) and
the emacs configuration directory (.emacs.d).

All backed up versions are stored in an archive directory (~/.spaceback) and named using a time-stamp.

Note: I strongly recommend you don't share the same backups between computers as the compiled elisp files don't
transfer well.

# Install

### Clone the repo
Copy this repo to location you like.

```
git clone https://github.com/peterwinter/spaceback.git
```

### Create Alias

In order to use the command *spaceback* from your terminal, you've got to
set up an alias in your profile.

Here's how I've set mine up:

```
alias spaceback='python /path/to/spaceback/spaceback.py'
```


# Usage

### save
for saving your current spacemacs setup
```
spaceback save
```

or, if you didn't set up the alias
```
python spaceback.py save
```

### show
to list all available spacemacs setups. The <backup-id> corresponds to that long 
integer in front of the date. It's a timestamp of the second you typed *spaceback save*.
```
spaceback show
```

or, if you didn't set up the alias
```
python spaceback.py show
```

### load
for retrieving an old spacemacs setup. 
```
spaceback load <backup-id>
```

or, if you didn't set up the alias
```
python spaceback.py load <backup-id>
```


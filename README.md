Shahar Ronen (c) 2012

Based on http://stackoverflow.com/questions/7374069/undo-git-reset-hard
and http://stackoverflow.com/questions/1108853/recovering-added-file-after-doing-git-reset-hard-head

- Run the following command and store response in file:
$ git fsck --cached --no-reflogs --lost-found --unreachable HEAD
- Execute this script on file.
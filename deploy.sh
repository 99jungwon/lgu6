git add .
if ! git diff --cached --quiet; then
    git commit -m "Update on $(date +'%Y-%m-%d %H:%M:%S')"
    git push
else
    echo "No changes to commit."
fi
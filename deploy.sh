# 현재 스크립트의 장점
# 자동 커밋 메시지로 커밋 시간 추적 용이

# 변경 사항 없을 때 커밋 생략 → 깔끔한 로그 유지

# GitHub에 바로 push까지 자동화 완료
git add .
if ! git diff --cached --quiet; then
    git commit -m "Update on $(date +'%Y-%m-%d %H:%M:%S')"
    git push
else
    echo "No changes to commit."
fi
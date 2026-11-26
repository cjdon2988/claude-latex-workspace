# note 模板修改紀錄

只追加,不改舊紀錄。每次 `release` 寫入一筆。

格式:

## YYYY-MM-DD HH:MM
- 改動檔案:
- 改前改後摘要:
- 原因:
- 對應 preferences:
- 快照:(`~/.claude/skills/latex/previous/note/<時間戳>/`)

## 2026-10-13 12:19
- 改動檔案:`note-template/kelong-cjk.sty`、`note-template/package_and_settings.tex`、`note-template/main.tex`、`content/__SUBJECT__/note/note_1/` 下的 `0. 標題與作者.tex`、`part0_all.tex`、`part1.tex`
- 改前改後摘要:
  - `kelong-cjk.sty`:`amsmath` 之後加入 `mathtools`、`amssymb`(解決 unicode-math 套件順序造成的 4 個 Error 與 mathtools 警告)
  - `package_and_settings.tex` 第 196-197 行:`\lhead`、`\rhead` 加上 `\CJKfamily{yuan}`(頁首改圓體)
  - `part1.tex`:改為完整範例(whitebox、一般表格、寬表格 resizebox、習題三件套、lstlisting、兩欄 minipage),取代原本的短版
  - `main.tex`、`part0_all.tex`、`0. 標題與作者.tex`、`part1.tex` 註解路徑:`linear_algebra` 換回 `__SUBJECT__`;標題與作者換回 `__TITLE__`、`__AUTHOR__`
- 原因:草稿在 Overleaf 上確認可編譯(0 error,5 warning),確認後寫入池。
- 對應 preferences:2026-10-12 頁首兩行(已套用);2026-10-13 表格超出仍為待確認(範例已用 resizebox 處理,模板層級 tabularx 方案未套用)。
- 快照:`~/.claude/skills/latex/previous/note/2026-10-13_1219/`

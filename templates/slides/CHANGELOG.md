# slides 模板修改紀錄

只追加,不改舊紀錄。每次 `release` 寫入一筆。

格式:

## YYYY-MM-DD HH:MM
- 改動檔案:
- 改前改後摘要:
- 原因:
- 對應 preferences:
- 快照:(`~/.claude/skills/latex/previous/slides/<時間戳>/`)

## 2026-10-13 14:12
- 改動檔案:note-template/package_and_settings.tex、note-template/main.tex、note-template/功能筆記readme.tex、note-template/fonts/KpMath-Bold.otf、note-template/fonts/KpMath-Regular.otf(新增)
- 改前改後摘要:色系改為四套(green/blue/orange/purple)結構一致,每套各自定義 darktitle、accentcolor、bodytextcolor、answerblue、solutionfill、examplefill、exampleline;預設 orange。標題列底色、投影片底色、框線與解答字色各色系獨立調整。problembox/highlightbox 框內改白底。頁尾(footer)三欄與字族調整,封面與 banner 用圓體。main.tex 與功能筆記readme.tex 補上資料夾結構與切換說明,範例路徑改為佔位符。新增 KpMath 字型。
- 原因:草稿 Template_Slides 調整完成後發布到模板池
- 對應 preferences:無(preferences.md 未列對應列)
- 快照:`~/.claude/skills/latex/previous/slides/2026-10-13_1410/`

## 2026-10-13 14:28
- 改動檔案:Content/course/__SUBJECT__/note/note_1/part0.tex
- 改前改後摘要:標題頁加入頂端色條(TikZ overlay,填 darktitle),改前為 `\frame{\titlepage}`。
- 原因:發布時漏掉草稿標題頁的色條,補上使池與草稿一致。
- 對應 preferences:無
- 快照:`~/.claude/skills/latex/previous/slides/2026-10-13_1410/Content/course/__SUBJECT__/note/note_1/part0.tex`(改前版本)

## 2026-10-13 14:30
- 改動檔案:Content/course/__SUBJECT__/note/note_1/part1.tex
- 改前改後摘要:範例「重點」框由 Beamer 內建 `block` 改為 `highlightbox`(`\begin{block}{重點}`→`\begin{highlightbox}{重點}`,結尾同步)。內建 block 標題為明體,與模板圓體標題不一致。
- 原因:內建 block 字型與其他框不一致,使用者不使用內建 block。
- 對應 preferences:無
- 快照:`~/.claude/skills/latex/previous/slides/2026-10-13_1410/Content/course/__SUBJECT__/note/note_1/part1.tex`(改前版本)

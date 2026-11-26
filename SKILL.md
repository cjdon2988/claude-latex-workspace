---
name: latex
description: 本機 LaTeX 工作區管理:第一次使用時設定工作區、編譯專案、依模板建立新專案、發布模板、累積排版偏好、把 Overleaf Dropbox 同步的專案遷移進來。處理 LaTeX 或 .tex 專案、編譯 PDF、改模板、遷移 Overleaf 時使用。
argument-hint: [setup | build <群組> <專案> | list | new <模板> <名稱> | folder <路徑> | release <模板> | migrate <專案>]
---

# LaTeX 本機工作區

本 skill 資料夾(下稱 `$SKILL`,通常是 `~/.claude/skills/latex/`)含 `scripts/`、`templates/`、`preferences.template.md`。使用者的工作區(下稱 `$L`)另外放在使用者指定的位置,路徑記在 `$SKILL/workspace.txt`(一行,本機檔,不進 git)。

## 每次叫用先判斷
- `$SKILL/workspace.txt` 不存在或指向的資料夾不存在:跑「setup」
- 存在:讀出 `$L`,依使用者要求進入對應子指令

## 硬規則
- 新建檔案或資料夾前,先說明是什麼、放哪、為什麼,等確認再動手
- 刪除一律移垃圾桶,不用 `rm -rf`
- 不讀、不改、不遷移不是使用者本人的專案(Overleaf 上別人的專案)
- 一次最多問 4 題,有限選項用 AskUserQuestion 按鈕,自由文字(名稱、標題、作者)用聊天輸入

## 工作區結構
```
$L/
├── .latex-config      TEXBIN、BUILD_ROOT(setup 產生)
├── 00_scripts/        tex-build(所有專案共用)、page_gaps.py
├── 01_pdfs/<群組>/<專案>/   PDF,結構鏡像 02_projects
├── 02_projects/<群組>/<專案>/   原始碼,一個專案一個資料夾
├── 03_templates/<名稱>/     模板池,含 template.json、README.md、CHANGELOG.md
└── preferences.md     使用者的排版偏好(長期累積)
```
- 群組是 Overleaf 專案外多包的一層,例如 `research`、`courses`。專案各自獨立
- 中間檔放 `BUILD_ROOT`,不進雲端同步資料夾

## setup(第一次)
逐批問,每批講清楚後果:
1. **TeX**:`which latexmk xelatex` 偵測。沒有就引導安裝(macOS:MacTeX 或 BasicTeX 加 `tlmgr install latexmk xetex ctex fontspec unicode-math beamer`),並請使用者指定或確認 TeX bin 資料夾,寫入 `TEXBIN`
2. **工作區位置**:建議放雲端同步資料夾(Dropbox 等)方便多機,問使用者放哪
3. **層數**:預設「群組/專案」兩層,問使用者想要哪些群組(例:`ai_lab`、`research_ra`),可事後再加。使用者想單層也可以,就只建一個群組
4. **中間檔位置**:`BUILD_ROOT`,預設 `~/.cache/latex-build`,不要放進同步資料夾
5. **Overleaf**:問是否用 Overleaf 的 Dropbox 同步。要的話建群組 `0_overleaf`,放遷移進來的專案,請使用者先在這裡用用看,習慣後可再把專案搬到其他群組(搬資料夾,並把 `01_pdfs` 對應資料夾一起搬)。不要的話跳過
6. **模板與偏好**:複製 `$SKILL/templates/*` 到 `$L/03_templates/`,複製 `$SKILL/scripts/*` 到 `$L/00_scripts/`,`preferences.template.md` 複製成 `$L/preferences.md`

說明完整清單(要建的資料夾與檔案)並等確認,才一次建立。建完:寫 `.latex-config`(`TEXBIN=...`、`BUILD_ROOT=...`)、寫 `$SKILL/workspace.txt`,然後用模板建一個測試專案跑 `tex-build` 驗證,成功後告知使用者,測試專案請使用者決定保留或刪。

向使用者說明這幾件事:
- 每個群組底下的專案獨立,原始碼可巢狀,一個專案能編出多份 PDF(每個不同檔名的主檔各一份)
- **同一專案同一檔名重編,預設覆蓋舊 PDF**,避免 PDF 越積越多。想鎖定當下版本說一聲(`--save`),會另存一份到 `0_saved/`。不同檔名的主檔各有自己的 PDF,互不覆蓋
- 模板之後會陸續增加,到 repo `git pull` 即可,新模板在 `$SKILL/templates/`,需要時請 Claude 複製進 `$L/03_templates/`(已有的同名模板不覆蓋,先問)

## 編譯(`build`)
- `$L/00_scripts/tex-build <群組> <專案> [--main 相對主檔路徑] [--save]`
- 主檔順序:`--main`、專案根目錄 `.texmain`(一行相對路徑)、自動偵測(唯一含 `\documentclass` 者);不唯一就列候選請使用者選,選定後問是否寫入 `.texmain`
- 預設覆蓋舊 PDF;`--save` 另存到 `01_pdfs/<群組>/<專案>/0_saved/`。編譯失敗不動舊 PDF,只印錯誤行
- 工作目錄是主檔所在資料夾,`TEXINPUTS` 含專案根目錄,所以 `\input{content/...}` 與 `Path=./fonts/` 都能找到
- 缺套件:`tlmgr install <套件>`(PATH 要含 TeX bin)。編譯進行中不補。需要 shell-escape 或 biber 時先問使用者
- 回報:PDF 完整路徑、頁數、錯誤摘要。要看版面用 Read 讀 PDF 指定頁

## 模板
- 列出可用模板:掃描 `$L/03_templates/*/template.json`,不依賴本檔清單
- `template.json` 欄位:`name`、`label`、`description`、`pattern`、`compiler`、`main`、`placeholders`、`exclude`、`source`。佔位字串替換範圍含資料夾名、檔名、檔案內容
- 模板內建字型(`kelong-cjk.sty` 與 `fonts/`)時字型與 sty 必須和主檔同層
- 新增模板:在 `$L/03_templates/` 建資料夾與 `template.json` 即可

## 建立新專案(`new <模板> <名稱>`)
1. 向使用者確認每個佔位字串的值、專案名稱,以及放哪個群組(列出現有群組,可新增)
2. 在 scratchpad 複製模板(排除 `exclude`),替換佔位字串
3. 說明名稱與位置後等確認
4. 確認後用最終名稱一次複製到 `$L/02_projects/<群組>/<名稱>/`
5. 跑 `tex-build` 驗證編譯,回報 PDF 路徑;失敗就依錯誤處理

## 遷移 Overleaf(`migrate <專案>`)
- 前提:使用者的 Overleaf 開了 Dropbox 同步,專案在 Dropbox 的 Overleaf 資料夾。先問資料夾位置
- 把專案「複製」到 `$L/02_projects/0_overleaf/`,原件不動;只遷移使用者本人 owner 的專案
- 複製後找主檔,跑 `tex-build`,比對頁數與版面。內容資料夾為空要先查線上是否真有內容再下結論
- 依賴系統字型的專案,遷移前先確認該字型有裝

## 新增資料夾(`folder <路徑>`)
在專案內新增,通常從現有資料夾複製後改名。動手前說明路徑與來源,等確認

## 發布模板(`release <模板>`)
先在 `02_projects` 的草稿專案改並確認編譯成功,滿意後才寫入模板池。
1. 池中現有版本複製到 `$SKILL/previous/<模板>/<YYYY-MM-DD_HHMM>/`(本機保存)
2. 列出將被覆寫的檔案與差異摘要,等確認
3. 草稿中的實際名稱換回佔位符,檢查 `template.json` 的 `main`、`compiler`
4. 寫入 `$L/03_templates/<模板>/`,在該模板 `CHANGELOG.md` 追加一筆(日期、改動檔案、改前改後、原因、對應 preferences 列、快照路徑;append-only)
- 已建立的專案不因模板改動而更新

## 查詢(`list`)
唯讀。掃描 `02_projects` 列出群組、專案、對應 PDF 最後編譯時間、有無 `.texmain`;模板列名稱、用途、佔位符

## 觀察偏好
使用者多次調整同一種樣式或指出版面問題時,記進 `$L/preferences.md`(日期、模板、觀察、建議改動、狀態「待確認」)。工作結束時列出新增候選,由使用者決定,不自行改模板池

## 版面微調(編譯後)
- 目標:換章節不留大片空白,也不到處強迫換頁。用 `$L/00_scripts/page_gaps.py <pdf>`(需要 poppler 的 `pdftotext`)量每頁底部留白
- 做法:`\usepackage{needspace}`,小節標題前 `\Needspace{N\baselineskip}`(剩餘空間不足才換頁);一般小節 N 約 5,標題後緊接不可切的圖或表的小節,N 取該區塊高度加幾行

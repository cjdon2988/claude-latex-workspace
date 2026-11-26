# claude-latex-workspace

給 Claude Code 用的本機 LaTeX 工作區 skill。裝好之後對 Claude 說「設定 LaTeX 工作區」,它會一題一題問你東西要放哪,然後替你建好。

## 安裝

```bash
git clone https://github.com/cjdon2988/claude-latex-workspace ~/.claude/skills/latex
```

之後在 Claude Code 裡輸入 `/latex`,或直接說「我要編譯 LaTeX」。第一次會自動進入設定。更新用 `git pull`。

## 設定時 Claude 會問你

1. TeX 裝在哪(沒裝會引導你裝)
2. 工作區放哪(建議放 Dropbox 等同步資料夾)
3. 要幾層:預設「群組 / 專案」兩層,例如 `ai_lab/`、`research_ra/` 底下才是各自獨立的專案
4. 要不要把 Overleaf 的 Dropbox 同步專案遷移進來(會放在 `0_overleaf` 群組,習慣後可搬到其他群組)

## 工作區資料夾說明

| 位置 | 放什麼 |
|---|---|
| `00_scripts/` | `tex-build` 編譯腳本,所有專案共用 |
| `01_pdfs/<群組>/<專案>/` | 編譯出的 PDF,結構與 `02_projects` 一樣 |
| `02_projects/<群組>/<專案>/` | 原始碼,一個專案一個資料夾,內部可以巢狀 |
| `03_templates/<名稱>/` | 模板池,新專案從這裡複製 |
| `preferences.md` | 你的排版偏好,Claude 會把你反覆調整的習慣記在這裡,由你決定要不要套用到模板 |
| `0_overleaf/`(群組) | 從 Overleaf 遷移來的專案 |

## 關於 PDF

- 一個專案可以編出多份 PDF:不同檔名的主檔各編一份,互不影響
- 同一專案同一檔名重編時,**預設覆蓋舊 PDF**,避免 PDF 越積越多
- 想鎖定現在這一版,跟 Claude 說「存這一版」,會另存一份到 `0_saved/`

## 模板

目前有:

- `note`:筆記型,依科目再依類型組織的課程筆記
- `slides`:投影片型,Beamer 投影片與論文解讀

之後會陸續新增模板。用 `git pull` 更新後,跟 Claude 說「把新模板加進工作區」即可。已建立的專案不受模板更新影響。

## 需求

- macOS 為主測試環境
- TeX Live 或 MacTeX(含 `latexmk`、`xelatex`)
- 排版微調功能需要 poppler(`pdftotext`)
- 字型(cwTeX、Kp、Libertine)已隨模板附上,為開源字型

## 授權

本 repo 為私人分享,僅供受邀者使用。

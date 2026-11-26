# 投影片模板（slides）：模板池母版

這是 `templates/slides/` 的母版，不是可直接編譯的專案。
新專案請用 skill 建立（`/latex new slides <名稱>`），會替換佔位字串並排除本檔與 `template.json`。

## 結構

```
slides/
├── template.json                       ← 模板宣告（佔位字串、編譯器、排除清單）
├── note-template/
│   ├── main.tex                        ← 編譯入口
│   ├── package_and_settings.tex        ← beamer 套件、字型、色彩主題
│   ├── 功能筆記readme.tex              ← 使用說明（會隨專案複製）
│   └── fonts/                          ← 字型檔，與 main.tex 同層
└── Content/
    └── course/__SUBJECT__/note/note_1/ ← 骨架：一份投影片
```

## 佔位字串

| 佔位字串 | 替換為 | 位置 |
|---|---|---|
| `__SUBJECT__` | 科目英文資料夾名 | 資料夾名、`main.tex`、`part0_all.tex`、`part1.tex` 路徑 |
| `__TITLE__` | 投影片標題 | `0. 標題與作者.tex` |
| `__AUTHOR__` | 作者 | `0. 標題與作者.tex` |
| `__DATE__` | 年份學期 | `0. 標題與作者.tex` |

## 參考文獻

不使用 bibtex / biblatex，參考文獻直接寫成文字清單（見 `part1.tex` 示範）。

## 修改模板

在這個資料夾直接改即可。已建立的專案不會自動更新。

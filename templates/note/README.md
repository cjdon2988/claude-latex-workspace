# 筆記模板（note）：模板池母版

這是 `templates/note/` 的母版，不是可直接編譯的專案。
新專案請用 skill 建立（`/latex new note <名稱>`），會替換佔位字串並排除本檔與 `template.json`。

## 結構

```
note/
├── template.json                 ← 模板宣告（佔位字串、編譯器、排除清單）
├── note-template/
│   ├── kelong-cjk.sty            ← 字型設定（來源 Template_Fonts）
│   ├── fonts/                    ← 字型檔，必須與 main.tex 同層（Overleaf 在主檔目錄編譯）
│   ├── main.tex                  ← 編譯入口
│   ├── package_and_settings.tex  ← 套件與全域設定
│   └── 功能筆記readme.tex        ← 使用說明（會隨專案複製）
└── content/
    └── __SUBJECT__/note/note_1/  ← 骨架：一份筆記
```

## 佔位字串

| 佔位字串 | 替換為 | 位置 |
|---|---|---|
| `__SUBJECT__` | 科目英文資料夾名 | 資料夾名與 `main.tex`、`part0_all.tex` 路徑 |
| `__TITLE__` | 文件標題 | `0. 標題與作者.tex` |
| `__AUTHOR__` | 作者與學號 | `0. 標題與作者.tex` |

## 修改模板

在這個資料夾直接改即可。已建立的專案不會自動更新。
字型來源若更新，覆蓋 `kelong-cjk.sty` 與 `fonts/` 即可。

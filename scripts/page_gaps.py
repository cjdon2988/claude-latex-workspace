# page_gaps.py:量 PDF 每頁底部留白(pt),找出換頁留白過大的頁。用法:python3 page_gaps.py <pdf> [門檻pt=120]
# 搭配 LaTeX \Needspace:小節標題前剩餘空間不足 N 行才換頁;緊接不可切圖表的小節用較大的 N。見 SKILL.md「版面微調」
import re,subprocess,sys
pdf=sys.argv[1]; thr=float(sys.argv[2]) if len(sys.argv)>2 else 120
out=subprocess.run(['pdftotext','-bbox-layout',pdf,'-'],capture_output=True,text=True).stdout
pages=out.split('<page ')[1:]
res=[]
for i,p in enumerate(pages,1):
    h=float(re.search(r'height="([\d.]+)"',p).group(1))
    ys=[float(m) for m in re.findall(r'<line [^>]*yMax="([\d.]+)"',p)]
    body=[y for y in ys if y<h-60]          # 排除頁尾
    bottom=h-72
    gap=bottom-max(body) if body else bottom
    res.append((i,round(gap)))
print(' '.join(f'{i}:{g}' for i,g in res if g>thr))
print('pages',len(pages),'| gap>%d: %d'%(thr,sum(1 for _,g in res if g>thr)),'| total gap pts',sum(g for _,g in res))

"""Build the printable guide from the editable Markdown; requires reportlab."""
from pathlib import Path
import re
from html import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'output/unit-2-study-guide.md'
DEST = ROOT / 'output/pdf/ap_stats_unit_2_lessons_2_1_to_2_9_study_guide.pdf'
FONT = Path('/System/Library/Fonts/Supplemental')
for name, filename in [('Arial','Arial.ttf'),('Arial-Bold','Arial Bold.ttf'),('Arial-Italic','Arial Italic.ttf'),('Arial-BoldItalic','Arial Bold Italic.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONT/filename)))
pdfmetrics.registerFontFamily('Arial',normal='Arial',bold='Arial-Bold',italic='Arial-Italic',boldItalic='Arial-BoldItalic')
NAVY=colors.HexColor('#17344c'); TEAL=colors.HexColor('#087f82'); GRAY=colors.HexColor('#52616c'); LIGHT=colors.HexColor('#edf5f7')
styles={
 'body':ParagraphStyle('body',fontName='Arial',fontSize=10.2,leading=14.3,spaceAfter=7,textColor=NAVY),
 'title':ParagraphStyle('title',fontName='Arial-Bold',fontSize=29,leading=33,spaceAfter=18,textColor=NAVY),
 'h2':ParagraphStyle('h2',fontName='Arial-Bold',fontSize=20,leading=25,spaceBefore=17,spaceAfter=12,textColor=NAVY,keepWithNext=True),
 'h3':ParagraphStyle('h3',fontName='Arial-Bold',fontSize=12,leading=16,spaceBefore=10,spaceAfter=6,textColor=TEAL,keepWithNext=True),
 'bullet':ParagraphStyle('bullet',fontName='Arial',fontSize=10.2,leading=14.3,leftIndent=13,firstLineIndent=-10,spaceAfter=6,textColor=NAVY),
 'source':ParagraphStyle('source',fontName='Arial-Italic',fontSize=8.5,leading=11.5,spaceBefore=7,spaceAfter=8,textColor=GRAY),
 'cell':ParagraphStyle('cell',fontName='Arial',fontSize=9,leading=12,spaceAfter=0,textColor=NAVY),
 'headcell':ParagraphStyle('headcell',fontName='Arial-Bold',fontSize=9,leading=12,spaceAfter=0,textColor=colors.white),
}
def markup(s):
    s=escape(s)
    return re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',s)
class Guide(SimpleDocTemplate):
    def afterFlowable(self,f):
        if isinstance(f,Paragraph) and f.style.name=='h2':
            title=f.getPlainText();key='section-'+str(self.seq.nextf('section'))
            self.canv.bookmarkPage(key);self.canv.addOutlineEntry(title,key,0)
            self.notify('TOCEntry',(0,title,self.page,key))
def footer(c,doc):
    c.saveState();w,h=doc.pagesize
    c.setStrokeColor(colors.HexColor('#c7d5dc'));c.line(46,h-37,w-46,h-37)
    c.setFont('Arial',8);c.setFillColor(GRAY)
    c.drawString(46,h-28,'AP STATISTICS  /  UNIT 2  /  LESSONS 2.1-2.9')
    c.drawString(46,27,'Class materials + worked review + practice')
    c.drawRightString(w-46,27,str(doc.page));c.restoreState()

doc=Guide(str(DEST),pagesize=(612,792),rightMargin=46,leftMargin=46,topMargin=53,bottomMargin=47,title='AP Statistics Unit 2: Lessons 2.1-2.9',author='Study guide based on supplied class materials')
lines=SOURCE.read_text().splitlines();story=[];i=0;firstsection=True
while i<len(lines):
    line=lines[i].strip()
    if not line:i+=1;continue
    if line.startswith('# '):story.append(Spacer(1,28));story.append(Paragraph(markup(line[2:]),styles['title']));i+=1;continue
    if line.startswith('## '):
        if firstsection:
            story.append(Spacer(1,12));story.append(Paragraph('Contents',styles['h3']))
            toc=TableOfContents();toc.levelStyles=[ParagraphStyle('toc',fontName='Arial',fontSize=9.2,leading=14,leftIndent=0,firstLineIndent=0,spaceBefore=3,textColor=NAVY)]
            story.append(toc);firstsection=False
        if line[3:] in ['Your study map', 'Practice - Sampling and bias', 'Worked answers - P1-P6']:
            story.append(PageBreak())
        story.append(Paragraph(markup(line[3:]),styles['h2']));i+=1;continue
    if line.startswith('### '):story.append(Paragraph(markup(line[4:]),styles['h3']));i+=1;continue
    if line.startswith('|'):
        rows=[]
        while i<len(lines) and lines[i].strip().startswith('|'):
            cells=[s.strip() for s in lines[i].strip().strip('|').split('|')]
            if not all(re.fullmatch(r'[-: ]+',s) for s in cells): rows.append(cells)
            i+=1
        n=len(rows[0]);widths={2:[145,375],3:[105,160,255],4:[90,95,180,155]}.get(n,[520/n]*n)
        if rows[0][0]=='Random sample?':widths=[72,85,363]
        if rows[0][0]=='Case':widths=[40,210,270]
        if rows[0][0]=='Problem':widths=[85,130,160,145]
        data=[[Paragraph(markup(c),styles['headcell' if j==0 else 'cell']) for c in row] for j,row in enumerate(rows)]
        t=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
        t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),NAVY),('ROWBACKGROUNDS',(0,1),(-1,-1),[LIGHT,colors.white]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),('LINEBELOW',(0,-1),(-1,-1),0.4,colors.HexColor('#c7d5dc'))]))
        story.extend([t,Spacer(1,9)]);continue
    if line.startswith('- '):story.append(Paragraph('• '+markup(line[2:]),styles['bullet']));i+=1;continue
    if re.match(r'^\d+\. ',line):story.append(Paragraph(markup(line),styles['bullet']));i+=1;continue
    para=[line];i+=1
    while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','|','- ')) and not re.match(r'^\d+\. ',lines[i]):para.append(lines[i].strip());i+=1
    content=' '.join(para);style=styles['source'] if content.startswith('**Sources:') else styles['body']
    story.append(Paragraph(markup(content),style))
doc.multiBuild(story,onFirstPage=footer,onLaterPages=footer)
print(DEST)

from fpdf import FPDF
import pandas as pd

pdf=FPDF(orientation="P",unit="mm",format="A4")
pdf.set_auto_page_break(auto=False
                        ,margin=0)# It does not automatically break the page and move the content to the nextpage

df=pd.read_csv("topics.csv")
pdf.set_text_color(100,100,100)
for index,row in df.iterrows():
  #Sets the header
    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=24)
    pdf.cell(w=0,h=24,txt=row["Topic"],border=0,ln=1,align="L")
    pdf.set_font(family="Times" ,style="B")
    pdf.line(12, 27, 200, 27)
    for line in range(37,294,10):
        pdf.line(12, line, 200, line)
#Sets the footer
    pdf.ln(252)
    pdf.set_font(family="Times", style="B", size=8)
    pdf.cell(w=0, h=8, txt=row["Topic"], border=0, ln=1, align="R")

    for i in range(row["Pages"]-1):
        pdf.add_page()
        # Sets the footer
        pdf.ln(252+24)# it is because , there is no content , we add up the height and length to get the exact mm for footers.
        pdf.set_font(family="Times", style="B", size=8)
        pdf.cell(w=0, h=8, txt=row["Topic"], border=0, ln=1, align="R")

        for line in range(10, 290, 10):
            pdf.line(12, line, 200, line)

pdf.output("Output.pdf")
import matplotlib.pyplot as plt
from fpdf import FPDF
import numpy


def create_graph():
    plt.figure(figsize=(8, 4.5), layout='constrained')
    # Graph 1
    plt.subplot(211)
    plt.plot(x, y1, label='Algorithm 1')
    plt.plot(x, y2, label='Algorithm 2')
    plt.plot(x, y3, label='Algorithm 3')
    plt.plot(x, y4, label='Algorithm 4')
    plt.xlabel("n")
    plt.ylabel("time (ms)")
    plt.grid()
    plt.legend()
    # Graph 2
    plt.subplot(212)
    plt.plot(x, y2, label='Algorithm 2')
    plt.plot(x, y3, label='Algorithm 3')
    plt.plot(x, y4, label='Algorithm 4')
    plt.xlabel("n")
    plt.ylabel("time (ms)")
    plt.grid()
    plt.legend()
    plt.savefig('outputs/graph.png')


def create_pdf_report():
    font_size = 12
    pdf = FPDF(unit='cm', format='A4')
    pdf.add_page()
    pdf.set_font('Times', 'B', font_size + 6)
    pdf.cell(0, pdf.font_size * 1.5, 'Report', align='C', ln=1)
    pdf.ln(pdf.font_size)

    # Insert graph
    pdf.image('outputs/graph.png', w=pdf.w - 2 * pdf.l_margin)
    pdf.ln(pdf.font_size)

    # Create table header
    pdf.set_font('Times', 'B', font_size)
    col_width = (pdf.w - 2 * pdf.l_margin) / 5
    row_height = pdf.font_size * 1.8
    pdf.cell(col_width, row_height * 2, 'Input', border=1, align='C', ln=0)
    pdf.cell(col_width * 4, row_height, 'Time (ms)', border=1, align='C', ln=1)
    pdf.cell(col_width, row_height, '', ln=0)
    pdf.cell(col_width, row_height, 'Algorithm 1', border=1, align='C', ln=0)
    pdf.cell(col_width, row_height, 'Algorithm 2', border=1, align='C', ln=0)
    pdf.cell(col_width, row_height, 'Algorithm 3', border=1, align='C', ln=0)
    pdf.cell(col_width, row_height, 'Algorithm 4', border=1, align='C', ln=1)

    # Create table body
    pdf.set_font('Times', '', font_size)
    for i in range(0, len(x)):
        pdf.cell(col_width, row_height, str(x[i]), border=1, ln=0, align='C')
        pdf.cell(col_width, row_height, str(y1[i]), border=1, ln=0, align='C')
        pdf.cell(col_width, row_height, str(y2[i]), border=1, ln=0, align='C')
        pdf.cell(col_width, row_height, str(y3[i]), border=1, ln=0, align='C')
        pdf.cell(col_width, row_height, str(y4[i]), border=1, ln=1, align='C')

    pdf.output('outputs/auto.pdf', 'F')


if __name__ == '__main__':
    x = list(map(int, open('inputs.txt', 'r').readlines()))
    y1 = list(map(int, open('outputs/PrimeNumberSimple/algorithm1.txt', 'r').readlines()))
    y2 = list(map(int, open('outputs/PrimeNumberSimple/algorithm2.txt', 'r').readlines()))
    y3 = list(map(int, open('outputs/PrimeNumberSimple/algorithm3.txt', 'r').readlines()))
    y4 = list(map(int, open('outputs/PrimeNumberSimple/algorithm4.txt', 'r').readlines()))
    create_graph()
    create_pdf_report()

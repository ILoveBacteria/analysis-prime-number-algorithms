import matplotlib.pyplot as plt
from fpdf import FPDF
import numpy


def create_graph():
    plt.figure(figsize=(8, 12), layout='constrained')
    # Graph 1
    plt.subplot(511)
    plt.plot(x, y_simple1, label='Algorithm 1 Non Parallel')
    plt.plot(x, y_simple2, label='Algorithm 2 Non Parallel')
    plt.plot(x, y_simple3, label='Algorithm 3 Non Parallel')
    plt.plot(x, y_simple4, label='Algorithm 4 Non Parallel')
    plt.xlabel("n")
    plt.ylabel("time (ms)")
    plt.grid()
    plt.legend()
    # Graph 2
    plt.subplot(512)
    plt.plot(x, y_simple2, label='Algorithm 2 Non Parallel')
    plt.plot(x, y_simple3, label='Algorithm 3 Non Parallel')
    plt.plot(x, y_simple4, label='Algorithm 4 Non Parallel')
    plt.xlabel("n")
    plt.ylabel("time (ms)")
    plt.grid()
    plt.legend()
    # Graph 3
    plt.subplot(513)
    plt.plot(x, y_parallel1, label='Algorithm 1 Parallel')
    plt.plot(x, y_simple1, label='Algorithm 1 Non Parallel')
    plt.xlabel("n")
    plt.ylabel("time (ms)")
    plt.grid()
    plt.legend()
    # Graph 4
    plt.subplot(514)
    plt.plot(x, y_parallel2, label='Algorithm 2 Parallel')
    plt.plot(x, y_simple2, label='Algorithm 2 Non Parallel')
    plt.xlabel("n")
    plt.ylabel("time (ms)")
    plt.grid()
    plt.legend()
    # Graph 5
    plt.subplot(515)
    plt.plot(x, y_parallel3, label='Algorithm 3 Parallel')
    plt.plot(x, y_simple3, label='Algorithm 3 Non Parallel')
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
    col_width = (pdf.w - 2 * pdf.l_margin) / 8
    row_height = pdf.font_size * 1.8
    pdf.cell(col_width, row_height * 2, 'Input', border=1, align='C', ln=0)
    pdf.cell(col_width * 7, row_height, 'Time (ms)', border=1, align='C', ln=1)
    pdf.cell(col_width, row_height, '', ln=0)
    pdf.set_font('Times', 'B', font_size - 4) # Reduce font size to fit text
    pdf.cell(col_width, row_height, 'Algorithm 1', border=1, align='C', ln=0)
    pdf.cell(col_width, row_height, 'Algorithm 1 (P)', border=1, align='C', ln=0)
    pdf.cell(col_width, row_height, 'Algorithm 2', border=1, align='C', ln=0)
    pdf.cell(col_width, row_height, 'Algorithm 2 (P)', border=1, align='C', ln=0)
    pdf.cell(col_width, row_height, 'Algorithm 3', border=1, align='C', ln=0)
    pdf.cell(col_width, row_height, 'Algorithm 3 (P)', border=1, align='C', ln=0)
    pdf.cell(col_width, row_height, 'Algorithm 4', border=1, align='C', ln=1)

    # Create table body
    pdf.set_font('Times', '', font_size)
    for i in range(0, len(x)):
        pdf.cell(col_width, row_height, str(x[i]), border=1, ln=0, align='C')
        pdf.cell(col_width, row_height, str(y_simple1[i]), border=1, ln=0, align='C')
        pdf.cell(col_width, row_height, str(y_parallel1[i]), border=1, ln=0, align='C')
        pdf.cell(col_width, row_height, str(y_simple2[i]), border=1, ln=0, align='C')
        pdf.cell(col_width, row_height, str(y_parallel2[i]), border=1, ln=0, align='C')
        pdf.cell(col_width, row_height, str(y_simple3[i]), border=1, ln=0, align='C')
        pdf.cell(col_width, row_height, str(y_parallel3[i]), border=1, ln=0, align='C')
        pdf.cell(col_width, row_height, str(y_simple4[i]), border=1, ln=1, align='C')

    pdf.output('outputs/auto.pdf', 'F')


if __name__ == '__main__':
    x = list(map(int, open('inputs.txt', 'r').readlines()))
    y_simple1 = list(map(int, open('outputs/PrimeNumberSimple/algorithm1.txt', 'r').readlines()))
    y_simple2 = list(map(int, open('outputs/PrimeNumberSimple/algorithm2.txt', 'r').readlines()))
    y_simple3 = list(map(int, open('outputs/PrimeNumberSimple/algorithm3.txt', 'r').readlines()))
    y_simple4 = list(map(int, open('outputs/PrimeNumberSimple/algorithm4.txt', 'r').readlines()))
    y_parallel1 = list(map(int, open('outputs/PrimeNumberParallel/algorithm1.txt', 'r').readlines()))
    y_parallel2 = list(map(int, open('outputs/PrimeNumberParallel/algorithm2.txt', 'r').readlines()))
    y_parallel3 = list(map(int, open('outputs/PrimeNumberParallel/algorithm3.txt', 'r').readlines()))
    create_graph()
    create_pdf_report()

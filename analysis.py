import matplotlib.pyplot as plt
from fpdf import FPDF
import numpy
import os


class Data:
    def __init__(self, label: str, data: list):
        self.label = label
        self.data = data


def create_graph(data):
    plt.figure(figsize=(8, 4.5), layout='constrained')
    for i in data:
        plt.plot(x[0:len(i.data)], list(map(int, i.data)), label=i.label)
    plt.xlabel("n")
    plt.ylabel("time (ms)")
    plt.grid()
    plt.legend()
    plt.savefig(f'outputs/graph{count_graphs}.png')


def create_pdf_report():
    font_size = 12
    pdf = FPDF(unit='cm', format='A4')
    pdf.add_page()
    pdf.set_font('Times', 'B', font_size + 6)
    pdf.cell(0, pdf.font_size * 1.5, 'Report', align='C', ln=1)
    pdf.ln(pdf.font_size)

    pdf.set_font('Times', '', font_size)
    pdf.cell(0, pdf.font_size, 'This pdf has been created automatically by analysis.py', align='C', ln=1)
    pdf.ln(pdf.font_size)

    pdf.cell(0, pdf.font_size, '*P: Parallel', align='L', ln=1)
    pdf.cell(0, pdf.font_size, '*O: Open Other Programs', align='L', ln=1)
    pdf.cell(0, pdf.font_size, '*NO: Not Optimized', align='L', ln=1)
    pdf.ln(pdf.font_size)

    # Insert graph
    for i in range(1, count_graphs + 1):
        pdf.image(f'outputs/graph{i}.png', w=pdf.w - 2 * pdf.l_margin)
        pdf.ln(pdf.font_size)

    # Create table header
    pdf.set_font('Times', 'B', font_size)
    col_width = (pdf.w - 2 * pdf.l_margin) / (1 + len(simple) + len(parallel) + len(not_optimized))
    row_height = pdf.font_size * 1.8
    pdf.cell(col_width, row_height * 2, 'Input', border=1, align='C', ln=0)
    pdf.cell(col_width * (len(simple) + len(parallel) + len(not_optimized)), row_height, 
            'Time (ms)', border=1, align='C', ln=1)
    pdf.cell(col_width, row_height, '', ln=0)
    pdf.set_font('Times', 'B', font_size - 4) # Reduce font size to fit text

    for i in simple:
        pdf.cell(col_width, row_height, i.label, border=1, align='C', ln=0)
    for i in parallel:
        pdf.cell(col_width, row_height, i.label, border=1, align='C', ln=0)
    for i in not_optimized:
        pdf.cell(col_width, row_height, i.label, border=1, align='C', ln=0)
    pdf.cell(col_width, row_height, '', ln=1)
    
    # Create table body
    pdf.set_font('Times', '', font_size)
    for i in range(0, len(x)):
        pdf.cell(col_width, row_height, str(x[i]), border=1, ln=0, align='C')
        for s in simple:
            pdf.cell(col_width, row_height, s.data[i] if len(s.data) > i else '', border=1, ln=0, align='C')
        for p in parallel:
            pdf.cell(col_width, row_height, p.data[i] if len(p.data) > i else '', border=1, ln=0, align='C')
        for n in not_optimized:
            pdf.cell(col_width, row_height, n.data[i] if len(n.data) > i else '', border=1, ln=0, align='C')
        pdf.cell(col_width, row_height, '', ln=1)

    pdf.output('outputs/auto.pdf', 'F')


if __name__ == '__main__':
    try:
        x = list(map(int, open('inputs.txt', 'r').readlines()))
    except:
        print('Error: inputs.txt not found')
        exit(1)

    # Read data from files
    simple = []
    parallel = []
    not_optimized = []
    data_exist = False
    if os.path.exists('outputs/PrimeNumberSimple'):
        data_exist = True
        for i in range(1, 5):
            with open(f'outputs/PrimeNumberSimple/algorithm{i}.txt', 'r') as f:
                lines = f.readlines()
                if len(lines) > 0:
                    simple.append(Data(f'Algo {i}', lines))
    if os.path.exists('outputs/PrimeNumberParallel'):
        data_exist = True
        for i in range(1, 4):
            with open(f'outputs/PrimeNumberParallel/algorithm{i}.txt', 'r') as f:
                lines = f.readlines()
                if len(lines) > 0:
                    parallel.append(Data(f'Algo {i} (P)', lines))
    if os.path.exists('outputs/PrimeNumberNotOptimized'):
        data_exist = True
        for i in range(1, 5):
            with open(f'outputs/PrimeNumberNotOptimized/algorithm{i}.txt', 'r') as f:
                lines = f.readlines()
                if len(lines) > 0:
                    not_optimized.append(Data(f'Algo {i} (NO)', lines))
    
    if not data_exist:
        print('Error: data not found')
        exit(1)
    
    count_graphs = 0
    if len(simple) > 0:
        count_graphs += 1
        create_graph(simple)
    if len(parallel) > 0:
        count_graphs += 1
        create_graph(parallel)
    if len(not_optimized) > 0:
        count_graphs += 1
        create_graph(not_optimized)
    for i in range(3):
        selected_data = []
        if len(simple) > 0:
            selected_data.append(simple[i])
        if len(parallel) > 0 and i < 3:
            selected_data.append(parallel[i])
        if len(not_optimized) > 0:
            selected_data.append(not_optimized[i])
        count_graphs += 1
        create_graph(selected_data)
    create_pdf_report()

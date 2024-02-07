from reportlab.lib.pagesizes import letter
from reportlabplatypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet

class PDFReport:
    def __init__(self, filename):
        self.filename = filename
        self.elements = []

    def add_title(self, title):
        style = getSampleStyleSheet()["Heading1"]
        self.elements.append(style.title(title))

    def add_content(self, content, style="Normal"):
        style = getSampleStyleSheet()[style]
        for line in content:
            self.elements.append(style.text(line))

    def create_report(self):
        doc = SimpleDocTemplate(self.filename, pagesize=letter)
        doc.build(self.elements)


if __name__ == "__main__":
    # Conteúdo do relatório
    conteudo_relatorio = [
        "Data: 2023-11-07",
        "Vendedor: João",
        "Produto: Widget XYZ",
        "Quantidade: 100",
        "Total: $5000",
    ]

    # Nome do arquivo de saída
    nome_arquivo_pdf = "relatorio_vendas.pdf"

    # Criar o relatório PDF
    report = PDFReport(nome_arquivo_pdf)
    report.add_title("Relatório de Vendas")
    report.add_content(conteudo_relatorio)
    report.create_report()

    print(f"Relatório gerado em {nome_arquivo_pdf}")
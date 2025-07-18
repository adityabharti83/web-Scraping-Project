import os
from excel_report.report_generator import generate_excel_report

def test_generate_excel_report():
    sample_data = [
        {"title": "Product 1", "price": 4999, "source": "Amazon"},
        {"title": "Product 2", "price": 5999, "source": "Flipkart"}
    ]
    filename = "samples/test_output.xlsx"
    generate_excel_report(sample_data, filename)

    assert os.path.exists(filename)

    # Cleanup
    os.remove(filename)

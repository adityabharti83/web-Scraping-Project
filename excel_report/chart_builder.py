from openpyxl.chart import BarChart, Reference

def add_price_chart(wb, ws, df):
    """
    Adds a bar chart of product titles vs prices.
    """
    chart = BarChart()
    chart.title = "Price Comparison"
    chart.x_axis.title = "Products"
    chart.y_axis.title = "Price (₹)"

    # Limit titles to first 10 items for clarity
    rows = min(10, len(df))
    if rows == 0:
        return

    data_ref = Reference(ws, min_col=2, min_row=1, max_row=rows + 1)
    cats_ref = Reference(ws, min_col=1, min_row=2, max_row=rows + 1)

    chart.add_data(data_ref, titles_from_data=True)
    chart.set_categories(cats_ref)
    chart.width = 20
    chart.height = 10

    ws.add_chart(chart, "E2")

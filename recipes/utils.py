from io import BytesIO
import base64
import matplotlib.pyplot as plt
import math


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode("utf-8")
    buffer.close()
    return graph


def get_chart(chart_type, data, total_recipes):
    plt.switch_backend("AGG")
    fig = plt.figure(figsize=(6, 3))
    if chart_type == "#1":
        plt.bar(data["name"], data["cooking_time"])
    elif chart_type == "#2":
        labels = "Ingredient present", "Ingredient not present"
        total_with_ingredient = len(data.index)
        total_without = total_recipes - total_with_ingredient
        data_pie = [
            int(total_with_ingredient),
            int(total_without),
        ]
        plt.pie(data_pie, labels=labels)
    elif chart_type == "#3":
        plt.bar(data["name"], data["ingredient_count"])
    else:
        print("unknown chart type")
    plt.tight_layout()
    chart = get_graph()
    return chart

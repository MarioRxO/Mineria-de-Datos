import json

file_path = r"c:\Users\LENOVO\Documents\Desatech\Mineria de Datos\Colab\regresionlineal.ipynb"

with open(file_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

for cell in nb.get("cells", []):
    if cell.get("id") == "52c53e10":
        cell["source"] = [
            "# Si escogemos esos parámetros\n",
            "# Hacemos calculo de predicciones y guardamos como nueva columna\n",
            "\n",
            "train['predd']=train['GrLivArea']*m+b"
        ]
    elif cell.get("id") == "783b904e":
        cell["source"] = [
            "# Calculamos el error cuadrático\n",
            "train['diff']=train['predd']-train['SalePrice']\n",
            "train['cuad']=train['diff']**2\n",
            "\n",
            "train[['GrLivArea','SalePrice']]"
        ]
    elif cell.get("id") == "954f5b36":
        cell["source"] = [
            "# Codigo que recibe un valor de m\n",
            "# Devuelve el MSE\n",
            "def sum_error(m, train_df):\n",
            "    b = 0\n",
            "    predd = (m * train_df['GrLivArea']) + b\n",
            "    diff = predd - train_df['SalePrice']\n",
            "    cuad = diff ** 2\n",
            "    return cuad.mean()\n"
        ]

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1)

{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNaDwKe3lVVBJRSozdTux3z",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Love1117/Machine_learning-Projects/blob/main/Machine_Learning%20Project/01_Supervised-%20Machine%20Learning/01_Linear_Regression/Car_price_prediction/main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "v7OpllKXEOlV"
      },
      "outputs": [],
      "source": [
        "mkdir -p Machine_Learning_Project/01_Supervised-_Machine_Learning/01_Linear_Regression/Car_price_prediction"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile Machine_Learning_Project/01_Supervised-_Machine_Learning/01_Linear_Regression/Car_price_prediction/main.py\n",
        "\n",
        "from fastapi import FastAPI\n",
        "import uvicorn\n",
        "\n",
        "app = FastAPI()\n",
        "\n",
        "@app.get(\"/\")\n",
        "def home():\n",
        "    return {\"message\": \"FastAPI API created in Colab\"}\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "G5A_ffAEEPWB",
        "outputId": "8eadf9e0-2534-4ad9-e416-1f85f890f5de"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing Machine_Learning_Project/01_Supervised-_Machine_Learning/01_Linear_Regression/Car_price_prediction/main.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "xkRaojTuEPcP"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "dTiYMNnhEPjY"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "z0ROcNKQEQFH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "7-kxhaBDEQJL"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
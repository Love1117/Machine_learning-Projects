{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMMNq7Ww+SKnfo2zrfEOGGJ",
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
      "source": [
        "!git clone https://github.com/love1117/Machine_learning-Projects.git\n",
        "%cd Machine_learning-Projects"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YzPqMe4XTh1F",
        "outputId": "6699c146-3fa7-4c4e-c8a5-5918c4671b75"
      },
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cloning into 'Machine_learning-Projects'...\n",
            "remote: Enumerating objects: 1070, done.\u001b[K\n",
            "remote: Counting objects:   0% (1/274)\u001b[K\rremote: Counting objects:   1% (3/274)\u001b[K\rremote: Counting objects:   2% (6/274)\u001b[K\rremote: Counting objects:   3% (9/274)\u001b[K\rremote: Counting objects:   4% (11/274)\u001b[K\rremote: Counting objects:   5% (14/274)\u001b[K\rremote: Counting objects:   6% (17/274)\u001b[K\rremote: Counting objects:   7% (20/274)\u001b[K\rremote: Counting objects:   8% (22/274)\u001b[K\rremote: Counting objects:   9% (25/274)\u001b[K\rremote: Counting objects:  10% (28/274)\u001b[K\rremote: Counting objects:  11% (31/274)\u001b[K\rremote: Counting objects:  12% (33/274)\u001b[K\rremote: Counting objects:  13% (36/274)\u001b[K\rremote: Counting objects:  14% (39/274)\u001b[K\rremote: Counting objects:  15% (42/274)\u001b[K\rremote: Counting objects:  16% (44/274)\u001b[K\rremote: Counting objects:  17% (47/274)\u001b[K\rremote: Counting objects:  18% (50/274)\u001b[K\rremote: Counting objects:  19% (53/274)\u001b[K\rremote: Counting objects:  20% (55/274)\u001b[K\rremote: Counting objects:  21% (58/274)\u001b[K\rremote: Counting objects:  22% (61/274)\u001b[K\rremote: Counting objects:  23% (64/274)\u001b[K\rremote: Counting objects:  24% (66/274)\u001b[K\rremote: Counting objects:  25% (69/274)\u001b[K\rremote: Counting objects:  26% (72/274)\u001b[K\rremote: Counting objects:  27% (74/274)\u001b[K\rremote: Counting objects:  28% (77/274)\u001b[K\rremote: Counting objects:  29% (80/274)\u001b[K\rremote: Counting objects:  30% (83/274)\u001b[K\rremote: Counting objects:  31% (85/274)\u001b[K\rremote: Counting objects:  32% (88/274)\u001b[K\rremote: Counting objects:  33% (91/274)\u001b[K\rremote: Counting objects:  34% (94/274)\u001b[K\rremote: Counting objects:  35% (96/274)\u001b[K\rremote: Counting objects:  36% (99/274)\u001b[K\rremote: Counting objects:  37% (102/274)\u001b[K\rremote: Counting objects:  38% (105/274)\u001b[K\rremote: Counting objects:  39% (107/274)\u001b[K\rremote: Counting objects:  40% (110/274)\u001b[K\rremote: Counting objects:  41% (113/274)\u001b[K\rremote: Counting objects:  42% (116/274)\u001b[K\rremote: Counting objects:  43% (118/274)\u001b[K\rremote: Counting objects:  44% (121/274)\u001b[K\rremote: Counting objects:  45% (124/274)\u001b[K\rremote: Counting objects:  46% (127/274)\u001b[K\rremote: Counting objects:  47% (129/274)\u001b[K\rremote: Counting objects:  48% (132/274)\u001b[K\rremote: Counting objects:  49% (135/274)\u001b[K\rremote: Counting objects:  50% (137/274)\u001b[K\rremote: Counting objects:  51% (140/274)\u001b[K\rremote: Counting objects:  52% (143/274)\u001b[K\rremote: Counting objects:  53% (146/274)\u001b[K\rremote: Counting objects:  54% (148/274)\u001b[K\rremote: Counting objects:  55% (151/274)\u001b[K\rremote: Counting objects:  56% (154/274)\u001b[K\rremote: Counting objects:  57% (157/274)\u001b[K\rremote: Counting objects:  58% (159/274)\u001b[K\rremote: Counting objects:  59% (162/274)\u001b[K\rremote: Counting objects:  60% (165/274)\u001b[K\rremote: Counting objects:  61% (168/274)\u001b[K\rremote: Counting objects:  62% (170/274)\u001b[K\rremote: Counting objects:  63% (173/274)\u001b[K\rremote: Counting objects:  64% (176/274)\u001b[K\rremote: Counting objects:  65% (179/274)\u001b[K\rremote: Counting objects:  66% (181/274)\u001b[K\rremote: Counting objects:  67% (184/274)\u001b[K\rremote: Counting objects:  68% (187/274)\u001b[K\rremote: Counting objects:  69% (190/274)\u001b[K\rremote: Counting objects:  70% (192/274)\u001b[K\rremote: Counting objects:  71% (195/274)\u001b[K\rremote: Counting objects:  72% (198/274)\u001b[K\rremote: Counting objects:  73% (201/274)\u001b[K\rremote: Counting objects:  74% (203/274)\u001b[K\rremote: Counting objects:  75% (206/274)\u001b[K\rremote: Counting objects:  76% (209/274)\u001b[K\rremote: Counting objects:  77% (211/274)\u001b[K\rremote: Counting objects:  78% (214/274)\u001b[K\rremote: Counting objects:  79% (217/274)\u001b[K\rremote: Counting objects:  80% (220/274)\u001b[K\rremote: Counting objects:  81% (222/274)\u001b[K\rremote: Counting objects:  82% (225/274)\u001b[K\rremote: Counting objects:  83% (228/274)\u001b[K\rremote: Counting objects:  84% (231/274)\u001b[K\rremote: Counting objects:  85% (233/274)\u001b[K\rremote: Counting objects:  86% (236/274)\u001b[K\rremote: Counting objects:  87% (239/274)\u001b[K\rremote: Counting objects:  88% (242/274)\u001b[K\rremote: Counting objects:  89% (244/274)\u001b[K\rremote: Counting objects:  90% (247/274)\u001b[K\rremote: Counting objects:  91% (250/274)\u001b[K\rremote: Counting objects:  92% (253/274)\u001b[K\rremote: Counting objects:  93% (255/274)\u001b[K\rremote: Counting objects:  94% (258/274)\u001b[K\rremote: Counting objects:  95% (261/274)\u001b[K\rremote: Counting objects:  96% (264/274)\u001b[K\rremote: Counting objects:  97% (266/274)\u001b[K\rremote: Counting objects:  98% (269/274)\u001b[K\rremote: Counting objects:  99% (272/274)\u001b[K\rremote: Counting objects: 100% (274/274)\u001b[K\rremote: Counting objects: 100% (274/274), done.\u001b[K\n",
            "remote: Compressing objects: 100% (118/118), done.\u001b[K\n",
            "remote: Total 1070 (delta 245), reused 155 (delta 155), pack-reused 796 (from 2)\u001b[K\n",
            "Receiving objects: 100% (1070/1070), 5.95 MiB | 24.07 MiB/s, done.\n",
            "Resolving deltas: 100% (639/639), done.\n",
            "/content/Machine_learning-Projects/Machine_learning-Projects/Machine_learning-Projects\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 47,
      "metadata": {
        "id": "v7OpllKXEOlV"
      },
      "outputs": [],
      "source": [
        "mkdir -p Machine_Learning_Project/01_Supervised_Machine_Learning/01_Linear_Regression/Car_Price_Prediction"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile Machine_Learning_Project/01_Supervised_Machine_Learning/01_Linear_Regression/Car_Price_Prediction/main.py\n",
        "\n",
        "from fastapi import FastAPI\n",
        "import uvicorn\n",
        "\n",
        "app = FastAPI()\n",
        "\n",
        "@app.get(\"/\")\n",
        "def home():\n",
        "    return {\"message\": \"FastAPI API created in Colab\"}"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "G5A_ffAEEPWB",
        "outputId": "9d581e32-f022-437b-e496-769c1f7ca943"
      },
      "execution_count": 48,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing Machine_Learning_Project/01_Supervised_Machine_Learning/01_Linear_Regression/Car_Price_Prediction/main.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8541d959"
      },
      "source": [
        "!git config --global user.email \"lovedayshadrack3@gmail.com\"\n",
        "!git config --global user.name \"loveday shadrack\""
      ],
      "execution_count": 49,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!git status\n",
        "!git add .\n",
        "!git commit -m \"Add FastAPI for car price prediction\"\n",
        "!git push"
      ],
      "metadata": {
        "id": "dTiYMNnhEPjY",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "12dca8aa-824d-4ef3-cbdb-355049800586"
      },
      "execution_count": 50,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "On branch main\n",
            "Your branch is up to date with 'origin/main'.\n",
            "\n",
            "Untracked files:\n",
            "  (use \"git add <file>...\" to include in what will be committed)\n",
            "\t\u001b[31mMachine_Learning_Project/\u001b[m\n",
            "\n",
            "nothing added to commit but untracked files present (use \"git add\" to track)\n",
            "[main e2832a5] Add FastAPI for car price prediction\n",
            " 1 file changed, 9 insertions(+)\n",
            " create mode 100644 Machine_Learning_Project/01_Supervised_Machine_Learning/01_Linear_Regression/Car_Price_Prediction/main.py\n",
            "fatal: could not read Username for 'https://github.com': No such device or address\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "13b68ae1"
      },
      "source": [
        "After setting your email and name, you will also need to authenticate with GitHub to push your changes. If you are using a personal access token, you might need to configure it as a credential helper or provide it when prompted. For simpler cases, after running the above cell, re-run the `!git push` command, and you should be prompted for your GitHub username and password/personal access token."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "c8d15015"
      },
      "source": [
        "### Essential Prerequisite: GitHub Personal Access Token (PAT) and Colab Secrets\n",
        "\n",
        "To push to GitHub, you need a Personal Access Token (PAT). If you haven't already:\n",
        "\n",
        "1.  **Create a PAT on GitHub**: Go to your GitHub `Settings` > `Developer settings` > `Personal access tokens` > `Tokens (classic)`. Generate a new token with at least `repo` scope.\n",
        "2.  **Store in Colab Secrets**: Click the 'key' icon (🔑) on Colab's left sidebar. Add a new secret named `GH_PAT` and paste your GitHub token as its value. Ensure 'Notebook access' is enabled for this secret."
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "z0ROcNKQEQFH"
      },
      "execution_count": 50,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "7-kxhaBDEQJL"
      },
      "execution_count": 50,
      "outputs": []
    }
  ]
}
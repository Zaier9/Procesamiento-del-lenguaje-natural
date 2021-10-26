{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Configurar_amb_de_trabajo.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyN5MHPmNF8t1tUe8g7ULT4Y",
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
        "<a href=\"https://colab.research.google.com/github/Zaier9/Procesamiento-del-lenguaje-natural/blob/master/Configurar_amb_de_trabajo.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "M9fcF3z60Z9I"
      },
      "source": [
        "# Como usar NLTK en Colab"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KoacHcud0P5S",
        "outputId": "29a0125c-97d1-4691-bcfd-93765950b52a"
      },
      "source": [
        "import nltk\n",
        "nltk.download('cess_esp')"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[nltk_data] Downloading package cess_esp to /root/nltk_data...\n",
            "[nltk_data]   Unzipping corpora/cess_esp.zip.\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 2
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "c7DdWD-e0sYg"
      },
      "source": [
        "# Expresiones Regulares\n",
        "\n",
        "\n",
        "*   Constituyen un lenguaje estandarizado para definir cadenas de búsquedas de texto.\n",
        "*   Librería de operaciones con expresiones regulares de Python re\n",
        "*   Reglas para escribir expresiones regulares Wiki\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UpyLDgjB0kgN",
        "outputId": "00f4af39-12b2-43d8-b8e1-c248f0dca5e3"
      },
      "source": [
        "import re\n",
        "corpus = nltk.corpus.cess_esp.sents()\n",
        "print(corpus)\n",
        "print(len(corpus))"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[['El', 'grupo', 'estatal', 'Electricité_de_France', '-Fpa-', 'EDF', '-Fpt-', 'anunció', 'hoy', ',', 'jueves', ',', 'la', 'compra', 'del', '51_por_ciento', 'de', 'la', 'empresa', 'mexicana', 'Electricidad_Águila_de_Altamira', '-Fpa-', 'EAA', '-Fpt-', ',', 'creada', 'por', 'el', 'japonés', 'Mitsubishi_Corporation', 'para', 'poner_en_marcha', 'una', 'central', 'de', 'gas', 'de', '495', 'megavatios', '.'], ['Una', 'portavoz', 'de', 'EDF', 'explicó', 'a', 'EFE', 'que', 'el', 'proyecto', 'para', 'la', 'construcción', 'de', 'Altamira_2', ',', 'al', 'norte', 'de', 'Tampico', ',', 'prevé', 'la', 'utilización', 'de', 'gas', 'natural', 'como', 'combustible', 'principal', 'en', 'una', 'central', 'de', 'ciclo', 'combinado', 'que', 'debe', 'empezar', 'a', 'funcionar', 'en', 'mayo_del_2002', '.'], ...]\n",
            "6030\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "msbH4i2H2F1Q"
      },
      "source": [
        "flatten = []"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
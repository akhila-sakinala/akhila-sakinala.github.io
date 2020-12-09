{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "makaan-webscraping.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPo5cKM1x2HUb80hG9Ppey1",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/akhila-sakinala/akhila-sakinala.github.io/blob/master/makaan_webscraping.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "up-AE6_-ysCr"
      },
      "source": [
        "## Import packages"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cDrxUSkyymLJ"
      },
      "source": [
        "# import packages\n",
        "import requests\n",
        "from bs4 import BeautifulSoup\n"
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9OaIH_0PzKtr"
      },
      "source": [
        "url = \"https://www.makaan.com/hyderabad-residential-property/rent-property-in-hyderabad-city\"\n",
        "\n",
        "response = requests.get(url)\n",
        "soup = BeautifulSoup(response.text,\"html.parser\")"
      ],
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UCUT4dgE1iWB"
      },
      "source": [
        "s_tag = soup.find_all('span',attrs={'class' : 'seller-type'})"
      ],
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2iW0mExf3K1p",
        "outputId": "3fda9e02-0db9-4f0f-c2de-8387e5d0e294"
      },
      "source": [
        "for each_owner in s_tag:\n",
        "  print(each_owner.text)"
      ],
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "OWNER\n",
            "OWNER\n",
            "OWNER\n",
            "OWNER\n",
            "OWNER\n",
            "OWNER\n",
            "OWNER\n",
            "OWNER\n",
            "OWNER\n",
            "OWNER\n",
            "OWNER\n",
            "OWNER\n",
            "OWNER\n",
            "OWNER\n",
            "OWNER\n",
            "OWNER\n",
            "OWNER\n",
            "OWNER\n",
            "OWNER\n",
            "OWNER\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BmoueXSj5XXY"
      },
      "source": [
        "s_val = soup.find_all('a',attrs={'class' : 'typelink'})"
      ],
      "execution_count": 31,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xlWxkmtr6oEB",
        "outputId": "e4c5d1ce-3bd7-4f43-c10b-cb2605e6513a"
      },
      "source": [
        "for price in s_val:\n",
        "  print(price.span.text)"
      ],
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "2 \n",
            "1 \n",
            "2 \n",
            "3 \n",
            "2 \n",
            "1 \n",
            "3 \n",
            "1 \n",
            "2 \n",
            "4 \n",
            "2 \n",
            "2 \n",
            "2 \n",
            "6 \n",
            "3 \n",
            "3 \n",
            "1 \n",
            "2 \n",
            "1 \n",
            "2 \n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3OTYcyrY6pah"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
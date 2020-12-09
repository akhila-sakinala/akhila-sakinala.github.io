{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "numpy.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPq6nW40jPT8rb5hOX/s8ZV",
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
        "<a href=\"https://colab.research.google.com/github/akhila-sakinala/akhila-sakinala.github.io/blob/master/numpy_methods.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "PmiWMLxrij6l"
      },
      "source": [
        "## Arthemetic operators in ***numpy***"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tfkJjFZ-iitT",
        "outputId": "3fc02fe7-6637-4607-8e77-c79147390922"
      },
      "source": [
        "import numpy as np\n",
        "arr = np.array([[1,2,3,4],[5,6,7,8]])\n",
        "arr.shape"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(2, 4)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 2
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "v_BjIa_yi92t",
        "outputId": "5cf39285-bd19-40f9-ab33-22966ff13076"
      },
      "source": [
        "arr1 = np.array([[10,20,30,40],[11,12,13,14]])\n",
        "arr1"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[10, 20, 30, 40],\n",
              "       [11, 12, 13, 14]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "VTk61WCDjj-H"
      },
      "source": [
        "Adding 2 arrays"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ppyveIBljfPr",
        "outputId": "53fb6f0a-36c1-41a4-9eee-450b82b782bd"
      },
      "source": [
        "arr + arr1"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[11, 22, 33, 44],\n",
              "       [16, 18, 20, 22]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CpYozbOljtO5",
        "outputId": "1dd11f7c-db6e-4813-8509-008cf7409658"
      },
      "source": [
        "arr * arr1"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[ 10,  40,  90, 160],\n",
              "       [ 55,  72,  91, 112]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "x9djWvV9kACT",
        "outputId": "02c1c6fa-eeab-4394-9bdf-cbca4c4f6eb8"
      },
      "source": [
        "arr - arr1"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[ -9, -18, -27, -36],\n",
              "       [ -6,  -6,  -6,  -6]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bQcQOt1JkCnl",
        "outputId": "a7f24c03-b1a4-4216-cae6-4dd4a7d5cf6f"
      },
      "source": [
        "np.exp(arr)"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[2.71828183e+00, 7.38905610e+00, 2.00855369e+01, 5.45981500e+01],\n",
              "       [1.48413159e+02, 4.03428793e+02, 1.09663316e+03, 2.98095799e+03]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AuRRwGZdkiKg",
        "outputId": "ff758083-82ee-4f46-9edb-b5f96a91f4a9"
      },
      "source": [
        "arr2 = np.array([1,2,3,4])\n",
        "arr2.shape"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(4,)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qav_dYiylbUz"
      },
      "source": [
        "# Adding different dimentions of arrays\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YXwPpPBOlDE4",
        "outputId": "710086c4-4fbd-4a73-ef9b-da09c00637d3"
      },
      "source": [
        "arr + arr2"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[ 2,  4,  6,  8],\n",
              "       [ 6,  8, 10, 12]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KBC3EQ2zlPUd",
        "outputId": "dd9b4e36-19f4-4a37-d684-71d8a59bea14"
      },
      "source": [
        "arr3 = np.array([[1,2,3],[1,2,3]])\n",
        "arr3"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[1, 2, 3],\n",
              "       [1, 2, 3]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PZhU1wdDl2LF",
        "outputId": "fa0c0104-1864-4412-a3cf-b9ba59b12426"
      },
      "source": [
        "arr4 = np.array([2,3])\n",
        "arr4"
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([2, 3])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 163
        },
        "id": "4i6zLAzSl5Rb",
        "outputId": "610db117-98e5-4658-8237-f786e3de12aa"
      },
      "source": [
        "arr3 + arr4"
      ],
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ValueError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-20-506014370a72>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0marr3\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0marr4\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mValueError\u001b[0m: operands could not be broadcast together with shapes (2,3) (2,) "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 163
        },
        "id": "-1OC8wjgl-lY",
        "outputId": "ac990413-0556-4fc6-8460-02a6edc92361"
      },
      "source": [
        "arr4 + arr3"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ValueError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-16-6dd2196c4744>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0marr4\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0marr3\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mValueError\u001b[0m: operands could not be broadcast together with shapes (2,) (2,3) "
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cCVrP0nupAFC"
      },
      "source": [
        "We cannot add different shape matrices "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5fPV9m1Npgxk"
      },
      "source": [
        "# Transpose of a matrix"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iMZHbPwwmKLM",
        "outputId": "1c886890-740d-4cb4-8ba5-210231a7e115"
      },
      "source": [
        "arr\n"
      ],
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[1, 2, 3, 4],\n",
              "       [5, 6, 7, 8]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Et3iQhIopJvP",
        "outputId": "fb2878b9-4a5a-4120-995d-8cbb1bf5e18d"
      },
      "source": [
        "arr.T"
      ],
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[1, 5],\n",
              "       [2, 6],\n",
              "       [3, 7],\n",
              "       [4, 8]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DsczH1pppYh8",
        "outputId": "697fda7f-6414-47d8-a75b-137ef813b55c"
      },
      "source": [
        "np.transpose(arr)"
      ],
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[1, 5],\n",
              "       [2, 6],\n",
              "       [3, 7],\n",
              "       [4, 8]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eCj6vAXQpeC-",
        "outputId": "e1ae646f-648f-441a-d908-c1a6865e4c6c"
      },
      "source": [
        "b = np.array([1,2])\n",
        "c = b[:,np.newaxis]\n",
        "c"
      ],
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[1],\n",
              "       [2]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "I5gQPb7yqGG5",
        "outputId": "e1900115-bbb3-4639-a1f9-544474dcc1dd"
      },
      "source": [
        "arr"
      ],
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[1, 2, 3, 4],\n",
              "       [5, 6, 7, 8]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "deXZKZD9qZVt",
        "outputId": "1d2cbfe4-1a80-434b-80e7-d69cd3a2831a"
      },
      "source": [
        "arr[0:1,0:3]"
      ],
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[1, 2, 3]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WX5v-zvRqd7L",
        "outputId": "2f1ece4c-9d7f-49a8-9dac-091652d7f01a"
      },
      "source": [
        "np.dot(b,c)"
      ],
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([5])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bdIumxiouMY_"
      },
      "source": [
        "# Reshaping matrix"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j_PChW48sfSz",
        "outputId": "765241ae-ecdf-4b4a-8c10-0397409472d4"
      },
      "source": [
        "d = np.random.random((4,5))\n",
        "d"
      ],
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[0.15630591, 0.50113219, 0.64165051, 0.26191216, 0.02782672],\n",
              "       [0.62090479, 0.26698439, 0.77781973, 0.54045216, 0.16410988],\n",
              "       [0.25490675, 0.27987804, 0.15076961, 0.0312649 , 0.64846117],\n",
              "       [0.48460045, 0.9836459 , 0.95129064, 0.64322683, 0.48503617]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qn3afuIWttBP",
        "outputId": "ad0f59f3-6e3d-4fc7-f9ca-bc9d6afdef0c"
      },
      "source": [
        "d.reshape((5,4))"
      ],
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[0.15630591, 0.50113219, 0.64165051, 0.26191216],\n",
              "       [0.02782672, 0.62090479, 0.26698439, 0.77781973],\n",
              "       [0.54045216, 0.16410988, 0.25490675, 0.27987804],\n",
              "       [0.15076961, 0.0312649 , 0.64846117, 0.48460045],\n",
              "       [0.9836459 , 0.95129064, 0.64322683, 0.48503617]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CFnIVJpVt0vG",
        "outputId": "e59b26ee-50c2-4d4d-affb-6f5331132cdf"
      },
      "source": [
        "d.reshape((2,10))"
      ],
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[0.15630591, 0.50113219, 0.64165051, 0.26191216, 0.02782672,\n",
              "        0.62090479, 0.26698439, 0.77781973, 0.54045216, 0.16410988],\n",
              "       [0.25490675, 0.27987804, 0.15076961, 0.0312649 , 0.64846117,\n",
              "        0.48460045, 0.9836459 , 0.95129064, 0.64322683, 0.48503617]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ovkG90Jlt8ZM",
        "outputId": "0136351c-f3e0-4d93-9219-d5d266a5582e"
      },
      "source": [
        "d.reshape((10,2))"
      ],
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[0.15630591, 0.50113219],\n",
              "       [0.64165051, 0.26191216],\n",
              "       [0.02782672, 0.62090479],\n",
              "       [0.26698439, 0.77781973],\n",
              "       [0.54045216, 0.16410988],\n",
              "       [0.25490675, 0.27987804],\n",
              "       [0.15076961, 0.0312649 ],\n",
              "       [0.64846117, 0.48460045],\n",
              "       [0.9836459 , 0.95129064],\n",
              "       [0.64322683, 0.48503617]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 34
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rDZJdJtTuBES",
        "outputId": "bf152fc0-8010-4f1e-b6e3-cea90dfc3c7e"
      },
      "source": [
        "a = np.random.random((3,3))\n",
        "b = np.random.random((3,3))\n",
        "a\n",
        "b"
      ],
      "execution_count": 38,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[0.91939929, 0.42226263, 0.90117743],\n",
              "       [0.03099378, 0.47369669, 0.81122912],\n",
              "       [0.02772609, 0.22804956, 0.93367784]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 38
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AbLykO8DueeK",
        "outputId": "386b5307-ed2a-487f-9b49-342eef42ba30"
      },
      "source": [
        "b\n"
      ],
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[0.91939929, 0.42226263, 0.90117743],\n",
              "       [0.03099378, 0.47369669, 0.81122912],\n",
              "       [0.02772609, 0.22804956, 0.93367784]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 39
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6NLJdZreuoip",
        "outputId": "ffed2ac0-fb1c-4ff0-e26d-b8b566a3ec57"
      },
      "source": [
        "a"
      ],
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[0.58371557, 0.06339596, 0.79760276],\n",
              "       [0.69251555, 0.9920377 , 0.98005917],\n",
              "       [0.46496685, 0.1095134 , 0.38365937]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 40
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ldK0SPjGuqm5",
        "outputId": "31b96c9e-637f-434f-daba-1dce03048c5b"
      },
      "source": [
        "b"
      ],
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[0.91939929, 0.42226263, 0.90117743],\n",
              "       [0.03099378, 0.47369669, 0.81122912],\n",
              "       [0.02772609, 0.22804956, 0.93367784]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 41
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "sYu7sU7tv6Zq"
      },
      "source": [
        "# Stacking arrays"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Zx6Of1F_ur3h",
        "outputId": "4b197865-fd4f-48dd-9f12-05391b7f6f35"
      },
      "source": [
        "np.hstack((a,b))"
      ],
      "execution_count": 45,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[0.58371557, 0.06339596, 0.79760276, 0.91939929, 0.42226263,\n",
              "        0.90117743],\n",
              "       [0.69251555, 0.9920377 , 0.98005917, 0.03099378, 0.47369669,\n",
              "        0.81122912],\n",
              "       [0.46496685, 0.1095134 , 0.38365937, 0.02772609, 0.22804956,\n",
              "        0.93367784]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 45
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4oM2y3EmuxWv",
        "outputId": "74dc3b71-0462-439f-dcab-68ab07b2b799"
      },
      "source": [
        "np.vstack((a,b))"
      ],
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[0.58371557, 0.06339596, 0.79760276],\n",
              "       [0.69251555, 0.9920377 , 0.98005917],\n",
              "       [0.46496685, 0.1095134 , 0.38365937],\n",
              "       [0.91939929, 0.42226263, 0.90117743],\n",
              "       [0.03099378, 0.47369669, 0.81122912],\n",
              "       [0.02772609, 0.22804956, 0.93367784]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 46
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7BV5NGuSvdZo"
      },
      "source": [
        ""
      ],
      "execution_count": 47,
      "outputs": []
    }
  ]
}
{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "redditbot-11.ipynb",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "y9dJgV4JO_Ub"
      },
      "source": [
        "import praw\r\n",
        "import time\r\n",
        "from prawcore import Requestor"
      ],
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ze4hLb3UXM-x"
      },
      "source": [
        "# reddit api login\r\n",
        "def login():\r\n",
        "    r = praw.Reddit(client_id='mI_9NuNJaoQvoA',\r\n",
        "                      client_secret='1tvX-iboQrU7afIlg-nU5Gne9ks',\r\n",
        "                      username='iamwordbot',\r\n",
        "                      password='iamwordbot',\r\n",
        "                      user_agent='wordbot by /u/jfishersolutions')\r\n",
        "    print(\"logged in\")\r\n",
        "    return r"
      ],
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "69OAXksxPKE6"
      },
      "source": [
        "cache = []"
      ],
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "O6ki773OPaFQ"
      },
      "source": [
        "def run_bot(r):\r\n",
        "    subreddit = r.subreddit(\"Test\")\r\n",
        "    comments = subreddit.get_comments(limit=25)\r\n",
        "    for comment in comments:\r\n",
        "        comment_text = comment.body.lower()\r\n",
        "        if \"xD\" in comment_text and comment.id not in cache:\r\n",
        "            comment.reply(\"xD\")\r\n",
        "            cache.append(comment.id)\r\n"
      ],
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jswo1auASB-7",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 374
        },
        "outputId": "7cd2996c-4786-4a82-b0ec-f38c55a5d320"
      },
      "source": [
        "while True:\r\n",
        "    r = login()\r\n",
        "    run_bot(r)\r\n",
        "    time.sleep(5)"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "logged in\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "error",
          "ename": "OAuthException",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mOAuthException\u001b[0m                            Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-17-f625163c3ff1>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mwhile\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m     \u001b[0mr\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mlogin\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m     \u001b[0mrun_bot\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mr\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m     \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m5\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-16-f4bb67ffd126>\u001b[0m in \u001b[0;36mrun_bot\u001b[0;34m(r)\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mrun_bot\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mr\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m     \u001b[0msubreddit\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mr\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msubreddit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Test\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m     \u001b[0mcomments\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msubreddit\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_comments\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlimit\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m25\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0mcomment\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mcomments\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m         \u001b[0mcomment_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcomment\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbody\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlower\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/praw/models/reddit/base.py\u001b[0m in \u001b[0;36m__getattr__\u001b[0;34m(self, attribute)\u001b[0m\n\u001b[1;32m     32\u001b[0m         \u001b[0;34m\"\"\"Return the value of `attribute`.\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     33\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mattribute\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstartswith\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"_\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fetched\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 34\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fetch\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     35\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mgetattr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mattribute\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     36\u001b[0m         raise AttributeError(\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/praw/models/reddit/subreddit.py\u001b[0m in \u001b[0;36m_fetch\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    540\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    541\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_fetch\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 542\u001b[0;31m         \u001b[0mdata\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fetch_data\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    543\u001b[0m         \u001b[0mdata\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdata\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"data\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    544\u001b[0m         \u001b[0mother\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mtype\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_reddit\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0m_data\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mdata\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/praw/models/reddit/subreddit.py\u001b[0m in \u001b[0;36m_fetch_data\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    537\u001b[0m         \u001b[0mname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfields\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fetch_info\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    538\u001b[0m         \u001b[0mpath\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mAPI_PATH\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m**\u001b[0m\u001b[0mfields\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 539\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_reddit\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrequest\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"GET\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mpath\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    540\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    541\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_fetch\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/praw/reddit.py\u001b[0m in \u001b[0;36mrequest\u001b[0;34m(self, method, path, params, data, files, json)\u001b[0m\n\u001b[1;32m    763\u001b[0m                 \u001b[0mparams\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mparams\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    764\u001b[0m                 \u001b[0mtimeout\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconfig\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtimeout\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 765\u001b[0;31m                 \u001b[0mjson\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mjson\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    766\u001b[0m             )\n\u001b[1;32m    767\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mBadRequest\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mexception\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/prawcore/sessions.py\u001b[0m in \u001b[0;36mrequest\u001b[0;34m(self, method, path, data, files, json, params, timeout)\u001b[0m\n\u001b[1;32m    337\u001b[0m             \u001b[0mparams\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mparams\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    338\u001b[0m             \u001b[0mtimeout\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mtimeout\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 339\u001b[0;31m             \u001b[0murl\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    340\u001b[0m         )\n\u001b[1;32m    341\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/prawcore/sessions.py\u001b[0m in \u001b[0;36m_request_with_retries\u001b[0;34m(self, data, files, json, method, params, timeout, url, retry_strategy_state)\u001b[0m\n\u001b[1;32m    233\u001b[0m             \u001b[0mretry_strategy_state\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    234\u001b[0m             \u001b[0mtimeout\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 235\u001b[0;31m             \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    236\u001b[0m         )\n\u001b[1;32m    237\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/prawcore/sessions.py\u001b[0m in \u001b[0;36m_make_request\u001b[0;34m(self, data, files, json, method, params, retry_strategy_state, timeout, url)\u001b[0m\n\u001b[1;32m    193\u001b[0m                 \u001b[0mjson\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mjson\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    194\u001b[0m                 \u001b[0mparams\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mparams\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 195\u001b[0;31m                 \u001b[0mtimeout\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mtimeout\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    196\u001b[0m             )\n\u001b[1;32m    197\u001b[0m             log.debug(\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/prawcore/rate_limit.py\u001b[0m in \u001b[0;36mcall\u001b[0;34m(self, request_function, set_header_callback, *args, **kwargs)\u001b[0m\n\u001b[1;32m     33\u001b[0m         \"\"\"\n\u001b[1;32m     34\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdelay\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 35\u001b[0;31m         \u001b[0mkwargs\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"headers\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mset_header_callback\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     36\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mrequest_function\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     37\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mheaders\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/prawcore/sessions.py\u001b[0m in \u001b[0;36m_set_header_callback\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    280\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authorizer\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"refresh\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    281\u001b[0m         ):\n\u001b[0;32m--> 282\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authorizer\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrefresh\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    283\u001b[0m         return {\n\u001b[1;32m    284\u001b[0m             \u001b[0;34m\"Authorization\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m\"bearer {}\"\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_authorizer\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0maccess_token\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/prawcore/auth.py\u001b[0m in \u001b[0;36mrefresh\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    354\u001b[0m             \u001b[0mgrant_type\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"password\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    355\u001b[0m             \u001b[0musername\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_username\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 356\u001b[0;31m             \u001b[0mpassword\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_password\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    357\u001b[0m         )\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/prawcore/auth.py\u001b[0m in \u001b[0;36m_request_token\u001b[0;34m(self, **data)\u001b[0m\n\u001b[1;32m    155\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;34m\"error\"\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mpayload\u001b[0m\u001b[0;34m:\u001b[0m  \u001b[0;31m# Why are these OKAY responses?\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    156\u001b[0m             raise OAuthException(\n\u001b[0;32m--> 157\u001b[0;31m                 \u001b[0mresponse\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mpayload\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"error\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mpayload\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"error_description\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    158\u001b[0m             )\n\u001b[1;32m    159\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mOAuthException\u001b[0m: invalid_grant error processing request"
          ]
        }
      ]
    }
  ]
}
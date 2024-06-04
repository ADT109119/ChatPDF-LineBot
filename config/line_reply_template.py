HELP_TEMPLATE="""
{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://opengraph.githubassets.com/{$TIME}/ADT109119/ChatPDF-LineBot",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://line.me/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "幫助選單",
        "weight": "bold",
        "size": "xl"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "資訊面板",
          "text": "/info"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "本專案GitHub Repo",
          "uri": "https://github.com/ADT109119/ChatPDF-LineBot"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "使用文件",
          "uri": "https://adt109119.github.io/ChatPDF-LineBot-Docs/"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "關於作者",
          "text": "/about"
        }
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "margin": "sm"
      }
    ],
    "flex": 0
  }
}
"""

INFO_TEMPLATE = """
{
  "type": "bubble",
  "hero": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "ChatPDF-LineBot ver {$VERSION}",
        "position": "absolute",
        "offsetTop": "10px",
        "offsetStart": "18px",
        "color": "#aaaaaa",
        "weight": "regular"
      },
      {
        "type": "text",
        "text": "資訊面板",
        "size": "3xl",
        "weight": "bold"
      },
      {
        "type": "text",
        "text": "by ADT109119",
        "size": "sm",
        "color": "#aaaaaa",
        "offsetTop": "-6px",
        "offsetStart": "2px"
      },
      {
        "type": "separator"
      }
    ],
    "paddingTop": "30px",
    "paddingBottom": "6px",
    "paddingStart": "16px"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "margin": "none",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "檔案數量",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 5
              },
              {
                "type": "text",
                "text": "{$FILE_AMOUNT}",
                "wrap": true,
                "color": "#666666",
                "size": "sm",
                "flex": 3,
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "單檔大小限制",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 5
              },
              {
                "type": "text",
                "text": "{$FILE_SIZE_LIMIT}",
                "wrap": true,
                "color": "#666666",
                "size": "sm",
                "flex": 3,
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "已使用空間",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 5
              },
              {
                "type": "text",
                "wrap": true,
                "color": "#666666",
                "size": "sm",
                "flex": 5,
                "align": "end",
                "text": "{$USED_SPACE}"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "backgroundColor": "#00a0ff",
                "width": "{$USED_SPACE_PERCENTAGE}",
                "height": "5px",
                "flex": 10
              }
            ],
            "height": "5px",
            "margin": "md",
            "backgroundColor": "#0060ff20"
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "對話歷史上限",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 5
              },
              {
                "type": "text",
                "text": "{$MAX_CHAT_HISTORY} 則對話",
                "wrap": true,
                "color": "#666666",
                "size": "sm",
                "flex": 3,
                "align": "end"
              }
            ],
            "margin": "md"
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "開啟幫助選單",
          "text": "/help"
        }
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "margin": "sm"
      }
    ],
    "flex": 0
  }
}
"""

ABOUT_ME = """
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://the-walking-fish.com/img/avatar_1_hu9a5663c003f5c52746527244f7342efc_867962_300x0_resize_q75_h2_box_3.webp",
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "cornerRadius": "100px",
            "width": "72px",
            "height": "72px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "contents": [
                  {
                    "type": "span",
                    "text": "The Walking Fish 步行魚",
                    "weight": "bold",
                    "color": "#000000"
                  },
                  {
                    "type": "span",
                    "text": "     "
                  },
                  {
                    "type": "span",
                    "text": "一個剛大學畢業的新鮮人，常在YouTube發一些實用的程式、專案分享，並會動手製做一些開源專案"
                  }
                ],
                "size": "sm",
                "wrap": true
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "icon",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                  },
                  {
                    "type": "text",
                    "text": "12k Subscribers",
                    "size": "sm",
                    "color": "#bcbcbc"
                  }
                ],
                "spacing": "sm",
                "margin": "md"
              }
            ]
          }
        ],
        "spacing": "xl",
        "paddingAll": "20px"
      },
      {
        "type": "separator"
      }
    ],
    "paddingAll": "0px"
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "YouTube頻道",
          "uri": "https://www.youtube.com/@the_walking_fish"
        }
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "GitHub",
          "uri": "https://github.com/ADT109119"
        }
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "頻道網站",
          "uri": "https://the-walking-fish.com/"
        }
      }
    ]
  }
}
"""
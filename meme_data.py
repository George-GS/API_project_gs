
body_for_post_token = {'name': 'george_gs'}


body_meme_id_1 = {
    "id": 1,
    "info": {
        "colors": [
            "green",
            "black",
            "white"
        ],
        "objects": [
            "picture",
            "text"
        ]
    },
    "tags": [
        "fun",
        "yoda"
    ],
    "text": "Only just begun the meme war has",
    "updated_by": "eugene",
    "url": "https://images.theconversation.com/files/177834/original/file-20170712-14488-19lw3sc.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=926&fit=clip"
}

# Валидное тело для POST
valid_body_for_post_meme = {
    "info": {
        "colors": [
            "green",
            "blue"
        ]
    },
    "tags": [
        "fun",
        "boy"
    ],
    "text": "Seriously? Yes, seriously",
    "url": "https://s00.yaplakal.com/pics/pics_original/4/7/1/20258174.jpg"
}

# Тело без tags
body_post_without_tags = {
    "info": {"colors": ["green", "blue"]},
    "text": "Seriously? Yes, seriously",
    "url": "https://s00.yaplakal.com/pics/pics_original/4/7/1/20258174.jpg"
}

# Тело без text
body_post_without_text = {
    "info": {"colors": ["green", "blue"]},
    "tags": ["fun", "boy"],
    "url": "https://s00.yaplakal.com/pics/pics_original/4/7/1/20258174.jpg"
}

# Тело без url
body_post_without_url = {
    "info": {"colors": ["green", "blue"]},
    "tags": ["fun", "boy"],
    "text": "Seriously? Yes, seriously"
}

valid_body_for_put_meme = {
    "id": 123,
    "info": {"colors": ["green", "blue"]},
    "tags": ["fun", "boy"],
    "text": "Updated text",
    "url": "https://new-url.com/image.jpg"
}

# Тело без id
body_put_without_id = {
    "info": {"colors": ["green", "blue"]},
    "tags": ["fun", "boy"],
    "text": "Updated text",
    "url": "https://new-url.com/image.jpg"
}

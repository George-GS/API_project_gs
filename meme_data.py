
valid_body_for_post_token = {'name': 'george_gs'}
valid_body_for_post_token_other_user = {'name': 'ivan23123'}

headers_bad_token = {'Authorization': 'bad_token'}
headers_empty_token = {'Authorization': ''}
headers_no_token = {}


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

body_post_without_tags = {
    "info": {"colors": ["green", "blue"]},
    "text": "Seriously? Yes, seriously",
    "url": "https://s00.yaplakal.com/pics/pics_original/4/7/1/20258174.jpg"
}

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
    "info": {"colors": ["yelow", "red"]},
    "tags": ["sad", "girl"],
    "text": "Updated text",
    "url": "https://new-url.com/image.jpg"
}

body_put_different_order = {
    "url": "https://new-url.com/image.jpg",
    "tags": ["sad", "girl"],
    "text": "Updated text",
    "id": 123,
    "info": {"colors": ["yelow", "red"]}
}

body_put_without_id = {
    "info": {"colors": ["green", "blue"]},
    "tags": ["fun", "boy"],
    "text": "Updated text",
    "url": "https://new-url.com/image.jpg"
}

body_post_different_order = {
    "url": "https://s00.yaplakal.com/pics/pics_original/4/7/1/20258174.jpg",
    "tags": ["fun", "boy"],
    "text": "Seriously? Yes, seriously",
    "info": {
        "colors": ["green", "blue"]
    }
}
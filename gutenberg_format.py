from requests import post
import base64

def wpp(text):
    data = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return data
def slugify(text):
    slug_word = text.strip().replace(' ','-')
    return slug_word

wp_user = "NafisT"
wp_password = "tSKG GrFu KoYI oIKV kQUV wbOS"
wp_credential = f"{wp_user}:{wp_password}"
wp_token = base64.b64encode(wp_credential.encode())
wp_headers = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}

def post_wp(title, content, authorization, status="publish"):
    api_url = 'https://localhost/PythonWordpress/wp-json/wp/v2/posts'
    data = {
        'title': title,
        'content': wpp(content),
        'slug': slugify(title)
    }
    res = post(api_url, json=data, headers = authorization, verify=False)
    print(res.status_code)

title = input("Please enter title")
content = input("Please enter content")

post_wp(title, content, wp_headers)
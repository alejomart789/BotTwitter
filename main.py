import tweepy
import openai

# Configurar las credenciales de acceso de la API de Twitter
consumer_key = 'tu_consumer_key'
consumer_secret = 'tu_consumer_secret'
access_token = 'tu_access_token'
access_token_secret = 'tu_access_token_secret'

# Configurar las credenciales de acceso de la API de OpenAI
openai.api_key = "tu_api_key"

# Configurar la autenticación de tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Configurar el cliente de Twitter
api = tweepy.API(auth)

# Configurar el prompt para generar el tweet
prompt = "Escribe aquí tu prompt"

# Configurar los parámetros de la API de GPT-3
model_engine = "text-davinci-002"
temperature = 0.5
max_tokens = 50

# Función para generar el tweet con GPT-3
def generate_tweet(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        timeout=5,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text.strip()

# Configurar los horarios para publicar los tweets
morning_time = "08:00:00"
afternoon_time = "15:00:00"
evening_time = "20:00:00"

# Publicar los tweets automáticamente en los horarios definidos
while True:
    current_time = datetime.now().strftime('%H:%M:%S')

    if current_time == morning_time:
        tweet = generate_tweet(prompt)
        api.update_status(tweet)
        print("Tweet publicado: ", tweet)

    if current_time == afternoon_time:
        tweet = generate_tweet(prompt)
        api.update_status(tweet)
        print("Tweet publicado: ", tweet)

    if current_time == evening_time:
        tweet = generate_tweet(prompt)
        api.update_status(tweet)
        print("Tweet publicado: ", tweet)

    time.sleep(1)

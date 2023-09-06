PATH_API_KEY = "C:\\Users\\jwson\\Desktop\\jwson\\llama_index_starter_pack\\openai_key.txt"
with open(PATH_API_KEY, "r") as f:
    openai_api_key = f.readline()
    f.close()

openai.api_key = openai_api_key
os.environ["OPENAI_API_KEY"] = openai_api_key
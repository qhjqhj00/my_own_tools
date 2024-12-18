
# request_url
# deepseek: https://api.deepseek.com/chat/completions
# openai: https://api.openai.com/v1/chat/completions

requests_filepath=$1
save_filepath=$2
api_key=$3
request_url=https://api.deepseek.com/chat/completions


echo $requests_filepath
echo $save_filepath
echo $request_url

python api_parallel.py \
  --requests_filepath $requests_filepath \
  --save_filepath $save_filepath \
  --request_url $request_url \
  --max_requests_per_minute 10 \
  --max_tokens_per_minute 300000 \
  --token_encoding_name cl100k_base \
  --max_attempts 5 \
  --logging_level 20 \
  --api_key $api_key

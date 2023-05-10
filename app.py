import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromtTemplate
from langchain.chain import LLMChain

os.environ['OPENAI_API_KEY'] = apikey


st.title('🦜️🔗 YouTube GPT Creator')
prompt = st.text_input('Plug in your promt here')

title_template = PromtTemplate(
    input_variable = ['topic'],
    template = 'Write me a youtube video title about {topic}'
)

#LLMs
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm,prompt=title_template,verbose=True)

if prompt:
    response = title_chain.run(topic = prompt)
    st.write(response)
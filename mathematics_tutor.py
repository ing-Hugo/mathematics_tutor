import os
from ai71 import AI71 



import streamlit as st


ai71_api_key = st.secrets["AI71_API_KEY"]
llm_ai71 = AI71(ai71_api_key)




if __name__ == "__main__":
   
   

   if "chat_engine" not in st.session_state:
     #chat_engine = index.as_chat_engine(chat_mode = "context",verbose = True)
       #chat_engine = index.as_chat_engine(chat_mode = "simple")

      



       st.set_page_config(page_title="Chat with Mathematics Tutor",
                   page_icon = "",
                   layout = "centered",
                   initial_sidebar_state="auto",
                   menu_items = None,
                   )

       st.title("Chat with Mathematics Tutor helper") 


   if "messages" not in st.session_state:
       st.session_state.messages=[{
        
         
         "role" : "assistant",
         "content" : "Ask me a question about Mathematics I am your Tutor helper?",
        #   ChatMessage(
         #      role="assistant", content="Ask me a question about Classiq open source framework for quantum computing?"
        #     ),
           
          }
        
          ]

   if prompt:= st.chat_input("Your Question"):
       st.session_state.messages.append({

        "role" : "User",
        "content": prompt,
         #ChatMessage(role="user", content=prompt), 
       }

    )


   for message in st.session_state.messages:
        with st.chat_message(message["role"]):
             st.write(message["content"])


   if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
             with st.spinner("Thinking...."):
                

                #response = client.chat.completions.create(
                #model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
                #messages=[{"role": "user", "content": prompt}],
                #stream=False,
                #)
                
            
              response = llm_ai71.chat.completions.create(
                        model="tiiuae/falcon-180b-chat",
                        messages=[
                        {"role": "assistant", "content": "You are a Mathematics Tutor,If you don't know the answer, say you don't know. "},
                       {"role": "user", "content": prompt},
                        ],
                       stream=False,
                       )
                
                
                    
                
              print(response.choices[0].message.content)

                  #response = llm.complete(prompt)
                #response = chat_engine.chat(prompt)
                  #response = chat_engine.chat(prompt)
                #st.write(response.response)  
              st.write(response.choices[0].message.content) 
              message = {"role": "assistant", "content":response.choices[0].message.content}
              st.session_state.messages.append(message) # Add response to message history

    
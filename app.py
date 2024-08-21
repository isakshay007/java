import os
from lyzr_agent import LyzrAgent
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LYZR_API_KEY = os.getenv("LYZR_API_KEY")

st.set_page_config(
    page_title="Lyzr",
    layout="centered",  # or "wide"
    initial_sidebar_state="auto",
    page_icon="lyzr-logo-cut.png",
)

st.title("Natural Language to Java Generator 👨‍💻")
st.markdown("### Built using Lyzr Agent-API🚀")
st.markdown("Welcome to the Natural Language to Java Generator app! No matter if you're a beginner or an expert, this tool effortlessly converts your everyday language into accurate Java code, streamlining the coding process for all skill levels.")

Agent = LyzrAgent(
        api_key=LYZR_API_KEY,
        llm_api_key=OPENAI_API_KEY
    )


@st.cache_resource
def create_agent():
    env_id = Agent.create_environment(
        name="Post_java",
        features=[{
            "type": "TOOL_CALLING",
            "config": {"max_tries": 3},
            "priority": 0
        }
        ],
        tools=["perplexity_search"]

    )
    print(env_id)

    prompt = """
You are an Expert in Java and User Input Analysis. Your task is to analyze the user's natural language input and provide the necessary Java responses.


Follow this step-by-step guide:


1. **User Input and Initial Data Gathering**

- Carefully assess the essential inputs provided by the user, which will be in natural language.
- Analyze these inputs to understand how best to approach and provide relevant code in Java.


2. **Research and Content Synthesis**
- Conduct a Perplexity Search using the tool (`perplexity_search`) mentioned in the 'create agent' function. Search based on the user's input using `perplexity_search` to find and provide relevant code in Java format.


You must follow these instructions meticulously, ensuring that each step is executed with precision to provide accurate and relevant Java code and explain them based on the user's requests.


    """


    agent_id = Agent.create_agent(
        env_id=env_id['env_id'],
        system_prompt=prompt,
        name="shell"
    )
    print(agent_id)

    return agent_id

query = st.text_area("Give your input in natural language below.")

if st.button("Generate!"):
    agent = create_agent()
    print(agent)
    chat = Agent.send_message(
        agent_id=agent['agent_id'],
        user_id="default_user",
        session_id="akshay@lyzr.ai",
        message=query
    )

    st.markdown(chat['response'])
# Footer or any additional information
with st.expander("ℹ️ - About this App"):
    st.markdown(
        """Experience the seamless integration of Lyzr's Agent-API. For any inquiries or issues, please contact Lyzr."""
    )
    st.link_button("Lyzr", url="https://www.lyzr.ai/", use_container_width=True)
    st.link_button(
        "Book a Demo", url="https://www.lyzr.ai/book-demo/", use_container_width=True
    )
    st.link_button(
        "Discord", url="https://discord.gg/nm7zSyEFA2", use_container_width=True
    )
    st.link_button(
        "Slack",
        url="https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw",
        use_container_width=True,
    )